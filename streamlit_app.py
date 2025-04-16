import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Motivatie", layout="wide")

# CSS voor styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #0d1b2a, #000000);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        padding-top: 100px;
    }
    .quote {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 50px;
    }
    .stButton>button {
        font-size: 20px;
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

# Init quote index
if "quote_index" not in st.session_state:
    st.session_state.quote_index = random.randint(0, len(quotes)-1)

# Toon quote
st.markdown(f"<div class='quote'>{quotes[st.session_state.quote_index]}</div>", unsafe_allow_html=True)

# Nieuwe quote bij knop
if st.button("💬 Toon een andere quote"):
    st.session_state.quote_index = random.randint(0, len(quotes)-1)
