# Bewertung v14: Aussagen-Datenbank (48 Berichte, 25 Fragen)

**Aufbau:** Jeder Bericht wird beim Eingang einmal vom Modell (Gemini 2.5 Pro über OpenRouter) in Einzelaussagen zerlegt: Thema, Art (regel / erfahrung / unklar / sonstiges), Kontext, Aussage, wörtliches Zitat. Titel und Datum liest das Programm. Das Modell bekommt die bisherige Themenliste, Berichte werden nacheinander verarbeitet. Abgleich über Fingerabdruck: Nur neue oder geänderte Dateien werden verarbeitet. Kein Antwortlauf; Suche ohne Sprachmodell (e5-small), ein Bericht erhält den Wert seiner besten Aussage.

Dateien: `aussagen_google_gemini-2.5-pro_2026-11-13_v14.json` (Datenbankinhalt), `ergebnisse_aussagen_suche_2026-11-13_v14.json` (Ranglisten), `sichtpruefung_aussagen_2026-11-13_v14.md` (Aussagen je Frage zur Sichtprüfung).

## Einlesen (Messung)

- 48 Berichte, 160 Aussagen, 55 Themen; Arten: 94 regel, 34 erfahrung, 20 unklar, 12 sonstiges.
- Kosten 1,01 USD (einmalig), Dauer 772 s (ca. 16 s je Bericht, nacheinander). Ein zweiter Abgleich ohne Änderungen verarbeitet nichts und kostet nichts (Attrappentest). Geänderte und entfernte Dateien werden erkannt (Attrappentest).
- Zitate: 157 von 160 wörtlich gefunden. Die 3 übrigen kürzen mit „...“ ab; inhaltlich korrekt, aber von der Prüfung nicht bestätigt.
- Probelauf vorab (2 Berichte, 0,042 USD): Zerlegung entsprach dem vorab abgestimmten Format; nebenbei erwähnte Unterlagen-Regel als eigene Regel erfasst, unsichere Vorgabe (Kantinen-Anmeldung) als „unklar“ markiert.

## Suche über Aussagen vs. ganze Berichte (Messung)

| vollständig@k | @3 | @5 | @10 | @20 | @30 |
|---|---|---|---|---|---|
| Aussagen (v14) | 58 % | 83 % | 92 % | 96 % | 96 % |
| Ganze Berichte (s5) | 71 % | 79 % | 88 % | 92 % | 96 % |

- Frage 22 (neuer Stand nur nebenbei): Rang 16 → 5. Frage 14 (Zusammenfassung Fahrzeuge): Tankregel Rang 6 → 1, alle 5 Berichte unter den ersten 5.
- Frage 25 (Gäste/Besucher): weiterhin Rang 10–38. Fragen 5, 8, 9, 24 etwas schlechter (@3 dadurch niedriger).
- Zum Vergleich die Attrappe (jeder Satz eine Aussage, Titel als Thema, kostenlos): @3 79 %, @5 88 %, @10 92 %. Die Suche allein profitiert also vor allem von kleineren Einheiten mit Titel, nicht von der Modellzerlegung. Der eigentliche Nutzen der Zerlegung liegt in Thema und Art (siehe unten), der über diese Kennzahl nicht gemessen wird.

## Themen (Sichtprüfung Agent)

- Meist einheitlich über Berichte hinweg: „Teilnehmerunterlagen“ (gedruckt 2023, USB 2025, Download 2026), „Rückgabe Beamer“ (4 Stände), „Winterkleidung“ (3 Berichte), „Rückgabe Dienstfahrzeuge“, „Rückgabe Materialsets“, „Rückgabe Schlüssel“.
- Zersplittert: Beamer-Ausgabe verteilt auf „Ausleihe Beamer“, „Reservierung Beamer“ und „Seminartechnik“ – der neueste Stand (Seminarbüro stellt bereit, 07.10.2025) steht unter „Seminartechnik“, nicht unter „Ausleihe Beamer“. Eine reine Programmregel „neueste Regel je Thema“ würde hier den überholten Stand (Abholung im Seminarbüro, 02.10.2024) liefern. Gäste-Themen verteilt auf sechs Themen (Ausweise, WLAN, Parkplätze, Empfang Gastreferenten …).
- Art: Der USB-Stand (2025) ist „unklar“, der Download (2026) „regel“. Eine Regel „neuester Stand nur unter Regeln“ muss „unklar“ einbeziehen.

