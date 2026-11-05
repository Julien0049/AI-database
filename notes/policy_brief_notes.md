# Bausteine für das Policy Brief

Laufend gepflegte Sammlung, gegliedert wie das spätere Policy Brief. Jeder Punkt ist gekennzeichnet: **(Messung vX)** = in einem Testlauf gemessen, **(Nutzer)** = Einschätzung oder Entscheidung des Nutzers, **(Vorschlag)** = Vorschlag des Agenten, nicht geprüft. Details stehen in den Bewertungsdateien unter `results/`.

## Hintergrund

- In Organisationen entstehen laufend Erfahrungsberichte (After-Action-Reports, AARs). Erkenntnisse daraus gehen leicht verloren, wenn niemand alle Berichte kennt oder Regeln sich über die Zeit ändern.
- Sprachmodelle können Fragen in natürlicher Sprache beantworten und Inhalte mehrerer Dokumente zusammenführen. Sie können aber auch Inhalte erfinden oder veraltete Aussagen wiedergeben.
- Projektform: Semesterarbeit, Proof of Concept (PoC) mit einem Frontier-Modell über Cloud-API (Gemini 2.5 Pro über OpenRouter). Offlinebetrieb mit lokalem Modell ist eine spätere Ausbaustufe.

## Problemstellung

- Kann ein Sprachmodell Fragen zu einer Berichtssammlung so beantworten, dass die Antwort ausschließlich auf den Berichten beruht, nachvollziehbar belegt ist, bei geänderten Regeln den neuesten Stand nennt, bei abweichenden Erfahrungen die Sichtweisen nebeneinander stellt und Lücken offen benennt?
- Teilfragen: Funktionieren Quellenangaben zuverlässig? Erkennt das Modell die zeitliche Reihenfolge? Bleibt das bei uneinheitlich formatierten Berichten und bei vielen Berichten (Suche) so?

## Vorgehen

- **Daten:** Fiktive, harmlose Testberichte zu Verwaltungsabläufen, derzeit 48. Vollständiger Katalog der eingebauten Testfälle: `data/synthetic_reports/README.md`. Gezielt eingebaute Fälle:
  - *Inhalt:* Widersprüche mit neuerem Stand, auch ohne Kennzeichnung als Änderung und nur über das Datum auflösbar; unterschiedliche Kontexte (eintägig/mehrtägig); ergänzende Aussagen; abweichende Erfahrungen mit einer Vorgabe darin; Fragen ohne Antwort in den Berichten.
  - *Störberichte für die Suche:* ähnliche Wörter in anderem Kontext (z. B. Fahrradgarage mit „Schlüssel“ und „Pforte“, Erste-Hilfe-Formular „HV-7“ als falsche Kennziffer); fremde Themen als Rauschen; mehrere Stände zu einem Thema (Beamer mit vier Ständen, der neueste ohne sprachlichen Hinweis; Teilnehmerunterlagen mit drei Ständen, der neueste nur nebenbei erwähnt); lange Berichte über ganze Seminartage, in denen eine Regel nur in einem Absatz steht.
  - *Format und Metadaten:* fehlende Überschrift, Datum in verschiedenen Formaten und an verschiedenen Stellen (auch nur als Unterschrift), fehlendes Datum, nur Monat und Jahr, Ereignisdatum vor dem Berichtsdatum, fehlender oder abgekürzter Name, Dateinamen ohne Datum.
- **Testfragen:** 25 Fragen mit erwarteten Belegen, Antwortentwürfen und Kriterien; alle vom Nutzer geprüft (Stand `dataset-v3`). Fragen 20–25 zielen auf die Suche: Regel nur nebenbei, neuester von mehreren Ständen, Wortfalle Sommer/Winter, keine Antwort trotz vieler ähnlicher Treffer, Zusammenfassung über viele Berichte.
- **Antwortregeln (bestätigte Anforderungen):** nur die Berichte als Quelle; bei Regeln gilt der jüngste vergleichbare Stand; bei Erfahrungen Sichtweisen nebeneinander; Lücken offen benennen; exakt und knapp; Quellen als Fußnoten mit Titel und Datum.
- **Versuchsweise Entwicklung:** pro Version möglichst nur eine Änderung, ab v5 drei Durchläufe je Version, Bewertung je Antwort (erfüllt/teilweise).

### Versuchsübersicht

| Version | Änderung | Ergebnis |
|---|---|---|
| v1 | 5 Berichte, 6 Fragen, alle Berichte im Prompt | 5/6 erfüllt |
| v2 | 10 Berichte (Fahrzeuge dazu), 10 Fragen | 7/10 |
| v3 | Regel: Lücken auch je Teilfrage benennen | 7/10, Regel ohne sichtbare Wirkung |
| v4 | 13 Berichte, Erfahrungsberichte dazu | 11/13 |
| v5 | Regel Erfahrungen vs. Regeln; Quellen mit Titel und Datum; 3 Durchläufe | 31/39; je Durchlauf 9–12 von 13 |
| v6 | Zusammenfassungen und Änderungsverlauf (17 Fragen) | 41/51 |
| v7 | Belege je Satz mit wörtlichem Zitat, automatische Prüfung, Quellen vom Programm | 213/213 Zitate gültig; 44/51 |
| v8 | Regel: exakt und knapp | 45/51; 11 % kürzer |
| v9 | 4 Berichte mit abweichendem Format | 43/51; Metadaten korrekt ausgelesen |
| v10 | Widerspruch nur über das Datum auflösbar | 6/6 |

## Erkenntnisse

