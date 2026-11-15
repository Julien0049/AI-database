# Projektkontext und Arbeitsweise

## Projektziel

Die Semesterarbeit soll einen Proof of Concept (PoC) einer AI Database hervorbringen. Einzelne Nutzer sollen Fragen zu einer Sammlung von After-Action-Reports (AARs) stellen können. Der PoC soll passende Aussagen aus mehreren Dokumenten zusammenführen, zeitliche Änderungen berücksichtigen und die verwendeten Quellen knapp nennen.

Für den PoC wird vorläufig Gemini 2.5 Pro (`google/gemini-2.5-pro`) über OpenRouter verwendet, bezahlt aus einem vorhandenen Guthaben; darüber hinaus sollen keine eigenen Kosten entstehen. Anfragen laufen damit über zwei Anbieter (OpenRouter und Google). Der API-Schlüssel wird nur lokal (Umgebungsvariable oder `.env`) gespeichert und nie ins Repository übernommen. Der PoC darf zur Laufzeit Internet für die Modell-API nutzen. Offlinebetrieb mit einem lokalen, mittelgroßen Modell ist eine spätere Ausbaustufe, nicht Teil des PoC. Die Entwicklung begann mit einem kleinen Datensatz fiktiver Berichte (anfangs zehn), um die Antwortregeln zu prüfen; danach wird der Datensatz schrittweise vergrößert, um zu sehen, wie der PoC mit größeren Mengen umgeht. Der aktuelle Stand liegt in `data/synthetic_reports/`. Die Berichte sind Testdaten, keine echten Berichte, gültige Doktrin oder fachlich geprüfte Empfehlungen.

## Bestätigte Anforderungen

- Die lokale Dokumentensammlung ist die einzige Wissensquelle für Antworten. Keine Websuche und kein nicht belegtes Ergänzen aus Modellwissen. Das gilt auch, wenn das Antwortmodell über eine Cloud-API läuft.
- Bei Regeln und Verfahren bestimmt der jüngste vergleichbare Stand die Antwort. Bei Erfahrungen und Einschätzungen werden unterschiedliche Sichtweisen mit Quelle und Datum nebeneinander genannt, mit dem Hinweis, dass die Berichte auseinandergehen; das Datum allein begründet dort keine Priorität.
- Zusammenfassungen aller Inhalte zu einem Thema müssen möglich sein. Sie geben bei Regeln und Verfahren nur den jüngsten vergleichbaren Stand wieder; frühere Stände erscheinen nur, wenn ausdrücklich nach Änderungen gefragt wird. Erfahrungen werden wie oben mit abweichenden Sichtweisen wiedergegeben.
- Für Regeln und Verfahren gilt außerdem: Die Nutzerantwort soll keine älteren Verfahren als gleichrangige Alternativen auflisten; sie nennt knapp die Quellen, die die Antwort stützen. Die Erkennung älterer Widersprüche wird separat in der Evaluation bewertet. Keine Quelle als formell gültig oder verbindlich bezeichnen, wenn das Material das nicht belegt.
- Wenn Dokumente unterschiedliche Kontexte betreffen oder keine sichere Priorisierung zulassen, darf der Agent keine Priorität behaupten. Ein jüngeres Dokument beweist nicht, dass eine Aussage wahr oder verbindlich ist.
- Aussagen aus einem anderen Kontext als dem gefragten (andere Veranstaltung, Lage, Ort) dürfen nur mit ausdrücklicher Kennzeichnung des Kontexts in die Antwort; unmarkiert gelten sie als Fehler, auch wenn sie belegt sind (Nutzer, 14.11.2026). Verwandtes, aber nicht Gefragtes gehört nicht in die Antwort. Ausnahmen (Nutzer, 14.11.2026): Die Frage lässt den Kontext offen und die Berichte unterscheiden sich je Kontext, oder zum gefragten Kontext gibt es nichts; dann Lücke nennen plus ein gekennzeichneter Hinweis auf den nächstliegenden Kontext, weil Nutzer ihre Frage nicht immer genau genug stellen.
- Ergänzende Aussagen aus mehreren Quellen dürfen zu einer klaren Antwort zusammengeführt werden. Die Antwort steht im Vordergrund; kompakte Quellenhinweise folgen am Ende, mindestens mit Titel und Datum des Berichts; das Datum allein reicht nicht, da an einem Tag viele Berichte entstehen können. Fußnotennummern im Text verweisen auf diese Liste, damit erkennbar ist, welche Aussage aus welchem Bericht stammt.
- Antworten sollen exakt und schlank sein: nur was zur Frage gehört, ohne Einleitung und Wiederholungen.
- Bei unzureichender Evidenz muss der Prototyp dies offen sagen und darf Lücken nicht auffüllen.
- Für die erste Version sind Markdown-/Textdateien vorgesehen. Neue oder geänderte Dokumente in einem festgelegten Ordner werden automatisch erfasst und sind ohne manuellen Import bei der nächsten Suche berücksichtigt. Jedes Dokument wird dabei nur einmal verarbeitet. (Geändert am 13.11.2026; vorher: Import gezielt starten.)
- Als erste Oberfläche ist eine einfache lokale Browser-Chat-Oberfläche vorgesehen. Anwendung, Dokumente und Index laufen auf dem eigenen Mac/Computer ohne zusätzliche GPU; nur die Antwortgenerierung läuft über die Modell-API.
- Spätere Ausbaustufen (nicht Teil des PoC): Umstieg auf ein lokales, mittelgroßes Modell mit Offlinebetrieb und Vergleich gegen die Frontier-Ergebnisse; optional Aussagen-Klassifikator und lokaler Mehrnutzerbetrieb.
- Skalierung bedeutet zunächst mehr Dokumente. Ergebnisse gelten nur für die getestete Datensatzgröße; jede Vergrößerung muss separat geprüft werden. In Bewertungen und Notizen die Anzahl der Berichte des jeweiligen Laufs angeben.

