import streamlit as st
import pandas as pd

# 1. DATABASE POTENZIATO: MOLTI PIÙ LOCALI PER ZONA
def get_club_data():
    return [
        # --- MILANO E DINTORNI (Tutti questi appariranno cercando 'Milano') ---
        {"Regione": "Lombardia", "Nome": "Amnesia Milano", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.461, "lon": 9.238},
        {"Regione": "Lombardia", "Nome": "Fabrique Milano", "Città": "Milano", "Prov": "MI", "Orario": "23:00 - 04:30", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.451, "lon": 9.250},
        {"Regione": "Lombardia", "Nome": "Gate Milano", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/gatemilano/", "lat": 45.492, "lon": 9.179},
        {"Regione": "Lombardia", "Nome": "Magazzini Generali", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/magazzinigeneralimila/", "lat": 45.444, "lon": 9.201},
        {"Regione": "Lombardia", "Nome": "Social Music City", "Città": "Milano", "Prov": "MI", "Orario": "16:00 - 00:00", "Link": "https://www.instagram.com/socialmusiccity/", "lat": 45.445, "lon": 9.238},
        {"Regione": "Lombardia", "Nome": "District", "Città": "Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/districtmilano/", "lat": 45.485, "lon": 9.202},
        {"Regione": "Lombardia", "Nome": "Bolgia", "Città": "Osio Sopra", "Prov": "BG", "Orario": "23:00 - 05:30", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.631, "lon": 9.592},
        {"Regione": "Lombardia", "Nome": "Number One", "Città": "Corte Franca", "Prov": "BS", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/numberone.disco/", "lat": 45.625, "lon": 9.985},
        
        # --- BOLOGNA E FERRARA ---
        {"Regione": "Emilia-Romagna", "Nome": "Link Bologna", "Città": "Bologna", "Prov": "BO", "Orario": "23:30 - 06:00", "Link": "https://www.instagram.com/link.bologna/", "lat": 44.524, "lon": 11.378},
        {"Regione": "Emilia-Romagna", "Nome": "Numa Club", "Città": "Bologna", "Prov": "BO", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/numa_club/", "lat": 44.520, "lon": 11.365},
        {"Regione": "Emilia-Romagna", "Nome": "Madam Club", "Città": "Ferrara", "Prov": "FE", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/madam.ferrara/", "lat": 44.832, "lon": 11.610},
        {"Regione": "Emilia-Romagna", "Nome": "College Ferrara", "Città": "Ferrara", "Prov": "FE", "Orario": "23:30 - 04:30", "Link": "https://www.instagram.com/college.ferrara/", "lat": 44.838, "lon": 11.619},
        
        # --- ALTRE BIG ---
        {"Regione": "Emilia-Romagna", "Nome": "Cocoricò", "Città": "Riccione", "Prov": "RN", "Orario": "23:59 - 06:00", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.991, "lon": 12.656},
        {"Regione": "Toscana", "Nome": "Tenax", "Città": "Firenze", "Prov": "FI", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.791, "lon": 11.201},
        {"Regione": "Lazio", "Nome": "Spazio Novecento", "Città": "Roma", "Prov": "RM", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.828, "lon": 12.473},
        {"Regione": "Campania", "Nome": "Duel Club", "Città": "Napoli", "Prov": "NA", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.826, "lon": 14.164},
        {"Regione": "Puglia", "Nome": "Guendalina", "Città": "Lecce", "Prov": "LE", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.012, "lon": 18.441}
    ]

st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="wide")

# CSS DESIGN
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    .club-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 15px;
        border-left: 5px solid #7000ff;
        margin-bottom: 15px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7000ff, #00f2ff);
        border: none; border-radius: 10px; color: white; font-weight: bold; width: 100%;
    }
    .badge { background-color: #7000ff; padding: 2px 8px; border-radius: 10px; font-size: 11px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 Techno Radar Italia")

data = get_club_data()
df = pd.DataFrame(data)

# BARRA DI RICERCA
query = st.text_input("📍 Cerca la tua zona (es: Milano, Bologna, Roma...)", placeholder="Scrivi qui...")

# Layout
col_map, col_list = st.columns([1.5, 1])

with col_map:
    # Filtriamo i dati per la mappa basandoci sulla ricerca
    if query:
        map_df = df[df.apply(lambda row: query.lower() in row.astype(str).str.lower().values, axis=1)]
    else:
        map_df = df
    
    st.map(map_df, latitude='lat', longitude='lon', color='#7000ff', size=80)

with col_list:
    if query:
        # LOGICA DI RICERCA CHE MOSTRA TUTTI I RISULTATI
        results = [
            c for c in data 
            if query.lower() in c['Nome'].lower() 
            or query.lower() in c['Città'].lower() 
            or query.lower() in c['Prov'].lower()
            or query.lower() in c['Regione'].lower()
        ]
        
        if results:
            st.success(f"Trovati {len(results)} club!")
            for club in results:
                st.markdown(f"""
                <div class="club-card">
                    <span class="badge">{club['Regione']}</span><br>
                    <b style="font-size:18px; color:#00f2ff;">{club['Nome']}</b><br>
                    <small>📍 {club['Città']} ({club['Prov']})</small><br>
                    <span style="font-size:14px;">🕒 {club['Orario']}</span>
                </div>
                """, unsafe_allow_html=True)
                st.link_button(f"INFO IG", club['Link'])
                st.write("")
        else:
            st.error("Nessun club trovato. Prova con un'altra parola!")
    else:
        st.info("Digita una città per visualizzare i club della zona.")
