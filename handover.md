# Handover – Applied AI Semesterprojekt

**Stand:** 19. Oktober 2026

## Projektziel und bestätigte Leitplanken

Die Semesterarbeit soll einen einfachen Prototyp einer AI Database für Fragen zu einer Sammlung von After-Action-Reports (AARs) hervorbringen. Der Prototyp soll zur Laufzeit ohne Internet funktionieren und zunächst mit zehn fiktiven Beispieldokumenten arbeiten. Diese Daten dienen nur dem Funktionstest, nicht als echte Berichte oder geprüfte Empfehlungen.

- Die lokale Dokumentensammlung ist die einzige Wissensquelle; keine Websuche und keine unbelegten Ergänzungen.
- Antworten dürfen passende Informationen aus mehreren Dokumenten zusammenführen. Die Antwort steht im Vordergrund; Quellenhinweise sollen knapp sein.
- Bei vergleichbarem Kontext die neueste passende Aussage priorisieren und ältere abweichende Stände mit Quelle und Datum als frühere Version kenntlich machen.
- Wenn Kontext oder Gültigkeit nicht vergleichbar sind, keine sichere Priorität behaupten.
- Fehlende Evidenz offen benennen und keine Lücken füllen.
- Für den ersten Prototyp: Markdown/Text, lokaler Dokumentenordner mit gezieltem Import, einfache Browser-Chat-Oberfläche, eigener Mac/Computer ohne zusätzliche GPU.
- Eine spätere Skalierung meint zunächst mehr Dokumente und muss gesondert getestet werden.
- Keine eingestuften Inhalte in dieses Projekt oder in externe Agenten-/Modell-/Webdienste einbringen. Offlinebetrieb ist keine Sicherheitsfreigabe.

## Sitzungsverlauf

1. Die ursprüngliche Projektidee und der längere Gemini-Dialog wurden als Kontext gelesen. Der Gemini-Dialog enthält mehrere iterative Entwürfe und ist keine verbindliche Spezifikation.
2. Das Ziel wurde als Semesterprojekt bestätigt; die zehn zuvor erstellten, iterativ überarbeiteten fiktiven Dokumente sollen als Ausgangspunkt dienen.
3. Interview zu Zielgruppe, Anwendungsfall, Datenquelle, Zeitkonflikten, fehlender Evidenz, Dateiformaten, Import, Quellenhinweisen, Oberfläche, Hardware und Erfolgskriterien durchgeführt.
4. Eine Recherche zu Offline-Architektur und Evaluation wurde in `notes/prototype_proposal.md` zusammengefasst. SQLite-FTS, lokale Embeddings und lokale Modelllaufzeiten sind Vorschläge, noch nicht ausgewählt oder auf der Hardware getestet.
5. Provenienz wurde besprochen: persönliche Rohmaterialien, Gesprächsprotokolle und Agentenentwürfe getrennt halten. `project_brainstorming.md` ist die eigene Kurzbeschreibung mit persönlichen Stichwortergänzungen.
6. `project_brainstorming.md` wurde mit dem Zusatzdatum `19.10.2026` aktualisiert.
7. Als mögliche Modellarbeit wurde ein kleiner Klassifikator besprochen, der zwei Textpassagen als ergänzend, widersprüchlich oder unterschiedlichen Kontexten zugehörig einordnet. Das ist noch nicht als endgültiger Projektumfang beschlossen; Datumsvergleich und Priorisierung sollen transparente Programmregeln bleiben.

## Wichtige Dateien

- `AGENTS.md` – dauerhafte Projektleitplanken und Arbeitsweise für Codex.
- `project_brainstorming.md` – ursprüngliche persönliche Projektbeschreibung und eigene Stichwortergänzungen.
- `KI-Projektideen.md` – Gemini-Gesprächsverlauf; Vorschläge und wechselnde Arbeitsstände.
- `notes/interview_raw.md` – Rohantworten des Projektinterviews.
- `notes/prototype_proposal.md` – vorläufiger Agentenentwurf mit Recherchequellen, Architektur- und Evaluationsvorschlag.

## Offene nächste Schritte

1. Gemeinsam den Prototyp-Entwurf und dessen Umfang prüfen.
2. Die zehn fiktiven Beispieldokumente im Gemini-Verlauf abgleichen und eine konsistente kanonische Fassung auswählen; derzeit sind sie nicht als eigene Quelldateien angelegt.
3. Eine kleine Testsammlung mit erwarteten Belegstellen erstellen: direkte Antworten, ergänzende Quellen, Konflikte, neutrale Fälle und fehlende/uneindeutige Evidenz.
4. Prüfen, ob der Aussagen-Klassifikator ein tragfähiger Semester-Schwerpunkt ist: gelabelte fiktive Textpaare, Datensatzgröße, Baseline und getrennte Testdaten festlegen.
5. Rechner und Betriebssystem genau feststellen und lokale Modell-/Laufzeitoptionen auf tatsächlicher Hardware testen; Offline-Einrichtung, Modelllizenzen und lokale Ressourcen prüfen.
6. Erst danach den minimalen Prototypumfang und konkrete Abhängigkeiten festlegen.
7. Offlinebetrieb praktisch testen und begrenzt dokumentieren; anschließend prüfen, wie sich die Suche mit mehr Dokumenten verhält.

## Relevante bisherige Commits

- `3c636a1` – persönliche Stichwortergänzung mit Datum in `project_brainstorming.md`
- `fcfb342` – Projektleitplanken, Interviewnotizen und Prototyp-Entwurf
- `7778120` – ursprüngliche Brainstorming-Materialien
- `3101832` – Übergabedatei

Beim letzten Statuscheck war nur `.DS_Store` ungetrackt. Nicht versehentlich löschen oder committen, ohne den Nutzer zu fragen. Den exakten aktuellen Stand mit `git status` und `git log` prüfen.
