# Synthetische AAR-Testberichte

Diese fünfzehn Berichte wurden als fiktives Testmaterial für den AI-Database-Prototyp erstellt. Sie beschreiben ausschließlich harmlose Abläufe: fünf zur Materialrückgabe in Seminaren, fünf zur Fahrzeugausleihe drei Erfahrungsberichte zur Kleidung bei Winter-Außenseminaren und zwei zur Schlüsselrückgabe nach Abendseminaren. Sie sind keine echten After-Action-Reports, Vorschriften oder verlässlichen Handlungsanweisungen.

Die Markdown-Dateien bilden eine kontrollierte Textbasis. Neun Berichte haben ein einheitliches Format (Überschrift, `**Datum:**`, Verfasser). Vier Berichte weichen bewusst davon ab, bei gleichem Inhalt: Fahrtenbuch-Formular (keine Überschrift, Name und ausgeschriebenes Datum als Unterschrift am Ende), Rückgabe gemeinsamer Sets (Datum als „Stand: 2025-01-20“, kein Name), Reservierung von Fahrzeugen (kein Datum, Namenskürzel am Ende), Kleidung im Winter (Datum ohne Beschriftung oben, keine Überschrift, kein Name). Der Testfall soll erkennen, ob ein System:

- widersprüchliche Aussagen zum Rückgabeverfahren bei mehrtägigen Seminaren erkennt;
- ergänzende Informationen zum Umgang mit fehlendem Material zusammenführt;
- eintägige und mehrtägige Veranstaltungen als unterschiedliche Kontexte behandelt.
- einen nicht als Änderung gekennzeichneten Widerspruch zur Tankregel erkennt;
- Fahrzeug- und Materialberichte trotz ähnlicher Stichworte („mehrtägig“, „gemeinsam genutzt“, „keine persönliche Verantwortung“) auseinanderhält.
- bei Erfahrungsberichten unterschiedliche Sichtweisen nebeneinander nennt, statt den jüngsten Bericht als gültigen Stand zu behandeln, und eine darin enthaltene Vorgabe als solche erkennt;
- einen Widerspruch allein über das Datum auflöst: Die beiden Schlüsselberichte widersprechen sich ohne sprachlichen Hinweis auf die Reihenfolge; ihre Dateinamen enthalten bewusst kein Datum, sodass der neuere Bericht in der Sammlung zuerst steht;
- Titel und Datum auch bei abweichendem oder fehlendem Format korrekt angibt und nichts erfindet;
- Zusammenfassungen zu einem Thema vollständig und ohne überholte Verfahren liefert und Änderungen nur auf ausdrückliche Frage chronologisch darstellt.

Der Stand mit nur den fünf Materialberichten und sechs Fragen ist als Git-Tag `dataset-v1` markiert, der Stand mit dreizehn einheitlich formatierten Berichten als `dataset-v2`.

Die Dokumente sind Agenten-erstellte synthetische Testdaten und von den persönlichen Projekt- und Interviewnotizen getrennt. [test_questions.md](./test_questions.md) enthält erste Fragen, erwartete Belege und Antwortentwürfe. Diese müssen noch geprüft und bestätigt werden, bevor sie als Referenz für einen Modellvergleich dienen.
