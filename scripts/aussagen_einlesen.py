"""Gleicht einen Berichtsordner mit der Aussagen-Datenbank ab (v14).

Standard ist die kostenlose Attrappe. Mit --modell wird Gemini 2.5 Pro über OpenRouter genutzt (kostet Guthaben).
Nur neue oder geänderte Dateien werden verarbeitet; ein zweiter Aufruf ohne Änderungen kostet nichts.

Beispiele (im Projektordner):
  .venv/bin/python scripts/aussagen_einlesen.py --db index/attrappe.sqlite
  .venv/bin/python scripts/aussagen_einlesen.py --modell --max 2          # kleiner bezahlter Probelauf
  .venv/bin/python scripts/aussagen_einlesen.py --modell --export results/aussagen_..._v14.json
"""
import argparse
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
import aidb  # noqa: E402
import aussagen  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--ordner", default=str(ROOT / "data/synthetic_reports"))
ap.add_argument("--db", default=str(ROOT / "index/aussagen.sqlite"))
ap.add_argument("--modell", action="store_true", help="echtes Modell statt Attrappe (kostet Guthaben)")
ap.add_argument("--max", type=int, default=None, help="höchstens so viele neue/geänderte Dateien verarbeiten")
ap.add_argument("--export", default=None, help="Datenbankinhalt zusätzlich als JSON speichern")
args = ap.parse_args()

key = None
if args.modell:
    key = aidb.read_key(ROOT / ".env")
    if not key:
        sys.exit("Kein OPENROUTER_API_KEY in Umgebung oder .env gefunden.")

db = aussagen.connect(args.db)
start = time.time()
summary = aussagen.sync(args.ordner, db, aussagen.extract_model if args.modell else aussagen.extract_dummy,
                        key=key, limit=args.max)
summary["dauer_s"] = round(time.time() - start, 1)
summary["themen"] = len(aussagen.topics(db))
summary["aussagen_gesamt"] = db.execute("SELECT COUNT(*) FROM aussagen").fetchone()[0]
summary["zitate_nicht_gefunden"] = db.execute("SELECT COUNT(*) FROM aussagen WHERE zitat_ok = 0").fetchone()[0]
print(json.dumps({k: (len(v) if isinstance(v, list) and k != "fehler" else v) for k, v in summary.items()},
                 ensure_ascii=False, indent=1))

if args.export:
    out = {"versuch": "Aussagen-Datenbank v14", "modell": aidb.MODEL if args.modell else "Attrappe",
           "abgleich": summary, **aussagen.export(db)}
    pathlib.Path(args.export).write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print("gespeichert:", args.export)
