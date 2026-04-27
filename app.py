import streamlit as st
import pandas as pd

# 1. DATABASE CLUB (Puoi aggiungerne quanti ne vuoi qui)
def get_club_data():
    clubs = [
        {"Nome": "Amnesia", "Città": "Milano", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.4612, "lon": 9.2385},
        {"Nome": "Fabrique", "Città": "Milano", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.4515, "lon": 9.2501},
        {"Nome": "Cocoricò", "Città": "Riccione", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.9856, "lon": 12.6565},
        {"Nome": "Spazio Novecento", "Città": "Roma", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.8285, "lon": 12.4735},
        {"Nome": "Tenax", "Città": "Firenze", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.7915, "lon": 11.2015},
        {"Nome": "Duel Club", "Città": "Napoli", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.8267, "lon": 14.1648},
        {"Nome": "Bolgia", "Città": "Bergamo", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.6250, "lon": 9.5160},
        {"Nome": "Cromie", "Città": "Taranto", "Link": "https://www.instagram.com/cromiedisco/", "lat": 40.4850, "lon": 17.0210}
    ]
    return pd.DataFrame(clubs)

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="wide")

# CSS PERSONALIZZATO PER RENDERLO BELLO
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #7000ff;
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00f2ff;
        color: black;
    }
    .club-card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #7000ff;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# HEADER
st.title("🔊 TECHNO RADAR ITALIA")
st.subheader("La mappa definitiva degli eventi underground")
st.markdown("---")

df_clubs = get_club_data()

# LAYOUT
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.markdown("### 📍 Esplora la Mappa")
    st.map(df_clubs, zoom=5, use_container_width=True)

with col_right:
    st.markdown("### 🔍 Cerca Club")
    search = st.text_input("Inserisci città o nome club...", placeholder="es. Milano")
    
    st.markdown("---")
    
    # Filtro
    filtered_df = df_clubs[
        df_clubs['Nome'].str.contains(search, case=False) | 
        df_clubs['Città'].str.contains(search, case=False)
    ]

    # Visualizzazione Card
    for i, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
                <div class="club-card">
                    <h3 style='margin:0; color:#00f2ff;'>{row['Nome']}</h3>
                    <p style='margin:5px 0; color:#ffffff;'>📍 {row['Città']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Vai al profilo di {row['Nome']}", row['Link'])
            st.markdown("<br>", unsafe_allow_html=True)

# FOOTER
st.sidebar.markdown("---")
st.sidebar.write("⚡ Powered by Gemini AI")
st.sidebar.write(f"📈 {len(df_clubs)} club monitorati")
