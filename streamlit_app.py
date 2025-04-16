import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for styling
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
    height: 100vh;
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
    font-size: 20px;
    line-height: 28px;
    color: #333;
    font-family: 'Caveat', cursive;
    white-space: pre-wrap;
    overflow-y: auto;
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

# Session state initialization
if 'pages' not in st.session_state:
    st.session_state.pages = [""]
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

# Function to handle navigation
def prev_page():
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1

def next_page():
    if st.session_state.current_page < len(st.session_state.pages) - 1:
        st.session_state.current_page += 1
    else:
        st.session_state.pages.append("")
        st.session_state.current_page += 1

# Layout
st.markdown(notebook_css, unsafe_allow_html=True)

st.markdown('<div class="notebook-container">', unsafe_allow_html=True)
st.markdown('<div class="notebook">', unsafe_allow_html=True)

# Text area input
content = st.text_area(
    label="",
    value=st.session_state.pages[st.session_state.current_page],
    height=420,
    label_visibility="collapsed"
)

# Update current page content
st.session_state.pages[st.session_state.current_page] = content

# Overlay lines
st.markdown('<div class="lines"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close .notebook
st.markdown('</div>', unsafe_allow_html=True)  # Close .notebook-container

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Vorige"):
        prev_page()
with col2:
    st.markdown(f"Pagina {st.session_state.current_page + 1} van {len(st.session_state.pages)}", unsafe_allow_html=True)
with col3:
    if st.button("Volgende →"):
        next_page()
