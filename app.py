import streamlit as st
import pandas as pd

# 1. DATABASE CLUB
def get_club_data():
    clubs = [
        {"Nome": "Amnesia Milano", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.4612, "lon": 9.2385},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.8285, "lon": 12.4735},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.6250, "lon": 9.5160},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.8267, "lon": 14.1648}
    ]
    return pd.DataFrame(clubs)

st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="centered")

st.title("🔊 Techno Radar Italia")
st.markdown("Seleziona un club per vedere la programmazione su Instagram")

df_clubs = get_club_data()

# Mappa
st.subheader("📍 Mappa dei Club")
st.map(df_clubs[['lat', 'lon']])

st.divider()

# Lista Club con Bottoni
st.subheader("🔥 Top Clubs & Events")

for i, row in df_clubs.iterrows():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"### {row['Nome']}")
        st.write(f"📍 {row['Città']}")
    with col2:
        st.link_button("Vedi Eventi 📸", row['Link'])
    st.divider()
