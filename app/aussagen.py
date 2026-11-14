"""Aussagen-Datenbank (v14): Jeder Bericht wird beim Eingang einmal in Einzelaussagen zerlegt und dauerhaft gespeichert.

- sync() gleicht einen Ordner mit der Datenbank ab: nur neue oder geänderte Dateien (Fingerabdruck) werden verarbeitet,
  Einträge entfernter Dateien gelöscht. Kein manueller Import nötig; jede Datei kostet nur einmal.
- Titel und Datum liest das Programm (aidb.find_title/find_date), nicht das Modell.
- Das Modell bekommt die bisherige Themenliste, damit Aussagen zum selben Gegenstand dasselbe Thema tragen.
  Deshalb werden Dateien nacheinander verarbeitet, nicht parallel.
- Jedes Zitat wird gegen den Berichtstext geprüft (zitat_ok).
"""
import datetime
import hashlib
import json
import pathlib
import re
import sqlite3

import aidb

PROMPT = (pathlib.Path(__file__).parent / "prompt_aussagen.txt").read_text()
ARTEN = {"regel", "erfahrung", "unklar", "sonstiges"}

SCHEMA = """
CREATE TABLE IF NOT EXISTS dokumente (
    datei TEXT PRIMARY KEY, fingerabdruck TEXT, titel TEXT, datum TEXT, datum_iso TEXT,
    eingelesen TEXT, kosten REAL);
CREATE TABLE IF NOT EXISTS aussagen (
    id INTEGER PRIMARY KEY AUTOINCREMENT, datei TEXT, thema TEXT, art TEXT, kontext TEXT,
    aussage TEXT, zitat TEXT, zitat_ok INTEGER);
"""


def connect(path):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.executescript(SCHEMA)
    return db


def iso(date):
    """'21.04.2026' -> '2026-04-21' (für Vergleiche); None bei unbekanntem Datum."""
    m = re.fullmatch(r"(\d{2})\.(\d{2})\.(\d{4})", date or "")
    return f"{m[3]}-{m[2]}-{m[1]}" if m else None


def topics(db):
    return [r[0] for r in db.execute("SELECT DISTINCT thema FROM aussagen ORDER BY thema")]


def user_message(text, topic_list):
    listed = "\n".join(f"- {t}" for t in topic_list) or "(noch keine)"
    return f"Bisherige Themen:\n{listed}\n\n<bericht>\n{text}\n</bericht>"


def extract_model(text, topic_list, key):
    """Zerlegt einen Bericht mit dem Modell. Gibt (Liste von Aussagen, Kosten in USD oder None) zurück."""
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
    response = client.chat.completions.create(
        model=aidb.MODEL,
        messages=[{"role": "system", "content": PROMPT},
                  {"role": "user", "content": user_message(text, topic_list)}])
    raw = response.choices[0].message.content
    return aidb.parse(raw)["aussagen"], getattr(response.usage, "cost", None)


def extract_dummy(text, topic_list, key=None):
    """Attrappe ohne Modell: jeder Satz des Fließtexts wird eine Aussage der Art 'sonstiges', Thema = Titel.
    Dient nur dazu, Abgleich, Speicher und Prüfskript kostenlos zu testen."""
    title = aidb.find_title(text) or "Ohne Titel"
    body = " ".join(line for line in text.splitlines()
                    if line.strip() and not line.startswith("#") and not line.startswith("**"))
    sentences = [s.strip() for s in re.split(r"(?<=[a-zäöüß0-9])[.!?] ", body) if len(s.strip()) > 20]
    return [{"thema": title, "art": "sonstiges", "kontext": "", "aussage": s, "zitat": s} for s in sentences], 0.0


def quote_ok(zitat, text):
    return aidb.quote_in(zitat, text)


