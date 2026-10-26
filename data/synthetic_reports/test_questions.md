# Testfragen und Antwortentwürfe

**Status:** Fragen 1–6 und ihre Antwortentwürfe wurden mit dem Nutzer einzeln geprüft (Stand `dataset-v1`). Fragen 7–10 zur Fahrzeugausleihe wurden vom Nutzer durchgesehen und als passend bestätigt. Vor einem Modellvergleich sollen sie nach Abschluss der weiteren Testdatensatz-Arbeit eingefroren werden.
**Datensatz:** Die zehn synthetischen Markdown-AARs in diesem Ordner (fünf zur Materialrückgabe, fünf zur Fahrzeugausleihe).
**Zweck:** Prüfen, ob ein System direkte Belege findet, Widersprüche und Ergänzungen unterscheidet, den passenden Kontext berücksichtigt und bei fehlender Evidenz nicht rät.

Die Zielantworten sind bewusst knapp und auf den geschilderten Anwendungsfall ausgerichtet. Die Hinweise zur Bewertung sind für die Auswertung gedacht und sollen nicht zwingend in der Nutzerantwort erscheinen. Bei Konfliktfällen kann das System den älteren Widerspruch intern erkennen und dafür bewertet werden, während die Nutzerantwort nur das passende Verfahren und dessen stützende Quelle(n) nennt.

## Frage 1 – Widerspruch und neuester passender Stand

**Frage**

> Ich nehme an einem dreitägigen Seminar teil. Unsere Gruppe hat ein Materialset gemeinsam genutzt. Wie wird die Rückgabe bestätigt?

**Erwartete Belege**

- [AAR-2022-09-14-material-return.md](./AAR-2022-09-14-material-return.md)
- [AAR-2024-03-02-multi-day-seminar-returns.md](./AAR-2024-03-02-multi-day-seminar-returns.md)
- [AAR-2025-01-20-shared-set-returns.md](./AAR-2025-01-20-shared-set-returns.md)

**Geprüfter Antwortentwurf**

> Jede teilnehmende Person bestätigt die Rückgabe der von ihr genutzten Bestandteile. Die Gruppenvertretung reicht zusätzlich eine Gesamtübersicht des gemeinsam genutzten Sets ein.
> **Quelle:** AAR 3 (20.01.2025).

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
> **Quellen:** AAR 3 (20.01.2025), AAR 4 (04.02.2025).

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
> **Quelle:** AAR 2025-03-18 (18.03.2025).

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
> **Quelle:** AAR 2025-09-15 (15.09.2025).

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
> **Quelle:** AAR 2024-11-05 (05.11.2024).

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
> **Quelle:** AAR 2024-01-08 (08.01.2024).

**Woran eine gute Antwort erkennbar ist**

- Beantwortet den belegten Teil.
- Sagt offen, dass zu Kosten nichts belegt ist, und erfindet keinen Betrag.

## Vorgeschlagene Auswertung

Pro Frage getrennt festhalten:

1. Wurden alle erwarteten Belegberichte abgerufen?
2. Sind die Kernaussagen der Antwort durch diese Berichte gedeckt?
3. Wurden Widerspruch, Ergänzung und Kontext richtig behandelt?
4. Wurde unbelegte Information vermieden?
5. Ist die Antwort knapp genug, um die konkrete Frage direkt zu beantworten?

Vor einem Modellvergleich sollten Frageformulierungen, erwartete Belege und Antwortentwürfe geprüft und danach eingefroren werden. Kleine Modellantworten lassen sich dann anhand derselben Kriterien vergleichen.
