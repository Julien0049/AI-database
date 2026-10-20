# Interview-Rohnotizen

Datum: 2026-10-19
Zweck: Rohantworten zum Kick-off der Semesterarbeit. Direkte Antworten sind wörtlich übernommen; ausgewählte Antwortoptionen sind als Auswahl markiert. Dies ist keine fachliche Spezifikation oder Zusammenfassung.

## Projekt und bisheriger Kontext

> „in KI projektidee.md ist schon ein langer dialog mit gemini, indem die idee schon ganz gut als start entwickelt wurde. schau dir bitte das auch an“

> „ok. ich wuerde schon gern an dem projekt auch als semester projekt arbeiten, ich hoffe, dass es genug hergibt und nicht zu simpel ist“

> „am ende der semesterarbeit soll gemaess der brainstorming datei eine einfache version einer AI database entstanden sein, die anhand von ein paar beispiel after action reports gezielte fragen fuer den endanwender beantwortet und gleichzeitig es schafft immer das neuste wissen zu benutzen“

> „wichtig ist am ende, dadurch dass es um eingestufte inhate geht, muss es moeglich sein, alles autark laufen zulassen. kein internet zugriff“

Ausgewählte Klärung: Offlinebetrieb während der Nutzung; Einrichtung darf vorher kontrolliert online erfolgen.

> „richtig, wenn es in den quellen verschiedene aussagen zu einem thema gibt, z.b. weil sich verfahren geandert haben, will ich schon, dass die antwort, dass neueste vorschlägt, aber darauf hinweist, dass es ältere andere versionen gibt. es darf nicht dazu führen, dass der endanwender nicht weiß, was er jetz machen soll, weil ihm mehrere optionen gegeben werden“

Ausgewählte Klärung: Die neueste Quelle nur priorisieren, wenn sie auf denselben Kontext passt; bei unklarer Anwendbarkeit keine sichere Priorität behaupten.

> „ja, wir koennen aber die 10 dokumente, die schonmal erstellt wurden als grundlage nutzen“

> „um zu zeigen, dass das projekt funktioniert reichen am ende auch fiktive testdaten, der inhalt ist erstmal zweitrangig solang die funktion passt und ja ich hatte im verlauf die beispieldokumente in interativen schon mit gemini verbessert“

Ausgewählte Klärung: Spätere Skalierung meint vor allem mehr Dokumente.

## Interviewantworten

**Zielgruppe (Auswahl):** Einzelne Angehörige einer Organisation, die frühere fiktive AARs nachschlagen.

> „es ist so, dass in unzaehligen ordnern irgendwelche after aktion reports liegen von denen entweder keiner weiß oder man nicht schafft alles zu lesen. es soll also eine datenbank entstehen, wo all dieses dokumente sind und wenn ich als soldat einen auftrag erhalte und fragen habe, z.b. welche ausruestung benoetige ich fur ein biwak im hochalpinen gelaende, dann soll die KI all die dokumente der datenbank durchsuchen und die passende antwort liefern“

> „da die database offline laufen muss, konnen nur die, jetzt noch fiktiven, dokumente die quelle der antworten sein“

**Wenn Evidenz fehlt (Auswahl):** Klar sagen, dass die Dokumente keine ausreichende Antwort enthalten, und keine Lücken füllen.

**Dateiformat für den Semesterprototyp (Auswahl):** Zunächst Markdown/Text; spätere Formate sind offen.

**Import neuer Dokumente (Auswahl):** Dateien in einen festgelegten lokalen Ordner legen; den Import gezielt starten.

> „vorangig ist die antwort selbst wichtig, oft wird es keine zeit geben alles selbst du referenzieren und nochmal im orginal nachzulesen. vor allem dann nicht, wenn die antwort aus mehreren quellen stammt. es ist nicht ausgeschlossen, dass in mehreren dokumenten antworten zu der frage stehen, die sich erganzen“

**Quellenformat (Auswahl):** Antwort zuerst und Quellen kompakt am Ende (Dokumentname und Datum, bei Bedarf relevante Stelle).

**Erfolgskriterium (Auswahl):** Testfragen mit passenden Quellen beantworten, bei vergleichbarem Kontext den neuesten Stand priorisieren und fehlende Evidenz erkennen.

**Oberfläche für die erste Version (Auswahl):** Einfache lokale Chat-Oberfläche im Browser.

**Zielhardware (Auswahl):** Eigener Mac/Computer ohne zusätzliche GPU.
