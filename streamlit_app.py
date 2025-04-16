import streamlit as st
import random

st.set_page_config(page_title="Motivationater", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    html, body, [class*="css"] {
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Roboto', sans-serif;
    }
    .stApp {
        background: linear-gradient(180deg, #213B88, #121F44);
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
        padding: 40px 20px;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .quote {
        font-size: 30px;
        font-weight: 500;
        max-width: 700px;
        margin-bottom: 60px;
    }
    .button-container {
        margin-top: auto;
        margin-bottom: 40px;
    }
    .stButton>button {
        font-size: 18px;
        padding: 12px 24px;
        background-color: #1b263b;
        color: white;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #3A70F5;
        color: white;
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

if "quote_index" not in st.session_state:
    st.session_state.quote_index = random.randint(0, len(quotes)-1)
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

st.markdown("<div class='title'>Motivationater</div>", unsafe_allow_html=True)
st.markdown(f"<div class='quote'>{quotes[st.session_state.quote_index]}</div>", unsafe_allow_html=True)

with st.container():
    if st.button("💬 Toon een andere quote"):
        st.session_state.quote_index = random.randint(0, len(quotes)-1)
        st.session_state.clicks += 1

if st.session_state.clicks == 2:
    st.markdown("""
        <div class='popup'>
            👋 Wil je écht verandering?  
            <br><br>
            <b><a href="#" style="color:#121F44; text-decoration: none;">Neem hier contact op</a></b>
        </div>
    """, unsafe_allow_html=True)
