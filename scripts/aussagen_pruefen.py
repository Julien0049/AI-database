"""Kostenloser Prüftest der Aussagen-Datenbank (v14), ohne Sprachmodell.

1. Suche: Liegen die nötigen Berichte je Frage unter den ersten k? Gesucht wird über die einzelnen Aussagen
   (Thema, Kontext, Aussage) mit intfloat/multilingual-e5-small; ein Bericht erhält den Wert seiner besten Aussage.
   Vergleich mit Suchtest s5 (gleiche Fragen, gleiche nötigen Berichte, Suche über ganze Berichte).
2. Übersicht: Aussagen der nötigen Berichte je Frage, zur Sichtprüfung, ob die entscheidenden Aussagen erfasst sind.
3. Themen: Anzahl, Arten, Zitatprüfung.

  .venv/bin/python scripts/aussagen_pruefen.py --db index/aussagen.sqlite --version v14
"""
import argparse
import datetime
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
import aussagen  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--db", default=str(ROOT / "index/aussagen.sqlite"))
ap.add_argument("--version", default="v14")
ap.add_argument("--ausgabe", default=str(ROOT / "results"))
ap.add_argument("--noetig", default=None, help="JSON mit nötigen Berichten je Frage (Standard: aus Suchtest s5)")
args = ap.parse_args()

S5 = json.loads((ROOT / "results/ergebnisse_suche_2026-11-05_s5.json").read_text())
NEEDED = {int(i): v for i, v in (json.loads(pathlib.Path(args.noetig).read_text()) if args.noetig else S5)["noetig"].items()}
QUESTIONS = re.findall(r"\*\*Frage\*\*\s*\n\s*> (.+)", (ROOT / "data/synthetic_reports/test_questions.md").read_text())
KS = (3, 5, 10, 15, 20, 30)

db = aussagen.connect(args.db)
units = aussagen.search_texts(db)
n_reports = db.execute("SELECT COUNT(*) FROM dokumente").fetchone()[0]

from sentence_transformers import SentenceTransformer  # noqa: E402
model = SentenceTransformer("intfloat/multilingual-e5-small")
vectors = model.encode([f"passage: {t}" for _, t in units], normalize_embeddings=True)


def ranking(question):
    q = model.encode(f"query: {question}", normalize_embeddings=True)
    best = {}
    for (name, _), s in zip(units, vectors @ q):
        best[name] = max(best.get(name, -1.0), float(s))
    return sorted(best, key=lambda n: -best[n])


rankings = {i: ranking(q) for i, q in enumerate(QUESTIONS, 1)}
scored = [i for i in NEEDED if NEEDED[i]]


def complete_at(ranks, k):
    return round(sum(set(NEEDED[i]) <= set(ranks[i][:k]) for i in scored) / len(scored), 2)


summary = {f"Aussagen ({args.version})": {f"vollständig@{k}": complete_at(rankings, k) for k in KS}}
s5_ranks = None
if not args.noetig:  # Vergleich mit s5 nur auf dem Datensatz von s5 (dataset-v3)
    s5_ranks = {int(i): r for i, r in S5["ranglisten"]["Bedeutung (klein)"].items()}
    summary["Ganze Berichte (s5)"] = {f"vollständig@{k}": complete_at(s5_ranks, k) for k in KS}

print(f"{n_reports} Berichte, {len(units)} Aussagen, {len(QUESTIONS)} Fragen\n")
print("Rang der nötigen Berichte je Frage (Aussagen v14 / ganze Berichte s5)")
for i in scored:
    print(f"Frage {i}: {QUESTIONS[i-1]}")
    for n in NEEDED[i]:
        a = rankings[i].index(n) + 1 if n in rankings[i] else "–"
        b = f" / {s5_ranks[i].index(n) + 1:>2}" if s5_ranks else ""
        print(f"   {a!s:>2}{b}   {n}")
print("\nvollständig@k (Anteil der", len(scored), "Fragen mit nötigen Berichten)")
for m, v in summary.items():
    print(f"   {m:22}", "  ".join(f"@{k}: {v[f'vollständig@{k}']:.0%}" for k in KS))

# v14b: Themensuche. Die M besten Aussagen bestimmen die Themen; geliefert werden ALLE Aussagen dieser Themen
# (alle Berichte, alle Stände). Gemessen: vollständig (ohne festes k) und wie viel dafür mitgeliefert wird.
topic_of = [r["thema"] for r in db.execute("SELECT thema FROM aussagen ORDER BY id")]
MS = (1, 3, 5, 10)


