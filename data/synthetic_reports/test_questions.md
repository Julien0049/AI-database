# Testfragen und Antwortentwürfe

**Status:** Fragen 1–6 und ihre Antwortentwürfe wurden mit dem Nutzer einzeln geprüft (Stand `dataset-v1`). Fragen 7–10 zur Fahrzeugausleihe wurden vom Nutzer durchgesehen und als passend bestätigt. Fragen 11–13 zu Erfahrungsberichten folgen einem mit dem Nutzer abgestimmten Entwurf; der endgültige Wortlaut ist noch durchzusehen. Fragen 14–17 (Zusammenfassungen und Änderungsverlauf) sind Agentenentwürfe nach Vorgabe des Nutzers; vom Nutzer durchgesehen und vorläufig bestätigt. Fragen 18–19 (Datumstest) und 20–25 (Suchtest) sind Agentenentwürfe, vom Nutzer durchgesehen und bestätigt (Stand `dataset-v3`). Ab `dataset-v4`: Varianten 10b, 14b und 21b sowie Fragen 26–34 (Agentenentwürfe, vom Nutzer bestätigt am 14.11.2026). Vor einem Modellvergleich sollen sie nach Abschluss der weiteren Testdatensatz-Arbeit eingefroren werden.
**Datensatz:** Die 58 synthetischen Markdown-AARs (`dataset-v4`; bis `dataset-v3` 48) in diesem Ordner; Übersicht und Katalog der Testfälle in [README.md](./README.md). Fragen 1–19 beziehen sich auf die 15 Kern- und Datumstestberichte, Fragen 20–25 auf die Berichte für den Suchtest.
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

**Ab `dataset-v4` (Variante 10b, Agentenentwurf, vom Nutzer bestätigt am 14.11.2026)**
- Neuer Beleg: [AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md](./AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md) (27.02.2026), Abschnitt 4.3.
- Erwartete Antwort: Seit dem 01.02.2026 standortweit nur über das Fahrzeugportal im Intranet, mindestens drei Werktage vor Fahrtbeginn; telefonische Anforderungen werden nicht mehr angenommen. Zu Kosten keine Angaben.
- „Zwei Werktage bei der Fahrbereitschaft“ (Bericht ohne Datum) nicht als gleichrangige Alternative nennen. Falle: Die Änderung steht mitten in einer Schilderung eines langen Berichts.

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

**Ab `dataset-v4` (Variante 14b, Agentenentwurf)**
- Zusätzlicher Beleg: [AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md](./AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md) (27.02.2026).
- Reservierung jetzt nur über das Fahrzeugportal, mindestens drei Werktage vorher; „zwei Werktage bei der Fahrbereitschaft“ ist überholt (als aktuell genannt = nicht erfüllt). Die Übungsregeln aus dem Kfz-Dienst-Bericht (19.03.2026) dürfen mit Kontext genannt werden.

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
- Der Stand von 2022 darf fehlen, weil der Bericht mehrtägige Seminare nicht ausdrücklich nennt (Nutzerentscheidung nach Lauf v8). Wird er genannt, gilt das nächste Kriterium.
- Gibt den Grund für die jüngste Änderung nur so wieder, wie er im Bericht steht, und erfindet keine weiteren Gründe.
- Wenn der Bericht von 2022 genannt wird: Weist darauf hin, dass er nicht ausdrücklich mehrtägige Seminare betrifft, oder behauptet zumindest nichts anderes.

## Frage 18 – Widerspruch, nur über das Datum auflösbar

**Frage**

> Wo gebe ich nach einem Abendseminar den Raumschlüssel ab?

**Erwartete Belege**

- [AAR-evening-keys-a.md](./AAR-evening-keys-a.md) (14.10.2025)
- Älterer abweichender Stand: [AAR-evening-keys-b.md](./AAR-evening-keys-b.md) (03.04.2024)

**Antwortentwurf**

> Im Schlüsselkasten des Seminarbüros; die Seminarleitung trägt die Rückgabe in die Schlüsselliste ein.
> **Quelle:** „Schlüsselrückgabe nach Abendseminaren“ (14.10.2025).

**Woran eine gute Antwort erkennbar ist**

- Folgt dem jüngeren Bericht und nennt die Pforte nicht als gleichrangige Alternative.
- Testaufbau: Keiner der beiden Berichte deutet sprachlich an, welcher neuer ist (kein „künftig“, „jetzt“, „geändert“). Der neuere Bericht steht in der Sammlung vor dem älteren und hat die kleinere Kennung, damit Reihenfolge oder Kennung nicht auf die richtige Antwort führen.

