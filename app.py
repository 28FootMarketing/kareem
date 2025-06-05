import streamlit as st
import random

st.set_page_config(page_title="Kareem Bot - Wisdom Coach", page_icon="🧠", layout="centered")

st.title("🧠 Kareem Bot: The Visionary")
st.subheader("Wisdom & Mindset Coach")

st.markdown("**Style of Play:** Thoughtful, intentional, deeply rooted in experience")

st.markdown("""
Kareem provides daily wisdom, motivational quotes, and clarity for the journey.  
Whether you are doubting, overwhelmed, or celebrating a small win—he has a word for that.

> “Kareem speaks to the moment—offering clarity when things get cloudy and grounding when the grind feels overwhelming.”
""")

quotes = [
    "“The best way to make your dreams come true is to wake up.” – Paul Valéry",
    "“Your greatness is not what you have, it is what you give.”",
    "“The grind is real. So is the growth.”",
    "“In moments of pressure, breathe, believe, and execute.”",
    "“Your mindset is the foundation of your momentum.”",
    "“Tough times test you. Wise responses define you.”",
    "“Every email you send is an opportunity. Stay ready.”"
]

st.header("Need some perspective today?")
if st.button("Give me a quote"):
    st.success("Kareem says:")
    st.markdown(f"**{random.choice(quotes)}**")

st.header("How are you feeling today?")
mood = st.radio("Choose the one that fits:", [
    "Motivated", "Frustrated", "Tired", "Focused", "Uncertain", "Discouraged", "Proud"
])

if mood:
    st.info(f"Kareem says: Even when you feel {mood.lower()}, remember—your effort echoes louder than your emotion.")
