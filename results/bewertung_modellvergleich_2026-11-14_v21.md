# Bewertung v21: Größenleiter offener Modelle und Prognose für einen Server

**Status:** Agentenmessung, 14.11.2026; regelbasierte Bewertung (`scripts/regelbewertung.py`) mit Stichproben von Hand. Vom Nutzer noch zu prüfen.
**Läufe:** gleicher Aufbau wie v19 (Aussagen-Datenbank, Berichte der 40 besten Aussagen vollständig, Antwortregeln 1–8), `dataset-v4` (58 Berichte), 34 Fragen × 3 Durchläufe; nur das Antwortmodell wechselt. Offene Modelle über OpenRouter (Anbieter je Antwort gespeichert; mehrere Anbieter je Modell, Rechengenauigkeit beim Anbieter nicht überprüfbar).
- `ergebnisse_google_gemma-3-27b-it_2026-11-14_v21.json`
- `ergebnisse_openai_gpt-oss-120b_2026-11-14_v21.json`
- `ergebnisse_qwen_qwen3.5-397b-a17b_2026-11-14_v21.json`
- Vergleich: v19 (Gemini 2.5 Pro), v20 (Gemma 3 4B lokal, 1 Durchlauf)

**Bewertungsregel:** je Frage Pflichtinhalte und verbotene Inhalte (überholte Stände, Erfundenes). Geeicht an der Handbewertung von v18/v19: „nicht erfüllt“ stimmt dort genau überein (2/2, 5/5); „erfüllt“ ist großzügiger als die Handbewertung, weil Störinhalte nicht erkannt werden. Harte Kennzahl ist daher **„inhaltlich falsch“** (verbotener Inhalt). Formatfehler (ungültiges JSON) werden getrennt gezählt; seit v21 liest das Programm einen häufigen Anführungszeichen-Fehler robust ein (gespeicherte Antworten neu eingelesen, kein neuer Modellaufruf).

## Ergebnis

| Modell | Parameter (gesamt / aktiv) | Lizenz | inhaltlich falsch | technisch ausgefallen | erfüllt (Regel, Obergrenze) | Ø Dauer | Kosten 102 Antworten |
|---|---|---|---|---|---|---|---|
| Gemma 3 4B, lokal (v20, 34 Antworten) | 4 Mrd. | Gemma | 35 % | 24 % | 12 % | 74 s | 0 |
| Gemma 3 27B | 27 Mrd. | Gemma | **29 %** (30) | 1 | 43 % | 16 s | 0,07 USD |
| gpt-oss-120b | 117 / 5 Mrd. | Apache 2.0 | **11 %** (11) | 2 | 68 % | 35 s | 0,06 USD |
| Qwen3.5-397B-A17B | 403 / 17 Mrd. | Apache 2.0 | **9 %** (9) | 2 | 82 % | 69 s | 1,56 USD |
| Gemini 2.5 Pro (v19) | nicht veröffentlicht | proprietär (Cloud) | **5 %** (5) | 0 | 95 % (Hand: 79 %) | 30 s | 3,14 USD |

Häufigster inhaltlicher Fehler bei allen Modellen: ein älterer Stand wird als gültig oder gleichrangig genannt (Fahrzeugreservierung „zwei Werktage“, Unterlagen „USB/gedruckt“, Beamer „Seminarbüro“, Raumschlüssel „Pforte“). Gemma 27B zusätzlich: falscher Kontext (Fahrzeugfrage mit dem Material-Verfahren, HV-7 bei Erste Hilfe), übertragene Zahlen („28 °C“).

## Programmprüfung „möglicherweise überholt“ an den neuen Antworten

| Modell | inhaltliche Fehler | davon gewarnt | Fehlalarme bei erfüllten Antworten |
|---|---|---|---|
| Gemma 3 27B | 30 | 9 (30 %) | 2/44 (5 %) |
| gpt-oss-120b | 11 | 6 (55 %) | 8/69 (12 %) |
| Qwen3.5-397B | 9 | 5 (56 %) | 4/84 (5 %) |
| Gemini 2.5 Pro (v19) | 5 | 5 (100 %) | 7/97 (7 %) |

Bestätigt die Grenze aus der ersten Messung: Die Schwellen wurden an Gemini-Antworten abgestimmt; an Antworten anderer Modelle erkennt die Prüfung nur etwa die Hälfte der Fehler. Sie ist eine zusätzliche Absicherung, kein Ersatz für ein gutes Modell.

## Prognose: Was bräuchte ein Server im geschlossenen Netz? (Vorschlag, Größenordnungen)

Speicherbedarf der Gewichte ≈ Parameter × Byte je Parameter (16 Bit = 2 Byte, 8 Bit = 1 Byte, 4 Bit = 0,5 Byte), zuzüglich 20–50 % für den verarbeiteten Text und gleichzeitige Nutzer. Preise aus Händler- und Fachquellen 2026; sie widersprechen sich teils stark und sind nur Spannen ohne Server-Gehäuse, Zulassung, Betrieb und Personal.

| Modellklasse (gemessen) | Speicher Gewichte | Hardware (grob) | Kosten Grafikkarten (grob) | Qualität (inhaltlich falsch) |
|---|---|---|---|---|
| ~27 Mrd. (Gemma 3 27B) | ca. 28 GB (8 Bit) | 1 Karte 48 GB (z. B. L40S) | ca. 7.000–10.000 USD | 29 % – nicht annehmbar |
| ~120 Mrd., Experten-Modell (gpt-oss-120b) | ca. 61–65 GB (4-Bit-Format des Herstellers) | 1 Karte 80–96 GB (z. B. H100, RTX PRO 6000) | ca. 15.000–25.000 USD je Karte | 11 % |
| ~400 Mrd., Experten-Modell (Qwen3.5-397B) | ca. 400 GB (8 Bit) | 1 Server mit 8 Karten (H100/H200) | ca. 285.000–530.000 USD (ganzer Server) | 9 % |
| Gemini 2.5 Pro | unbekannt | nur als Cloud-Dienst | – | 5 % |

**Lesart (Agent):** Ein Modell der Klasse **gpt-oss-120b** läuft auf **einer** großen Grafikkarte und liegt mit 11 % inhaltlich falscher Antworten nahe am viel größeren Qwen (9 %), aber noch etwa doppelt so hoch wie Gemini (5 %). Der Sprung von 27 auf ~120 Mrd. Parameter bringt am meisten; darüber flacht der Gewinn ab. Ob 10 % „annehmbar“ ist, hängt vom Einsatz ab und ist eine Nutzerentscheidung; zusammen mit Programmprüfungen und einer Pflicht, Quellen zu prüfen, wäre die 120-Mrd.-Klasse ein realistischer Ausgangspunkt für einen Pilotbetrieb.

## Grenzen

- Ein Datensatz (58 synthetische Berichte), 34 Fragen, je 3 Durchläufe; Prompt für Gemini entwickelt, nicht je Modell angepasst.
- Bewertung regelbasiert (Störinhalte nicht erfasst); Stichproben von Hand bestätigen die Regel für „inhaltlich falsch“.
- Rechengenauigkeit (Kompression) bei den OpenRouter-Anbietern nicht überprüfbar; Eigenbetrieb kann leicht abweichen.
- Geschwindigkeit bei Anbietern sagt nichts über eigene Hardware; Mehrnutzerbetrieb nicht gemessen.
- Parameterzahl von Gemini nicht veröffentlicht; kein direkter Größenvergleich möglich.
- Hardwarepreise: widersprüchliche Quellen, nur Größenordnungen.
