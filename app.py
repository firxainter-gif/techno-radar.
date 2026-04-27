import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. DATABASE DEI CLUB (Nomi e link ai post IG più recenti/importanti)
def get_club_data():
    clubs = [
        {
            "Nome": "Amnesia Milano",
            "Città": "Milano",
            "IG_Post": "https://www.instagram.com/p/C6E7_I_I9Xy/", # Esempio di post
            "lat": 45.4612, "lon": 9.2385
        },
        {
            "Nome": "Spazio Novecento",
            "Città": "Roma",
            "IG_Post": "https://www.instagram.com/p/C58S-i_Is5t/",
            "lat": 41.8285, "lon": 12.4735
        },
        {
            "Nome": "Bolgia",
            "Città": "Bergamo",
            "IG_Post": "https://www.instagram.com/p/C6B9-i_Is5t/",
            "lat": 45.6250, "lon": 9.5160
        }
    ]
    return pd.DataFrame(clubs)

# 2. CONFIGURAZIONE APP
st.set_page_config(page_title="Techno Radar Social", page_icon="📸", layout="wide")

st.title("📸 Techno Radar: Social Edition")
st.markdown("Guarda gli ultimi annunci direttamente da Instagram")

df_clubs = get_club_data()

# --- MAPPA ---
st.subheader("📍 Localizzazione Club")
st.map(df_clubs[['lat', 'lon']])

# --- SEZIONE SOCIAL ---
st.subheader("🔥 Ultime news dai Club")

col1, col2 = st.columns(2)

for i, row in df_clubs.iterrows():
    # Scegliamo in quale colonna mettere il post
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        st.write(f"### {row['Nome']} ({row['Città']})")
        
        # Codice per incorporare il post di Instagram
        # Usiamo un iframe standard di Instagram
        ig_url = row['IG_Post']
        if ig_url.endswith('/'):
            embed_url = ig_url + "embed"
        else:
            embed_url = ig_url + "/embed"
            
        components.iframe(embed_url, height=500)
        st.markdown("---")

st.sidebar.success("App connessa ai feed Social 🟢")

