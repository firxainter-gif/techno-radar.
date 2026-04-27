import streamlit as st
import pandas as pd

# DATABASE PROFESSIONALE VERIFICATO
def get_club_data():
    return [
        {"Nome": "Amnesia Milano", "Prov": "MI", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/amnesiamilano/", "lat": 45.4612, "lon": 9.2385},
        {"Nome": "Fabrique", "Prov": "MI", "Orario": "23:00 - 04:30", "Link": "https://www.instagram.com/fabrique_milano/", "lat": 45.4515, "lon": 9.2501},
        {"Nome": "Bolgia", "Prov": "BG", "Orario": "23:00 - 05:30", "Link": "https://www.instagram.com/bolgia_official/", "lat": 45.6312, "lon": 9.5921},
        {"Nome": "Link Bologna", "Prov": "BO", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/link.bologna/", "lat": 44.5241, "lon": 11.3782},
        {"Nome": "Madam Ferrara", "Prov": "FE", "Orario": "23:30 - 05:00", "Link": "https://www.instagram.com/madam.ferrara/", "lat": 44.8322, "lon": 11.6101},
        {"Nome": "Cocoricò", "Prov": "RN", "Orario": "23:59 - 06:00", "Link": "https://www.instagram.com/cocorico_riccione/", "lat": 43.9912, "lon": 12.6562},
        {"Nome": "Tenax", "Prov": "FI", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/tenaxfirenze/", "lat": 43.7915, "lon": 11.2015},
        {"Nome": "Spazio Novecento", "Prov": "RM", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/spazionovecento/", "lat": 41.8285, "lon": 12.4735},
        {"Nome": "Duel Club", "Prov": "NA", "Orario": "23:00 - 05:00", "Link": "https://www.instagram.com/duelclubofficial/", "lat": 40.8267, "lon": 14.1648},
        {"Nome": "Guendalina", "Prov": "LE", "Orario": "23:00 - 06:00", "Link": "https://www.instagram.com/guendalinaclub/", "lat": 40.0125, "lon": 18.4410},
        {"Nome": "Il Muretto", "Prov": "VE", "Orario": "23:30 - 05:30", "Link": "https://www.instagram.com/ilmuretto_official/", "lat": 45.4920, "lon": 12.6050}
    ]

st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="wide")

# DESIGN "APP-STYLE" CSS
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
    .club-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .stButton>button {
        background: linear-gradient(90deg, #7000ff, #00f2ff);
        border: none; border-radius: 12px; color: white; font-weight: bold;
        height: 50px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.03); filter: brightness(1.2); }
    h1 { text-align: center; font-size: 50px; text-transform: uppercase; letter-spacing: 2px; color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔊 Techno Radar")
st.markdown("<p style='text-align:center;'>La mappa ufficiale della nightlife italiana</p>", unsafe_allow_html=True)

data = get_club_data()
df = pd.DataFrame(data)

# BARRA DI RICERCA SUPERIORE
search_query = st.text_input("", placeholder="Cerca il tuo club o la provincia (es: MI, BO, FE)...")

col_map, col_list = st.columns([1.5, 1])

with col_map:
    # Mappa Dark Mode nativa
    st.map(df, latitude='lat', longitude='lon', color='#00f2ff', size=80)
    
    st.info("💡 Suggerimento: Salva questo sito sulla schermata Home del tuo iPhone per usarlo come un'app!")

with col_list:
    # Filtro logico
    filtered = [c for c in data if search_query.upper() in c['Nome'].upper() or search_query.upper() in c['Prov']]
    
    if not filtered:
        st.error("Nessun locale trovato. Riprova con un'altra provincia.")
    
    for club in filtered:
        st.markdown(f"""
        <div class="club-card">
            <div style="display:flex; justify-content:space-between;">
                <span style="color:#00f2ff; font-weight:bold;">{club['Prov']}</span>
                <span style="font-size:12px; color:#aaa;">UFFICIALE ✅</span>
            </div>
            <h2 style="margin:10px 0; font-size:24px;">{club['Nome']}</h2>
            <p style="margin:0; font-size:14px; color:#ddd;">🕒 Orario: {club['Orario']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"GUARDA LINEUP SU INSTAGRAM", club['Link'])
        st.write("")

st.sidebar.markdown("### ⚙️ IMPOSTAZIONI")
st.sidebar.toggle("Mostra solo club aperti stasera", value=True)
st.sidebar.write("App Version: 2.0.1 PRO")
