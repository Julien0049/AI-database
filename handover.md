# Handover – Applied AI Semesterprojekt

**Stand:** 26. Oktober 2026

## Projektziel und bestätigte Leitplanken

Die Semesterarbeit soll einen Proof of Concept (PoC) einer AI Database für Fragen zu einer Sammlung von After-Action-Reports (AARs) hervorbringen. Der PoC nutzt ein Frontier-Modell über OpenRouter (vorläufig Gemini 2.5 Pro, bezahlt aus vorhandenem Guthaben) und arbeitet zunächst mit zehn fiktiven Beispieldokumenten. Diese Daten dienen nur dem Funktionstest, nicht als echte Berichte oder geprüfte Empfehlungen. Offlinebetrieb mit einem lokalen, mittelgroßen Modell ist eine spätere Ausbaustufe.

- Die lokale Dokumentensammlung ist die einzige Wissensquelle; keine Websuche und keine unbelegten Ergänzungen.
- Antworten dürfen passende Informationen aus mehreren Dokumenten zusammenführen. Die Antwort steht im Vordergrund; Quellenhinweise sollen knapp sein.
- Bei vergleichbarem Kontext die neueste passende Aussage priorisieren und ältere abweichende Stände mit Quelle und Datum als frühere Version kenntlich machen.
- Wenn Kontext oder Gültigkeit nicht vergleichbar sind, keine sichere Priorität behaupten.
- Fehlende Evidenz offen benennen und keine Lücken füllen.
- Für den PoC: Markdown/Text, lokaler Dokumentenordner mit gezieltem Import, einfache Browser-Chat-Oberfläche auf dem eigenen Mac/Computer; nur die Antwortgenerierung läuft über die Modell-API.
- Eine spätere Skalierung meint zunächst mehr Dokumente und muss gesondert getestet werden.
- Keine eingestuften Inhalte in dieses Projekt oder in externe Agenten-/Modell-/Webdienste einbringen. Der PoC sendet Passagen an eine Cloud-API; ein späterer Offlinebetrieb wäre ebenfalls keine Sicherheitsfreigabe.

## Sitzungsverlauf

