# Lokale Oberfläche (PoC)

Browser-Chat für Fragen an die Berichte. Aufbau seit 14.11.2026 wie Versuche v16–v19:

- **Automatische Erfassung:** Vor jeder Frage gleicht die Oberfläche den Ordner mit der Aussagen-Datenbank ab (`index/`, von Git ausgeschlossen). Nur neue oder geänderte Berichte werden eingelesen; im Gemini-Modus zerlegt das Modell sie dabei in Aussagen (ca. 2–9 Cent je Bericht, einmalig). Kein Import-Knopf mehr.
- **Auswahl:** Die 40 besten Aussagen (Suche nach Bedeutung, `intfloat/multilingual-e5-small`) bestimmen die relevanten Berichte; diese gehen vollständig an das Modell (`suche.py`).
- **Antwortregeln:** `prompt_antwort.txt` (Regeln 1–8, Stand v19: nur der gefragte Kontext).
- **Programmprüfung:** Belege werden gegen die Datenbank geprüft; gibt es zum selben Thema im selben Kontext einen neueren Stand, erscheint „⚠ Möglicherweise überholt“ unter der Antwort (warnt, löscht nicht; Messung siehe `results/bewertung_aktualitaetspruefung_2026-11-14.md`).
- Zitatprüfung und Fußnoten wie im Notebook `citation_check_v7.ipynb`.

**Einmalig einrichten** (im Projektordner):

```bash
python3 -m venv .venv
.venv/bin/pip install -r app/requirements.txt
```

Für echte Antworten in die Datei `.env` im Projektordner eintragen: `OPENROUTER_API_KEY=...` (die Datei ist von Git ausgeschlossen).

**Starten:**

```bash
.venv/bin/streamlit run app/app.py
```

Der Browser öffnet sich unter `http://localhost:8501`. Der Ordner wird automatisch abgeglichen, dann fragen. Standard ist die **Attrappe** (kostenlos, keine Modellantwort, eigene Datenbank `index/attrappe.sqlite`, nur zum Testen der Anzeige); echte Antworten erst nach Umschalten auf Gemini 2.5 Pro. Beim ersten Start wird das Suchmodell geladen (ca. 470 MB, einmalig).

**Protokoll:** Jede Frage wird mit Antwort, Rohantwort des Modells, ausgewählten Berichten, Warnungen, Dauer und Kosten in `protokoll/oberflaeche.jsonl` gespeichert (lokal, von Git ausgeschlossen), damit Antworten nachträglich geprüft werden können.

**Folgefragen:** Die letzten drei Fragen des Gesprächs gehen als Kontext mit (nicht die Antworten); „Neues Gespräch“ setzt den Verlauf zurück.

**Formate:** Markdown, Text, Word (`.docx`) und PDF; `README.md` und `test_questions.md` werden übersprungen. Bei PDF geht die Überschrift verloren (Dateiname als Titel), eingescannte PDFs ohne Text werden übersprungen.

**Grenzen:** Themenübergreifende Sammelfragen finden nicht immer alle Berichte (Frage 25); die Programmprüfung warnt in ca. 7 % der richtigen Antworten fälschlich (an denselben Daten abgestimmt); Neuaufbau des Suchindex nach jeder Änderung der Datenbank dauert einige Sekunden.
