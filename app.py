import streamlit as st
import pandas as pd
import pydeck as pdk

# Database
def get_club_data():
    return [
        {"Nome": "Amnesia", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.46, "lon": 9.23},
        {"Nome": "Fabrique", "Città": "Milano", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.45, "lon": 9.25},
        {"Nome": "Cocoricò", "Città": "Riccione", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.98, "lon": 12.65},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.82, "lon": 12.47},
        {"Nome": "Tenax", "Città": "Firenze", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.79, "lon": 11.20},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.62, "lon": 9.51},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.82, "lon": 14.16},
        {"Nome": "Guendalina", "Città": "Lecce", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.01, "lon": 18.44}
    ]

st.set_page_config(page_title="Techno Radar Interattivo", layout="wide")

# CSS Base
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div.stButton > button { width: 100%; border-radius: 20px; background-color: #7000ff; color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 TECHNO RADAR INTERATTIVO")

data = get_club_data()
df = pd.DataFrame(data)

# CONFIGURAZIONE MAPPA INTERATTIVA (Pydeck)
view_state = pdk.ViewState(
    latitude=42.0,
    longitude=12.5,
    zoom=5,
    pitch=40,
)

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[lon, lat]',
    get_color='[112, 0, 255, 160]', # Viola Techno
    get_radius=20000,
    pickable=True, # Rende i puntini cliccabili/interattivi
)

# Render della mappa
col1, col2 = st.columns([2, 1])

with col1:
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{Nome}\nCittà: {Città}"} # Cosa appare quando tocchi il puntino
    ))

with col2:
    search = st.text_input("🔍 Cerca Città o Club", "")
    for club in data:
        if search.lower() in club['Città'].lower() or search.lower() in club['Nome'].lower():
            st.markdown(f"### {club['Nome']}")
            st.link_button(f"Instagram {club['Città']}", club['Link'])
            st.write("---")
