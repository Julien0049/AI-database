"""Antwortlauf v15/v16 über die Aussagen-Datenbank.

v15: Das Modell bekommt statt ganzer Berichte die N besten Aussagen aus der Aussagen-Datenbank.
v16 (--volltext): Die N besten Aussagen bestimmen nur, welche Berichte relevant sind; das Modell bekommt diese
     Berichte vollständig ("Aussagen zum Finden, Berichte zum Antworten").

Einzige Änderung gegenüber v11–v13: der Inhalt der Anfrage. Antwort-Prompt (app/prompt_antwort.txt), Modell,
Zitatprüfung und Fußnoten bleiben gleich. Aussagen werden nach Bericht gruppiert, mit Titel, Datum, Art und Kontext;
das Zitat jeder Aussage ist eine wörtliche Stelle aus dem Bericht, die Zitatprüfung läuft gegen den vollen Berichtstext.

  .venv/bin/python scripts/antwortlauf_aussagen.py --nur 1 25          # Kostenprobe mit zwei Fragen
  .venv/bin/python scripts/antwortlauf_aussagen.py --durchlaeufe 3     # Hauptlauf
"""
import argparse
import concurrent.futures
import datetime
import json
import pathlib
import re
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
import aidb  # noqa: E402
import aussagen  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--db", default=str(ROOT / "index/aussagen.sqlite"))
ap.add_argument("--ordner", default=str(ROOT / "data/synthetic_reports"))
ap.add_argument("--n", type=int, default=40, help="Anzahl der besten Aussagen je Frage")
ap.add_argument("--durchlaeufe", type=int, default=1)
ap.add_argument("--nur", type=int, nargs="*", help="nur diese Fragennummern")
ap.add_argument("--version", default="v15")
ap.add_argument("--attrappe", action="store_true", help="ohne Modell (kostenlos)")
ap.add_argument("--ausgabe", default=str(ROOT / "results"))
ap.add_argument("--volltext", action="store_true", help="v16: gefundene Berichte vollständig statt nur Aussagen")
args = ap.parse_args()

key = None if args.attrappe else aidb.read_key(ROOT / ".env")
if not args.attrappe and not key:
    sys.exit("Kein OPENROUTER_API_KEY gefunden.")

reports, _ = aidb.load_reports(args.ordner)          # B-Kennungen wie in v11–v13
rid_of = {r["datei"]: rid for rid, r in reports.items()}
db = aussagen.connect(args.db)
rows = [dict(r) for r in db.execute("SELECT * FROM aussagen ORDER BY id")]
units = aussagen.search_texts(db)
questions = re.findall(r"\*\*Frage\*\*\s*\n\s*> (.+)", (pathlib.Path(args.ordner) / "test_questions.md").read_text())

from sentence_transformers import SentenceTransformer  # noqa: E402
model = SentenceTransformer("intfloat/multilingual-e5-small")
vectors = model.encode([f"passage: {t}" for _, t in units], normalize_embeddings=True)


def select(question):
    q = model.encode(f"query: {question}", normalize_embeddings=True)
    order = sorted(range(len(rows)), key=lambda j: -float(vectors[j] @ q))
    return [rows[j] for j in order[:args.n]]


def statement_corpus(selected):
    """Ausgewählte Aussagen je Bericht, in Berichtsreihenfolge, mit Titel und Datum vom Programm."""
    by_rid = {}
    for r in selected:
        by_rid.setdefault(rid_of[r["datei"]], []).append(r)
    blocks = []
    for rid in sorted(by_rid, key=lambda x: int(x[1:])):
        rep = reports[rid]
        lines = [f'<bericht id="{rid}">', f"# {rep['titel']}", f"Datum: {rep['datum']}", "Aussagen aus diesem Bericht:"]
        for r in by_rid[rid]:
            ctx = f", Kontext: {r['kontext']}" if r["kontext"] else ""
            lines.append(f"- [{r['art']}{ctx}] {r['aussage']} (Originalstelle: „{r['zitat']}“)")
        blocks.append("\n".join(lines + ["</bericht>"]))
    return "\n\n".join(blocks), sorted(by_rid, key=lambda x: int(x[1:]))


def ask(nr, run):
    question = questions[nr - 1]
    selected = select(question)
    corpus, rids = statement_corpus(selected)
    if args.volltext:
        corpus = aidb.corpus_for({rid: reports[rid] for rid in rids})
    start = time.time()
    entry = {"durchlauf": run, "nr": nr, "frage": question, "berichte_im_prompt": rids,
             "aussagen_im_prompt": [r["id"] for r in selected]}
    try:
        if args.attrappe:
            raw, cost = aidb.ask_dummy(question, {rid: reports[rid] for rid in rids})
        else:
            from openai import OpenAI
            client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
            resp = client.chat.completions.create(model=aidb.MODEL, messages=[
                {"role": "system", "content": aidb.PROMPT},
                {"role": "user", "content": f"{corpus}\n\nFrage: {question}"}])
            raw, cost = resp.choices[0].message.content, getattr(resp.usage, "cost", None)
        entry.update(roh=raw, kosten=cost)
        text, sources, problems = aidb.render(aidb.check(aidb.parse(raw), reports), reports)
        entry["antwort"] = {"text": text, "quellen": sources, "probleme": problems}
    except Exception as e:
        entry["fehler"] = str(e)
        entry["status_code"] = getattr(e, "status_code", None)
    entry["dauer_s"] = round(time.time() - start, 1)
    return entry


nrs = args.nur or list(range(1, len(questions) + 1))
jobs = [(nr, run) for run in range(1, args.durchlaeufe + 1) for nr in nrs]
start, results, stop = time.time(), [], False
with concurrent.futures.ThreadPoolExecutor(5) as pool:
    futures = [pool.submit(ask, nr, run) for nr, run in jobs]
    for f in concurrent.futures.as_completed(futures):
        e = f.result()
        results.append(e)
        print(f"D{e['durchlauf']} Frage {e['nr']}: {e['dauer_s']} s, {e.get('kosten') or 0:.4f} USD"
              + (f"  FEHLER {e['fehler'][:120]}" if "fehler" in e else ""))
        if e.get("status_code") in (402, 403) and not stop:
            stop = True
            for other in futures:
                other.cancel()

results.sort(key=lambda e: (e["durchlauf"], e["nr"]))
total = sum(e.get("kosten") or 0 for e in results)
label = "Berichte der" if args.volltext else "statt Berichte:"
out = {"versuch": f"Antwortlauf {args.version}: {label} beste {args.n} Aussagen" + (" (Berichte vollständig)" if args.volltext else ""),
       "volltext": args.volltext,
       "modell": "Attrappe" if args.attrappe else aidb.MODEL,
       "zeitpunkt": datetime.datetime.now().isoformat(timespec="seconds"), "durchlaeufe": args.durchlaeufe,
       "n_aussagen": args.n, "berichte": len(reports), "aussagen_in_db": len(rows),
       "kosten_usd": round(total, 4), "dauer_s": round(time.time() - start, 1),
       "systemprompt": aidb.PROMPT, "ergebnisse": results}
suffix = "_test" if args.nur else ""
name = pathlib.Path(args.ausgabe) / f"ergebnisse_{'attrappe' if args.attrappe else 'google_gemini-2.5-pro'}_{datetime.date.today()}_{args.version}{suffix}.json"
name.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(f"{len(results)} Antworten, {total:.4f} USD, {out['dauer_s']} s -> {name}")
