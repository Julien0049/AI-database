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

### Warum eine vorgeschaltete Suche und wie sie getestet wird

- **Warum (Vorschlag, vom Nutzer befürwortet):** Bis v10 bekam das Modell alle Berichte in jeder Anfrage. Das geht nur bei einer kleinen Sammlung. Eine reale Sammlung mit Tausenden Berichten passt nicht in eine Anfrage, und schon bei 13–15 kurzen Berichten war die Laufzeit spürbar. Üblich ist deshalb ein zweistufiges Vorgehen (Retrieval-Augmented Generation): Ein Suchprogramm wählt zu jeder Frage die passendsten Berichte aus, und nur diese gehen an das Modell.
- **Neues Risiko:** Findet die Suche einen nötigen Bericht nicht, kann auch das beste Modell nicht richtig antworten. Besonders kritisch für die Kernregel „der neueste Stand gilt“: Fehlt der neueste Bericht unter den Treffern, nennt das Modell einen überholten Stand als aktuell, ohne dass es das merken kann. Bei Zusammenfassungen fehlen sonst Inhalte.
- **Warum die Suche getrennt messen (Nutzerentscheidung):** Für jede Testfrage ist festgelegt, welche Berichte nötig sind. Ob sie unter den ersten k Treffern liegen, lässt sich ohne Sprachmodell prüfen: kostenlos, beliebig wiederholbar und unabhängig von der Schwankung der Modellantworten. So lassen sich Fehler der Suche von Fehlern des Modells trennen. Erst danach folgt ein Antwortlauf mit der besten Suchmethode.
- **Strenge Kennzahl „vollständig@k“:** Anteil der Fragen, bei denen *alle* nötigen Berichte unter den ersten k Treffern liegen (k = 3, 5, 10). Ein einzelner fehlender Bericht kann die Antwort falsch oder unvollständig machen; deshalb zählt nur Vollständigkeit.
- **Warum zwei Methoden vergleichen (Nutzerentscheidung):** Die Stichwortsuche (BM25) ist durchschaubar und ohne Zusatzsoftware, übersieht aber andere Wortformen und Synonyme. Die Suche nach Bedeutung (Embeddings mit einem kleinen lokalen Modell, `intfloat/multilingual-e5-small`) erkennt ähnliche Bedeutungen, ist aber weniger nachvollziehbar und kann ähnlich klingende Themen verwechseln. Zusätzlich wird die Kombination beider Ranglisten geprüft. Beide Verfahren laufen lokal ohne GPU und passen damit auch zur späteren Offline-Ausbaustufe.
- **Warum Störberichte (Nutzerentscheidung):** Mit nur 15 passenden Berichten müsste die Suche kaum etwas aussortieren. Die Sammlung wurde deshalb auf 48 Berichte erweitert, mit gezielten Fallen: ähnliche Wörter in anderem Kontext, fremde Themen, mehrere Stände zu einem Thema, Regeln nur nebenbei in langen Berichten. Die bisherigen 19 Fragen behalten ihre erwarteten Antworten, damit „alle Berichte im Prompt“ und „mit Suche“ direkt vergleichbar bleiben.
- **Einheit der Suche:** ein ganzer Bericht, weil die Berichte kurz sind (höchstens etwa 140 Wörter). Bei längeren Dokumenten müsste man sie in Abschnitte teilen; das ist nicht getestet.

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
| s1 | Suchtest ohne Sprachmodell, 48 Berichte, 25 Fragen: Stichwort vs. Bedeutung vs. Kombination | alle nötigen Berichte unter den ersten 5: 50 % / 79 % / 67 %; unter den ersten 10: 58 % / 88 % / 83 % |
| s2 | Suche nach Abschnitten aus zwei Sätzen statt ganzer Berichte | Bedeutung: unter den ersten 5: 79 % → 83 %, unter den ersten 10: 88 % → 83 %; kein klarer Gewinn |

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
- **Suche nach Bedeutung schlägt Stichwortsuche deutlich (Messung s1):** Bei 79 % der Fragen liegen alle nötigen Berichte unter den ersten 5 Treffern (Stichwortsuche: 50 %). Die Stichwortsuche scheitert an anderen Wortformen und zusammengesetzten Wörtern („Fahrzeugausleihe“, „reservieren“/„reserviert“). Die einfache Kombination beider ist schlechter als die Suche nach Bedeutung allein.
- **Einzelfragen ja, Zusammenfassungen nein (Messung s1):** Bei Einzelfragen sind die nötigen Berichte in 19 von 20 Fällen unter den ersten 5; Wortfallen (Sommer/Winter, Fahrradgarage/Raumschlüssel) führten nicht in die Irre. Bei Zusammenfassungen über mehrere Berichte waren es 0 von 4 (unter den ersten 10: 2 von 4). Zusammenfassungen brauchen eine andere Strategie als „die besten k Treffer“.
- **Risiko überholter Stand durch die Suche (Messung s1):** Ein nur nebenbei erwähnter neuester Stand (Seminarunterlagen als Download) wurde von keiner Methode unter den ersten 10 gefunden, die älteren Stände (gedruckt, USB-Stick) standen vorn. Ältere Stände stehen auch sonst oft vor dem neuesten (Beamer: Platz 1–2 alt, Platz 3 neu). Die Suche kann damit die Kernregel „neuester Stand gilt“ unterlaufen, bevor das Modell überhaupt antwortet.
- **Kleinere Sucheinheiten helfen hier nicht (Messung s2):** Suche nach Abschnitten aus zwei Sätzen statt ganzer Berichte änderte das Ergebnis nur um je eine Frage (in beide Richtungen). Der nebenbei erwähnte neueste Stand und die verstreuten Gästeregeln blieben unauffindbar. Die Ursache liegt eher beim kleinen Embedding-Modell und bei der festen Trefferzahl für Zusammenfassungen als bei der Länge der Einheiten.
- **Laufzeit (Messung v7–v10, Nutzer):** Rund 190 s für 51 Anfragen mit fünf parallelen Anfragen; schon bei 13–15 kurzen Berichten spürbar lang, für einen PoC akzeptabel. Ein Testlauf stellt aber viele Fragen auf einmal; im Einsatz stellt man eine oder wenige gezielte Fragen (Wartezeit je Frage nicht gemessen).