- **Grundsätzlich tragfähig (Messung v1–v10):** Mit allen Berichten im Prompt beantwortet das Modell die meisten Fragen korrekt; erfundene Sachinhalte wurden nicht beobachtet.
- **Neuester Stand wird über das Datum erkannt (Messung v10):** Das Modell ordnet widersprüchliche Berichte nach dem Datum, auch wenn Reihenfolge und Kennung in die falsche Richtung zeigen und kein sprachlicher Hinweis vorhanden ist.
- **Regeln und Erfahrungen müssen ausdrücklich unterschieden werden (Messung v4/v5):** Ohne eigene Regel ordnet das Modell abweichende Erfahrungen nicht den Berichten zu; mit Regel gelingt das zuverlässig.
- **Prompt-Regeln wirken nicht immer (Messung v3, v8):** Die Regel, Lücken je Teilfrage zu benennen, änderte die Antworten auf Verantwortungsfragen nicht; die Regel gegen Formulierungen wie „ein Bericht“ wirkte kaum.
- **Quellen sollte das Programm erzeugen, nicht das Modell (Messung v2–v7):** Vom Modell geschriebene Quellenlisten waren unzuverlässig (fehlende Daten, falsche Zusatzquellen in 2–3 von 51 Antworten). Mit Belegen je Satz und Zitatprüfung waren alle Zitate echt; Titel und Datum kommen aus den Berichten.
- **Zitatprüfung hat eine Grenze (Messung v7–v9):** Ein echtes Zitat aus einem unpassenden Bericht wird nicht erkannt; falsche Zusatzquellen bleiben vereinzelt.
- **Fußnoten als Kompromiss (Nutzer):** Nummern im Text und Liste am Ende verbinden Lesbarkeit und Glaubwürdigkeit.
- **Knappe Antworten möglich (Messung v8):** Rund 11 % kürzer ohne Verlust der Pflichthinweise; die Kürzung kann vereinzelt zu weit gehen.
- **Zusammenfassungen gelingen bei kleiner Sammlung (Messung v6–v9):** Checklisten nahezu vollständig, überholte Stände erscheinen nicht.
- **Schwankung zwischen Durchläufen (Messung v5):** Bei identischem Aufbau 9–12 von 13 Fragen erfüllt; Einzelläufe reichen für Vergleiche nicht.
- **Uneinheitliche Formate (Messung v9):** Das Programm liest Titel und Datum in bekannten Formaten korrekt aus; fehlt die Überschrift, bleibt nur der Dateiname als Titel. Die Antwortqualität sank nicht erkennbar.
- **Laufzeit (Messung v7–v10, Nutzer):** Rund 190 s für 51 Anfragen mit fünf parallelen Anfragen; schon bei 13–15 kurzen Berichten spürbar lang, für einen PoC akzeptabel. Ein Testlauf stellt aber viele Fragen auf einmal; im Einsatz stellt man eine oder wenige gezielte Fragen (Wartezeit je Frage nicht gemessen).

## Grenzen

- Kleiner, synthetischer Datensatz mit kurzen Berichten; Berichte und Fragen von einem KI-Agenten erstellt.
- Bewertung durch ein anderes KI-Modell (Claude), keine unabhängige menschliche Prüfung; die Nutzerprüfung steht teilweise aus.
- Bisher alle Berichte vollständig im Prompt; das Finden relevanter Berichte (Suche) ist noch nicht getestet.
- Ein Modell, eine Sprache (Deutsch), drei Durchläufe; keine belastbaren Häufigkeiten.
- Datumstest nur mit einem Berichtspaar, großem Zeitabstand und ohne Gegenprobe.
- Cloud-API, kein Offlinebetrieb; nur fiktive Daten, keine Aussage zur Eignung für eingestufte Inhalte.
- Bewertungskriterien teils vom Nutzer nachträglich angepasst (Frage 17 nach v8); Neubewertungen sind in den Bewertungsdateien vermerkt.

## Empfehlungen

- **Einheitliches Ablageformat (Nutzer, gestützt durch Messung v9):** Fließtext frei, aber feste Plätze für Metadaten: immer eine Überschrift, Datum immer an derselben Stelle (etwa rechts oben), am Ende ein Name. Titel und Datum werden für Quellen und zeitliche Einordnung gebraucht und lassen sich nur dann zuverlässig und nachvollziehbar auslesen; ohne Überschrift bleibt nur der Dateiname als Titel.
- **Quellen vom Programm erzeugen und als Fußnoten zeigen (Nutzer, Messung v7):** Das Modell belegt mit Kennung und Zitat; Titel und Datum stammen aus den Berichten.
- **Jede Änderung mit mehreren Testläufen prüfen (Messung v5).**
- **Bessere technische Umsetzung für den realen Einsatz (Vorschlag, vom Nutzer befürwortet, technisch ungeprüft):** vorgeschaltete Suche statt aller Berichte im Prompt, schrittweise Zusammenfassung bei vielen Berichten, schnelleres Modell oder weniger Denkzeit; Wirkung und Qualitätsverlust jeweils messen.

## Nächste Schritte

- **In Arbeit:** Suche statt aller Berichte im Prompt. Sammlung auf etwa 50 Berichte mit Störberichten (ähnliche Wörter in anderem Kontext, fremde Themen, mehrere Stände, lange Berichte mit mehreren Themen); Stichwortsuche und Suche nach Bedeutung ohne Modellkosten vergleichen, danach Antwortlauf (Nutzerentscheidung).
- **Danach:** einfache lokale Browser-Oberfläche; andere Dateiformate (PDF, Word) als eigener Importtest.
- **Optional:** prüfen, ob ein Zitat die Aussage wirklich stützt; härtere Datumstests (nahe Daten, gemischte Formate, mehrere Stände).
- **Spätere Ausbaustufen:** lokales, mittelgroßes Modell offline im Vergleich zu den Frontier-Ergebnissen; Aussagen-Klassifikator; Mehrnutzerbetrieb.
