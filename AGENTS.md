# AGENTS.md – Übergabe und Arbeitsanweisungen

Diese Datei lesen KI-Agenten beim Laden des Repositorys automatisch. Sie beschreibt Stand, Aufbau, Regeln und nächste Schritte so, dass ein Agent ohne Vorwissen weiterarbeiten kann. Ausführliche Begründungen und alle Messungen: `notes/technischer_bericht_de.md`. Einstieg für Menschen: `README.md`.

## 1. Projekt in Kürze

Proof of Concept (PoC) einer „AI Database“: Nutzer stellen Fragen in Alltagssprache zu einer Sammlung von After-Action-Reports (AARs). Der Assistent führt passende Aussagen aus mehreren Berichten zusammen, beachtet zeitliche Änderungen und Kontext, nennt die Quellen mit Titel und Datum und sagt offen, wenn die Berichte nichts enthalten. Entstanden als Semesterarbeit (Abgabe 14.12.2026) mit Policy Brief an einen militärischen Vorgesetzten und technischem Bericht.

**Stand 15.11.2026:** PoC abgeschlossen. Aufbau v19 (Aussagen-Datenbank, Auswahl der Berichte, Antwortregeln 1–8, Zitat- und Aktualitätsprüfung) läuft in der Oberfläche. Offline-Betrieb und Modellgrößen-Vergleich gemessen (v20, v21). Alle Daten sind fiktiv (`dataset-v4`, 58 Berichte, 34 Testfragen).

## 2. Bestätigte Anforderungen

- Die lokale Dokumentensammlung ist die **einzige Wissensquelle**. Keine Websuche, kein unbelegtes Ergänzen aus Modellwissen – auch nicht, wenn das Modell über eine Cloud-API läuft.
- **Regeln und Verfahren:** Der jüngste vergleichbare Stand bestimmt die Antwort. Ältere Verfahren nicht als gleichrangige Alternativen nennen; frühere Stände nur, wenn ausdrücklich nach Änderungen gefragt wird. Keine Quelle als formell gültig oder verbindlich bezeichnen, wenn das Material das nicht belegt.
- **Erfahrungen und Einschätzungen:** unterschiedliche Sichtweisen mit Quelle und Datum nebeneinander, mit Hinweis, dass die Berichte auseinandergehen; das Datum allein begründet keinen Vorrang.
- **Zusammenfassungen** zu einem Thema müssen möglich sein und folgen denselben Regeln.
- **Kontext:** Wenn Dokumente unterschiedliche Kontexte betreffen oder keine sichere Priorisierung zulassen, keine Priorität behaupten. Aussagen aus einem anderen Kontext als dem gefragten (andere Veranstaltung, Lage, Ort) gehören nicht in die Antwort; unmarkiert gelten sie als Fehler. Ausnahmen, je höchstens ein gekennzeichneter Satz: die Frage lässt den Kontext offen und die Berichte unterscheiden sich je Kontext; oder zum gefragten Kontext gibt es nichts (dann erst die Lücke, dann der nächstliegende Kontext).
- **Belege:** Antwort zuerst, kompakte Quellen am Ende mit Titel und Datum (Datum allein reicht nicht); Fußnotennummern im Text.
- **Knapp:** nur was zur Frage gehört, ohne Einleitung und Wiederholungen.
- **Lücken:** Bei unzureichender Evidenz offen sagen, nichts auffüllen – auch bei Teilfragen.
- **Automatische Erfassung:** Neue oder geänderte Dokumente im Ablageordner werden ohne manuellen Import bei der nächsten Suche berücksichtigt; jedes Dokument wird nur einmal verarbeitet.
- **Skalierung:** Ergebnisse gelten nur für die getestete Datensatzgröße; in Bewertungen immer die Zahl der Berichte angeben.

## 3. Aufbau

Datenfluss: Ablageordner → Abgleich über Fingerabdrücke → Zerlegung neuer Berichte in Aussagen (Thema, Art, Kontext, wörtliches Zitat; Titel und Datum vom Programm) → Suche der 40 besten Aussagen (lokal, `intfloat/multilingual-e5-small`) → deren Berichte vollständig an das Antwortmodell → Zitatprüfung, Fußnoten, Warnung bei möglicherweise überholten Aussagen → Oberfläche.

