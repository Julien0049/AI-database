# Testfragen und Antwortentwürfe

**Status:** Fragen 1–6 und ihre Antwortentwürfe wurden mit dem Nutzer einzeln geprüft (Stand `dataset-v1`). Fragen 7–10 zur Fahrzeugausleihe wurden vom Nutzer durchgesehen und als passend bestätigt. Fragen 11–13 zu Erfahrungsberichten folgen einem mit dem Nutzer abgestimmten Entwurf; der endgültige Wortlaut ist noch durchzusehen. Fragen 14–17 (Zusammenfassungen und Änderungsverlauf) sind Agentenentwürfe nach Vorgabe des Nutzers und noch zu prüfen. Vor einem Modellvergleich sollen sie nach Abschluss der weiteren Testdatensatz-Arbeit eingefroren werden.
**Datensatz:** Die dreizehn synthetischen Markdown-AARs in diesem Ordner (fünf zur Materialrückgabe, fünf zur Fahrzeugausleihe, drei Erfahrungsberichte zur Winterkleidung).
**Zweck:** Prüfen, ob ein System direkte Belege findet, Widersprüche und Ergänzungen unterscheidet, den passenden Kontext berücksichtigt und bei fehlender Evidenz nicht rät.

Quellen werden in den Antwortentwürfen mit Titel und Datum angegeben, weil ein Datum allein bei vielen Berichten pro Tag nicht eindeutig ist. Die Zielantworten sind bewusst knapp und auf den geschilderten Anwendungsfall ausgerichtet. Die Hinweise zur Bewertung sind für die Auswertung gedacht und sollen nicht zwingend in der Nutzerantwort erscheinen. Bei Konfliktfällen kann das System den älteren Widerspruch intern erkennen und dafür bewertet werden, während die Nutzerantwort nur das passende Verfahren und dessen stützende Quelle(n) nennt.

## Frage 1 – Widerspruch und neuester passender Stand

**Frage**

> Ich nehme an einem dreitägigen Seminar teil. Unsere Gruppe hat ein Materialset gemeinsam genutzt. Wie wird die Rückgabe bestätigt?

**Erwartete Belege**

- [AAR-2022-09-14-material-return.md](./AAR-2022-09-14-material-return.md)
- [AAR-2024-03-02-multi-day-seminar-returns.md](./AAR-2024-03-02-multi-day-seminar-returns.md)
- [AAR-2025-01-20-shared-set-returns.md](./AAR-2025-01-20-shared-set-returns.md)

**Geprüfter Antwortentwurf**

> Jede teilnehmende Person bestätigt die Rückgabe der von ihr genutzten Bestandteile. Die Gruppenvertretung reicht zusätzlich eine Gesamtübersicht des gemeinsam genutzten Sets ein.
> **Quelle:** „Rückgabe gemeinsamer Sets im Seminarbetrieb“ (20.01.2025).

**Woran eine gute Antwort erkennbar ist**

- Ordnet „dreitägig“ korrekt als mehrtägig ein.
- Gibt die im jüngsten passenden Bericht beschriebene Verfahrensweise knapp wieder.
- Nennt AAR 3 als Quelle, ohne den älteren abweichenden Stand in der Nutzerantwort aufzuzählen.
- Die Erkennung des Widerspruchs zum älteren Bericht wird separat in der internen Evaluation bewertet.
- Bezeichnet AAR 3 nicht als formell „gültig“ oder verbindlich; die Testquellen belegen nur, dass es die jüngste passende Quelle ist.

## Frage 2 – Widerspruch plus ergänzende Quelle

**Frage**

> Bei unserem dreitägigen Seminar fehlt nach der gemeinsamen Nutzung ein Adapter aus dem Materialset. Wie dokumentieren wir die Rückgabe und den fehlenden Adapter?

**Erwartete Belege**

- [AAR-2025-01-20-shared-set-returns.md](./AAR-2025-01-20-shared-set-returns.md)
- [AAR-2025-02-04-missing-items.md](./AAR-2025-02-04-missing-items.md)
- Ältere abweichende Stände: [AAR-2022-09-14-material-return.md](./AAR-2022-09-14-material-return.md) und [AAR-2024-03-02-multi-day-seminar-returns.md](./AAR-2024-03-02-multi-day-seminar-returns.md)

