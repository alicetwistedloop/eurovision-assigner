import streamlit as st
import random
import json
import os

st.set_page_config(page_title="Eurovision Country Assigner", page_icon="🎤")

# Country list with emojis
COUNTRIES = [
    "🇸🇪 Sweden", "🇫🇷 France", "🇮🇹 Italy", "🇪🇸 Spain", "🇩🇪 Germany",
    "🇳🇴 Norway", "🇫🇮 Finland", "🇬🇧 United Kingdom", "🇮🇪 Ireland", "🇵🇹 Portugal",
    "🇬🇷 Greece", "🇷🇸 Serbia", "🇺🇦 Ukraine", "🇨🇭 Switzerland", "🇳🇱 Netherlands",
    "🇦🇹 Austria", "🇧🇪 Belgium", "🇨🇿 Czech Republic", "🇦🇺 Australia", "🇮🇱 Israel"
]

NAMES = ["Alice", "Allie", "Dan", "Kate", "Andy", "Emily", "Jack", "Mike", "Amy", "Seb", "Copper", "Lucy", "Sophie"]

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

# --- App Header ---
st.markdown("<h1 style='text-align: center;'>🎤 Eurovision Country Assigner 🎉</h1>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/en/6/69/Eurovision_Song_Contest_logo.png", width=250)

# --- Button Selection ---
st.subheader("Click your name to get your country:")

clicked_name = None
cols = st.columns(3)

for i, name in enumerate(NAMES):
    if cols[i % 3].button(name):
        clicked_name = name

if clicked_name:
    if clicked_name in assignments:
        country = assignments[clicked_name]
        st.success(f"{clicked_name}, you are already representing: **{country}** 🎉")
    else:
        used = set(assignments.values())
        available = [c for c in COUNTRIES if c not in used]

        if not available:
            st.error("All countries have been assigned!")
        else:
            country = random.choice(available)
            assignments[clicked_name] = country
            save_assignments(assignments)
            st.balloons()
            st.success(f"{clicked_name}, you are representing: **{country}** 🎉")
