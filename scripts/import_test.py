"""Importtest: Kommen Text, Titel und Datum aus Word- und PDF-Dateien so heraus wie aus Markdown?

Erzeugt aus sechs Markdown-Testberichten je eine Word- und eine PDF-Datei (data/format_test/), liest sie
wieder ein und vergleicht Titel, Datum und Vollständigkeit des Texts mit dem Ergebnis für die Markdown-Vorlage.
Kein Sprachmodell, keine Kosten. Start im Projektordner: .venv/bin/python scripts/import_test.py
"""
import datetime
import json
import pathlib
import re
import sys
from xml.sax.saxutils import escape

from docx import Document
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))
import aidb  # noqa: E402

SOURCE = ROOT / "data" / "synthetic_reports"
OUT = ROOT / "data" / "format_test"
CASES = {
    "AAR-2025-02-04-missing-items.md": "Überschrift und „Datum:“-Zeile",
    "AAR-2023-02-15-winter-clothing-layers.md": "keine Überschrift, Datum ohne Beschriftung",
    "AAR-2025-03-18-logbook-form.md": "keine Überschrift, ausgeschriebenes Datum in der Unterschrift",
    "AAR-2024-01-08-vehicle-reservations.md": "kein Datum",
    "AAR-2025-03-14-printer-outage.md": "Ereignisdatum vor dem Berichtsdatum",
    "AAR-2025-01-20-shared-set-returns.md": "„Stand: 2025-01-20“",
}


def lines(md):
    """Zerlegt den Markdown-Text in (ist_überschrift, Zeile); Fettschrift-Sterne bleiben für die Formatierung."""
    for line in md.splitlines():
        if line.strip():
            yield line.startswith("# "), line[2:].strip() if line.startswith("# ") else line.strip()


def write_docx(md, path):
    """Word-Datei mit echter Überschrift-Formatvorlage; „**Datum:**“ wird fett gesetzt."""
    doc = Document()
    for heading, text in lines(md):
        if heading:
            doc.add_heading(text, level=1)
            continue
        paragraph = doc.add_paragraph()
        for i, part in enumerate(re.split(r"\*\*", text)):
            paragraph.add_run(part).bold = i % 2 == 1
    doc.save(path)


def write_pdf(md, path):
    """PDF mit großer, fetter Titelzeile; ein PDF kennt keine Überschrift als Struktur, nur als Schriftbild."""
    styles = getSampleStyleSheet()
    story = []
    for heading, text in lines(md):
        markup = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(text))
        story.append(Paragraph(markup, styles["Heading1" if heading else "Normal"]))
    SimpleDocTemplate(str(path)).build(story)


read_docx, read_pdf = aidb.read_docx, aidb.read_pdf  # dieselben Leseregeln wie in der Oberfläche


def first_line(text):
    return next((line.strip() for line in text.splitlines() if line.strip()), None)


def pieces(md):
    """Sätze und kurze Zeilen der Vorlage ohne Markdown-Zeichen, für die Vollständigkeitsprüfung."""
    body = [re.sub(r"\*\*", "", text) for _, text in lines(md)]
    return [p for line in body for p in re.split(r"(?<=[a-zäöüß])[.;]\s+", line) if p.strip()]


def complete(md, text):
    found = [aidb.norm(p) in aidb.norm(text) for p in pieces(md)]
    return sum(found), len(found)


OUT.mkdir(exist_ok=True)
rows = []
for name, case in CASES.items():
    md = (SOURCE / name).read_text()
    expected = {"titel": aidb.find_title(md) or name, "datum": aidb.find_date(md) or "Datum unbekannt"}
    row = {"datei": name, "fall": case, "markdown": expected}
    for fmt, write, read in (("docx", write_docx, read_docx), ("pdf", write_pdf, read_pdf)):
        path = OUT / name.replace(".md", f".{fmt}")
        write(md, path)
        text = read(path)
        title = aidb.find_title(text) or path.name
        found, total = complete(md, text)
        row[fmt] = {
            "titel": title,
            "titel_wie_markdown": title in (expected["titel"], path.name) and (title == expected["titel"]) == (expected["titel"] != name),
            "titel_erste_zeile": first_line(text),
            "datum": aidb.find_date(text) or "Datum unbekannt",
            "datum_wie_markdown": (aidb.find_date(text) or "Datum unbekannt") == expected["datum"],
            "text_vollstaendig": f"{found}/{total}",
        }
    rows.append(row)

for r in rows:
    print(f"\n{r['datei']} ({r['fall']})\n  Markdown: {r['markdown']['titel']} | {r['markdown']['datum']}")
    for fmt in ("docx", "pdf"):
        x = r[fmt]
        print(f"  {fmt:4}: Titel {'ok ' if x['titel_wie_markdown'] else 'ABW'} {x['titel']!r} | erste Zeile {x['titel_erste_zeile']!r}"
              f" | Datum {'ok ' if x['datum_wie_markdown'] else 'ABW'} {x['datum']} | Text {x['text_vollstaendig']}")

result = ROOT / "results" / f"importtest_{datetime.date.today()}.json"
result.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(f"\nGespeichert: {result.relative_to(ROOT)}")
