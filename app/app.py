"""Lokale Browser-Oberfläche für den PoC. Start im Projektordner: streamlit run app/app.py"""
import pathlib
import sys

import streamlit as st

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import aidb  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

st.set_page_config(page_title="AI Database (PoC)", page_icon="📄")
st.title("Fragen an die Berichte")
st.caption("Proof of Concept mit fiktiven Testberichten. Antworten stützen sich nur auf die importierten Berichte; "
           "jede Frage wird einzeln beantwortet, frühere Fragen fließen nicht ein.")

with st.sidebar:
    st.header("Berichte")
    folder = st.text_input("Ordner", "data/synthetic_reports")
    if st.button("Importieren"):
        st.session_state.reports, st.session_state.notes = aidb.load_reports(ROOT / folder)
        st.session_state.messages = []
    reports = st.session_state.get("reports")
    if reports:
        st.success(f"{len(reports)} Berichte importiert")
        notes = st.session_state.get("notes", [])
        if notes:
            with st.expander(f"{len(notes)} Hinweise zu fehlenden Angaben"):
                for note in notes:
                    st.write(note)
    elif reports is not None:
        st.warning("Im Ordner wurden keine Berichte gefunden.")
    else:
        st.info("Noch keine Berichte importiert.")

    st.header("Antworten")
    mode = st.radio("Antworten kommen von", ["Attrappe (kostenlos)", "Gemini 2.5 Pro (verbraucht Guthaben)"])
    key = None
    if mode.startswith("Gemini"):
        key = aidb.read_key(ROOT / ".env")
        if not key:
            st.error("Kein Schlüssel gefunden. Bitte OPENROUTER_API_KEY in die Datei .env im Projektordner eintragen.")

for message in st.session_state.get("messages", []):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Frage an die Berichte", disabled=not reports)
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Die Berichte werden ausgewertet …"):
            result = aidb.answer(question, reports, key if mode.startswith("Gemini") else None)
        if "fehler" in result:
            content = result["fehler"]
        else:
            content = result["text"]
            if result["quellen"]:
                content += "\n\n**Quellen**\n\n" + "\n".join(f"- {q}" for q in result["quellen"])
            if result["probleme"]:
                content += "\n\n**Nicht bestätigte Belege**\n\n" + "\n".join(f"- {p}" for p in result["probleme"])
        info = f"{result['berichte']} von {len(reports)} Berichten berücksichtigt · {result['modell']} · {result['dauer_s']} s"
        if result.get("kosten"):
            info += f" · {result['kosten']:.3f} USD"
        content += f"\n\n<sub>{info}</sub>"
        st.markdown(content, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": content})