def topic_search(question, m):
    q = model.encode(f"query: {question}", normalize_embeddings=True)
    order = sorted(range(len(units)), key=lambda j: -float(vectors[j] @ q))
    chosen = {topic_of[j] for j in order[:m]}
    picked = [j for j in range(len(units)) if topic_of[j] in chosen]
    return {"themen": sorted(chosen), "berichte": sorted({units[j][0] for j in picked}), "aussagen": len(picked)}


topic_results = {m: {i: topic_search(q, m) for i, q in enumerate(QUESTIONS, 1)} for m in MS}
topic_summary = {}
print("\nThemensuche: M beste Aussagen -> alle Aussagen ihrer Themen")
for m in MS:
    res = topic_results[m]
    topic_summary[f"M={m}"] = {
        "vollständig": round(sum(set(NEEDED[i]) <= set(res[i]["berichte"]) for i in scored) / len(scored), 2),
        "berichte_mittel": round(sum(len(res[i]["berichte"]) for i in res) / len(res), 1),
        "aussagen_mittel": round(sum(res[i]["aussagen"] for i in res) / len(res), 1)}
    t = topic_summary[f"M={m}"]
    missing = [i for i in scored if not set(NEEDED[i]) <= set(res[i]["berichte"])]
    print(f"   M={m:<3} vollständig {t['vollständig']:.0%}  | im Mittel {t['berichte_mittel']} Berichte, "
          f"{t['aussagen_mittel']} Aussagen | unvollständig: Fragen {missing}")

rows = [dict(r) for r in db.execute("SELECT a.*, d.titel, d.datum FROM aussagen a JOIN dokumente d USING (datei) ORDER BY a.id")]
stats = {"berichte": n_reports, "aussagen": len(rows), "themen": len({r["thema"] for r in rows}),
         "arten": dict(Counter(r["art"] for r in rows)),
         "zitate_nicht_gefunden": sum(1 for r in rows if not r["zitat_ok"]),
         "aussagen_je_thema": dict(Counter(r["thema"] for r in rows).most_common())}
print("\nThemen:", stats["themen"], "| Arten:", stats["arten"], "| Zitate nicht gefunden:", stats["zitate_nicht_gefunden"])

today = datetime.date.today()
out = pathlib.Path(args.ausgabe)
(out / f"ergebnisse_aussagen_suche_{today}_{args.version}.json").write_text(json.dumps(
    {"versuch": f"Prüftest Aussagen-Datenbank {args.version}", "zeitpunkt": datetime.datetime.now().isoformat(timespec="seconds"),
     "embedding_modell": "intfloat/multilingual-e5-small", "statistik": stats, "kennzahlen": summary,
     "noetig": NEEDED, "ranglisten": rankings,
     "themensuche": {"kennzahlen": topic_summary, "treffer": topic_results}}, ensure_ascii=False, indent=1))

lines = [f"# Sichtprüfung Aussagen {args.version} ({n_reports} Berichte)", "",
         "Aussagen der nötigen Berichte je Frage. Prüfen: Ist die Aussage erfasst, die die Frage beantwortet, "
         "mit passender Art und passendem Kontext?", ""]
by_file = {}
for r in rows:
    by_file.setdefault(r["datei"], []).append(r)
for i in scored:
    lines += [f"## Frage {i}: {QUESTIONS[i-1]}", ""]
    for n in NEEDED[i]:
        first = by_file.get(n, [{}])[0]
        lines += [f"**{first.get('titel', n)}** ({first.get('datum', '?')}, `{n}`)", ""]
        for r in by_file.get(n, []):
            flag = "" if r["zitat_ok"] else " ⚠ Zitat nicht gefunden"
            ctx = f" [{r['kontext']}]" if r["kontext"] else ""
            lines.append(f"- *{r['thema']}* · {r['art']}{ctx}: {r['aussage']}{flag}")
        lines.append("")
lines += ["## Alle Themen", ""] + [f"- {t} ({c})" for t, c in stats["aussagen_je_thema"].items()]
(out / f"sichtpruefung_aussagen_{today}_{args.version}.md").write_text("\n".join(lines) + "\n")
print("gespeichert in", out)