1. Die ursprüngliche Projektidee und der längere Gemini-Dialog wurden als Kontext gelesen. Der Gemini-Dialog enthält mehrere iterative Entwürfe und ist keine verbindliche Spezifikation.
2. Das Ziel wurde als Semesterprojekt bestätigt; die zehn zuvor erstellten, iterativ überarbeiteten fiktiven Dokumente sollen als Ausgangspunkt dienen.
3. Interview zu Zielgruppe, Anwendungsfall, Datenquelle, Zeitkonflikten, fehlender Evidenz, Dateiformaten, Import, Quellenhinweisen, Oberfläche, Hardware und Erfolgskriterien durchgeführt.
4. Eine Recherche zu Offline-Architektur und Evaluation wurde in `notes/prototype_proposal.md` zusammengefasst. SQLite-FTS, lokale Embeddings und lokale Modelllaufzeiten sind Vorschläge, noch nicht ausgewählt oder auf der Hardware getestet.
5. Provenienz wurde besprochen: persönliche Rohmaterialien, Gesprächsprotokolle und Agentenentwürfe getrennt halten. `project_brainstorming.md` ist die eigene Kurzbeschreibung mit persönlichen Stichwortergänzungen.
6. `project_brainstorming.md` wurde mit dem Zusatzdatum `19.10.2026` aktualisiert.
7. Als mögliche Modellarbeit wurde ein kleiner Klassifikator besprochen, der zwei Textpassagen als ergänzend, widersprüchlich oder unterschiedlichen Kontexten zugehörig einordnet. Das ist noch nicht als endgültiger Projektumfang beschlossen; Datumsvergleich und Priorisierung sollen transparente Programmregeln bleiben.
8. Mehrnutzerbetrieb auf einem lokalen Server mit Anmeldung und Zugriffsrechten wurde als mögliche spätere Erweiterung eingeordnet. Der Nutzer würde es gern ausprobieren, falls Zeit und Infrastruktur es erlauben; es ist kein Muss. Dafür wären mindestens ein Serverrechner und zusätzliche Clientgeräte nötig. Der Ein-Rechner-Prototyp bleibt das ausreichende Kernziel.
9. Fünf kurze, einheitlich formatierte, harmlose synthetische AARs zur Materialverwaltung wurden als kontrollierte Textbasis in `data/synthetic_reports/` erstellt.
10. Sechs Testfragen und knappe Antwortentwürfe in `data/synthetic_reports/test_questions.md` wurden einzeln mit dem Nutzer geprüft. Nutzerantworten sollen beim Widerspruchsfall nur die neueste passende Aussage und deren stützende Quelle(n) nennen; die Erkennung älterer Widersprüche wird intern separat bewertet. Quellen nicht als formell gültig bezeichnen, wenn das Material keine Verbindlichkeit belegt.
11. Scope-Änderung: Das Projekt ist jetzt ein Proof of Concept mit einem Frontier-Modell über Cloud-API. Vorläufige Wahl: Gemini-API im kostenlosen Kontingent mit vorhandenem Schlüssel; Limits und mögliche Datennutzung durch Google werden akzeptiert, da nur fiktive Daten verwendet werden. Gemini 4 Argon wurde geprüft und verworfen, weil es laut Google (Stand Oktober 2026) nicht im kostenlosen Kontingent enthalten ist; der PoC bleibt bewusst kostenlos. Vorläufiges Modell: zunächst Gemini 3.8 Flash geplant; da der vorhandene kostenlose Schlüssel nur Gemini 2.5 Flash freigibt, wird Gemini 2.5 Flash verwendet. Für den ersten Test wurde dann Gemini 2.5 Pro über OpenRouter mit vorhandenem Guthaben genutzt und als vorläufiges Modell übernommen; Anfragen laufen dabei über OpenRouter und Google. Gemini 2.5 Pro ist eine ältere Modellgeneration als Gemini 3.8 Flash. Mögliche spätere, kostenpflichtige Referenz für einen einmaligen Messlauf: Gemini 4 Argon oder Claude Opus 5.5 (nicht beschlossen). Offlinebetrieb mit lokalem, mittelgroßem Modell, Aussagen-Klassifikator und Mehrnutzerbetrieb sind spätere Optionen, nicht Teil des PoC.
12. Erster Modelltest mit Gemini 2.5 Pro über OpenRouter in Colab (`notebooks/gemini_first_test.ipynb`), alle fünf Berichte vollständig im Prompt, ohne Suche. Antworten in `results/ergebnisse_google_gemini-2.5-pro_2026-10-26.json`, Agentenbewertung in `results/bewertung_google_gemini-2.5-pro_2026-10-26.md` (noch vom Nutzer zu prüfen).
13. Datensatz erweitert: Stand mit fünf Material-AARs und sechs Fragen als Git-Tag `dataset-v1` markiert; fünf AARs zur Fahrzeugausleihe und Fragen 7–10 ergänzt; die Fragen wurden vom Nutzer durchgesehen und bestätigt. Im Bericht zum Fahrtenbuch-Formular ist die abweichende Tankregel auf Wunsch des Nutzers nur beiläufig und nicht als Änderung formuliert.
14. Zweiter Lauf mit zehn Berichten und zehn Fragen ausgewertet (`results/bewertung_google_gemini-2.5-pro_2026-10-26_v2.md`): 7 erfüllt, 3 teilweise. Auf Wunsch des Nutzers wurde Regel 6 im Systemprompt ergänzt: Fehlende Informationen müssen auch bei Teilfragen ausdrücklich benannt werden, weil der Anwender das wissen muss. Der nächste Lauf prüft diese Änderung (Fragen 5 und 9).
15. Anforderung präzisiert (vom Nutzer bestätigt): Bei Regeln und Verfahren bestimmt der jüngste vergleichbare Stand die Antwort; bei Erfahrungen und Einschätzungen werden unterschiedliche Sichtweisen mit Quelle und Datum nebeneinander genannt, mit Hinweis auf die Abweichung. Geplant nach Lauf v3: drei Erfahrungsberichte zu Winterkleidung bei mehrtägigen Außenseminaren (E1 15.02.2023 Schichten statt Daunenjacke, E2 25.01.2024 Daunenjacke bei langen Wartezeiten, E3 10.12.2025 Wollsocken, Uneinigkeit bei Jacken, vorgeschriebene wasserdichte Überjacke) und Fragen 11–13. Danach Lauf v4 mit unverändertem Prompt, Lauf v5 mit ergänzter Erfahrungsregel im Prompt.
16. Lauf v3 ausgewertet (`results/bewertung_google_gemini-2.5-pro_2026-10-27_v3.md`): 7 erfüllt, 3 teilweise wie in Lauf 2. Ergänzte Regel 6 ohne sichtbare Wirkung auf Fragen 5 und 9; falsche Zusatzquelle bei Frage 4 wiederholt; fehlende Daten in Quellenangaben treten bei wechselnden Fragen auf.