**Geprüfter Antwortentwurf**

> Jede teilnehmende Person bestätigt die Rückgabe der von ihr genutzten Bestandteile; die Gruppenvertretung reicht zusätzlich die Gesamtübersicht ein. Den fehlenden Adapter mit Set-Kennung und Entdeckungsdatum im Abweichungsprotokoll erfassen und noch am selben Tag der Materialverwaltung melden.
> **Quellen:** „Rückgabe gemeinsamer Sets im Seminarbetrieb“ (20.01.2025); „Umgang mit fehlenden Bestandteilen“ (04.02.2025).

**Woran eine gute Antwort erkennbar ist**

- Führt das Rückgabeverfahren und die Meldeanforderung zusammen.
- Erfindet keine Adapter-Seriennummer oder zusätzliche Meldepflicht.
- Gibt nur das neueste passende Rückgabeverfahren aus und nennt AAR 3 sowie AAR 4 als Quellen.
- Die Erkennung des älteren Konflikts wird separat intern bewertet, nicht als zusätzliche Option in der Nutzerantwort ausgegeben.

## Frage 3 – Anderer Kontext trotz jüngeren Datums

**Frage**

> Ich nehme an einem eintägigen Einführungsseminar teil und habe Gegenstände auf meiner persönlichen Ausgabeliste. Wie bestätige ich die Rückgabe?

**Erwartete Belege**

- [AAR-2025-06-10-one-day-seminars.md](./AAR-2025-06-10-one-day-seminars.md)

**Antwortentwurf**

> Du bestätigst anhand deiner persönlichen Ausgabeliste die Rückgabe der dir zugeordneten Gegenstände.

**Woran eine gute Antwort erkennbar ist**

- Wendet den Bericht zu eintägigen Einführungsveranstaltungen an.
- Überträgt nicht automatisch das Verfahren für mehrtägige Seminare.
- Erfindet keinen Konflikt, wenn die Frage im beschriebenen Kontext beantwortbar ist.

## Frage 4 – Direkte Regel zu einzeln nummeriertem Gerät

**Frage**

> Ein einzeln nummeriertes Gerät wurde einer Person zugeordnet, aber während des Seminars gemeinsam genutzt. Wer bestätigt die Rückgabe?

**Erwartete Belege**

- [AAR-2022-09-14-material-return.md](./AAR-2022-09-14-material-return.md)

**Antwortentwurf**

> Die eingetragene Person bleibt dem Gerät zugeordnet und gibt es zurück; sie bestätigt auch die Rückgabe der aufgeführten Gegenstände.

**Woran eine gute Antwort erkennbar ist**

- Findet die direkte Regel im Bericht.
- Verallgemeinert nicht aus den Verfahren für gemeinsam genutzte Sets auf einzeln nummerierte Geräte.

## Frage 5 – Fehlende Evidenz zu persönlicher Verantwortung

**Frage**

> Ein Adapter fehlt, nachdem mehrere Gruppen das Set gemeinsam genutzt haben. Welche Person ist dafür verantwortlich?

**Erwartete Belege**

- [AAR-2025-02-04-missing-items.md](./AAR-2025-02-04-missing-items.md)

**Antwortentwurf**

> Das lässt sich aus den Berichten nicht feststellen. Das Fehlen allein belegt keine persönliche Verantwortung.

**Woran eine gute Antwort erkennbar ist**

- Lehnt es ab, eine Person oder Gruppe zu beschuldigen.
- Erfindet keine Übergabe oder Zuständigkeit.

## Frage 6 – Nicht belegtes Verfahrensdetail

**Frage**

> Welches konkrete Formularfeld oder welche interne Kennziffer muss ich verwenden, wenn ich den fehlenden Adapter melde?

**Erwartete Belege**

- [AAR-2025-02-04-missing-items.md](./AAR-2025-02-04-missing-items.md)

**Antwortentwurf**

> Die Berichte nennen Set-Kennung, Gegenstandsbezeichnung und Entdeckungsdatum für das Abweichungsprotokoll, aber kein konkretes Formularfeld oder eine interne Kennziffer.

**Woran eine gute Antwort erkennbar ist**

