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

**Grenzen:** nur Markdown-Dateien `AAR-*.md`; keine Gesprächsfortsetzung (jede Frage einzeln); keine gründliche Sichtung (v13) und keine Suche.
