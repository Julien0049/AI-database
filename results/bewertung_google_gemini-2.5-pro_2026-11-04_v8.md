# Bewertung: Gemini 2.5 Pro, achter Test (knappe Antworten)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-11-04_v8.json](./ergebnisse_google_gemini-2.5-pro_2026-11-04_v8.json), 04.11.2026, Modell `google/gemini-2.5-pro` über OpenRouter, Notebook [citation_check_v7.ipynb](../notebooks/citation_check_v7.ipynb).
**Aufbau:** Wie v7 (dreizehn Berichte im einheitlichen Format, Datenstand `dataset-v2`). Einzige Änderung: Regel 7 (exakt und knapp, ohne Einleitung und Wiederholungen, keine Verweise wie „ein Bericht“ im Text; Hinweise auf abweichende Berichte und Lücken bleiben). Geplant war ein Durchlauf als Sichtprüfung; die Datei enthält drei Durchläufe.
**Maßstab:** Wie v7.

## Kennzahlen

| Kennzahl | v7 | v8 |
|---|---|---|
| Belege gültig | 213 von 213 | 208 von 208 |
| Nicht auswertbares JSON | 0 | 0 |
| Sätze ohne Beleg (alle Lückenhinweise) | 15 | 15 |
| Sätze / Wörter gesamt | 207 / 2971 | 194 / 2643 (−11 %) |
| Sätze mit Verweis wie „ein Bericht“, „einigen Berichten zufolge“ | 5 | 3 |
| Laufzeit gesamt | 188 s | 190 s |

## Ergebnis (inhaltlich)

42 von 51 Antworten erfüllen die Kriterien, 9 teilweise (v7: 43). Fragen 1–13: 33 von 39 (v7: 32). Fragen 14–16: 9 von 9. Frage 17: 0 von 3.

| Frage | D1 | D2 | D3 | Anmerkung |
|---|---|---|---|---|
| 1–3 | erfüllt | erfüllt | erfüllt | Stabil, teils kürzer. |
| 4 | erfüllt | erfüllt | erfüllt | **Verbessert:** Kein Satz aus dem Fahrzeugbericht mehr (v7: in allen drei Durchläufen). |
| 5 | teilweise | teilweise | erfüllt | D1/D2 nur indirekt; D2 besteht aus einem einzigen Satz. D3 sagt ausdrücklich, dass die Berichte keine verantwortliche Person nennen. |
| 6 | erfüllt | teilweise | erfüllt | D2 lässt das Entdeckungsdatum weg und benennt nur die fehlende Kennziffer, nicht das fehlende Formularfeld. |
| 7–8 | erfüllt | erfüllt | erfüllt | Stabil. |
| 9 | teilweise | teilweise | teilweise | Verantwortung nur indirekt (Entscheidung C). |
| 10–13 | erfüllt | erfüllt | erfüllt | Hinweise auf auseinandergehende Erfahrungen und Lücken bleiben erhalten. |
| 14 | erfüllt | erfüllt | erfüllt | Kernpunkte vollständig, kürzer als v7; D1 ohne „getrennte Felder“ und ohne „Kennzeichen und Datum“. |
| 15–16 | erfüllt | erfüllt | erfüllt | Vollständig; in Frage 16 bleiben in D1 eine Wiederholung und in D1/D2 Verweise wie „ein Bericht“. |
| 17 | teilweise | teilweise | teilweise | Stände 2024 und 2025 korrekt, Grund der Änderung in D1/D3 richtig. Der Stand von 2022 fehlt in allen drei Durchläufen (v7: in einem). |

## Beobachtungen

- **Knapper ohne Verlust bei den Pflichthinweisen:** Etwa 11 % weniger Text. Hinweise, dass die Berichte auseinandergehen oder nichts sagen, bleiben erhalten (Fragen 10–13, 15).
- **Weniger Abschweifen:** Die Übertragung der Fahrzeugregel bei Frage 4 verschwindet in allen Durchläufen. Plausible Erklärung: „nur was zur Frage gehört“. Bei drei Durchläufen ist Zufall nicht ausgeschlossen.
- **Kürzung kann zu weit gehen:** Frage 5 D2 und Frage 6 D2 lassen Teile weg, die zur Antwort gehören. Frage 17 lässt den Stand von 2022 durchgehend aus. Weil dieser Bericht mehrtägige Seminare nicht ausdrücklich nennt, ist das Weglassen vertretbar; nach dem bisherigen Maßstab gilt es als „teilweise“. Ob der Maßstab angepasst wird, entscheidet der Nutzer.
- **Verweise wie „ein Bericht“ werden nur wenig seltener** (5 → 3). Die Regel wirkt hier kaum.

## Grenzen

- Ein Unterschied von einer Antwort (42 statt 43) liegt innerhalb der beobachteten Schwankung.
- Die Länge wurde in Wörtern der Antwortsätze gemessen, ohne Fußnoten und Quellenliste.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.
