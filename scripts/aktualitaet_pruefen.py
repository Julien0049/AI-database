"""Programmprüfung „möglicherweise überholt“ (kostenlos, ohne Sprachmodell), nachträglich an vorhandenen Antwortläufen.

Idee: Jeder Beleg einer Antwort zeigt auf eine Stelle in einem Bericht. Das Programm sucht die passende Aussage in der
Aussagen-Datenbank (Thema, Art, Datum). Ist sie eine Regel (oder „unklar“) und gibt es zu demselben Gegenstand eine
NEUERE Regel aus einem anderen Bericht, wird der Satz als „möglicherweise überholt“ markiert.
„Derselbe Gegenstand“ wird auf zwei Arten bestimmt und verglichen:
  - Thema: gleiches Thema in der Datenbank,
  - Bedeutung: Ähnlichkeit der Aussagen (e5-small) über einer Schwelle.
Fragen nach Änderungen („verändert“, „früher“, „über die Zeit“) werden nicht geprüft, dort sind alte Stände gewollt.

Bekannte Fehlerfälle (Agentenbewertung v17–v19, überholter Stand als aktuell) dienen als Maßstab.

  .venv/bin/python scripts/aktualitaet_pruefen.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
import aidb  # noqa: E402
import aussagen  # noqa: E402

RUNS = {"v17": "2026-11-14_v17", "v18": "2026-11-14_v18", "v19": "2026-11-14_v19"}
KNOWN = {("v17", 21, 1), ("v17", 21, 2), ("v17", 21, 3), ("v18", 10, 1), ("v18", 21, 1),
         ("v19", 10, 1), ("v19", 10, 2), ("v19", 21, 1), ("v19", 21, 2), ("v19", 21, 3)}
HISTORY = re.compile(r"veränder|geändert|früher|über die zeit", re.I)
THRESHOLDS = (0.88, 0.90, 0.92)

reports, _ = aidb.load_reports(ROOT / "data/synthetic_reports")
file_of = {rid: r["datei"] for rid, r in reports.items()}
db = aussagen.connect(ROOT / "index/aussagen.sqlite")
rows = [dict(r) for r in db.execute(
    "SELECT a.*, d.datum_iso FROM aussagen a JOIN dokumente d USING (datei) ORDER BY a.id")]
by_file = {}
for i, r in enumerate(rows):
    by_file.setdefault(r["datei"], []).append(i)

from sentence_transformers import SentenceTransformer  # noqa: E402
model = SentenceTransformer("intfloat/multilingual-e5-small")
vec = model.encode([f"passage: {r['thema']} – {r['aussage']}" for r in rows], normalize_embeddings=True)
sim = vec @ vec.T
kvec = model.encode([f"passage: {r['kontext'] or 'allgemein'}" for r in rows], normalize_embeddings=True)
ksim = kvec @ kvec.T  # Ähnlichkeit des Kontexts zweier Aussagen


def words(t):
    return set(w for w in re.findall(r"[a-zäöüß0-9]+", t.lower()) if len(w) > 3)


def source_statement(rid, zitat):
    """Aussage des Berichts, deren Zitat/Text am besten zum Beleg passt."""
    cand = by_file.get(file_of.get(rid), [])
    if not cand:
        return None
    z = words(zitat)
    return max(cand, key=lambda i: len(z & words(rows[i]["zitat"] + " " + rows[i]["aussage"])))


KONTEXT_MIN, GLEICH_MAX = 0.90, 0.93  # auf v17–v19 abgestimmt (14.11.2026)


def newer(i, mode, threshold=None, filters=False):
    """Neuere Regel (oder unklar) zu demselben Gegenstand aus einem anderen Bericht?"""
    r = rows[i]
    if r["art"] not in ("regel", "unklar") or not r["datum_iso"]:
        return []
    out = []
    for j, s in enumerate(rows):
        if s["datei"] == r["datei"] or s["art"] not in ("regel", "unklar") or not s["datum_iso"]:
            continue
        if s["datum_iso"] <= r["datum_iso"]:
            continue
        same = s["thema"] == r["thema"] if mode == "thema" else sim[i, j] >= threshold
        if same and filters:
            # Variante 2: nur gleicher Kontext, und keine bloße Bestätigung (fast gleicher Inhalt)
            same = ksim[i, j] >= KONTEXT_MIN and sim[i, j] < GLEICH_MAX
        if same:
            out.append(j)
    return out


modes = [("thema", None, False), ("thema", None, True)] + [("bedeutung", t, f) for f in (False, True) for t in THRESHOLDS]
stats = {f"{m}{'' if t is None else ' ≥' + str(t)}{' + Kontext/Bestätigung' if f else ''}":
         {"treffer": 0, "fehlalarme": 0, "geprüft": 0, "bekannt": 0} for m, t, f in modes}
examples = []
for run, tag in RUNS.items():
    d = json.loads((ROOT / f"results/ergebnisse_google_gemini-2.5-pro_{tag}.json").read_text())
    for e in d["ergebnisse"]:
        if HISTORY.search(e["frage"]) or not e.get("roh"):
            continue
        try:
            saetze = aidb.parse(e["roh"])["saetze"]
        except Exception:
            continue
        known = (run, e["nr"], e["durchlauf"]) in KNOWN
        for (m, t, f), key in zip(modes, stats):
            flagged = []
            for s in saetze:
                for b in s.get("belege", []):
                    i = source_statement(b.get("bericht"), b.get("zitat", ""))
                    hit = newer(i, m, t, f) if i is not None else []
                    if hit:
                        flagged.append((s["text"], i, hit[0]))
            st = stats[key]
            st["geprüft"] += 1
            st["bekannt"] += known
            if flagged and known:
                st["treffer"] += 1
            elif flagged:
                st["fehlalarme"] += 1
                if m == "thema" and f and len(examples) < 15:
                    txt, i, j = flagged[0]
                    examples.append(f"{run} F{e['nr']} D{e['durchlauf']}: „{txt[:90]}…“ – {rows[i]['datei'][4:30]} "
                                    f"({rows[i]['datum_iso']}, {rows[i]['thema']}) vs. neuer {rows[j]['datei'][4:30]} ({rows[j]['datum_iso']})")

print("Antworten geprüft (ohne Fragen nach Änderungen):", stats["thema"]["geprüft"], "| bekannte Fehler:", stats["thema"]["bekannt"])
for key, st in stats.items():
    ok = st["geprüft"] - st["bekannt"]
    print(f"  {key:16} erkannt {st['treffer']}/{st['bekannt']} | Fehlalarme {st['fehlalarme']}/{ok} ({st['fehlalarme']/ok:.0%})")
print("\nBeispiele für Fehlalarme (Thema + Kontext/Bestätigung):")
for x in examples:
    print("  ", x)
