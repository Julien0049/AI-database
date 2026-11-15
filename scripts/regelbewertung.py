"""Regelbasierte Vorprüfung der Antworten (ohne Sprachmodell), für den Modellvergleich v21.

Je Frage: Pflichtinhalte (alle müssen vorkommen, Alternativen mit |) und verbotene Inhalte (überholte Stände,
erfundene oder übertragene Regeln). Ergebnis je Antwort:
  nicht erfüllt – verbotener Inhalt oder keine verwertbare Antwort,
  teilweise     – Pflichtinhalt fehlt oder kein bestätigter Beleg (bei Fragen mit Belegpflicht),
  erfüllt       – sonst.
Grenze: Störinhalte (Verwandtes ohne Bezug) und Feinheiten erkennt die Regel nicht; sie ist daher etwas großzügiger
als die Handbewertung. Geeicht an der Handbewertung von v19 (Agent, 14.11.2026).

  .venv/bin/python scripts/regelbewertung.py results/ergebnisse_*_v21.json
"""
import json
import re
import sys
from collections import Counter

R = {  # Frage: (Pflicht, Verboten)
    1: (["persönlich", "gesamtübersicht"], ["gemeinsame rückgabeliste", "prüft das set|geprüft"]),
    2: (["persönlich", "gesamtübersicht", "abweichungsprotokoll", "selben tag"], ["gemeinsame rückgabeliste"]),
    3: (["ausgabeliste"], ["gesamtübersicht"]),
    4: (["zugeordnet|eingetragen"], ["fahrzeug"]),
    5: (["nicht (?:fest|ableit|abgeleitet|ermittel|genannt|nennen)|keine persönliche verantwortung|sagen nicht|keine angaben"], ["ist verantwortlich", "haftet"]),
    6: (["set-kennung|gegenstandsbezeichnung", "kein|nicht"], ["hv-7"]),
    7: (["fahrbereitschaft"], [r"^ja\b", "müssen? (?:das fahrzeug )?vollgetankt zurückgegeben werden(?![^.]*übung)"]),
    8: (["ausleihend|ausgeliehen"], ["gruppenvertretung", "gesamtübersicht"]),
    9: (["schadensformular"], ["abweichungsprotokoll", "ist verantwortlich"]),
    10: (["drei werktage", "fahrzeugportal"], ["zwei werktage", "vollgetankt"]),
    11: (["schicht", "daune", "überjacke", "wollsocken"], []),
    12: (["auseinander|uneinig|unterschiedlich", "warte"], []),
    13: (["keine|nicht"], [r"\d+\s*°"]),
    14: (["drei werktage", "fahrzeugportal", "schadensformular", "tankstand"], ["zwei werktage", "vollgetankt zurückgegeben werden(?![^.]*übung)"]),
    15: (["schicht", "warte", "wollsocken", "überjacke"], []),
    16: (["persönlich", "gesamtübersicht", "ausleihend|ausgeliehen", "überjacke"], ["gemeinsame rückgabeliste(?![^.]*(?:früher|zuvor|bisher))", "usb"]),
    17: (["gruppenvertretung", "persönlich"], []),
    18: (["schlüsselkasten"], ["pforte"]),
    19: (["pforte", "schlüsselkasten"], []),
    20: (["garderobe", "erdgeschoss"], []),
    21: (["it-service|serviceportal|ticket"], ["seminarbüro stellt", "im seminarbüro (?:abgeholt|ausgegeben)", "haustechnik"]),
    22: (["download"], ["usb", "gedruckt"]),
    23: (["langärmelig"], ["daune", "wollsocken"]),
    24: (["keine|nicht"], [r"\d+ (?:werk)?tage? (?:im )?voraus", "spätestens"]),
    25: (["besucherausweis", "wlan", "parkpl", "empfang"], []),
    26: (["mängelmeldung"], ["hv-7", "abweichungsprotokoll"]),
    27: (["vollgetankt|volltank|vollzutank", "übung|truppenübungsplatz"], []),
    28: (["unteroffizier vom dienst|uvd"], ["schlüsselkasten des seminarbüros"]),
    29: (["va-3", "zehn werktage|10 werktage", "namentlich"], ["mittwoch der vorwoche(?![^.]*(?:entf|früher|bisher|nicht mehr))", "vortag"]),
    30: (["fernmeldewerkstatt"], ["materialausgabe(?![^.]*(?:früher|bisher|nicht mehr|gesammelt))"]),
    31: (["schicht", "stillstand|standzeit|stellung|posten", "wollsocken|socken"], []),
    32: (["fünf werktage", "begleitung", "besucherausweis", "fotograf"], []),
    33: (["keine|nicht"], [r"\d+[.,]?\d*\s*(?:euro|€)(?![^.]*mittagessen)"]),
    34: (["60 minuten", "nicht entschieden|offen|einzelfall|nur für (?:die|diese)"], []),
}
NO_EVIDENCE_OK = {13, 24, 33}  # Fragen, bei denen eine Lücke ohne Beleg richtig sein kann


def judge(e):
    a = e.get("antwort")
    if not a or not a.get("text"):
        return "nicht erfüllt", "keine Antwort"
    t = a["text"].lower()
    need, banned = R[e["nr"]]
    for b in banned:
        if re.search(b, t, re.M):
            return "nicht erfüllt", f"verboten: {b}"
    missing = [n for n in need if not re.search(n, t)]
    if missing:
        return "teilweise", "fehlt: " + ", ".join(missing)
    if not a.get("quellen") and e["nr"] not in NO_EVIDENCE_OK:
        return "teilweise", "kein bestätigter Beleg"
    return "erfüllt", ""


def reparse(d):
    """Antworten ohne Auswertung aus der gespeicherten Rohantwort neu einlesen (robuster Parser seit v21).
    Ändert nichts an den Dateien; kein Modellaufruf."""
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root / "app"))
    import aidb
    reports, _ = aidb.load_reports(root / "data/synthetic_reports")
    fixed = 0
    for e in d["ergebnisse"]:
        if not e.get("antwort") and e.get("roh"):
            try:
                sel = {rid: reports[rid] for rid in e.get("berichte_im_prompt", []) if rid in reports}
                text, sources, problems = aidb.render(aidb.check(aidb.parse(e["roh"]), sel), sel)
                e["antwort"] = {"text": text, "quellen": sources, "probleme": problems}
                fixed += 1
            except Exception:
                pass
    return fixed


if __name__ == "__main__":
    DETAIL = "-d" in sys.argv
    NEU = "-n" in sys.argv
    for f in [a for a in sys.argv[1:] if a not in ("-d", "-n")]:
        d = json.loads(open(f).read())
        if NEU:
            print(f"   neu eingelesen: {reparse(d)} Antworten")
        res = [(e, *judge(e)) for e in d["ergebnisse"]]
        c = Counter(r[1] for r in res)
        n = len(res)
        print(f"{d['modell'][:45]:45} erfüllt {c['erfüllt']:3}/{n} ({c['erfüllt']/n:.0%}) | teilweise {c['teilweise']:3} | "
              f"nicht erfüllt {c['nicht erfüllt']:3} ({c['nicht erfüllt']/n:.0%}) | {d.get('kosten_usd', 0):.2f} USD")
        if DETAIL:
            for e, verdict, why in res:
                if verdict != "erfüllt":
                    print(f"   F{e['nr']} D{e['durchlauf']}: {verdict} – {why}")
