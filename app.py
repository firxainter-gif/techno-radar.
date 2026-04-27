import streamlit as st
import pandas as pd

# 1. DATABASE CLUB (Ho aggiunto le coordinate precise per il colore)
def get_club_data():
    return [
        {"Nome": "Amnesia", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.4612, "lon": 9.2385},
        {"Nome": "Fabrique", "Città": "Milano", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.4515, "lon": 9.2501},
        {"Nome": "Cocoricò", "Città": "Riccione", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.9856, "lon": 12.6565},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.8285, "lon": 12.4735},
        {"Nome": "Tenax", "Città": "Firenze", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.7915, "lon": 11.2015},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.6250, "lon": 9.5160},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.8267, "lon": 14.1648},
        {"Nome": "Guendalina", "Città": "Lecce", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.0125, "lon": 18.4410},
        {"Nome": "Cromie", "Città": "Taranto", "Link": "https://www.instagram.com/cromiedisco/", "lat": 40.4850, "lon": 17.0210}
    ]

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Techno Radar Italia", page_icon="🔊", layout="wide")

# CSS PER LO STILE DARK E BOTTONI VIOLA
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div.stButton > button { 
        width: 100%; 
        border-radius: 20px; 
        background-color: #7000ff; 
        color: white; 
        font-weight: bold;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #00f2ff;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 TECHNO RADAR ITALIA")
st.markdown("Esplora i club e clicca sui puntini per i dettagli.")

data = get_club_data()
df = pd.DataFrame(data)

# Creazione delle colonne
col1, col2 = st.columns([2, 1])

with col1:
    # MAPPA INTERATTIVA (Mappa reale + Puntini Viola)
    # color='#7000ff' è il viola techno
    st.map(df, latitude='lat', longitude='lon', color='#7000ff', size=40)

with col2:
    st.subheader("🔍 Cerca Club")
    search = st.text_input("Inserisci città o nome...", placeholder="es. Riccione")
    st.write("---")
    
    # Filtro dinamico
    for club in data:
        if search.lower() in club['Città'].lower() or search.lower() in club['Nome'].lower():
            st.markdown(f"### {club['Nome']}")
            st.caption(f"📍 {club['Città']}")
            st.link_button(f"Vedi Programmazione IG", club['Link'])
            st.write("---")

st.sidebar.info(f"Monitoraggio attivo su {len(data)} club.")
