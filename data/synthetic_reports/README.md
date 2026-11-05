# Synthetische AAR-Testberichte

Fiktives, von einem KI-Agenten erstelltes Testmaterial für den AI-Database-PoC. Die Berichte beschreiben ausschließlich harmlose Verwaltungsabläufe. Sie sind keine echten After-Action-Reports, Vorschriften oder verlässlichen Handlungsanweisungen und sind von den persönlichen Projekt- und Interviewnotizen getrennt.

[test_questions.md](./test_questions.md) enthält die Testfragen mit erwarteten Belegen, Antwortentwürfen und Kriterien.

## Bestand (48 Berichte)

| Gruppe | Anzahl | Zweck |
|---|---|---|
| Kernberichte: Materialrückgabe, Fahrzeugausleihe, Winterkleidung | 13 | Grundlage der Fragen 1–17 |
| Datumstest: Schlüsselrückgabe nach Abendseminaren | 2 | Fragen 18–19 |
| Störberichte: ähnliche Wörter, anderer Kontext | 10 | Suche und Modell sollen den Kontext trennen |
| Störberichte: fremde Themen | 10 | Rauschen wie in einer echten Sammlung |
| Mehrere Stände zu neuen Themen: Beamer (4), Teilnehmerunterlagen (3) | 7 | Suche muss den neuesten Stand mitfinden |
| Lange Berichte mit mehreren Themen (Tages- und Abendseminare) | 6 | nebenbei erwähnte Regeln, mehrere Daten im Text |

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

### Mehrere Stände zu einem Thema

| Thema | Stände | Fallen |
|---|---|---|
| Beamer | Haustechnik (08.03.2022) → Seminarbüro (20.06.2023) → Reservierung über Raumkalender, Abholung im Seminarbüro (02.10.2024) → Seminarbüro stellt im Raum bereit und holt ab (07.10.2025) | Der jüngste Stand enthält keinen sprachlichen Hinweis auf eine Änderung. Der Bericht von 2023 hat einen Dateinamen ohne Datum und steht in der Sammlung zuletzt. Formate gemischt (Unterschrift, „Stand:“). |
| Teilnehmerunterlagen | gedruckt (15.03.2023) → USB-Stick (24.06.2025) → nur Download im Seminarportal (21.04.2026) | Der jüngste Stand steht nur nebenbei in einem Bericht über die Vorbereitung eines Seminartags. |

### Lange Berichte mit mehreren Themen

Gesamtberichte über einzelne Tages- oder Abendseminare (94–137 Wörter, drei bis vier Absätze). Sie sind mit den übrigen Berichten vereinbar und betreffen bewusst keine mehrtägigen Seminare, damit sich die erwartete Antwort zu Frage 16 nicht ändert.

| Bericht | Nebenbei erwähnte Regel oder Falle |
|---|---|
| Tagesseminar „Kommunikation im Team“ (20.05.2025) | **neue Regel nur hier:** Jacken und Taschen an der Garderobe im Erdgeschoss; „Jacke“ als Wortfalle zu den Winterberichten |
| Abendseminar „Projektplanung“ (16.06.2026) | **neue Regel nur hier:** Gastreferierende melden sich am Empfang an; drei Daten im Text, Berichtsdatum nur in der Unterschrift |
| Großes Tagesseminar im Herbst (17.09.2024) | Sammelplatz bei Feueralarm; gedruckte Unterlagen (damaliger Stand) |
| Abendseminar Verhandlungsführung (29.09.2026) | Getränke nur in verschließbaren Flaschen; keine Überschrift, kein Name |
| Tagesseminar „Präsentieren“ (02.12.2025) | Fotos nur mit Zustimmung; Beamer bereits im Raum (bestätigt den neuesten Beamer-Stand) |
| Tagesseminar mit externen Gästen (24.03.2026) | nur Bekanntes (Besucherausweise, Parkplätze, WLAN, Fundsachen) in neuer Kombination |

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
| Ereignisdatum im Text vor dem Berichtsdatum | Druckerausfall (Ausfall 10.03.2025, Bericht 14.03.2025); Abendseminar „Projektplanung“ (Vorbereitung 02.06.2026, Bericht 16.06.2026) | Programm nimmt fälschlich das erste Datum (bekannte Grenze) |
| Kein Name oder nur Kürzel | Rückgabe gemeinsamer Sets, Kleidung im Winter, Erste-Hilfe-Kästen, Fundsachen, Gruppenräume, Reservierung („D. Lenz“), Schäden („Hausverwaltung“) | ohne Auswirkung auf Quellen |
| Dateiname ohne Datum | Schlüsselberichte, Besucherparkplätze | Reihenfolge in der Sammlung nicht chronologisch |

## Versionen

- `dataset-v1`: fünf Materialberichte, sechs Fragen.
- `dataset-v2`: dreizehn einheitlich formatierte Berichte.
- Seitdem: vier umformatierte Kernberichte (v9), Datumstest (v10), Störberichte, mehrere Stände und lange Berichte; Fragen 20–25.
- `dataset-v3`: 48 Berichte, 25 vom Nutzer geprüfte Fragen; Grundlage für den Suchtest.
