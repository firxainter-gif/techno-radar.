import streamlit as st
import pandas as pd

# DATABASE NAZIONALE COMPLETO (Regioni e Province)
def get_club_data():
    return [
        # --- NORD ITALIA ---
        {"Regione": "Lombardia", "Nome": "Amnesia Milano", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.46, "lon": 9.23},
        {"Regione": "Lombardia", "Nome": "Bolgia", "Città": "Osio Sopra", "Prov": "BG", "Orario": "23:00 - 05:30", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.63, "lon": 9.59},
        {"Regione": "Lombardia", "Nome": "Number One", "Città": "Corte Franca", "Prov": "BS", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/numberone.disco/", "lat": 45.62, "lon": 9.98},
        {"Regione": "Piemonte", "Nome": "Audiodrome", "Città": "Moncalieri", "Prov": "TO", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/audiodromeclub/", "lat": 45.00, "lon": 7.67},
        {"Regione": "Piemonte", "Nome": "Khaos", "Città": "Torino", "Prov": "TO", "Orario": "00:00 - 06:00", "Link": "https://www.instagram.com/khaos_torino/", "lat": 45.07, "lon": 7.68},
        {"Regione": "Veneto", "Nome": "Il Muretto", "Città": "Jesolo", "Prov": "VE", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/ilmuretto_official/", "lat": 45.49, "lon": 12.60},
        {"Regione": "Veneto", "Nome": "Story Club", "Città": "Padova", "Prov": "PD", "Orario": "23:30 - 04:30", "Link": "https://www.instagram.com/story_club/", "lat": 45.40, "lon": 11.87},
        {"Regione": "Liguria", "Nome": "Pacha (Ex Cavo)", "Città": "Genova", "Prov": "GE", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/pachagenova/", "lat": 44.41, "lon": 8.93},
        {"Regione": "Friuli-V.G.", "Nome": "Area Venezia", "Città": "Lignano", "Prov": "UD", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/areavenezia/", "lat": 45.68, "lon": 13.11},

        # --- CENTRO ITALIA ---
        {"Regione": "Emilia-Romagna", "Nome": "Cocoricò", "Città": "Riccione", "Prov": "RN", "Orario": "23:59 - 06:00", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.99, "lon": 12.65},
        {"Regione": "Emilia-Romagna", "Nome": "Link Bologna", "Città": "Bologna", "Prov": "BO", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/link.bologna/", "lat": 44.52, "lon": 11.37},
        {"Regione": "Emilia-Romagna", "Nome": "Madam Club", "Città": "Ferrara", "Prov": "FE", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/madam.ferrara/", "lat": 44.83, "lon": 11.61},
        {"Regione": "Toscana", "Nome": "Tenax", "Città": "Firenze", "Prov": "FI", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.79, "lon": 11.20},
        {"Regione": "Lazio", "Nome": "Spazio Novecento", "Città": "Roma", "Prov": "RM", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.82, "lon": 12.47},
        {"Regione": "Umbria", "Nome": "Red Zone", "Città": "Perugia", "Prov": "PG", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/redzone_club/", "lat": 43.11, "lon": 12.38},
        {"Regione": "Marche", "Nome": "Mamamia", "Città": "Senigallia", "Prov": "AN", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/mamamia_senigallia/", "lat": 43.71, "lon": 13.21},
        {"Regione": "Abruzzo", "Nome": "Megà", "Città": "Pescara", "Prov": "PE", "Orario": "23:30 - 04:30", "Link": "https://www.instagram.com/megapescara/", "lat": 42.46, "lon": 14.21},

        # --- SUD E ISOLE ---
        {"Regione": "Campania", "Nome": "Duel Club", "Città": "Pozzuoli", "Prov": "NA", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.82, "lon": 14.16},
        {"Regione": "Puglia", "Nome": "Guendalina", "Città": "S. Cesarea", "Prov": "LE", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.03, "lon": 18.45},
        {"Regione": "Puglia", "Nome": "Cromie", "Città": "Castellaneta", "Prov": "TA", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/cromiedisco/", "lat": 40.50, "lon": 16.93},
        {"Regione": "Basilicata", "Nome": "Basura", "Città": "Matera", "Prov": "MT", "Orario": "23:30 - 04:30", "Link": "https://www.instagram.com/basuraclub/", "lat": 40.66, "lon": 16.60},
        {"Regione": "Calabria", "Nome": "La Suerte", "Città": "Pisciotta", "Prov": "CS", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/lasuerteofficial/", "lat": 39.30, "lon": 16.25},
        {"Regione": "Sicilia", "Nome": "Mob Disco Theatre", "Città": "Palermo", "Prov": "PA", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/mobdiscotheatre/", "lat": 38.11, "lon": 13.36},
        {"Regione": "Sicilia", "Nome": "Afrobar", "Città": "Catania", "Prov": "CT", "Orario": "22:00 - 04:00", "Link": "https://www.instagram.com/afrobarcatania/", "lat": 37.50, "lon": 15.09},
        {"Regione": "Sardegna", "Nome": "Phi Beach", "Città": "Arzachena", "Prov": "SS", "Orario": "18:00 - 03:00", "Link": "https://www.instagram.com/phibeach_official/", "lat": 41.13, "lon": 9.47},
    ]

# CONFIGURAZIONE APP
st.set_page_config(page_title="Techno Radar Italia", page_icon="🔊", layout="wide")

# CSS DESIGN PROFESSIONALE
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0b0d11, #161b22); color: white; }
    .club-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 15px;
        border-left: 5px solid #7000ff;
        margin-bottom: 10px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7000ff, #00f2ff);
        border: none; border-radius: 10px; color: white; font-weight: bold; width: 100%;
    }
    .regione-badge {
        background-color: #7000ff; color: white; padding: 2px 8px; border-radius: 10px; font-size: 11px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 Techno Radar: Italia")

data = get_club_data()
df = pd.DataFrame(data)

# Barra di ricerca
query = st.text_input("🔍 Cerca per Regione, Provincia o Nome Club", placeholder="Es: Milano, Emilia-Romagna, Roma...")

col_map, col_list = st.columns([1.6, 1])

with col_map:
    # Mappa con tutti i club
    st.map(df, latitude='lat', longitude='lon', color='#7000ff', size=70)

with col_list:
    # LOGICA DI FILTRO GLOBALE
    if query:
        filtered = [
            c for c in data 
            if query.lower() in c['Regione'].lower() 
            or query.lower() in c['Città'].lower() 
            or query.lower() in c['Prov'].lower() 
            or query.lower() in c['Nome'].lower()
        ]
    else:
        filtered = data[:10] # Mostra i primi 10 se vuoto
        st.info("Digita una zona per vedere i club.")

    for club in filtered:
        st.markdown(f"""
        <div class="club-card">
            <span class="regione-badge">{club['Regione']}</span><br>
            <b style="font-size:18px;">{club['Nome']}</b><br>
            <small>📍 {club['Città']} ({club['Prov']})</small><br>
            <span style="color:#00f2ff; font-size:13px;">🕒 {club['Orario']}</span>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"INFO LINEUP", club['Link'])
        st.write("")

st.sidebar.markdown("### 📊 Stato Database")
st.sidebar.write(f"Regioni coperte: {len(df['Regione'].unique())}")
st.sidebar.write(f"Totale Club: {len(data)}")