Grundsatz: **Was sich nachprüfen lässt (Daten, Zitate, Vorhandensein, Aktualität), gehört ins Programm; Sprachverständnis bleibt beim Modell.**

| Pfad | Inhalt |
|---|---|
| `app/app.py` | Streamlit-Oberfläche; Abgleich vor jeder Frage; Attrappe (kostenlos, eigene DB) oder Gemini |
| `app/aidb.py` | Lesen (md, txt, docx, pdf), Titel/Datum, Antwort anfordern, robustes JSON, Zitatprüfung, Fußnoten |
| `app/aussagen.py` | Aussagen-Datenbank (SQLite in `index/`, von Git ignoriert), Abgleich, Zerlegung |
| `app/suche.py` | Auswahl der Berichte, Aktualitätsprüfung (Schwellen an v17–v19 abgestimmt) |
| `app/prompt_antwort.txt` | Antwortregeln 1–8 (Stand v19) |
| `app/prompt_aussagen.txt` | Anweisung zur Zerlegung in Aussagen |
| `scripts/aussagen_einlesen.py` | Ordner mit der Datenbank abgleichen (mit `--modell` kostenpflichtig) |
| `scripts/antwortlauf_aussagen.py` | Antwortläufe über alle Testfragen; `--volltext` (Aufbau v16+), `--modell` (anderes OpenRouter-Modell), `--lokal` (Ollama) |
| `scripts/regelbewertung.py` | regelbasierte Bewertung (Pflicht-/verbotene Inhalte je Frage) |
| `scripts/aussagen_pruefen.py`, `aktualitaet_pruefen.py` | Suchtest und Aktualitätsprüfung an vorhandenen Antworten (kostenlos) |
| `scripts/grafik_modellgroesse.py` | Abbildung Modellvergleich (DE/EN) |
| `scripts/offline_lauf.sh` | Offline-Lauf mit lokalem Modell und Netzprotokoll |
| `scripts/import_test.py` | Word/PDF-Importtest (kostenlos) |
| `data/synthetic_reports/` | 58 fiktive Berichte, `test_questions.md` (Kriterien), `noetig_v4.json` (nötige Berichte je Frage), `README.md` (Fallenkatalog) |
| `results/` | Rohantworten und Bewertungen je Lauf (`_v1`…`_v21`, `_s1`…`_s5`) |
| `notes/` | technischer Bericht, Policy-Brief-Arbeitsdateien, Abbildungen |
| `verlauf/` | frühe Materialien (Interview, Ideen, Notebooks v1–v13); nicht der aktuelle Stand |

Datenstände als Git-Tags `dataset-v1` … `dataset-v4`.

## 4. Befehle

Alle Befehle im Projektordner.

