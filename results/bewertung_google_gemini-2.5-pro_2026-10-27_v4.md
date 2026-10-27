# Bewertung: Gemini 2.5 Pro, vierter Test (Erfahrungsberichte, Prompt unverändert)

**Status:** Agentenbewertung (Claude), vom Nutzer noch zu prüfen.
**Lauf:** [ergebnisse_google_gemini-2.5-pro_2026-10-27_v4.json](./ergebnisse_google_gemini-2.5-pro_2026-10-27_v4.json), 27.10.2026, Modell `google/gemini-2.5-pro` über OpenRouter.
**Aufbau:** Dreizehn Berichte vollständig im Prompt (neu: drei Erfahrungsberichte zur Winterkleidung), keine Suche. Systemprompt identisch mit Lauf v3; er enthält noch keine Regel zu Erfahrungsberichten. Ein Durchlauf.
**Maßstab:** Antwortentwürfe und Kriterien in [test_questions.md](../data/synthetic_reports/test_questions.md) sowie der Wortlaut der Berichte. Quellenangaben ohne Titel werden hier nicht als Fehler gewertet, weil der Prompt noch Dateiname und Datum verlangt.

## Ergebnis

Elf von dreizehn Antworten erfüllen die Kriterien, zwei teilweise. Nichts wurde erfunden.

| Frage | Ergebnis | Vergleich zu v3 | Begründung |
|---|---|---|---|
| 1 | erfüllt | gleich | Neuester passender Stand, richtige Quelle. |
| 2 | erfüllt | gleich | Rückgabe und Meldung korrekt zusammengeführt. |
| 3 | erfüllt (Formfehler) | gleich | Inhalt korrekt; Quelle ohne Datum. |
| 4 | erfüllt (Formfehler) | **besser** | Diesmal keine falsche Zusatzquelle; Quelle ohne Datum. |
| 5 | teilweise | gleich | Verantwortung weiterhin nur indirekt beantwortet (vom Nutzer als nicht falsch akzeptiert, Entscheidung C). |
| 6 | erfüllt | gleich | Lücke klar benannt; das Entdeckungsdatum fehlt in der Aufzählung. |
| 7 | erfüllt | gleich | Versteckter Widerspruch korrekt aufgelöst. |
| 8 | erfüllt | gleich | Material-Verfahren nicht übertragen. |
| 9 | erfüllt | **besser** | Benennt diesmal ausdrücklich, dass die Berichte nichts dazu sagen, wie Verantwortung festgestellt wird. |
| 10 | erfüllt (Formfehler) | gleich | Fehlende Kosteninformation benannt; Quelle ohne Datum. |
| 11 | teilweise | neu | Führt Socken, Handschuhe und vorgeschriebene Überjacke zusammen und erwähnt die Uneinigkeit bei Jacken. Der Bericht zu langen Wartezeiten (25.01.2024) fehlt ganz; die beiden Sichtweisen zur Daunenjacke werden nicht einzelnen Berichten mit Datum zugeordnet. |
| 12 | erfüllt | neu | Sagt, dass die Berichte auseinandergehen, nennt beide Situationen (Gehen, lange Wartezeiten) und priorisiert nicht nach Datum. Die Sichtweisen werden aber nicht einzeln mit Quelle und Datum belegt, sondern nur gesammelt am Ende. |
| 13 | erfüllt | neu | Lücke klar benannt, nichts erfunden. |

## Beobachtungen

- **Erfahrungen ohne eigene Regel:** Das Modell behandelt die abweichenden Erfahrungen bereits ohne entsprechende Prompt-Regel nicht als „neuester Stand gewinnt“. Was fehlt, ist die Zuordnung jeder Sichtweise zu Bericht und Datum, die die bestätigte Anforderung verlangt.
- **Vorgabe erkannt:** Die wasserdichte Überjacke wird in Frage 11 und 12 als Vorschrift wiedergegeben.
- **Deutliche Schwankung zwischen Läufen:** Frage 4 und 9 sind besser als in v3, obwohl sich an Prompt und betroffenen Berichten nichts geändert hat. Einzelne Durchläufe reichen damit nicht, um kleine Prompt-Änderungen sicher zu bewerten.

## Grenzen

- Quellenabruf ist nicht getestet, weil das Modell alle Dokumente vollständig erhielt.
- Je ein Durchlauf pro Fassung; die beobachtete Schwankung macht Vergleiche zwischen einzelnen Läufen unsicher.
- Die Bewertung stammt von einem anderen KI-Modell und ist keine unabhängige menschliche Prüfung.