## Projektdateien und Provenienz

- `project_brainstorming.md` enthält die ursprüngliche Kurzbeschreibung.
- `KI-Projektideen.md` enthält einen langen Gemini-Dialog mit mehreren iterativ überarbeiteten Projekt- und Beispieldokument-Entwürfen. Diese Fassungen sind Arbeitsmaterial, nicht automatisch eine konsistente oder verbindliche Spezifikation.
- Interview-Rohnotizen und Agentenentwürfe sollen getrennt aufbewahrt werden. Rohnotizen nicht stillschweigend umformulieren; abgeleitete Anforderungen und Vorschläge als solche kennzeichnen.

## Projektstruktur

- `app/` – lokale Streamlit-Oberfläche (`app.py`) und Kernlogik (`aidb.py`: Import, Antwort, Zitatprüfung); Antwort-Prompt in `prompt_antwort.txt`; Details in `app/README.md`.
- `data/synthetic_reports/` – fiktive Testberichte (AAR-*.md); `data/format_test/` – erzeugte Word/PDF-Kopien aus dem Importtest (von Git ignoriert).
- `notebooks/` – Versuche (Gemini-Ersttest, Retrieval, Zitatprüfung v7).
- `scripts/` – `import_test.py` prüft Word-/PDF-Import gegen Markdown (ohne Modell, ohne Kosten).
- `results/` – Rohantworten und Bewertungen je Versuchslauf (versioniert, z.B. `_v10`); nicht überschreiben, neue Läufe mit neuer Versionsnummer ablegen.
- `notes/` – Interview-Rohnotizen, Prototyp-Vorschlag, Policy-Brief-Notizen und -Entwurf.
- `protokoll/` – lokales Frage-/Antwortprotokoll der Oberfläche (von Git ignoriert).

## Befehle

Alle Befehle im Projektordner ausführen.

