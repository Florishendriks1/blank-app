import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Motivatie", layout="wide")

# CSS voor volledige gradient background en centrering
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        height: 100%;
        margin: 0;
        padding: 0;
    }

    .stApp {
        background: linear-gradient(180deg, #213B88, #121F44);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        height: 100vh;
        text-align: center;
    }

    .quote {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 40px;
        max-width: 800px;
    }

    .stButton>button {
        font-size: 18px;
        padding: 12px 24px;
        background-color: #1b263b;
        color: white;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Quotes
quotes = [
    "Succes begint waar comfort stopt.",
    "Kleine stappen vooruit zijn beter dan geen stappen.",
    "Jij bent tot meer in staat dan je denkt.",
    "Focus op groei, niet op perfectie.",
    "Iedere dag is een nieuwe kans.",
    "Blijf bewegen, blijf leren, blijf winnen.",
    "Zelfvertrouwen is de sleutel tot actie.",
    "Geduld + doorzettingsvermogen = resultaat."
]

# Init session state
if "quote_index" not in st.session_state:
    st.session_state.quote_index = random.randint(0, len(quotes)-1)

# Quote tonen
st.markdown(f"<div class='quote'>{quotes[st.session_state.quote_index]}</div>", unsafe_allow_html=True)

# Knop
if st.button("💬 Toon een andere quote"):
    st.session_state.quote_index = random.randint(0, len(quotes)-1)
