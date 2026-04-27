import streamlit as st
import pandas as pd

# 1. IL MEGA-DATABASE NAZIONALE (MI, BO, FE + ITALIA)
def get_club_data():
    return [
        # --- MILANO (MI) ---
        {"Regione": "Lombardia", "Nome": "Amnesia", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.461, "lon": 9.238},
        {"Regione": "Lombardia", "Nome": "Fabrique", "Città": "Milano", "Prov": "MI", "Orario": "23:00 - 04:30", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.451, "lon": 9.250},
        {"Regione": "Lombardia", "Nome": "Gate Milano", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/gatemilano/", "lat": 45.492, "lon": 9.179},
        {"Regione": "Lombardia", "Nome": "Magazzini Generali", "Città": "Milano", "Prov": "MI", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/magazzinigeneralimila/", "lat": 45.444, "lon": 9.201},
        {"Regione": "Lombardia", "Nome": "Bolgia", "Città": "Osio Sopra", "Prov": "BG", "Orario": "23:00 - 05:30", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.631, "lon": 9.592},
        
        # --- BOLOGNA (BO) ---
        {"Regione": "Emilia-Romagna", "Nome": "Link", "Città": "Bologna", "Prov": "BO", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/link.bologna/", "lat": 44.524, "lon": 11.378},
        {"Regione": "Emilia-Romagna", "Nome": "Numa Club", "Città": "Bologna", "Prov": "BO", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/numa_club/", "lat": 44.520, "lon": 11.365},
        {"Regione": "Emilia-Romagna", "Nome": "Matis Dinner Club", "Città": "Bologna", "Prov": "BO", "Orario": "22:30 - 04:30", "Link": "https://www.instagram.com/matis_dinner_club/", "lat": 44.492, "lon": 11.282},
        {"Regione": "Emilia-Romagna", "Nome": "Cassero DNA", "Città": "Bologna", "Prov": "BO", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/cassero_dna/", "lat": 44.502, "lon": 11.336},
        
        # --- FERRARA (FE) ---
        {"Regione": "Emilia-Romagna", "Nome": "Madam Club", "Città": "Ferrara", "Prov": "FE", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/madam.ferrara/", "lat": 44.832, "lon": 11.610},
        {"Regione": "Emilia-Romagna", "Nome": "College Ferrara", "Città": "Ferrara", "Prov": "FE", "Orario": "23:30 - 04:30", "Link": "https://www.instagram.com/college.ferrara/", "lat": 44.838, "lon": 11.619},
        {"Regione": "Emilia-Romagna", "Nome": "Sinapsi (Eventi)", "Città": "Ferrara", "Prov": "FE", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/sinapsi_fe/", "lat": 44.835, "lon": 11.625},

        # --- RESTO D'ITALIA ---
        {"Regione": "Emilia-Romagna", "Nome": "Cocoricò", "Città": "Riccione", "Prov": "RN", "Orario": "23:59 - 06:00", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.991, "lon": 12.656},
        {"Regione": "Toscana", "Nome": "Tenax", "Città": "Firenze", "Prov": "FI", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.791, "lon": 11.201},
        {"Regione": "Lazio", "Nome": "Spazio Novecento", "Città": "Roma", "Prov": "RM", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.828, "lon": 12.473},
        {"Regione": "Campania", "Nome": "Duel Club", "Città": "Napoli", "Prov": "NA", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.826, "lon": 14.164},
        {"Regione": "Puglia", "Nome": "Guendalina", "Città": "Lecce", "Prov": "LE", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.012, "lon": 18.441},
        {"Regione": "Veneto", "Nome": "Il Muretto", "Città": "Jesolo", "Prov": "VE", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/ilmuretto_official/", "lat": 45.492, "lon": 12.605},
    ]

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="wide")

# STILE CSS PERSONALIZZATO (DARK & NEON)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    div.stButton > button { 
        width: 100%; border-radius: 12px; background-color: #7000ff; color: white; 
        font-weight: bold; border: none; height: 45px; transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #00f2ff; color: black; transform: translateY(-2px); }
    .card {
        background-color: #1a1c24; padding: 18px; border-radius: 15px;
        border-left: 5px solid #7000ff; margin-bottom: 12px;
    }
    .regione-tag { background-color: #333; padding: 2px 8px; border-radius: 5px; font-size: 11px; color: #bbb; }
    .orario-tag { color: #00f2ff; font-weight: bold; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 TECHNO RADAR ITALIA")
st.write("Database ufficiale Club: MI - BO - FE e Top Nazionali.")

data = get_club_data()
df = pd.DataFrame(data)

# Layout: Mappa (sinistra) e Lista (destra)
col_map, col_list = st.columns([1.7, 1])

with col_map:
    # Mostra la mappa con i puntini viola
    st.map(df, latitude='lat', longitude='lon', color='#7000ff', size=70)
    st.sidebar.header("📍 Filtro Rapido")
    regione_sel = st.sidebar.selectbox("Filtra per Regione", ["Tutte"] + sorted(list(df['Regione'].unique())))

with col_list:
    search = st.text_input("🔍 Cerca Provincia (MI, BO, FE) o Nome", "").upper()
    st.markdown("---")
    
    # Logica di filtraggio
    if regione_sel != "Tutte":
        df = df[df['Regione'] == regione_sel]
    
    final_list = df.to_dict('records')
    if search:
        final_list = [c for c in final_list if search in c['Nome'].upper() or search in c['Prov'] or search in c['Città'].upper()]

    if not final_list:
        st.warning("Nessun club trovato con questi criteri.")
    
    for club in final_list:
        st.markdown(f"""
        <div class="card">
            <span class="regione-tag">{club['Regione']}</span><br>
            <b style="color:#ffffff; font-size:20px;">{club['Nome']}</b><br>
            <span style="color:#7000ff;">📍 {club['Città']} ({club['Prov']})</span><br>
            <span class="orario-tag">🕒 {club['Orario']}</span>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Vedi Eventi Instagram", club['Link'])
        st.write("")

st.sidebar.markdown("---")
st.sidebar.success(f"Radar attivo su {len(data)} club")