## Grenzen

- Kleiner, synthetischer Datensatz mit kurzen Berichten; Berichte und Fragen von einem KI-Agenten erstellt.
- Bewertung durch ein anderes KI-Modell (Claude), keine unabhängige menschliche Prüfung; die Nutzerprüfung steht teilweise aus.
- Die Suche ist bisher nur für sich gemessen (s1); wie gut die Antworten mit Suche sind, ist noch nicht getestet. Ein Embedding-Modell, Einheit ganzer Bericht, keine Variation der Einstellungen.
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

- **In Arbeit:** Suche verbessern, bevor Antworten mit Suche gemessen werden (Nutzereinwand nach s1: „Wenn so viel verloren geht, ist die Strategie vielleicht nicht gut“). Je Version eine Änderung, ohne Modellkosten: s2 kleinere Sucheinheiten (gemessen: kein klarer Gewinn), s3 Thema erweitern (zu jedem Treffer ähnliche Berichte dazunehmen, damit alle Stände eines Themas ankommen), danach eigene Strategie für Zusammenfassungen. Erst dann ein Antwortlauf mit k = 5 (Nutzerentscheidung).
- **Danach:** einfache lokale Browser-Oberfläche; andere Dateiformate (PDF, Word) als eigener Importtest.
- **Optional:** eigene Strategie für Zusammenfassungen (z. B. mehr Treffer oder Suche nach Thema); Stichwortsuche mit Grundformbildung; prüfen, ob ein Zitat die Aussage wirklich stützt; härtere Datumstests (nahe Daten, gemischte Formate, mehrere Stände).
- **Spätere Ausbaustufen:** lokales, mittelgroßes Modell offline im Vergleich zu den Frontier-Ergebnissen; Aussagen-Klassifikator; Mehrnutzerbetrieb.
