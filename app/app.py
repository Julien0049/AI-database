"""Lokale Browser-Oberfläche für den PoC. Start im Projektordner: streamlit run app/app.py

Aufbau seit 14.11.2026 (Versuche v16–v19):
- Kein Import-Knopf: Vor jeder Frage gleicht die Oberfläche den Berichtsordner mit der Aussagen-Datenbank ab;
  nur neue oder geänderte Berichte werden eingelesen (Anforderung: automatische Erfassung).
- Die besten Aussagen bestimmen die relevanten Berichte; diese gehen vollständig an das Modell (v16).
- Antwortregeln aus prompt_antwort.txt (Stand v19); danach Programmprüfung auf möglicherweise überholte Aussagen.
"""
import importlib
import json
import pathlib
import sys

import streamlit as st

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import aidb  # noqa: E402
import aussagen  # noqa: E402
import suche  # noqa: E402

aidb, aussagen, suche = importlib.reload(aidb), importlib.reload(aussagen), importlib.reload(suche)

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_PREVIOUS = 3  # so viele bisherige Fragen gehen als Kontext mit
DB_FILES = {True: ROOT / "index" / "aussagen.sqlite",    # Gemini: vom Modell zerlegte Aussagen
            False: ROOT / "index" / "attrappe.sqlite"}   # Attrappe: eigene Datenbank, damit die echte sauber bleibt

st.set_page_config(page_title="AI Database (PoC)", page_icon="📄")
st.title("Fragen an die Berichte")
st.caption("Proof of Concept mit fiktiven Testberichten. Antworten stützen sich nur auf die Berichte im Ordner. "
           "Neue Berichte werden automatisch erfasst. Folgefragen verstehen die letzten drei Fragen mit.")


@st.cache_resource(show_spinner="Suchmodell wird geladen …")
def embedding_model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(suche.EMBEDDING_MODEL)


@st.cache_resource(show_spinner="Suchindex wird aufgebaut …")
def build_index(db_file, stand):
    """Suchindex über alle Aussagen; wird neu gebaut, wenn sich die Datenbank geändert hat (stand)."""
    return suche.Index(aussagen.connect(db_file), embedding_model())


def synchronize(folder, use_model, key):
    """Ordner mit der Datenbank abgleichen. Gibt (Datenbankdatei, Übersicht, Stand) zurück."""
    db_file = DB_FILES[use_model]
    db = aussagen.connect(db_file)
    extract = aussagen.extract_model if use_model else aussagen.extract_dummy
    summary = aussagen.sync(folder, db, extract, key=key, log=lambda *_: None)
    if summary["neu"] or summary["geändert"] or summary["entfernt"]:
        aussagen.recheck_quotes(db, folder)
    stand = db.execute("SELECT COUNT(*), MAX(id), MAX(eingelesen) FROM aussagen JOIN dokumente USING (datei)").fetchone()
    return db_file, summary, tuple(stand)


with st.sidebar:
    st.header("Berichte")
    folder_text = st.text_input("Ordner", "data/synthetic_reports")
    folder = ROOT / folder_text.strip()

    st.header("Antworten")
    mode = st.radio("Antworten kommen von", ["Attrappe (kostenlos)", "Gemini 2.5 Pro (verbraucht Guthaben)"])
    use_model = mode.startswith("Gemini")
    key = None
    if use_model:
        key = aidb.read_key(ROOT / ".env")
        if not key:
            st.error("Kein Schlüssel gefunden. Bitte OPENROUTER_API_KEY in die Datei .env im Projektordner eintragen.")
            use_model = False

    status = st.empty()
    if st.button("Neues Gespräch"):
        st.session_state.messages = []

if not folder.is_dir():
    st.error(f"Ordner nicht gefunden: {folder}")
    st.stop()

with st.spinner("Berichtsordner wird abgeglichen …"):
    db_file, summary, stand = synchronize(folder, use_model, key)
reports, notes = aidb.load_reports(folder)
with status.container():
    changes = len(summary["neu"]) + len(summary["geändert"]) + len(summary["entfernt"])
    st.success(f"{len(reports)} Berichte erfasst")
    if changes:
        st.info(f"Gerade abgeglichen: {len(summary['neu'])} neu, {len(summary['geändert'])} geändert, "
                f"{len(summary['entfernt'])} entfernt" + (f" · {summary['kosten']:.3f} USD" if summary["kosten"] else ""))
    for f in summary["fehler"]:
        st.warning(f)
    if notes:
        with st.expander(f"{len(notes)} Hinweise zu fehlenden Angaben"):
            for note in notes:
                st.write(note)
    if not use_model:
        st.caption("Attrappe: eigene Datenbank, Aussagen = Sätze der Berichte, Antwort = erster Satz eines Treffers.")

for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

question = st.chat_input("Frage an die Berichte", disabled=not reports)
if question:
    st.session_state.setdefault("messages", [])
    previous = [m["content"] for m in st.session_state.messages if m["role"] == "user"][-MAX_PREVIOUS:]
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Passende Berichte werden gesucht und ausgewertet …"):
            index = build_index(str(db_file), stand)
            files = set(index.select(" ".join([*previous, question])))
            selected = {rid: r for rid, r in reports.items() if r["datei"] in files}
            result = aidb.answer(question, selected, key if use_model else None, previous)
            warnings = []
            if result.get("roh"):
                try:
                    warnings = index.outdated(question, aidb.parse(result["roh"])["saetze"], selected)
                except (json.JSONDecodeError, KeyError, TypeError):
                    pass
            result["warnungen"] = warnings
            result["berichte_ausgewaehlt"] = sorted(r["datei"] for r in selected.values())
        aidb.log(ROOT / "protokoll" / "oberflaeche.jsonl", question, result)
        if "fehler" in result:
            content = result["fehler"]
        else:
            content = result["text"]
            if result["quellen"]:
                content += "\n\n**Quellen**\n\n" + "\n".join(f"- {q}" for q in result["quellen"])
            if warnings:
                content += "\n\n**⚠ Möglicherweise überholt** (Programmprüfung)\n\n" + "\n".join(f"- {w}" for w in warnings)
            if result["probleme"]:
                content += "\n\n**Nicht bestätigte Belege**\n\n" + "\n".join(f"- {p}" for p in result["probleme"])
        info = f"{len(selected)} von {len(reports)} Berichten ausgewählt · {result['modell']} · {result['dauer_s']} s"
        if previous:
            info += f" · mit {len(previous)} vorheriger Frage(n) als Kontext"
        if result.get("kosten"):
            info += f" · {result['kosten']:.3f} USD"
        content += f"\n\n<sub>{info}</sub>"
        st.markdown(content, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": content})
