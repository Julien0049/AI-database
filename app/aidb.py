"""Kernlogik der lokalen Oberfläche: Berichte einlesen, Modell fragen, Zitate prüfen, Fußnoten setzen.

Übernommen aus notebooks/citation_check_v7.ipynb, Aufbau wie v11 (alle Berichte im Prompt).
Der Antwort-Prompt in prompt_antwort.txt entspricht dem Notebook (Regeln 1–7, Stand v8–v13).
"""
import json
import os
import pathlib
import re
import time

MODEL = "google/gemini-2.5-pro"
PROMPT = (pathlib.Path(__file__).parent / "prompt_antwort.txt").read_text()

MONTHS = {m: i for i, m in enumerate(["januar", "februar", "märz", "april", "mai", "juni", "juli",
                                      "august", "september", "oktober", "november", "dezember"], 1)}
DATE_PATTERNS = [
    (r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b", lambda m: (m[1], m[2], m[3])),                          # 15.2.2023
    (r"\b(\d{4})-(\d{2})-(\d{2})\b", lambda m: (m[3], m[2], m[1])),                                # 2025-01-20
    (r"\b(\d{1,2})\. (" + "|".join(MONTHS) + r") (\d{4})\b", lambda m: (m[1], MONTHS[m[2]], m[3])),  # 18. März 2025
]


def find_title(text):
    """Erste Markdown-Überschrift; None, wenn keine vorhanden ist."""
    m = re.search(r"^# (?:After-Action-Report: )?(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def find_date(text):
    """Frühestes Datum im Text, gleich in welchem der bekannten Formate; None, wenn keines vorkommt."""
    hits = []
    for pattern, parts in DATE_PATTERNS:
        for m in re.finditer(pattern, text, re.I):
            d, mo, y = parts([None] + [g.lower() for g in m.groups()])
            hits.append((m.start(), f"{int(d):02d}.{int(mo):02d}.{y}"))
    return min(hits)[1] if hits else None


def load_reports(folder, pattern="AAR-*.md"):
    """Liest alle Berichte eines Ordners ein. Gibt (Berichte, Hinweise zu fehlenden Metadaten) zurück."""
    reports, notes = {}, []
    for n, path in enumerate(sorted(pathlib.Path(folder).glob(pattern)), 1):
        text = path.read_text()
        title, date = find_title(text), find_date(text)
        if not title:
            notes.append(f"{path.name}: keine Überschrift, Dateiname wird als Titel genutzt")
        if not date:
            notes.append(f"{path.name}: kein Datum erkannt")
        reports[f"B{n}"] = {"datei": path.name, "titel": title or path.name,
                            "datum": date or "Datum unbekannt", "text": text}
    return reports, notes


def read_key(env_file, name="OPENROUTER_API_KEY"):
    """API-Schlüssel aus der Umgebung oder aus der lokalen .env-Datei; None, wenn keiner vorhanden ist."""
    if os.environ.get(name):
        return os.environ[name]
    if pathlib.Path(env_file).exists():
        for line in pathlib.Path(env_file).read_text().splitlines():
            key, _, value = line.partition("=")
            if key.strip() == name and value.strip():
                return value.strip().strip('"').strip("'")
    return None


def corpus_for(reports):
    return "\n\n".join(f'<bericht id="{rid}">\n{r["text"]}\n</bericht>' for rid, r in reports.items())


def ask_model(question, reports, key):
    """Fragt das Modell über OpenRouter. Gibt (Rohantwort, Kosten in USD oder None) zurück."""
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": f"{corpus_for(reports)}\n\nFrage: {question}"}
        ]
    )
    return response.choices[0].message.content, getattr(response.usage, "cost", None)


def words(text):
    return set(w for w in re.findall(r"[a-zäöüß]+", text.lower()) if len(w) > 3)