def recheck_quotes(db, folder):
    """Prüft alle gespeicherten Zitate erneut gegen die aktuellen Dateien und liest Titel und Datum neu
    (ohne Modell, ohne Kosten). Nötig, wenn sich die Leseregeln des Programms ändern, nicht aber die Dateien."""
    texts = {p.name: aidb.read_file(p) for p in aidb.report_files(folder)}
    for name, text in texts.items():
        date = aidb.find_date(text) or "Datum unbekannt"
        db.execute("UPDATE dokumente SET titel = ?, datum = ?, datum_iso = ? WHERE datei = ?",
                   (aidb.find_title(text) or name, date, iso(date), name))
    for r in db.execute("SELECT id, datei, zitat FROM aussagen").fetchall():
        ok = r["datei"] in texts and quote_ok(r["zitat"], texts[r["datei"]])
        db.execute("UPDATE aussagen SET zitat_ok = ? WHERE id = ?", (int(ok), r["id"]))
    db.commit()


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync(folder, db, extract, key=None, log=print, limit=None):
    """Gleicht den Ordner mit der Datenbank ab. Gibt eine Übersicht zurück (neu, geändert, entfernt, Fehler, Kosten).
    Bei Guthaben- oder Berechtigungsfehlern (402/403) wird abgebrochen; bereits verarbeitete Dateien bleiben gespeichert."""
    summary = {"neu": [], "geändert": [], "entfernt": [], "unverändert": 0, "fehler": [], "kosten": 0.0}
    files = {p.name: p for p in aidb.report_files(folder)}
    known = {r["datei"]: r["fingerabdruck"] for r in db.execute("SELECT datei, fingerabdruck FROM dokumente")}

    for name in sorted(set(known) - set(files)):
        db.execute("DELETE FROM aussagen WHERE datei = ?", (name,))
        db.execute("DELETE FROM dokumente WHERE datei = ?", (name,))
        summary["entfernt"].append(name)
    db.commit()

    for name, path in files.items():
        fp = fingerprint(path)
        if known.get(name) == fp:
            summary["unverändert"] += 1
            continue
        if limit is not None and len(summary["neu"]) + len(summary["geändert"]) >= limit:
            break  # z. B. kleiner bezahlter Probelauf; Rest folgt beim nächsten Abgleich
        try:
            text = aidb.read_file(path)
            if not text.strip():
                raise ValueError("kein Text gefunden")
            items, cost = extract(text, topics(db), key)
        except Exception as e:
            if getattr(e, "status_code", None) in (402, 403):
                summary["fehler"].append(f"{name}: Abbruch, Guthaben oder Berechtigung ({e})")
                break
            summary["fehler"].append(f"{name}: {e}")
            log(f"Fehler {name}: {e}")
            continue  # Datei bleibt unverarbeitet und wird beim nächsten Abgleich erneut versucht
        title, date = aidb.find_title(text) or name, aidb.find_date(text) or "Datum unbekannt"
        db.execute("DELETE FROM aussagen WHERE datei = ?", (name,))
        for it in items:
            zitat = it.get("zitat", "")
            ok = quote_ok(zitat, text)
            art = it.get("art", "").lower()
            db.execute("INSERT INTO aussagen (datei, thema, art, kontext, aussage, zitat, zitat_ok) VALUES (?,?,?,?,?,?,?)",
                       (name, it.get("thema", "").strip(), art if art in ARTEN else "unklar",
                        it.get("kontext", "").strip(), it.get("aussage", "").strip(), zitat, int(ok)))
        db.execute("INSERT OR REPLACE INTO dokumente VALUES (?,?,?,?,?,?,?)",
                   (name, fp, title, date, iso(date), datetime.datetime.now().isoformat(timespec="seconds"), cost))
        db.commit()
        summary["geändert" if name in known else "neu"].append(name)
        summary["kosten"] += cost or 0.0
        log(f"{name}: {len(items)} Aussagen, {cost or 0:.4f} USD")
    return summary


def export(db):
    """Gesamter Inhalt als Python-Struktur (für die Ablage in results/)."""
    return {"dokumente": [dict(r) for r in db.execute("SELECT * FROM dokumente ORDER BY datei")],
            "aussagen": [dict(r) for r in db.execute("SELECT * FROM aussagen ORDER BY datei, id")]}


def search_texts(db):
    """(Datei, Suchtext) je Aussage: Thema, Kontext und Aussage zusammen."""
    return [(r["datei"], " – ".join(x for x in (r["thema"], r["kontext"], r["aussage"]) if x))
            for r in db.execute("SELECT * FROM aussagen ORDER BY id")]


if __name__ == "__main__":
    print(json.dumps(export(connect("index/aussagen.sqlite")), ensure_ascii=False, indent=1)[:2000])
