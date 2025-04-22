import streamlit as st
import random
import json
import os
import time

st.set_page_config(page_title="Eurovision Country Assigner", page_icon="🎤")

# Country list with emojis
COUNTRIES = [
    "🇸🇪 Sweden", "🇫🇷 France", "🇮🇹 Italy", "🇪🇸 Spain", "🇩🇪 Germany",
    "🇳🇴 Norway", "🇫🇮 Finland", "🇬🇧 United Kingdom", "🇮🇪 Ireland", "🇵🇹 Portugal",
    "🇬🇷 Greece", "🇷🇸 Serbia", "🇺🇦 Ukraine", "🇨🇭 Switzerland", "🇳🇱 Netherlands",
    "🇦🇹 Austria", "🇧🇪 Belgium", "🇨🇿 Czech Republic", "🇦🇺 Australia", "🇮🇱 Israel"
]

DATA_FILE = "assignments.json"

def load_assignments():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_assignments(assignments):
    with open(DATA_FILE, "w") as f:
        json.dump(assignments, f)

assignments = load_assignments()

# --- Styling and Logo ---
st.markdown("<h1 style='text-align: center;'>🎤 Eurovision Country Assigner 🎉</h1>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/en/6/69/Eurovision_Song_Contest_logo.png", width=250)

name = st.text_input("Enter your name to receive your Eurovision country:")

if name:
    if name in assignments:
        country = assignments[name]
        st.success(f"You are already representing: **{country}**! 🎉")
    else:
        used = set(assignments.values())
        available = [c for c in COUNTRIES if c not in used]

        if not available:
            st.error("All countries have been assigned!")
        else:
            with st.spinner("Spinning the wheel... 🌀"):
                time.sleep(2.5)  # Simulate delay
            country = random.choice(available)
            assignments[name] = country
            save_assignments(assignments)
            st.balloons()
            st.success(f"You are representing: **{country}**! 🎉")

