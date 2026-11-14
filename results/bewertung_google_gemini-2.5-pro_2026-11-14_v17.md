# Bewertung: Gemini 2.5 Pro, v17 (Aufbau v16 auf `dataset-v4`, 58 Berichte)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen. Grenzfälle markiert.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-14_v17.json](./ergebnisse_google_gemini-2.5-pro_2026-11-14_v17.json), 14.11.2026, `scripts/antwortlauf_aussagen.py --volltext`, drei Durchläufe, 34 Fragen, 58 Berichte (359 Aussagen). Kostenprobe: `…_v17_test.json` (Fragen 10, 32). Einlesen der zehn neuen Berichte (Nachtragstest): `aussagen_google_gemini-2.5-pro_2026-11-14_v17.json`.
**Aufbau:** unverändert gegenüber v16 (40 beste Aussagen bestimmen die Berichte, diese gehen vollständig ins Modell). Geändert ist nur der Datensatz: zehn lange, fiktive Berichte aus militärischem Lehrgangs- und Übungsbetrieb, Fragen 26–34, Varianten 10b, 14b, 21b. Außerdem liest das Programm seit dataset-v4 das Berichtsdatum anders (Zeile „Datum:“, sonst Unterschrift).
**Maßstab:** wie v11–v16 (Störinhalte oder Inhalte aus anderem Kontext ohne Kennzeichnung = teilweise, überholter Stand als aktuell = nicht erfüllt).

## Kennzahlen

| Kennzahl | v16 (48 Berichte) | v17 (58 Berichte) |
|---|---|---|
| Fragen 1–25: erfüllt (von 75) | 58 | 48 |
| Fragen 26–34 (neu, lange Berichte): erfüllt (von 27) | – | **26** |
| Gesamt erfüllt / teilweise / nicht erfüllt | 58 / 17 / 0 (von 75) | 74 / 25 / 3 (von 102) |
| Berichte im Antwortschritt je Frage | 19,7 | 18,4 |
| Belege nicht bestätigt | 0 | 6 (gekürzte Zitate mit „[...]“, inhaltlich korrekt) |
| Kosten | 1,78 USD | 2,86 USD (ca. 2,8 Cent je Frage) |
| Wartezeit je Frage (5 parallel) | – | 19 s im Mittel |

## Neue Fragen 26–34 (lange Berichte)

| Frage | Ergebnis | Anmerkung |
|---|---|---|
| 26 Erste-Hilfe-Meldung | 3 | Digitale Mängelmeldung gefunden, obwohl nur nebenbei im Schießbericht; HV-7 nicht genannt. |
| 27 Volltanken nach Übung | 3 | Mit Kontext „nur Übungsbetrieb“; D3 nennt zusätzlich die Standortregel. Gegenprobe Frage 7: alle Durchläufe korrekt „Fahrbereitschaft tankt“. |
| 28 Stubenschlüssel | 3 | Keine Übertragung der Abendseminar-Regel. |
| 29 Verpflegung Übung | 3 | VA-3, zehn Werktage, Sonderkost namentlich; alte Frist als entfallen benannt. |
| 30 Funkgeräte-Akkus | 3 | „Früher“ und „gilt seitdem nicht mehr“ richtig aufgelöst. |
| 31 Kälte im Gelände/Biwak | 2 | Abweichende Sichtweisen nebeneinander; D1 nennt die Überjacken-Vorschrift (Seminar) ohne Kontext. |
| 32 Besuchertag | 3 | Checkliste im Wesentlichen vollständig; Parkplatz P3 nicht namentlich. |
| 33 Honorar | 3 | Lücke benannt, keine Beträge übertragen. |
| 34 Wachablösung bei Frost | 3 | Als Einzelfall mit „nicht entschieden“ wiedergegeben. |

## Geänderte Fragen (Nachtragstest)

