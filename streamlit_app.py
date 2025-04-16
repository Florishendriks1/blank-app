import streamlit as st
import streamlit.components.v1 as components

# Custom CSS
notebook_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat&display=swap');

body {
    background-color: #DDD5C7;
    margin: 0;
    padding: 0;
    font-family: 'Caveat', cursive;
}

.notebook-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 85vh;
}

.notebook {
    position: relative;
    width: 700px;
    height: 500px;
    background: linear-gradient(to right, #1A1A1A 50px, #FAF3E0 50px);
    border: 1px solid #999;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
    transform: perspective(800px) rotateY(-3deg);
    overflow: hidden;
    padding-left: 70px;
}

.page {
    position: relative;
    width: 100%;
    height: 100%;
    background-color: #FAF3E0;
    border-left: 2px solid #E8D8B6;
    padding: 20px;
    box-sizing: border-box;
    font-size: 22px;
    line-height: 28px;
    color: #333;
    font-family: 'Caveat', cursive;
    white-space: pre-wrap;
    overflow-y: auto;
    z-index: 2;
}

.page:before {
    content: 'Date:';
    position: absolute;
    top: 10px;
    left: 20px;
    font-size: 16px;
    color: #4A4A4A;
    font-family: serif;
}

.lines {
    background-image: repeating-linear-gradient(#3C3C3C 0px, #3C3C3C 1px, transparent 1px, transparent 28px);
    height: 100%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 0;
    pointer-events: none;
}

.nav-buttons {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

button {
    background-color: #FAF3E0;
    border: 2px solid #3C3C3C;
    color: #3C3C3C;
    padding: 5px 15px;
    margin: 0 10px;
    cursor: pointer;
    font-family: serif;
    font-size: 16px;
}

button:hover {
    background-color: #E8D8B6;
}
</style>
"""

# Session state
if 'pages' not in st.session_state:
    st.session_state.pages = [""]
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

# Navigation functions
def prev_page():
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1

def next_page():
    if st.session_state.current_page < len(st.session_state.pages) - 1:
        st.session_state.current_page += 1
    else:
        st.session_state.pages.append("")
        st.session_state.current_page += 1

# Input form
st.markdown(notebook_css, unsafe_allow_html=True)
with st.form("notebook_input_form"):
    user_input = st.text_area(
        "Typ hier je notitie voor deze pagina:",
        value=st.session_state.pages[st.session_state.current_page],
        height=150,
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("📜 Schrijf op pagina")
    if submitted:
        st.session_state.pages[st.session_state.current_page] = user_input

# Notebook display
st.markdown('<div class="notebook-container"><div class="notebook">', unsafe_allow_html=True)
st.markdown('<div class="lines"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="page">{st.session_state.pages[st.session_state.current_page]}</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("← Vorige"):
        prev_page()
with col2:
    st.markdown(f"<center><b>Pagina {st.session_state.current_page + 1} van {len(st.session_state.pages)}</b></center>", unsafe_allow_html=True)
with col3:
    if st.button("Volgende →"):
        next_page()