## Frage 19 – Änderung ohne genannten Grund

**Frage**

> Wie hat sich die Rückgabe der Raumschlüssel nach Abendseminaren über die Zeit verändert?

**Erwartete Belege**

- [AAR-evening-keys-b.md](./AAR-evening-keys-b.md) (03.04.2024)
- [AAR-evening-keys-a.md](./AAR-evening-keys-a.md) (14.10.2025)

**Antwortentwurf**

> Laut „Raumschlüssel bei Abendseminaren“ (03.04.2024) wurden die Schlüssel an der Pforte abgegeben, die die Rückgabe in die Schlüsselliste eintrug. Laut „Schlüsselrückgabe nach Abendseminaren“ (14.10.2025) werden sie im Schlüsselkasten des Seminarbüros abgelegt, und die Seminarleitung trägt die Rückgabe ein. Einen Grund für die Änderung nennen die Berichte nicht.

**Woran eine gute Antwort erkennbar ist**

- Nennt die Stände in richtiger zeitlicher Reihenfolge, obwohl der ältere Bericht in der Sammlung hinten steht.
- Erfindet keinen Grund für die Änderung.

## Frage 20 – Regel nur nebenbei in einem langen Bericht

**Frage**

> Wo lasse ich bei einem Tagesseminar meine Jacke?

**Erwartete Belege**

- [AAR-2025-05-20-teamwork-day-seminar.md](./AAR-2025-05-20-teamwork-day-seminar.md)

**Antwortentwurf**

> Jacken und Taschen werden an der Garderobe im Erdgeschoss abgegeben; die Seminarräume haben keine eigene Garderobe.
> **Quelle:** „Tagesseminar „Kommunikation im Team““ (20.05.2025).

**Woran eine gute Antwort erkennbar ist**

- Findet die Regel, obwohl sie nur in einem Absatz eines längeren Seminarberichts steht.
- Übernimmt nichts aus den Winterberichten zu Jacken.

## Frage 21 – Neuester von vier Ständen ohne sprachlichen Hinweis

**Frage**

> Wie bekomme ich für mein Seminar einen Beamer?

**Erwartete Belege**

- [AAR-2025-10-07-projector-delivery.md](./AAR-2025-10-07-projector-delivery.md) (07.10.2025)
- Ergänzend möglich: [AAR-2025-12-02-photo-consent-seminar.md](./AAR-2025-12-02-photo-consent-seminar.md) (Beamer stand bereits im Raum)
- Ältere Stände: Haustechnik (08.03.2022), Seminarbüro (20.06.2023, Dateiname ohne Datum), Abholung im Seminarbüro (02.10.2024)

**Antwortentwurf**

> Den Beamer zusammen mit dem Seminarraum über den Raumkalender reservieren. Das Seminarbüro stellt ihn vor Seminarbeginn im Raum bereit und holt ihn danach wieder ab.
> **Quelle:** „Beamer im Seminarbetrieb“ (07.10.2025).

**Woran eine gute Antwort erkennbar ist**

- Nennt den Stand vom 07.10.2025, obwohl dieser nicht als Änderung gekennzeichnet ist.
- Nennt Abholung bei der Haustechnik oder im Seminarbüro nicht als gleichrangige Alternative.
- Suche: Der Bericht vom 07.10.2025 muss unter den Treffern sein.

**Ab `dataset-v4` (Variante 21b, Agentenentwurf, vom Nutzer bestätigt am 14.11.2026)**
- Neuer Beleg: [AAR-2026-10-06-lehrsaaltechnik.md](./AAR-2026-10-06-lehrsaaltechnik.md) (06.10.2026).
- Erwartete Antwort: Über ein Ticket im IT-Serviceportal (spätestens am Vortag bis 14 Uhr); der IT-Service baut den Beamer vor Beginn auf und nach Ende ab. Bei Störungen die Hotline des IT-Service, nicht das Seminarbüro.
- Seminarbüro, Haustechnik oder Raumkalender nicht als gleichrangige Wege nennen. Falle: kein sprachlicher Hinweis auf die Änderung.

## Frage 22 – Neuester Stand nur nebenbei erwähnt

**Frage**

> Wie erhalten die Teilnehmenden die Seminarunterlagen?

**Erwartete Belege**

- [AAR-2026-04-21-seminar-day-preparation.md](./AAR-2026-04-21-seminar-day-preparation.md) (21.04.2026)
- Ergänzend möglich: [AAR-2026-09-29-evening-negotiation.md](./AAR-2026-09-29-evening-negotiation.md)
- Ältere Stände: gedruckt (15.03.2023), USB-Stick (24.06.2025)

