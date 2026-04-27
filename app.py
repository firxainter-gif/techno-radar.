import streamlit as st
import pandas as pd

# Database
def get_club_data():
    return [
        {"Nome": "Amnesia", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.46, "lon": 9.23},
        {"Nome": "Cocoricò", "Città": "Riccione", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.98, "lon": 12.65},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.82, "lon": 12.47},
        {"Nome": "Tenax", "Città": "Firenze", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.79, "lon": 11.20},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.62, "lon": 9.51},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.82, "lon": 14.16}
    ]

st.set_page_config(page_title="Techno Radar", layout="wide")

# Stile CSS Base
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div.stButton > button { width: 100%; border-radius: 20px; background-color: #7000ff; color: white; }
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
    search = st.text_input("🔍 Cerca Città", "")
    for club in data:
        if search.lower() in club['Città'].lower() or search.lower() in club['Nome'].lower():
            st.markdown(f"### {club['Nome']}")
            st.link_button(f"Instagram {club['Città']}", club['Link'])
            st.write("---")
