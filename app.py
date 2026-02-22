import streamlit as st
import json
from voice_input import get_voice_input
from parser import extract_schedule

st.title("Voice Calendar Assistant")

if st.button("Speak Schedule"):
    text = get_voice_input()
    st.write("You said:", text)

    parsed = extract_schedule(text)
    st.write("Extracted:", parsed)

try:
    with open("events.json") as f:
        events = json.load(f)
        st.write(events)
except:
    st.write("No events yet")