## Folgerungen (Vorschlag)

1. Die Zerlegung ist günstig (ca. 2 Cent je Bericht, einmalig) und erfasst Nebenbemerkungen; das trägt für große Mengen.
2. Themen allein sind für eine automatische Priorisierung nicht zuverlässig genug. Nächster kostenloser Test: Suche zuerst passende Themen und nimm dann **alle** Aussagen dieser Themen (alle Stände) in die Antwort; misst, ob Zusammenfassungen (Frage 25) und Stände vollständig ankommen.
3. Zitatprüfung um Auslassungen („...“) erweitern: Teile einzeln und in Reihenfolge prüfen.

## Grenzen

48 kurze synthetische Berichte; ein Lauf; Sichtprüfung der Erfassung durch den Nutzer steht aus; kein Antwortlauf.

---

# Nachtrag v14b: Themensuche und Zitatprüfung (kostenlos, gleiche Datenbank, 48 Berichte)

**Zitatprüfung:** Auslassungen („...“) sind jetzt erlaubt, die Teile müssen in Reihenfolge vorkommen. Ergebnis: 160 von 160 Zitaten bestätigt (vorher 157).

**Themensuche:** Die M besten Aussagen bestimmen die Themen; geliefert werden alle Aussagen dieser Themen (alle Berichte, alle Stände). Datei: `ergebnisse_aussagen_suche_2026-11-13_v14b.json`.

| Variante | vollständig | Berichte im Mittel | fehlt bei Frage |
|---|---|---|---|
| Themen der besten 3 Aussagen | 71 % | 3,8 | 2, 5, 8, 9, 14, 16, 25 |
| Themen der besten 5 Aussagen | 75 % | 5,3 | 2, 5, 8, 9, 14, 25 |
| Themen der besten 10 Aussagen | 88 % | 8,4 | 2, 5, 25 |
| zum Vergleich: beste 5 / 10 Berichte nach bester Aussage (v14) | 83 % / 92 % | 5 / 10 | |

**Zusatzauswertung:** die N besten Aussagen direkt (Bericht zählt als gefunden, wenn eine seiner Aussagen dabei ist):

| N beste Aussagen | vollständig | Berichte im Mittel | fehlt bei Frage |
|---|---|---|---|
| 10 | 83 % | 5,4 | 2, 5, 16, 25 |
| 20 | 92 % | 11,6 | 16, 25 |
| 40 | 96 % | 20,0 | 25 |

**Bewertung (Agent):**
- Die Themensuche findet nicht mehr als die einfache Suche nach besten Aussagen bei gleicher Menge. Sie hat einen anderen Nutzen: Zu einem gefundenen Thema kommen alle Stände mit (Frage 22: alle sechs Berichte zu Teilnehmerunterlagen inkl. Download 2026), sodass ein überholter Stand nicht allein ankommt.
- Frage 25 (Zusammenfassung über Gäste: Ausweise, WLAN, Parkplätze, Gastreferierende) wird von keiner Variante vollständig gefunden; die Aussagen verteilen sich auf viele Themen, die alle nur entfernt nach „Gästen und Besuchern“ klingen. Themenübergreifende Sammelfragen bleiben die Grenze der Suche.
- Aussagen sind im Testdatensatz im Mittel 16 Wörter lang, Berichte nur etwa 47 Wörter (sehr kurze Testberichte). Der Vorteil, statt weniger langer Berichte viele kurze Aussagen mitzuschicken, ist bei echten, mehrseitigen Berichten deutlich größer, aber mit diesen Daten nicht messbar.