- Einrichten: `python3 -m venv .venv && .venv/bin/pip install -r app/requirements.txt`
- Oberfläche starten: `.venv/bin/streamlit run app/app.py` (http://localhost:8501; Standard ist die kostenlose Attrappe, echte Antworten erst nach Umschalten auf Gemini 2.5 Pro)
- Importtest: `.venv/bin/pip install -r scripts/requirements-importtest.txt`, dann `.venv/bin/python scripts/import_test.py`
- Läufe mit echtem Modell kosten Guthaben: vorher mit dem Nutzer abstimmen.

## Arbeitsweise für Agenten

- Arbeite schrittweise und erkläre Fachbegriffe sowie technische Entscheidungen in verständlichem Deutsch.
- Unterscheide bestätigte Anforderungen, Vorschläge und ungeprüfte Annahmen. Frage bei wesentlichen Scope- oder Designentscheidungen nach; triff kleine, reversible Entscheidungen begründet.
- Unterstütze nachvollziehbare Entscheidungen und den Lernprozess. Erzeuge keine großen Mengen an Code oder Daten, bevor Projektfrage und Versuchsaufbau geklärt sind.
- Lege Abhängigkeiten, Datenquellen und Modellanforderungen offen, bevor du sie einführst. Behaupte keine Evaluationsergebnisse, bevor sie gemessen wurden.
- Halte Dokumentation knapp, aktuell und ohne doppelte oder widersprüchliche Anweisungen.
- Abgabe voraussichtlich am 14.12.2026.
- Policy Brief: Adressat ist ein militärischer Vorgesetzter, der den Vorschlag befürworten und weitertragen soll; bewertet wird er von der Kursleitung. Ton und Argumentation auf den Entscheider ausrichten, fachlich so belastbar, dass er der Bewertung standhält.
- Am Ende steht ein Policy Brief. Trage neue Erkenntnisse, Grenzen, Empfehlungen und nächste Schritte nach jedem Versuch oder jeder Entscheidung direkt in `notes/policy_brief_notes.md` ein, gegliedert wie das Brief und mit Kennzeichnung der Herkunft (Messung, Nutzer, Vorschlag), sodass der Nutzer die Abschnitte ohne erneute Aufarbeitung übernehmen kann.

## Dateien löschen

- Nie endgültig löschen; Dateien mit `trash` in den Papierkorb verschieben.
- Ersatz-Papierkorb, falls `trash` nicht verfügbar ist oder fehlschlägt: `.trash/` im Projektordner (von Git ignoriert). Nie ein vorhandenes Element überschreiben; bei Namensgleichheit einen Zeitstempel anhängen (z.B. `notes_2026-11-12T1530.md`) und den Wiederherstellungsort melden.
- Rohdaten, Testergebnisse (`results/`) und Interview-Rohnotizen nie ohne ausdrückliche Bestätigung verschieben oder ersetzen.

## Inhaltliche und Evaluationsleitplanken

- Verwende für Prototyp und Experimente ausschließlich ausdrücklich fiktive oder unklassifizierte Beispieldaten. Keine eingestuften Inhalte in Agenten, Modell- oder Webdiensten verwenden. Da der PoC Dokumentpassagen an eine Cloud-API sendet, gilt das besonders für alle importierten Dokumente.
- Richte Beispiele und Antworten auf Informationsabruf, Quellenbelege, Zeitbezug, Widerspruchserkennung und Evaluation aus, nicht auf die praktische Durchführung militärischer oder gewaltsamer Handlungen.
- Prüfe getrennt, ob relevante Quellen gefunden, Aussagen ausreichend belegt, zeitliche Konflikte erkannt und unbelegte Fragen korrekt zurückgewiesen werden.
- Berichte die Grenzen des kleinen synthetischen Datensatzes und der verwendeten Metriken.
- Als mögliche, noch nicht festgelegte spätere Modellarbeit (nicht Teil des PoC) wird ein kleiner Klassifikator erwogen, der zwei Textstellen als ergänzend, widersprüchlich oder unterschiedlichen Kontexten zugehörig einordnet. Datumsvergleich und Priorisierung bleiben davon getrennte, transparente Programmregeln.
