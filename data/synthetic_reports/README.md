# Synthetische AAR-Testberichte

Fiktives, von einem KI-Agenten erstelltes Testmaterial für den AI-Database-PoC. Die Berichte beschreiben ausschließlich harmlose Verwaltungsabläufe. Sie sind keine echten After-Action-Reports, Vorschriften oder verlässlichen Handlungsanweisungen und sind von den persönlichen Projekt- und Interviewnotizen getrennt.

[test_questions.md](./test_questions.md) enthält die Testfragen mit erwarteten Belegen, Antwortentwürfen und Kriterien.

## Bestand (im Aufbau auf etwa 50 Berichte)

| Gruppe | Anzahl | Zweck |
|---|---|---|
| Kernberichte: Materialrückgabe, Fahrzeugausleihe, Winterkleidung | 13 | Grundlage der Fragen 1–17 |
| Datumstest: Schlüsselrückgabe nach Abendseminaren | 2 | Fragen 18–19 |
| Störberichte: ähnliche Wörter, anderer Kontext | 10 | Suche und Modell sollen den Kontext trennen |
| Störberichte: fremde Themen | 10 | Rauschen wie in einer echten Sammlung |
| Geplant: weitere Stände zu neuen Themen, lange Berichte mit mehreren Themen | ~13 | neuester Stand bei Suche, nebenbei erwähnte Regeln |

Die Störberichte ändern keine erwartete Antwort der Fragen 1–19, solange der Kontext richtig getrennt wird.

## Eingebaute Testfälle

### Inhalt

| Fall | Berichte | Was geprüft wird |
|---|---|---|
| Widerspruch mit neuerem Stand | Materialrückgabe 2022/2024/2025 (gemeinsame Sets) | jüngster vergleichbarer Stand bestimmt die Antwort |
| Widerspruch ohne Kennzeichnung als Änderung | Tankregel: Fahrzeugrückgabe 2023 vs. Fahrtenbuch-Formular 2025 | Regel wird gefunden, obwohl sie nur nebenbei steht |
| Widerspruch nur über das Datum auflösbar | `AAR-evening-keys-a.md` (2025) / `-b.md` (2024) | kein sprachlicher Hinweis; der neuere Bericht steht zuerst und hat die kleinere Kennung |
| Anderer Kontext trotz jüngeren Datums | eintägige Einführungsveranstaltungen 2025 | Verfahren für mehrtägige Seminare wird nicht übertragen |
| Ähnliche Stichworte zwischen Kernthemen | Fahrzeug- vs. Materialberichte („mehrtägig“, „gemeinsam genutzt“, „keine persönliche Verantwortung“) | Verfahren werden nicht vermischt |
| Ergänzende Aussagen | gemeinsame Sets + fehlende Bestandteile | Zusammenführung zu einer Antwort |
| Abweichende Erfahrungen und eine Vorgabe | drei Winterberichte; wasserdichte Überjacke vorgeschrieben | Sichtweisen nebeneinander, keine Priorität nach Datum; Vorgabe erkannt |
| Fehlende Evidenz | Kosten, Marken, Temperaturen, Kennziffern, verantwortliche Person | Lücken werden offen benannt |

### Ähnliche Wörter, anderer Kontext (Störberichte)

| Bericht | Ähnlich zu | Falle |
|---|---|---|
| Rückgabe von Büchern aus der Seminarbibliothek | Materialrückgabe | „Rückgabe“, „Seminar“, „bestätigt“ |
| Schlüssel für die Fahrradgarage | Raumschlüssel (Frage 18) | „Schlüssel“ und „Pforte“ wie im älteren Schlüsselbericht |
| Kleidung beim Sommer-Außenseminar | Winterkleidung | „Kleidung“, „Außenseminar“, „bewährt“; bewusst eintägig |
| Schäden in Seminarräumen | Fahrzeugschaden | „Schaden“, „Formular“, „am Tag der Feststellung“ |
| Rückgabe von Leihlaptops | Einzelgerät, Adapter | „Gerät“, „ausleihende Person“, „Ladegerät“ |
| Fehlendes Material in Erste-Hilfe-Kästen | fehlende Gegenstände | nennt Formular „HV-7“; darf bei Frage 6 nicht als Kennziffer übernommen werden |
| Rückgabe von Sportgeräten | Materialrückgabe | „Rückgabe“, „vollständig“, „Liste“ |
| Besucherausweise | Schlüssel, fehlende Gegenstände | „Pforte“, „abgeben“, „am selben Tag melden“ |
| Gemeinsam genutzte Gruppenräume | gemeinsames Set, gemeinsames Fahrzeug | „gemeinsam genutzt“, „Liste“, „jede Gruppe“ |
| Winterdienst am Seminargebäude | Winterseminare | „Winter“, „Winterseminare“, aber keine Kleidung |

### Fremde Themen (Störberichte)

Raumbuchung, Verpflegung, Druckerausfall, Seminaranmeldung, Reisekosten, WLAN für Gäste, Feedbackbögen, Besucherparkplätze, Fundsachen, Teilnahmebescheinigungen.

### Format und Metadaten

| Fall | Berichte | Erwartetes Verhalten des Programms |
|---|---|---|
| Einheitliches Format (Überschrift, `**Datum:**`, Verfasser) | Mehrzahl | Titel und Datum korrekt |
| Keine Überschrift, Thema am Anfang des Fließtexts | Fahrtenbuch-Formular, Kleidung im Winter, Schäden in Seminarräumen, Feedback nach Seminaren | Dateiname als Titel |
| Datum ausgeschrieben („18. März 2025“) | Fahrtenbuch-Formular, Schäden in Seminarräumen | Datum korrekt |
| Datum als „Stand: 2025-01-20“ oder „Stand: 06.05.2025“ | Rückgabe gemeinsamer Sets, Fahrradgarage | Datum korrekt |
| Datum ohne Beschriftung | Kleidung im Winter, Gruppenräume | Datum korrekt |
| Name und Datum nur als Unterschrift am Ende | Fahrtenbuch-Formular, Feedback, Druckerausfall, Fahrradgarage | Datum korrekt |
| Kein Datum | Reservierung von Fahrzeugen, Besucherparkplätze | „Datum unbekannt“ |
| Nur Monat und Jahr („März 2025“) | WLAN für Gäste | „Datum unbekannt“ (bekannte Grenze) |
| Ereignisdatum im Text vor dem Berichtsdatum | Druckerausfall (Ausfall 10.03.2025, Bericht 14.03.2025) | Programm nimmt fälschlich 10.03.2025 (bekannte Grenze) |
| Kein Name oder nur Kürzel | Rückgabe gemeinsamer Sets, Kleidung im Winter, Erste-Hilfe-Kästen, Fundsachen, Gruppenräume, Reservierung („D. Lenz“), Schäden („Hausverwaltung“) | ohne Auswirkung auf Quellen |
| Dateiname ohne Datum | Schlüsselberichte, Besucherparkplätze | Reihenfolge in der Sammlung nicht chronologisch |

## Versionen

- `dataset-v1`: fünf Materialberichte, sechs Fragen.
- `dataset-v2`: dreizehn einheitlich formatierte Berichte.
- Seitdem: vier umformatierte Kernberichte (v9), Datumstest (v10), Störberichte (im Aufbau).
