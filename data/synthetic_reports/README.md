# Synthetische AAR-Testberichte

Diese dreizehn Berichte wurden als fiktives Testmaterial für den AI-Database-Prototyp erstellt. Sie beschreiben ausschließlich harmlose Abläufe: fünf zur Materialrückgabe in Seminaren, fünf zur Fahrzeugausleihe und drei Erfahrungsberichte zur Kleidung bei Winter-Außenseminaren. Sie sind keine echten After-Action-Reports, Vorschriften oder verlässlichen Handlungsanweisungen.

Die einheitlichen Markdown-Dateien bilden zunächst eine kontrollierte Textbasis. Der geplante Testfall soll erkennen, ob ein System:

- widersprüchliche Aussagen zum Rückgabeverfahren bei mehrtägigen Seminaren erkennt;
- ergänzende Informationen zum Umgang mit fehlendem Material zusammenführt;
- eintägige und mehrtägige Veranstaltungen als unterschiedliche Kontexte behandelt.
- einen nicht als Änderung gekennzeichneten Widerspruch zur Tankregel erkennt;
- Fahrzeug- und Materialberichte trotz ähnlicher Stichworte („mehrtägig“, „gemeinsam genutzt“, „keine persönliche Verantwortung“) auseinanderhält.
- bei Erfahrungsberichten unterschiedliche Sichtweisen nebeneinander nennt, statt den jüngsten Bericht als gültigen Stand zu behandeln, und eine darin enthaltene Vorgabe als solche erkennt;
- Zusammenfassungen zu einem Thema vollständig und ohne überholte Verfahren liefert und Änderungen nur auf ausdrückliche Frage chronologisch darstellt.

Der Stand mit nur den fünf Materialberichten und sechs Fragen ist als Git-Tag `dataset-v1` markiert.

Die Dokumente sind Agenten-erstellte synthetische Testdaten und von den persönlichen Projekt- und Interviewnotizen getrennt. [test_questions.md](./test_questions.md) enthält erste Fragen, erwartete Belege und Antwortentwürfe. Diese müssen noch geprüft und bestätigt werden, bevor sie als Referenz für einen Modellvergleich dienen.
