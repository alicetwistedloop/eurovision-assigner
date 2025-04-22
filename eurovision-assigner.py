import streamlit as st
import random
import json
import os
import time

st.set_page_config(page_title="Eurovision Country Assigner", page_icon="🎤")

COUNTRIES = [
    "🇸🇪 Sweden", "🇫🇷 France", "🇮🇹 Italy", "🇪🇸 Spain", "🇩🇪 Germany",
    "🇳🇴 Norway", "🇫🇮 Finland", "🇬🇧 United Kingdom", "🇮🇪 Ireland", "🇵🇹 Portugal",
    "🇬🇷 Greece", "🇷🇸 Serbia", "🇺🇦 Ukraine", "🇨🇭 Switzerland", "🇳🇱 Netherlands",
    "🇦🇹 Austria", "🇧🇪 Belgium", "🇨🇿 Czech Republic", "🇦🇺 Australia", "🇮🇱 Israel"
]

SUGGESTIONS = {
    "🇸🇪 Sweden": "Try bringing Swedish meatballs or a bottle of Aquavit! 🇸🇪",
    "🇫🇷 France": "Consider bringing a baguette, brie, or a bottle of red wine 🍷",
    "🇮🇹 Italy": "Pasta salad, tiramisu, or some limoncello would be perfect! 🍝",
    "🇪🇸 Spain": "Tapas or sangria are great options to represent Spain! 🍷",
    "🇩🇪 Germany": "Bratwurst, pretzels, or German beer are crowd-pleasers! 🍺",
    "🇳🇴 Norway": "How about smoked salmon or a bottle of Linie Aquavit? 🐟",
    "🇫🇮 Finland": "Try Karelian pies or a bottle of Salmiakki liqueur! 🥧",
    "🇬🇧 United Kingdom": "Scones, Pimm’s, or even fish and chips will do nicely 🇬🇧",
    "🇮🇪 Ireland": "Bring some Guinness or an Irish stew for the win! 🍻",
    "🇵🇹 Portugal": "Pastéis de nata or a bottle of Port wine = perfection 🇵🇹",
    "🇬🇷 Greece": "Spanakopita, tzatziki, or ouzo are all great ideas 🇬🇷",
    "🇷🇸 Serbia": "Ćevapi or rakija would represent Serbia well 🇷🇸",
    "🇺🇦 Ukraine": "Borscht or varenyky (dumplings) would be a delicious hit! 🥟",
    "🇨🇭 Switzerland": "How about fondue or some Swiss chocolate? 🍫",
    "🇳🇱 Netherlands": "Stroopwafels or Heineken will bring the Dutch vibes 🇳🇱",
    "🇦🇹 Austria": "Sacher torte or schnitzel would be wunderbar 🇦🇹",
    "🇧🇪 Belgium": "Belgian waffles, fries, or Trappist beer are classics 🇧🇪",
    "🇨🇿 Czech Republic": "Try bringing goulash or some Czech pilsner 🇨🇿",
    "🇦🇺 Australia": "Lamingtons, pavlova, or a good Shiraz would be ace 🇦🇺",
    "🇮🇱 Israel": "Shakshuka, hummus, or arak for a tasty touch 🇮🇱",
}

NAMES = ["Alice", "Allie", "Amy", "Emily", "Kate", "Sophie", "Dan", "Andy", "Tom", "Mike", "Jack", "Seb", "Copper", "Lucy"]

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
used_names = set(assignments.keys())
available_names = [n for n in NAMES if n not in used_names]

# --- App Header ---
st.markdown("<h1 style='text-align: center;'>🎤 Eurovision Country Assigner 🎉</h1>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/en/6/69/Eurovision_Song_Contest_logo.png", width=250)

# --- Name Selection ---
if "name_selected" not in st.session_state:
    st.session_state.name_selected = False

if not st.session_state.name_selected:
    st.subheader("Choose your name to reveal your country:")
    name = st.selectbox("Select your name", [""] + available_names)

    if name:
        st.session_state.name_selected = True
        st.session_state.current_name = name
        st.experimental_rerun()

# --- Result Reveal ---
elif st.session_state.name_selected:
    name = st.session_state.current_name

    if name in assignments:
        country = assignments[name]
        st.success(f"{name}, you are already representing: **{country}** 🎉")
    else:
        used = set(assignments.values())
        available = [c for c in COUNTRIES if c not in used]

        if not available:
            st.error("All countries have been assigned!")
        else:
            with st.spinner("Spinning the wheel... 🌀"):
                time.sleep(2.5)
            country = random.choice(available)
            assignments[name] = country
            save_assignments(assignments)
            st.balloons()
            st.success(f"{name}, you are representing: **{country}** 🎉")

    # Show suggestion
    if country in SUGGESTIONS:
        st.info(SUGGESTIONS[country])