- Gibt die tatsächlich belegten Angaben wieder.
- Erfindet weder ein Formularlayout noch eine Kennziffer.

## Frage 7 – Versteckter Widerspruch, neuester Stand

**Frage**

> Muss ich das Dienstfahrzeug vollgetankt zurückgeben?

**Erwartete Belege**

- [AAR-2025-03-18-logbook-form.md](./AAR-2025-03-18-logbook-form.md)
- Älterer abweichender Stand: [AAR-2023-04-12-vehicle-returns.md](./AAR-2023-04-12-vehicle-returns.md)

**Antwortentwurf**

> Nein. Bei der Rückgabe wird der Tankstand im Fahrtenbuch vermerkt; das Betanken übernimmt anschließend die Fahrbereitschaft.
> **Quelle:** „Erfahrungen mit dem Fahrtenbuch-Formular“ (18.03.2025).

**Woran eine gute Antwort erkennbar ist**

- Findet die Tankregel, obwohl der Bericht hauptsächlich vom Fahrtenbuch-Formular handelt.
- Folgt dem jüngeren Bericht und nennt „vollgetankt“ nicht als gleichrangige Alternative.
- Der Widerspruch zu AAR 2023-04-12 ist im jüngeren Bericht nicht als Änderung gekennzeichnet; seine Erkennung wird separat intern bewertet.

## Frage 8 – Ähnliche Stichworte, anderer Kontext

**Frage**

> Wir haben bei einem dreitägigen Seminar ein Fahrzeug gemeinsam genutzt. Wer bestätigt die Rückgabe?

**Erwartete Belege**

- [AAR-2025-09-15-vehicles-multi-day-seminars.md](./AAR-2025-09-15-vehicles-multi-day-seminars.md)
- Ergänzend möglich: [AAR-2023-04-12-vehicle-returns.md](./AAR-2023-04-12-vehicle-returns.md)

**Antwortentwurf**

> Die Person, die das Fahrzeug ausgeliehen hat. Das Fahrzeug bleibt ihr auch bei gemeinsamer Nutzung zugeordnet; sie gibt es zurück und bestätigt die Rückgabe gegenüber der Fahrbereitschaft.
> **Quelle:** „Fahrzeugnutzung bei mehrtägigen Seminaren“ (15.09.2025).

**Woran eine gute Antwort erkennbar ist**

- Überträgt nicht das Verfahren für gemeinsam genutzte Materialsets (persönliche Bestätigung plus Gesamtübersicht der Gruppenvertretung).
- Nennt keine Material-AARs als Quelle.

## Frage 9 – Ergänzung und fehlende Evidenz zur Verantwortung

**Frage**

> Bei der Rückgabe ist ein Kratzer am Fahrzeug. Was ist zu tun, und wer ist verantwortlich?

**Erwartete Belege**

- [AAR-2024-11-05-vehicle-damage.md](./AAR-2024-11-05-vehicle-damage.md)

**Antwortentwurf**

> Den Schaden mit Kennzeichen und Datum im Schadensformular erfassen und das Formular mit dem Fahrzeugschlüssel bei der Fahrbereitschaft abgeben. Wer verantwortlich ist, lässt sich aus den Berichten nicht feststellen; aus dem Schaden allein wird keine persönliche Verantwortung abgeleitet.
> **Quelle:** „Erfassung von Fahrzeugschäden“ (05.11.2024).

**Woran eine gute Antwort erkennbar ist**

- Verwendet das Schadensformular, nicht das Abweichungsprotokoll für fehlendes Material.
- Benennt keine verantwortliche Person und erfindet keine Meldefrist.

## Frage 10 – Teilweise belegte Frage

**Frage**

> Wie früh muss ich ein Fahrzeug reservieren, und was kostet die Ausleihe?

**Erwartete Belege**

- [AAR-2024-01-08-vehicle-reservations.md](./AAR-2024-01-08-vehicle-reservations.md)

**Antwortentwurf**

> Mindestens zwei Werktage vor der geplanten Fahrt bei der Fahrbereitschaft. Zu Kosten der Ausleihe enthalten die Berichte keine Angaben.
> **Quelle:** „Reservierung von Fahrzeugen“ (08.01.2024).