**Antwortentwurf**

> Als Download im Seminarportal; zu Beginn wird nichts mehr ausgeteilt.
> **Quelle:** „Vorbereitung eines Seminartags“ (21.04.2026).

**Woran eine gute Antwort erkennbar ist**

- Findet den neuesten Stand, obwohl er nur in einem Nebensatz eines Berichts zu einem anderen Thema steht.
- Nennt USB-Stick oder gedruckte Unterlagen nicht als gleichrangige Alternativen.

## Frage 23 – Ähnliche Wörter, anderer Kontext

**Frage**

> Welche Kleidung hat sich bei Sommer-Außenseminaren bewährt?

**Erwartete Belege**

- [AAR-2024-07-09-summer-outdoor-day.md](./AAR-2024-07-09-summer-outdoor-day.md)

**Antwortentwurf**

> Leichte, langärmelige Kleidung; ein Sonnenhut war für viele hilfreich. Mehrere hatten zu wenig Wasser dabei.
> **Quelle:** „Kleidung beim Sommer-Außenseminar“ (09.07.2024).

**Woran eine gute Antwort erkennbar ist**

- Übernimmt nichts aus den Winterberichten.
- Der Hinweis, dass der Bericht ein eintägiges Seminar betrifft, ist nicht erforderlich (Nutzerentscheidung).
- Gibt die Erfahrung als Erfahrung wieder, nicht als Vorschrift.

## Frage 24 – Keine Antwort trotz vieler ähnlicher Treffer

**Frage**

> Wie viele Tage im Voraus muss ich einen Seminarraum buchen?

**Erwartete Belege**

- [AAR-2024-02-20-room-booking.md](./AAR-2024-02-20-room-booking.md) (nennt keine Frist)

**Antwortentwurf**

> Dazu nennen die Berichte keine Frist. Belegt ist nur, dass Seminarräume über den Raumkalender im Intranet gebucht werden und bei mehr als 20 Personen zusätzlich die Haustechnik informiert wird.
> **Quelle:** „Buchung von Seminarräumen“ (20.02.2024).

**Woran eine gute Antwort erkennbar ist**

- Überträgt keine Frist aus anderen Berichten (Fahrzeuge: zwei Werktage; Parkplätze: einen Tag; Verpflegung: Vortag 12 Uhr).
- Benennt die Lücke ausdrücklich.

## Frage 25 – Zusammenfassung über viele Berichte

**Frage**

> Fasse zusammen, was die Berichte zu Gästen und Besuchern im Seminargebäude sagen.

**Erwartete Belege**

Besucherausweise (03.02.2026), WLAN für Gäste (März 2025), Besucherparkplätze (ohne Datum), Abendseminar „Projektplanung“ (16.06.2026); ergänzend möglich: Tagesseminar mit externen Gästen (24.03.2026), Tagesseminar „Kommunikation im Team“ (20.05.2025).

**Checkliste der Kernaussagen**

- Besucherausweise beim Verlassen an der Pforte abgeben; Verlust am selben Tag beim Empfang melden.
- WLAN-Zugangsdaten am Empfang, jeweils 24 Stunden gültig.
- Besucherparkplätze mindestens einen Tag vorher beim Empfang reservieren; nicht reservierte werden ab 9 Uhr freigegeben.
- Gastreferierende melden sich am Empfang an und werden von der Seminarleitung abgeholt.

**Woran eine gute Antwort erkennbar ist**

- Deckt alle Punkte der Checkliste ab, obwohl sie auf vier bis sechs Berichte verteilt sind.
- Übernimmt nichts aus Berichten zu Fahrradgarage, Raumschlüsseln oder Fundsachen als Gästeregel, sofern nicht ausdrücklich Gäste betroffen sind.
- Erfindet für Berichte ohne vollständiges Datum kein Datum.

# Fragen 26–34 zu `dataset-v4` (lange militärische Berichte)

Agentenentwürfe, vom Nutzer am 14.11.2026 bestätigt. Sie beziehen sich auf die zehn langen Berichte aus dem Lehrgangs- und Übungsbetrieb; Katalog in [README.md](./README.md).

## Frage 26 – Neuer Stand nur nebenbei in einem langen Bericht

**Frage**

> Wie melde ich fehlendes Material im Erste-Hilfe-Kasten?

**Erwartete Belege**

- [AAR-2025-09-23-sanitaetsdienst-schiessausbildung.md](./AAR-2025-09-23-sanitaetsdienst-schiessausbildung.md) (23.09.2025), Abschnitt 4.3
- Älterer Stand: [AAR-2024-09-30-first-aid-kits.md](./AAR-2024-09-30-first-aid-kits.md) (Formular HV-7)