## Wichtige Dateien

- `AGENTS.md` – dauerhafte Projektleitplanken und Arbeitsweise für Codex.
- `project_brainstorming.md` – ursprüngliche persönliche Projektbeschreibung und eigene Stichwortergänzungen.
- `KI-Projektideen.md` – Gemini-Gesprächsverlauf; Vorschläge und wechselnde Arbeitsstände.
- `notes/interview_raw.md` – Rohantworten des Projektinterviews.
- `notes/prototype_proposal.md` – vorläufiger Agentenentwurf mit Recherchequellen, Architektur- und Evaluationsvorschlag.
- `data/synthetic_reports/` – fünf fiktive AARs zur Materialverwaltung plus README und geprüfte Testfragen/Antwortentwürfe.

## Offene nächste Schritte

1. Gemeinsam den Prototyp-Entwurf und dessen Umfang prüfen.
2. Die fünf neuen Test-AARs prüfen und entscheiden, wie sie mit den zehn AAR-Entwürfen aus dem Gemini-Verlauf abgeglichen oder erweitert werden.
3. Testfragen und Antwortentwürfe gegen die endgültige Dokumentensammlung prüfen und nach Fertigstellung des Datensatzes einfrieren.
4. Danach den Datensatz schrittweise um längere Inhalte und zusätzliche Dateiformate erweitern; Formaterkennung und Beziehungsanalyse getrennt auswerten.
5. Agentenbewertung des ersten Tests prüfen; Modell für die Messungen nicht wechseln; Guthaben im Blick behalten. API-Schlüssel nur lokal bzw. in Colab-Secrets ablegen.
6. Danach den minimalen PoC-Umfang und konkrete Abhängigkeiten festlegen.
7. PoC umsetzen und an den Testfragen messen; anschließend prüfen, wie sich die Suche mit mehr Dokumenten verhält.
8. Spätere Ausbaustufe: ein lokales, mittelgroßes Modell auf der tatsächlichen Hardware testen, gegen die Frontier-Ergebnisse vergleichen und Offlinebetrieb praktisch prüfen.
9. Weitere spätere Optionen, nur bei Zeit: Aussagen-Klassifikator (gelabelte fiktive Textpaare, Baseline, getrennte Testdaten) und Mehrgerätezugriff im abgeschotteten lokalen Netzwerk. Beides ist kein Muss.

## Relevante bisherige Commits

- `290279b` – optionale lokale Mehrnutzer-Ausbaustufe
- `dbad516` – Klassifikator als mögliche Modellarbeit
- `3101832` – Übergabedatei
- `3c636a1` – persönliche Stichwortergänzung mit Datum in `project_brainstorming.md`
- `fcfb342` – Projektleitplanken, Interviewnotizen und Prototyp-Entwurf
- `7778120` – ursprüngliche Brainstorming-Materialien

Beim letzten Statuscheck waren `project_brainstorming.md` geändert sowie `.DS_Store` und `data/` ungetrackt. `project_brainstorming.md` enthält Änderungen des Nutzers und darf nicht versehentlich überschrieben werden. Vor Commit oder Push den exakten Status prüfen; `.DS_Store` nicht versehentlich aufnehmen.