**Woran eine gute Antwort erkennbar ist**

- Beantwortet den belegten Teil.
- Sagt offen, dass zu Kosten nichts belegt ist, und erfindet keinen Betrag.

## Frage 11 – Erfahrungen zusammenführen, Abweichung benennen

**Frage**

> Welche Kleidung hat sich bei mehrtägigen Winter-Außenseminaren bewährt?

**Erwartete Belege**

- [AAR-2023-02-15-winter-clothing-layers.md](./AAR-2023-02-15-winter-clothing-layers.md)
- [AAR-2024-01-25-winter-waiting-times.md](./AAR-2024-01-25-winter-waiting-times.md)
- [AAR-2025-12-10-winter-socks-and-jackets.md](./AAR-2025-12-10-winter-socks-and-jackets.md)

**Antwortentwurf**

> Bewährt haben sich mehrere dünne Kleidungsschichten und zwei Paar Handschuhe zum Wechseln (15.02.2023) sowie Wollsocken statt Baumwollsocken mit Ersatzsocken (10.12.2025). Eine wasserdichte Überjacke ist laut Bericht vom 10.12.2025 für alle Teilnehmenden vorgeschrieben. Bei der Daunenjacke gehen die Erfahrungen auseinander: beim Gehen meist zu warm (15.02.2023), bei langen Wartezeiten im Freien unverzichtbar (25.01.2024); zuletzt waren die Teilnehmenden uneinig (10.12.2025).
> **Quellen:** „Kleidung bei mehrtägigen Winter-Außenseminaren“ (15.02.2023); „Wartezeiten im Freien bei Winterseminaren“ (25.01.2024); „Ausrüstung beim Winter-Außenseminar“ (10.12.2025).

**Woran eine gute Antwort erkennbar ist**

- Führt die ergänzenden Erfahrungen zusammen.
- Kennzeichnet die wasserdichte Überjacke als Vorgabe, nicht als bloße Erfahrung.
- Nennt bei der Daunenjacke beide Sichtweisen mit Quelle und Datum und weist auf die Abweichung hin.

## Frage 12 – Abweichende Erfahrungen ohne Priorität nach Datum

**Frage**

> Brauche ich bei einem mehrtägigen Winter-Außenseminar eine dicke Daunenjacke?

**Erwartete Belege**

- [AAR-2023-02-15-winter-clothing-layers.md](./AAR-2023-02-15-winter-clothing-layers.md)
- [AAR-2024-01-25-winter-waiting-times.md](./AAR-2024-01-25-winter-waiting-times.md)
- [AAR-2025-12-10-winter-socks-and-jackets.md](./AAR-2025-12-10-winter-socks-and-jackets.md)

**Antwortentwurf**

> Die Berichte gehen auseinander. Beim Gehen fanden die meisten eine dicke Daunenjacke zu warm und haben darin geschwitzt (15.02.2023). Bei langen Wartezeiten im Freien war sie nach Erfahrung der meisten unverzichtbar (25.01.2024). Zuletzt waren die Teilnehmenden uneinig (10.12.2025). Eine klare Empfehlung lässt sich daraus nicht ableiten.
> **Quellen:** „Kleidung bei mehrtägigen Winter-Außenseminaren“ (15.02.2023); „Wartezeiten im Freien bei Winterseminaren“ (25.01.2024); „Ausrüstung beim Winter-Außenseminar“ (10.12.2025).

**Woran eine gute Antwort erkennbar ist**

- Behandelt den jüngeren Bericht nicht als „aktuellen Stand“, der ältere Erfahrungen ersetzt.
- Nennt die unterschiedlichen Situationen (Gehen gegenüber langen Wartezeiten), soweit die Berichte sie beschreiben.
- Gibt keine eigene Empfehlung, die über die Berichte hinausgeht.

## Frage 13 – Nicht belegtes Detail

**Frage**

> Welche Marke wird für die Winterjacke empfohlen, und ab welcher Temperatur sollte man sie tragen?

**Erwartete Belege**

- Keine; die Erfahrungsberichte zur Winterkleidung nennen weder Temperaturen noch Marken.

**Antwortentwurf**

> Dazu enthalten die Berichte keine Angaben.