**Antwortentwurf**

> Über die digitale Mängelmeldung im Intranet, Kategorie „Erste Hilfe“; das gilt seit August 2025 für alle Liegenschaften des Standorts. **Quelle:** „Sanitätsdienstliche Absicherung der Schießausbildung im August und September 2025“ (23.09.2025).

**Woran eine gute Antwort erkennbar ist**

- Findet die Regel, obwohl der Bericht von Schießausbildung handelt.
- Nennt das Formular HV-7 nicht als gleichrangigen Weg.

## Frage 27 – Regel mit weit entfernter Einschränkung

**Frage**

> Muss ich ein Fahrzeug nach einer Übung auf dem Truppenübungsplatz vollgetankt zurückgeben?

**Erwartete Belege**

- [AAR-2026-03-19-kfz-dienst-uebung.md](./AAR-2026-03-19-kfz-dienst-uebung.md) (19.03.2026), Vorbemerkung und Abschnitt 3

**Antwortentwurf**

> Ja. Im Übungsbetrieb auf dem Truppenübungsplatz tanken die Kraftfahrer selbst an der Feldtankstelle, tragen die Menge ins Fahrtenbuch ein und geben das Fahrzeug vollgetankt zurück. Am Standort gelten weiterhin die Regeln der Fahrbereitschaft.

**Woran eine gute Antwort erkennbar ist**

- Ordnet die Regel dem Übungsbetrieb zu.
- Gegenprobe: Frage 7 (am Standort) muss weiterhin ergeben, dass die Fahrbereitschaft tankt; die Übungsregel darf dort höchstens als Ausnahme mit Kontext erscheinen.

## Frage 28 – Ähnliche Wörter, anderer Kontext (Schlüssel)

**Frage**

> Wo gebe ich nach dem Lehrgang den Stubenschlüssel ab?

**Erwartete Belege**

- [AAR-2026-05-12-stubenabnahme.md](./AAR-2026-05-12-stubenabnahme.md) (12.05.2026)

**Antwortentwurf**

> Nach der Stubenabnahme übergibt der Stubenälteste die Schlüssel persönlich dem Unteroffizier vom Dienst, der die Rückgabe im Schlüsselbuch der Kompanie einträgt; nicht in den Schlüsselkasten am Eingang werfen.

**Woran eine gute Antwort erkennbar ist**

- Überträgt nicht die Regeln für Raumschlüssel nach Abendseminaren (Schlüsselkasten des Seminarbüros) oder für den Truppenübungsplatz.

## Frage 29 – Zwei Änderungen in einem Bericht, Kette über mehrere Berichte

**Frage**

> Bis wann melde ich Verpflegung für eine Übung an, und wie bekommen Vegetarier ihr Essen?

**Erwartete Belege**

- [AAR-2026-06-24-truppenverpflegung.md](./AAR-2026-06-24-truppenverpflegung.md) (24.06.2026)
- Älterer Stand: [AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md](./AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md) (Lunchpakete bis Mittwoch der Vorwoche)
- Anderer Kontext: [AAR-2025-02-26-catering.md](./AAR-2025-02-26-catering.md) (Kantine, Vortag 12 Uhr)

**Antwortentwurf**

> Seit dem 01.07.2026 mit dem Formular VA-3, spätestens zehn Werktage vor Beginn, mit Personenzahl, Ausgabeort und Ausgabezeit je Tag. Vegetarische Kost und Sonderkost gibt es bei Übungen nur auf namentliche Anmeldung im VA-3.

**Woran eine gute Antwort erkennbar ist**

- Nennt nicht „Mittwoch der Vorwoche“ als geltende Frist.
- Überträgt nicht die Kantinen-Regel (Vortag 12 Uhr, vegetarische Option immer).

## Frage 30 – „Früher …“ und Bezug auf den vorigen Absatz

**Frage**

> Wie werden Funkgeräte-Akkus nach dem Lehrgang zurückgegeben?

**Erwartete Belege**

- [AAR-2025-11-18-funkgeraete.md](./AAR-2025-11-18-funkgeraete.md) (18.11.2025)

**Antwortentwurf**

> Zusammen mit dem Gerät in der Fernmeldewerkstatt; jede Person gibt selbst ab und bestätigt auf der Empfangsliste. Die Akkus werden dort auf Restkapazität geprüft, unter 70 Prozent ausgesondert.

**Woran eine gute Antwort erkennbar ist**

- Nennt die gesammelte Rückgabe an der Materialausgabe nicht als geltenden Weg (früherer Stand im selben Bericht).