| Frage | Ergebnis | Anmerkung |
|---|---|---|
| 10b Fahrzeugreservierung | 3 | Neuer Stand (Portal, drei Werktage) in allen Durchläufen; alte Frist nicht genannt. |
| 14b Zusammenfassung Fahrzeuge | 2 | Neue Reservierungsregel und Übungsregeln mit Kontext; D1 überträgt Übernahmeprotokoll und Prüfung aus der Übung ohne Kontext. |
| 21b Beamer | 0 (3 × nicht erfüllt) | **Testfehler (Agent):** Der neue Bericht beschreibt die Technik „im Gebäude 3“; das Modell liest die IT-Ticket-Regel daher als Sonderfall für Gebäude 3 und nennt weiterhin Seminarbüro und Raumkalender. Diese Lesart ist vom Berichtstext gedeckt. Ohne Frage 21: 74 von 99. |

## Fragen 1–25 mit den neuen Berichten im Bestand

| Frage | v16 | v17 | Anmerkung zu v17 |
|---|---|---|---|
| 4 | 2 | 0 | Satz zur Führung gemeinsamen Materials auf persönlichen Listen (eintägige Veranstaltungen) in allen Durchläufen; D1/D3 zusätzlich Funkgeräte-Bericht als Beleg. |
| 6 | 2 | 1 | Digitale Mängelmeldung (Erste Hilfe) als Störinhalt in D1/D2. |
| 11, 12 | 6 | **0** | **Kontextvermischung:** Erfahrungen aus Biwak und Truppenübungsplatz (Stillstand, Kälteschutzjacke griffbereit, „hängt vom Auftrag ab“) fließen ohne Kennzeichnung in die Antwort zu Winter-**Seminaren** ein. Grenzfall: inhaltlich verwandt und belegt, aber anderer Kontext. |
| 15 | 0 | 0 | Zusätzlich Biwak-Themen (Akkus, Wachablösung, warme Mahlzeit) und Winterdienst. |
| 14 | 0 | 2 | siehe 14b. |
| übrige | – | wie v16 | Fragen 1–3, 7, 8, 13, 16–20, 22–24 vollständig erfüllt; 5 und 9 wie bisher nur indirekt; 25 weiterhin ohne die drei nicht gefundenen Gäste-Berichte. |

## Beobachtungen

- **Lange Berichte sind kein Problem, wenn sie gefunden werden:** 26 von 27 bei den neuen Fragen. Vergrabene Regeländerungen, „früher …“, weit entfernte Einschränkungen, Einzelfall-Anordnungen und Lücken werden zuverlässig richtig behandelt.
- **Der Nachtragstest gelingt:** Neue Stände aus nachträglich hinzugefügten Berichten (Fahrzeugportal, VA-3, digitale Mängelmeldung) werden ohne Neuaufbau sofort als aktueller Stand genannt.
- **Neue Fehlerquelle mit wachsender Sammlung: Kontextvermischung.** Mehr Berichte zu verwandten Themen (Kälte, Material, Schlüssel) bedeuten mehr fast passende Inhalte im Antwortschritt. Das Modell trennt Kontexte bei gezielten neuen Fragen gut (28, 27/7), mischt aber bei Erfahrungsfragen und Zusammenfassungen Inhalte aus anderem Rahmen ohne Kennzeichnung bei (11, 12, 15). Ob eine gekennzeichnete Übertragung erwünscht wäre (Biwak-Erfahrung als Hinweis für Winterseminare), ist eine Nutzerentscheidung.
- **Testfehler 21b:** Ein Bericht, der seinen Geltungsbereich eingrenzt („im Gebäude 3“), löst einen allgemeinen Stand nicht ab. Das Modell hat hier vorsichtiger gelesen als der Testentwurf.

## Folgerungen (Vorschlag)

1. Für den Brief: Der Aufbau trägt auch bei langen Berichten und nachträglichem Wachstum; die verbleibenden Fehler sind Kontextvermischung und unvollständige themenübergreifende Sammelfragen.
2. Gegen Kontextvermischung: Antwortregel „Inhalte aus anderem Kontext nur mit ausdrücklichem Hinweis auf den Kontext“ ergänzen (eine Prompt-Änderung, eigener Lauf) oder den Kontext der Aussagen (bereits in der Datenbank) bei der Auswahl berücksichtigen.
3. Frage 21b: Bericht oder Kriterium anpassen (Nutzerentscheidung).

## Grenzen

58 synthetische Berichte, davon 10 lang; Fragen und Fallen vom selben Agenten entworfen, der auch bewertet; ein Lauf mit drei Durchläufen; Grenzfälle (11, 12, 15, 21) vom Nutzer zu prüfen.