**Woran eine gute Antwort erkennbar ist**

- Erfindet weder Temperaturgrenzen noch Marken.
- Darf knapp auf die belegten Erfahrungen zu Jacken verweisen, ohne sie als Antwort auf diese Frage auszugeben.

## Frage 14 – Zusammenfassung eines Themas mit Verfahren

**Frage**

> Fasse alles zusammen, was die Berichte zur Fahrzeugausleihe sagen.

**Erwartete Belege**

Alle fünf Fahrzeugberichte (12.04.2023, 08.01.2024, 05.11.2024, 18.03.2025, 15.09.2025).

**Checkliste der Kernaussagen**

- Reservierung mindestens zwei Werktage vorher bei der Fahrbereitschaft, mit Datum, voraussichtlicher Rückgabezeit und Fahrtziel – „Reservierung von Fahrzeugen“ (08.01.2024).
- Rückgabe durch die ausleihende Person: Schlüssel bei der Fahrbereitschaft abgeben, Kilometerstand ins Fahrtenbuch – „Rückgabe von Dienstfahrzeugen“ (12.04.2023).
- Tankstand bei der Rückgabe vermerken, die Fahrbereitschaft tankt; Kilometerstand und Fahrtzweck in getrennten Feldern – „Erfahrungen mit dem Fahrtenbuch-Formular“ (18.03.2025).
- Schäden vor Fahrtantritt und bei Rückgabe mit Kennzeichen und Datum im Schadensformular erfassen, Formular mit dem Schlüssel abgeben; aus einem Schaden allein keine persönliche Verantwortung – „Erfassung von Fahrzeugschäden“ (05.11.2024).
- Bei gemeinsamer Nutzung in mehrtägigen Seminaren bleibt das Fahrzeug der ausleihenden Person zugeordnet; sie gibt es zurück und bestätigt die Rückgabe – „Fahrzeugnutzung bei mehrtägigen Seminaren“ (15.09.2025).

**Woran eine gute Antwort erkennbar ist**

- Deckt alle Punkte der Checkliste ab.
- Nennt nur den aktuellen Stand zur Tankregel; „vollgetankt zurückgeben“ erscheint nicht.
- Übernimmt nichts aus den Material- oder Kleidungsberichten.

## Frage 15 – Zusammenfassung von Erfahrungen

**Frage**

> Gib mir eine Zusammenfassung der Erfahrungen mit Winter-Außenseminaren.

**Erwartete Belege**

Alle drei Erfahrungsberichte zur Winterkleidung (15.02.2023, 25.01.2024, 10.12.2025).

**Checkliste der Kernaussagen**

- Mehrere dünne Schichten haben sich beim Gehen bewährt; eine dicke Daunenjacke war dabei meist zu warm – „Kleidung bei mehrtägigen Winter-Außenseminaren“ (15.02.2023).
- Zwei Paar Handschuhe zum Wechseln waren hilfreich – ebenda.
- Bei langen Wartezeiten im Freien war eine Daunenjacke unverzichtbar; Schichten allein reichten den meisten nicht – „Wartezeiten im Freien bei Winterseminaren“ (25.01.2024).
- Wollsocken besser als Baumwollsocken, Ersatzsocken häufig gebraucht – „Ausrüstung beim Winter-Außenseminar“ (10.12.2025).
- Bei Jacken waren die Teilnehmenden uneinig – ebenda.
- Vorgabe: Eine wasserdichte Überjacke ist für alle vorgeschrieben – ebenda.

**Woran eine gute Antwort erkennbar ist**

- Deckt alle Punkte der Checkliste ab.
- Stellt die abweichenden Erfahrungen zur Daunenjacke nebeneinander, jeweils mit Titel und Datum, ohne Priorität nach Datum.
- Trennt die Vorgabe zur Überjacke erkennbar von den Erfahrungen.

## Frage 16 – Themenübergreifende Zusammenfassung

**Frage**

> Fasse zusammen, was bei mehrtägigen Seminaren zu beachten ist.

**Erwartete Belege**