def ask_dummy(question, reports):
    """Attrappe ohne Modell: nimmt den Bericht mit den meisten gemeinsamen Wörtern und zitiert dessen ersten Satz.
    Dient nur dazu, Import, Zitatprüfung und Fußnoten kostenlos zu testen."""
    rid = max(reports, key=lambda r: len(words(question) & words(reports[r]["text"])))
    body = [line for line in reports[rid]["text"].splitlines()
            if line.strip() and not line.startswith("#") and not line.startswith("**")]
    sentence = re.split(r"(?<=[a-zäöüß])\. ", body[0] if body else reports[rid]["text"])[0].rstrip(".") + "."
    answer = {"saetze": [
        {"text": sentence, "belege": [{"bericht": rid, "zitat": sentence}]},
        {"text": "(Attrappe: keine Modellantwort, sondern der erste Satz des Berichts mit den meisten gemeinsamen Wörtern.)",
         "belege": []},
    ]}
    return json.dumps(answer, ensure_ascii=False), 0.0


def norm(s):
    s = s.lower()
    for a, b in [("„", '"'), ("“", '"'), ("”", '"'), ("‚", "'"), ("‘", "'"), ("’", "'"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip(" .,;:\"'")


def parse(raw):
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip())
    return json.loads(raw)


def check(answer, reports):
    """Markiert jeden Beleg als gültig, falscher Bericht oder nicht gefunden."""
    for satz in answer["saetze"]:
        for beleg in satz.get("belege", []):
            zitat = norm(beleg.get("zitat", ""))
            rid = beleg.get("bericht")
            if rid in reports and zitat and zitat in norm(reports[rid]["text"]):
                beleg["status"] = "gültig"
            elif zitat and any(zitat in norm(r["text"]) for r in reports.values()):
                beleg["status"] = "falscher Bericht"
            else:
                beleg["status"] = "nicht gefunden"
    return answer


def render(answer, reports):
    """Antworttext mit Fußnoten, Quellenliste und nicht bestätigten Belegen.
    Aufeinanderfolgende Sätze aus denselben Berichten teilen sich eine Fußnote."""
    numbers = {}
    for s in answer["saetze"]:
        for b in s.get("belege", []):
            if b["status"] == "gültig":
                numbers.setdefault(b["bericht"], len(numbers) + 1)

    def refs(s):
        return sorted({numbers[b["bericht"]] for b in s.get("belege", []) if b["status"] == "gültig"})

    sentences = answer["saetze"]
    parts = []
    for i, s in enumerate(sentences):
        text, r = s["text"].strip(), refs(s)
        if r and (i + 1 == len(sentences) or refs(sentences[i + 1]) != r):
            mark = " [" + ", ".join(map(str, r)) + "]"
            text = text[:-1] + mark + text[-1] if text[-1:] in ".!?" else text + mark
        parts.append(text)
    sources = [f'[{n}] „{reports[rid]["titel"]}“ ({reports[rid]["datum"]})' for rid, n in numbers.items()]
    problems = [f'{b["bericht"]}: {b["status"]} – „{b.get("zitat", "")}“'
                for s in sentences for b in s.get("belege", []) if b["status"] != "gültig"]
    return " ".join(parts), sources, problems


def answer(question, reports, key=None):
    """Beantwortet eine Frage mit allen Berichten. Ohne Schlüssel antwortet die Attrappe.
    Gibt ein Wörterbuch mit Text, Quellen, Problemen, Dauer, Kosten oder Fehler zurück."""
    start = time.time()
    result = {"berichte": len(reports), "modell": MODEL if key else "Attrappe"}
    if not reports:  # ohne Berichte nicht fragen: in v13 erfand das Modell dann eine Regel samt Zitat
        result.update(text="Es sind keine Berichte importiert.", quellen=[], probleme=[], dauer_s=0.0)
        return result
    try:
        raw, cost = ask_model(question, reports, key) if key else ask_dummy(question, reports)
        result["roh"], result["kosten"] = raw, cost
        result["text"], result["quellen"], result["probleme"] = render(check(parse(raw), reports), reports)
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        result["fehler"] = f"Die Antwort des Modells war nicht auswertbar ({e})."
    except Exception as e:  # z. B. Netzwerkfehler oder aufgebrauchtes Budget
        result["fehler"] = f"Die Anfrage ist fehlgeschlagen: {e}"
    result["dauer_s"] = round(time.time() - start, 1)
    return result


def log(path, question, result):
    """Hängt Frage und Ergebnis als eine JSON-Zeile an die lokale Protokolldatei an."""
    entry = {"zeit": time.strftime("%Y-%m-%d %H:%M:%S"), "frage": question, **result}
    path = pathlib.Path(path)
    path.parent.mkdir(exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
