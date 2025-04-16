import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Motivatie", layout="wide")

# CSS voor de achtergrond en styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #0d1b2a, #000000);
        color: white;
    }
    .stApp {
        background: linear-gradient(to bottom right, #0d1b2a, #000000);
        color: white;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    .quote {
        font-size: 36px;
        font-weight: bold;
        margin-top: 100px;
        margin-bottom: 50px;
    }
    .button {
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

# Layout
st.markdown("<div class='quote'>" + random.choice(quotes) + "</div>", unsafe_allow_html=True)

if st.button("💬 Toon een andere quote"):
    st.experimental_rerun()
