import streamlit as st
import random

st.title("🤣 De Digitale Moppentrommel")

moppen = [
    "Waarom kunnen geheimagenten niet goed schaken? Ze zijn bang voor openingen.",
    "Wat zegt een wiskundeleraar tijdens het daten? Jij bent echt mijn type!",
    "Waarom nam de computer een pauze? Hij had te veel tabs open!",
    "Wat zegt een boom als hij wordt omgezaagd? ‘Ik voel me geveld…’"
]

if st.button("Vertel een mop!"):
    st.success(random.choice(moppen))