- [AAR-2025-01-20-shared-set-returns.md](./AAR-2025-01-20-shared-set-returns.md)
- [AAR-2025-09-15-vehicles-multi-day-seminars.md](./AAR-2025-09-15-vehicles-multi-day-seminars.md)
- Die drei Erfahrungsberichte zur Winterkleidung (beziehen sich auf mehrtägige Außenseminare)
- Ergänzend möglich: allgemeine Berichte zu fehlendem Material, Schäden oder Fahrzeugrückgabe

**Checkliste der Kernaussagen**

- Gemeinsam genutzte Materialsets: Jede Person bestätigt die von ihr genutzten Bestandteile auf der persönlichen Liste, die Gruppenvertretung reicht zusätzlich eine Gesamtübersicht ein – „Rückgabe gemeinsamer Sets im Seminarbetrieb“ (20.01.2025).
- Gemeinsam genutzte Fahrzeuge bleiben der ausleihenden Person zugeordnet; sie gibt sie zurück und bestätigt die Rückgabe – „Fahrzeugnutzung bei mehrtägigen Seminaren“ (15.09.2025).
- Bei Winter-Außenseminaren: Erfahrungen zur Kleidung mit abweichenden Sichtweisen zur Daunenjacke und vorgeschriebener wasserdichter Überjacke (drei Kleidungsberichte).

**Woran eine gute Antwort erkennbar ist**

- Ordnet Material, Fahrzeuge und Kleidung jeweils richtig zu und vermischt die Verfahren nicht.
- Nennt beim Material nur den aktuellen Stand, nicht das Verfahren vom 02.03.2024.
- Übernimmt nicht die Regel für eintägige Einführungsveranstaltungen.

## Frage 17 – Ausdrückliche Frage nach Änderungen

**Frage**

> Wie hat sich das Verfahren zur Rückgabe gemeinsam genutzter Materialsets bei mehrtägigen Seminaren über die Zeit verändert?

**Erwartete Belege**

- [AAR-2022-09-14-material-return.md](./AAR-2022-09-14-material-return.md)
- [AAR-2024-03-02-multi-day-seminar-returns.md](./AAR-2024-03-02-multi-day-seminar-returns.md)
- [AAR-2025-01-20-shared-set-returns.md](./AAR-2025-01-20-shared-set-returns.md)

**Antwortentwurf**

> Laut „Rückgabe ausgegebener Materialsets“ (14.09.2022) wurden auch gemeinsam genutzte Sets einer Person zugeordnet, die die Rückgabe bestätigte; dieser Bericht bezieht sich nicht ausdrücklich auf mehrtägige Seminare. Laut „Materialrückgabe bei mehrtägigen Seminaren“ (02.03.2024) prüfte die Gruppenvertretung das Set und führte eine gemeinsame Rückgabeliste; eine persönliche Bestätigung war nicht vorgesehen. Laut „Rückgabe gemeinsamer Sets im Seminarbetrieb“ (20.01.2025) bestätigt jede Person die von ihr genutzten Bestandteile, und die Gruppenvertretung reicht zusätzlich eine Gesamtübersicht ein, weil Bestandteile zuvor nicht immer eindeutig zuzuordnen waren.

**Woran eine gute Antwort erkennbar ist**

- Nennt die Stände in zeitlicher Reihenfolge mit Titel und Datum.
- Gibt den Grund für die jüngste Änderung nur so wieder, wie er im Bericht steht, und erfindet keine weiteren Gründe.
- Weist darauf hin, dass der Bericht von 2022 nicht ausdrücklich mehrtägige Seminare betrifft, oder behauptet zumindest nichts anderes.

## Vorgeschlagene Auswertung

Pro Frage getrennt festhalten:

1. Wurden alle erwarteten Belegberichte abgerufen?
2. Sind die Kernaussagen der Antwort durch diese Berichte gedeckt?
3. Wurden Widerspruch, Ergänzung und Kontext richtig behandelt?
4. Wurde unbelegte Information vermieden?
5. Ist die Antwort knapp genug, um die konkrete Frage direkt zu beantworten?
6. Bei Zusammenfassungen: Welcher Anteil der Checkliste ist abgedeckt?

Vor einem Modellvergleich sollten Frageformulierungen, erwartete Belege und Antwortentwürfe geprüft und danach eingefroren werden. Kleine Modellantworten lassen sich dann anhand derselben Kriterien vergleichen.
