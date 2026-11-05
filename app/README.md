# Lokale Oberfläche (PoC)

Browser-Chat für Fragen an die Berichte. Aufbau wie Versuch v11: Alle Berichte des gewählten Ordners gehen mit jeder Frage an das Modell; Zitatprüfung und Fußnoten wie im Notebook `citation_check_v7.ipynb`.

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

Der Browser öffnet sich unter `http://localhost:8501`. Links „Importieren“ klicken, dann fragen. Standard ist die **Attrappe** (kostenlos, keine Modellantwort, nur zum Testen der Anzeige); echte Antworten erst nach Umschalten auf Gemini 2.5 Pro.

**Protokoll:** Jede Frage wird mit Antwort, Rohantwort des Modells, Dauer und Kosten in `protokoll/oberflaeche.jsonl` gespeichert (lokal, von Git ausgeschlossen), damit Antworten nachträglich geprüft werden können.

**Folgefragen:** Die letzten drei Fragen des Gesprächs gehen als Kontext mit (nicht die Antworten); „Neues Gespräch“ setzt den Verlauf zurück.

**Formate:** Markdown, Text, Word (`.docx`) und PDF; `README.md` und `test_questions.md` werden übersprungen. Bei PDF geht die Überschrift verloren (Dateiname als Titel), eingescannte PDFs ohne Text werden übersprungen.

**Grenzen:** keine gründliche Sichtung (v13) und keine Suche.