- Einrichten: `python3 -m venv .venv && .venv/bin/pip install -r app/requirements.txt`
- Oberfläche: `.venv/bin/streamlit run app/app.py` (http://localhost:8501; Standard Attrappe)
- Abgleich mit Modell: `.venv/bin/python scripts/aussagen_einlesen.py --modell`
- Antwortlauf: `.venv/bin/python scripts/antwortlauf_aussagen.py --volltext --version vNN --durchlaeufe 3` (zuerst Kostenprobe mit `--nur <Fragen>`)
- Bewertung: `.venv/bin/python scripts/regelbewertung.py -n results/ergebnisse_*_vNN.json`
- Offline: Ollama installieren, Modell laden, `bash scripts/offline_lauf.sh <modell> vNN`
- API-Schlüssel nur lokal in `.env` (`OPENROUTER_API_KEY=...`), nie committen.

## 5. Regeln für Agenten

- **Nur fiktive oder ausdrücklich offene Daten.** Keine eingestuften Inhalte in Agenten, Modell- oder Webdiensten; der PoC sendet Berichtstext an eine Cloud-API.
- Beispiele und Antworten auf Informationsabruf, Quellen, Zeitbezug, Widerspruchserkennung und Evaluation ausrichten, nicht auf die praktische Durchführung militärischer oder gewaltsamer Handlungen.
- **Kosten:** Läufe mit echtem Modell kosten Guthaben – vorher mit dem Projektinhaber abstimmen, Kostenprobe mit zwei Fragen.
- **Messen statt behaupten:** Keine Evaluationsergebnisse ohne Messung; eine Änderung je Version; in der Regel drei Durchläufe.
- **Ergebnisse:** `results/` nie überschreiben; neue Läufe mit neuer Versionsnummer; Bewertung als `bewertung_*.md` mit Aufbau, Maßstab, Kennzahlen, Grenzen und Zahl der Berichte.
- **Löschen:** nie endgültig; Dateien mit `trash` verschieben (Ersatz: `.trash/` im Projektordner, von Git ignoriert, nichts überschreiben). Rohdaten, Ergebnisse und Interview-Notizen nur mit ausdrücklicher Zustimmung verschieben oder ersetzen.
- Abhängigkeiten, Datenquellen und Modelle offenlegen, bevor sie eingeführt werden; Lizenzen prüfen.
- Bestätigte Anforderungen, Vorschläge und ungeprüfte Annahmen unterscheiden; bei Scope- oder Designentscheidungen nachfragen.
- Dokumentation knapp, aktuell und ohne Dopplungen halten; Veraltetes nach `verlauf/` oder entfernen statt liegen lassen.
- Lizenz: noch keine gewählt (nach Rücksprache); bis dahin keine Lizenzdatei anlegen.

## 6. Offene nächste Schritte

1. Pilot mit echten, offenen AARs eines Bereichs auf eigener Hardware im geschlossenen Netz; offenes Modell der ~120-Mrd.-Klasse; Antwortregeln auf das Zielmodell abstimmen; gleiche Messgrößen (Testfragen wiederverwendbar).
2. Mehrnutzerbetrieb mit Anmeldung, Zugriffsrechten nach Einstufung und Personenkreis, Lasttest.
3. Themenübergreifende Sammelfragen verbessern (Gäste-Frage findet nicht alle Berichte).
4. Aktualitätsprüfung für andere Modelle neu abstimmen (erkennt dort nur 30–56 % der Fehler).
5. Texterkennung für eingescannte Berichte; Anbindung an vorhandene Ablagesysteme.
6. Optional: Klassifikator „ergänzend / widersprüchlich / anderer Kontext“; Datumsvergleich und Priorisierung bleiben transparente Programmregeln.

## 7. Arbeitsweise mit dem Projektinhaber bis zur Abgabe (14.12.2026)

- Schrittweise arbeiten, Fachbegriffe und Entscheidungen in verständlichem Deutsch erklären.
- Policy Brief: Adressat ist ein militärischer Vorgesetzter, der den Vorschlag befürworten und weitertragen soll; bewertet von der Kursleitung. Der Projektinhaber schreibt das Brief auf Englisch aus `notes/policy_brief_stichpunkte.md` (Gliederung nach `notes/policy_brief_vorgaben_kurs.md`), am Ende Übersetzung ins Deutsche. Technischer Bericht vom Agenten, Deutsch und Englisch.
- Abgabeform (Nutzer, 15.11.2026): ein finales PDF – Policy Brief, als Anlagen der technische Bericht und die Demo-Seite (aufgezeichnete Antworten; interaktiv unter claude.ai, für das PDF als statische Fassung). Zwei Fassungen: englisches PDF mit englischem Bericht und englischer Demo, deutsches PDF mit deutschem Bericht und deutscher Demo.
- Neue Erkenntnisse, Grenzen und Empfehlungen nach jedem Versuch oder jeder Entscheidung in `notes/policy_brief_notes.md` eintragen, gegliedert wie das Brief, mit Herkunft (Messung, Nutzer, Vorschlag).
- Nach der Abgabe: Brief-Arbeitsdateien aufräumen, Endfassungen ablegen, diesen Abschnitt entfernen.
