# Bewertung: lokales Modell Gemma 3 4B, v20 (offline auf dem eigenen Mac)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_lokal_gemma3-4b_2026-11-14_v20.json](./ergebnisse_lokal_gemma3-4b_2026-11-14_v20.json), 14.11.2026, 21:38–22:30, ein Durchlauf, 34 Fragen, 58 Berichte. Netzprotokoll: [netzprotokoll_v20_2026-11-14.txt](./netzprotokoll_v20_2026-11-14.txt), Laufprotokoll `lauf_v20.log`. Ein erster Start wurde abgebrochen, weil das WLAN zwischendurch wieder an war (Dateien `…_abgebrochen`); Probe mit zwei Fragen: `…_v20_test.json`.
**Aufbau:** wie v19 (gleiche Aussagen-Datenbank, gleiche Auswahl der Berichte, gleiche Antwortregeln 1–8); einzige Änderung: Antwortmodell **Gemma 3 4B** (Google, 3,9 Mrd. Parameter, Q4_K_M, 3,4 GB, Lizenz „Gemma Terms of Use“) über Ollama 0.40.16 auf `127.0.0.1`, Kontext 12.288 Tokens, JSON-Ausgabe erzwungen, Anfragen nacheinander. Hardware: Apple M2, 8 GB Arbeitsspeicher.
**Maßstab:** wie v19; zusätzlich gilt eine Antwort ohne bestätigten Beleg (keine Quellenangabe) höchstens als teilweise erfüllt.

## Offline-Nachweis (Messung)

- Lauf vollständig bei getrennter Internetverbindung (Prüfung alle 10 s: 0 Mal erreichbar).
- Verbindungen von Ollama oder Python nach außen: **0** (lsof alle 10 s); Ollama lauscht nur auf 127.0.0.1.
- Suchmodell mit `HF_HUB_OFFLINE=1` (keine Nachlade-Versuche).
- Grenze: Testnachweis auf einem Laptop, keine Sicherheitszertifizierung.

## Kennzahlen

| Kennzahl | Gemini 2.5 Pro (v19, 3 Durchläufe) | Gemma 3 4B lokal (v20, 1 Durchlauf) |
|---|---|---|
| Erfüllt | 81 von 102 (79 %) | **1 von 34 (3 %)**; nur inhaltlich gewertet (ohne Quellenpflicht): 5 von 34 |
| Teilweise | 16 (16 %) | 10 (29 %) |
| Nicht erfüllt | 5 (5 %) | **23 (68 %)**, davon 8 ohne verwertbare Antwort |
| Technische Ausfälle | 0 | 8 (4 × Serverfehler während der Ausgabe, 4 × ungültiges oder abgebrochenes JSON) |
| Dauer je Frage | ca. 20 s | **74 s** im Mittel (16–579 s), nacheinander |
| Kosten | ca. 3 Cent | 0 (nur Strom) |
| Speicher | – | 3,6 GB, 27 % Arbeitsspeicher frei |

## Fehlerarten (Beispiele)

- **Überholter Stand als aktuell oder gleichrangig:** Frage 7 „Ja, vollgetankt“; Frage 10 „zwei Werktage bei der Fahrbereitschaft“; Frage 18 Pforte und Schlüsselkasten nebeneinander; Frage 22 „Download oder USB-Stick“; Frage 21 Seminarbüro.
- **Falscher Kontext / vermischte Regeln:** Frage 8 (Fahrzeug) beantwortet mit dem Verfahren für Materialsets; Frage 2 verweist auf Beamer-Berichte; Frage 26 nennt das Abweichungsprotokoll für Erste-Hilfe-Material.
- **Erfundenes:** Frage 13 „28 °C“ und eine Jackenempfehlung; Frage 24 „spätestens sechs Werktage“; Frage 5 leitet eine persönliche Verantwortung ab.
- **Fremdes in Zusammenfassungen:** Frage 15 (Winter) mit Hitzeerschöpfung, Landeplätzen, Lehrsaaltechnik.
- **Belege:** In vielen Antworten keine wörtlichen Zitate, sondern Kennungen im Text („(B39)“); die Zitatprüfung erkennt das, die Fußnoten fehlen dann.
- **Richtig:** Frage 20 (Garderobe) vollständig; Fragen 4, 27, 28, 30 inhaltlich richtig, aber ohne bestätigten Beleg.

## Einordnung

- Mit einem Modell dieser Größe auf einem Laptop ist der PoC **nicht brauchbar**: Zwei Drittel der Antworten sind falsch oder fehlen, gerade bei den Kernanforderungen (aktueller Stand, Kontext, keine Erfindungen, Belege).
- Der Offline-Betrieb selbst ist technisch nachgewiesen: Suche, Datenbank und Antwort laufen ohne Internet.
- Das Ergebnis ist eine **untere Grenze**. Es sagt nichts darüber, wie ein mittelgroßes offenes Modell auf Serverhardware abschneidet; dafür wäre ein eigener Test nötig.
- Die Lizenz von Gemma enthält Nutzungsbeschränkungen; für einen echten Einsatz rechtlich zu prüfen.

## Grenzen

Ein Modell, ein Durchlauf, 4-Bit-Kompression, 8 GB Arbeitsspeicher; Prompt für Gemini entwickelt und nicht an das kleine Modell angepasst; JSON-Zwang über Ollama kann die Qualität beeinflussen und erklärt einen Teil der Ausfälle.
