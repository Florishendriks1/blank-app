import streamlit as st
import random

# Pagina setup
st.set_page_config(page_title="Motivationater", layout="wide")

# Custom CSS
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

    .title {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 60px;
        margin-top: -60px;
    }

    .quote {
        font-size: 32px;
        font-weight: 500;
        margin-bottom: 40px;
        max-width: 700px;
    }

    .stButton>button {
        font-size: 18px;
        padding: 12px 24px;
        background-color: #1b263b;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .popup {
        background-color: white;
        color: black;
        padding: 25px;
        border-radius: 15px;
        font-size: 18px;
        margin-top: 30px;
        width: 300px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Titeltje bovenaan
st.markdown("<div class='title'>Motivationater</div>", unsafe_allow_html=True)

# Motivatie quotes
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

# Session state voor quote en klikcount
if "quote_index" not in st.session_state:
    st.session_state.quote_index = random.randint(0, len(quotes)-1)
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

# Toon quote
st.markdown(f"<div class='quote'>{quotes[st.session_state.quote_index]}</div>", unsafe_allow_html=True)

# Quote button
if st.button("💬 Toon een andere quote"):
    st.session_state.quote_index = random.randint(0, len(quotes)-1)
    st.session_state.clicks += 1

# Popup melding na 2 klikken
if st.session_state.clicks == 2:
    st.markdown("""
        <div class='popup'>
            👋 Wil je écht verandering?  
            <br><br>
            <b><a href="#" style="color:#121F44; text-decoration: none;">Neem hier contact op</a></b>
        </div>
    """, unsafe_allow_html=True)
