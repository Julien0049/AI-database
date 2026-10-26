# Projektkontext und Arbeitsweise

## Projektziel

Die Semesterarbeit soll einen einfachen, lokal betriebenen Prototyp einer AI Database hervorbringen. Einzelne Nutzer sollen Fragen zu einer Sammlung von After-Action-Reports (AARs) stellen können. Der Prototyp soll passende Aussagen aus mehreren Dokumenten zusammenführen, zeitliche Änderungen berücksichtigen und die verwendeten Quellen knapp nennen.

Der Prototyp muss zur Laufzeit ohne Internetzugriff funktionieren. Für die Entwicklung sind zunächst zehn fiktive Beispieldokumente vorgesehen. Sie sind Testdaten, keine echten Berichte, gültige Doktrin oder fachlich geprüfte Empfehlungen.

## Bestätigte Anforderungen

- Die lokale Dokumentensammlung ist die einzige Wissensquelle für Antworten. Keine Websuche und kein nicht belegtes Ergänzen aus Modellwissen.
- Bei vergleichbarem Kontext soll die jüngste passende Aussage die praktische Antwort bestimmen. Die Nutzerantwort soll keine älteren Verfahren als gleichrangige Alternativen auflisten; sie nennt knapp die Quellen, die die Antwort stützen. Die Erkennung älterer Widersprüche wird separat in der Evaluation bewertet. Keine Quelle als formell gültig oder verbindlich bezeichnen, wenn das Material das nicht belegt.
- Wenn Dokumente unterschiedliche Kontexte betreffen oder keine sichere Priorisierung zulassen, darf der Agent keine Priorität behaupten. Ein jüngeres Dokument beweist nicht, dass eine Aussage wahr oder verbindlich ist.
- Ergänzende Aussagen aus mehreren Quellen dürfen zu einer klaren Antwort zusammengeführt werden. Die Antwort steht im Vordergrund; kompakte Quellenhinweise (mindestens Dokument und Datum) folgen am Ende.
- Bei unzureichender Evidenz muss der Prototyp dies offen sagen und darf Lücken nicht auffüllen.
- Für die erste Version sind Markdown-/Textdateien vorgesehen. Neue Dokumente liegen in einem festgelegten lokalen Ordner; der Import wird gezielt gestartet.
- Als erste Oberfläche ist eine einfache lokale Browser-Chat-Oberfläche vorgesehen. Zielhardware ist der eigene Mac/Computer ohne zusätzliche GPU.
- Der erste Datensatz umfasst zehn Beispiele. Spätere Skalierung bedeutet zunächst mehr Dokumente; sie muss separat geprüft werden und ist mit zehn Beispielen nicht belegt.

## Projektdateien und Provenienz

- `project_brainstorming.md` enthält die ursprüngliche Kurzbeschreibung.
- `KI-Projektideen.md` enthält einen langen Gemini-Dialog mit mehreren iterativ überarbeiteten Projekt- und Beispieldokument-Entwürfen. Diese Fassungen sind Arbeitsmaterial, nicht automatisch eine konsistente oder verbindliche Spezifikation.
- Interview-Rohnotizen und Agentenentwürfe sollen getrennt aufbewahrt werden. Rohnotizen nicht stillschweigend umformulieren; abgeleitete Anforderungen und Vorschläge als solche kennzeichnen.

## Arbeitsweise für Agenten

- Arbeite schrittweise und erkläre Fachbegriffe sowie technische Entscheidungen in verständlichem Deutsch.
- Unterscheide bestätigte Anforderungen, Vorschläge und ungeprüfte Annahmen. Frage bei wesentlichen Scope- oder Designentscheidungen nach; triff kleine, reversible Entscheidungen begründet.
- Unterstütze nachvollziehbare Entscheidungen und den Lernprozess. Erzeuge keine großen Mengen an Code oder Daten, bevor Projektfrage und Versuchsaufbau geklärt sind.
- Lege Abhängigkeiten, Datenquellen und Modellanforderungen offen, bevor du sie einführst. Behaupte keine Evaluationsergebnisse, bevor sie gemessen wurden.
- Halte Dokumentation knapp, aktuell und ohne doppelte oder widersprüchliche Anweisungen.

## Inhaltliche und Evaluationsleitplanken

- Verwende für Prototyp und Experimente ausschließlich ausdrücklich fiktive oder unklassifizierte Beispieldaten. Keine eingestuften Inhalte in Agenten, Modell- oder Webdiensten verwenden.
- Richte Beispiele und Antworten auf Informationsabruf, Quellenbelege, Zeitbezug, Widerspruchserkennung und Evaluation aus, nicht auf die praktische Durchführung militärischer oder gewaltsamer Handlungen.
- Prüfe getrennt, ob relevante Quellen gefunden, Aussagen ausreichend belegt, zeitliche Konflikte erkannt und unbelegte Fragen korrekt zurückgewiesen werden.
- Berichte die Grenzen des kleinen synthetischen Datensatzes und der verwendeten Metriken.
- Als mögliche, noch nicht festgelegte Modellarbeit wird ein kleiner Klassifikator erwogen, der zwei Textstellen als ergänzend, widersprüchlich oder unterschiedlichen Kontexten zugehörig einordnet. Datumsvergleich und Priorisierung bleiben davon getrennte, transparente Programmregeln.