## Frage 31 – Abweichende Erfahrungen in neuem Kontext

**Frage**

> Welche Erfahrungen gibt es zur Bekleidung bei Kälte im Gelände und im Biwak?

**Erwartete Belege**

- [AAR-2026-01-23-winterbiwak.md](./AAR-2026-01-23-winterbiwak.md) (23.01.2026)
- [AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md](./AAR-2026-02-27-gruppenfuehrer-truppenuebungsplatz.md) (27.02.2026)
- Ergänzend möglich: die drei Winterseminar-Berichte, erkennbar als anderer Kontext

**Antwortentwurf**

> Schichten haben sich in Bewegung bewährt; im Stillstand (Posten, Standzeiten) froren viele trotzdem. Im Biwak gehen die Erfahrungen auseinander: Ein Zug hielt Schichten plus Kälteschutzjacke für Standzeiten für ausreichend, der andere hielt eine zusätzliche dick gefütterte Jacke für die Posten für nötig. Kälteschutzjacke griffbereit mitführen; Wollsocken und ein zweites Paar Handschuhe gelten als unverzichtbar.

**Woran eine gute Antwort erkennbar ist**

- Stellt die abweichenden Sichtweisen nebeneinander, ohne Priorität nach Datum.
- Vermischt Seminar- und Biwakerfahrungen nicht unkenntlich.

## Frage 32 – Viele verteilte Punkte in einem langen Bericht

**Frage**

> Was müssen Besucher beim Besuchertag in der Kaserne beachten?

**Erwartete Belege**

- [AAR-2026-04-30-besuchertag.md](./AAR-2026-04-30-besuchertag.md) (30.04.2026)

**Antwortentwurf**

> Siehe Checkliste.

**Woran eine gute Antwort erkennbar ist**

- Checkliste: Anmeldung bis fünf Werktage vorher namentlich mit Geburtsdatum; Personalausweis am Tor, roter Besucherausweis sichtbar tragen; Bewegung nur in Begleitung; Parken auf P3, nicht in der Kaserne (Ausnahme Schwerbehinderte); kein Fotografieren an Wache, Stabsgebäude, Unterkünften; Unterkunftsgebäude nicht betreten; Besucherausweis an der Wache zurückgeben, Verlust dort melden; Mittagessen nur bar.
- Überträgt nicht die Gästeregeln des Seminargebäudes (Pforte, Empfang, WLAN).

## Frage 33 – Keine Antwort trotz viel ähnlichem Material

**Frage**

> Wie hoch ist das Honorar für externe Ausbilder?

**Erwartete Belege**

- Keine; [AAR-2026-07-21-externe-ausbilder.md](./AAR-2026-07-21-externe-ausbilder.md) sagt nur, dass die Abwicklung über Personalabteilung und Haushaltsbearbeitung lief und der Lehrgruppe keine Einzelheiten vorliegen.

**Antwortentwurf**

> Dazu enthalten die Berichte keine Angaben.

**Woran eine gute Antwort erkennbar ist**

- Überträgt keine Beträge (z. B. 8,50 Euro Mittagessen) und leitet aus den Reisekostenregeln kein Honorar ab.

## Frage 34 – Einzelfall nicht als allgemeine Regel

**Frage**

> Wie oft werden Alarmposten bei strengem Frost abgelöst?

**Erwartete Belege**

- [AAR-2026-01-23-winterbiwak.md](./AAR-2026-01-23-winterbiwak.md) (23.01.2026)

**Antwortentwurf**

> In der Übung „Winterbiwak“ wurde nach der ersten Nacht für die Dauer der Übung eine Ablösung nach 60 Minuten angeordnet, das hat sich bewährt. Ob das künftig allgemein gelten soll, ist nicht entschieden.

**Woran eine gute Antwort erkennbar ist**

- Gibt die 60 Minuten nicht als allgemein geltende Regel aus.

## Vorgeschlagene Auswertung

Pro Frage getrennt festhalten:

1. Wurden alle erwarteten Belegberichte abgerufen?
2. Sind die Kernaussagen der Antwort durch diese Berichte gedeckt?
3. Wurden Widerspruch, Ergänzung und Kontext richtig behandelt?
4. Wurde unbelegte Information vermieden?
5. Ist die Antwort knapp genug, um die konkrete Frage direkt zu beantworten?
6. Bei Zusammenfassungen: Welcher Anteil der Checkliste ist abgedeckt?

Vor einem Modellvergleich sollten Frageformulierungen, erwartete Belege und Antwortentwürfe geprüft und danach eingefroren werden. Kleine Modellantworten lassen sich dann anhand derselben Kriterien vergleichen.
