# Handover – Applied AI Semesterprojekt

**Stand:** 26. Oktober 2026

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
8. Mehrnutzerbetrieb auf einem lokalen Server mit Anmeldung und Zugriffsrechten wurde als mögliche spätere Erweiterung eingeordnet. Der Nutzer würde es gern ausprobieren, falls Zeit und Infrastruktur es erlauben; es ist kein Muss. Dafür wären mindestens ein Serverrechner und zusätzliche Clientgeräte nötig. Der Ein-Rechner-Prototyp bleibt das ausreichende Kernziel.
9. Fünf kurze, einheitlich formatierte, harmlose synthetische AARs zur Materialverwaltung wurden als kontrollierte Textbasis in `data/synthetic_reports/` erstellt.
10. Sechs Testfragen und knappe Antwortentwürfe in `data/synthetic_reports/test_questions.md` wurden einzeln mit dem Nutzer geprüft. Nutzerantworten sollen beim Widerspruchsfall nur die neueste passende Aussage und deren stützende Quelle(n) nennen; die Erkennung älterer Widersprüche wird intern separat bewertet. Quellen nicht als formell gültig bezeichnen, wenn das Material keine Verbindlichkeit belegt.

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
5. Prüfen, ob der Aussagen-Klassifikator ein tragfähiger Semester-Schwerpunkt ist: gelabelte fiktive Textpaare, Datensatzgröße, Baseline und getrennte Testdaten festlegen.
6. Rechner und Betriebssystem genau feststellen und lokale Modell-/Laufzeitoptionen auf tatsächlicher Hardware testen; Offline-Einrichtung, Modelllizenzen und lokale Ressourcen prüfen.
7. Erst danach den minimalen Prototypumfang und konkrete Abhängigkeiten festlegen.
8. Offlinebetrieb praktisch testen und begrenzt dokumentieren; anschließend prüfen, wie sich die Suche mit mehr Dokumenten verhält.
9. Nur wenn nach Fertigstellung des Kernprototyps Zeit und geeignete Infrastruktur verfügbar sind: Mehrgerätezugriff im abgeschotteten lokalen Netzwerk mit Anmeldung/Zugriffsrechten ausprobieren. Andernfalls beim Ein-Rechner-Prototyp bleiben; Mehrnutzerbetrieb ist kein Muss.

## Relevante bisherige Commits

- `290279b` – optionale lokale Mehrnutzer-Ausbaustufe
- `dbad516` – Klassifikator als mögliche Modellarbeit
- `3101832` – Übergabedatei
- `3c636a1` – persönliche Stichwortergänzung mit Datum in `project_brainstorming.md`
- `fcfb342` – Projektleitplanken, Interviewnotizen und Prototyp-Entwurf
- `7778120` – ursprüngliche Brainstorming-Materialien

Beim letzten Statuscheck waren `project_brainstorming.md` geändert sowie `.DS_Store` und `data/` ungetrackt. `project_brainstorming.md` enthält Änderungen des Nutzers und darf nicht versehentlich überschrieben werden. Vor Commit oder Push den exakten Status prüfen; `.DS_Store` nicht versehentlich aufnehmen.
