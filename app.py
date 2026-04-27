import streamlit as st
import pandas as pd

# Database Ampliato (Struttura sicura)
def get_club_data():
    return [
        {"Nome": "Amnesia", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.46, "lon": 9.23},
        {"Nome": "Fabrique", "Città": "Milano", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.45, "lon": 9.25},
        {"Nome": "Social Music City", "Città": "Milano", "Link": "https://www.instagram.com/socialmusiccity/", "lat": 45.44, "lon": 9.23},
        {"Nome": "Cocoricò", "Città": "Riccione", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.98, "lon": 12.65},
        {"Nome": "Peter Pan", "Città": "Riccione", "Link": "https://www.instagram.com/peterpanclub/", "lat": 43.97, "lon": 12.66},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.82, "lon": 12.47},
        {"Nome": "Room 26", "Città": "Roma", "Link": "https://www.instagram.com/room26_roma/", "lat": 41.83, "lon": 12.47},
        {"Nome": "Tenax", "Città": "Firenze", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.79, "lon": 11.20},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.62, "lon": 9.51},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.82, "lon": 14.16},
        {"Nome": "Old River Park", "Città": "Caserta", "Link": "https://www.instagram.com/oldriverparkofficial/", "lat": 41.14, "lon": 14.34},
        {"Nome": "Cromie", "Città": "Taranto", "Link": "https://www.instagram.com/cromiedisco/", "lat": 40.48, "lon": 17.02},
        {"Nome": "Guendalina", "Città": "Lecce", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.01, "lon": 18.44},
        {"Nome": "Musica Riccione", "Città": "Riccione", "Link": "https://www.instagram.com/musicariccione/", "lat": 43.99, "lon": 12.64},
        {"Nome": "Red Zone", "Città": "Perugia", "Link": "https://www.instagram.com/redzone_club/", "lat": 43.11, "lon": 12.38},
        {"Nome": "Il Muretto", "Città": "Jesolo", "Link": "https://www.instagram.com/ilmuretto_official/", "lat": 45.49, "lon": 12.60}
    ]

st.set_page_config(page_title="Techno Radar", layout="wide")

# Stile CSS Base (Semplificato per non rompere l'app)
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
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 TECHNO RADAR ITALIA")

data = get_club_data()
df = pd.DataFrame(data)

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.map(df)

with col2:
    st.subheader("🔍 Cerca il tuo Club")
    search = st.text_input("Scrivi città o nome...", "")
    st.write("---")
    for club in data:
        if search.lower() in club['Città'].lower() or search.lower() in club['Nome'].lower():
            st.markdown(f"### {club['Nome']}")
            st.caption(f"📍 {club['Città']}")
            st.link_button(f"Programmazione IG", club['Link'])
            st.write("---")
