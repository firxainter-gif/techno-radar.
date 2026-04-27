import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURAZIONE APP
st.set_page_config(page_title="Techno Radar Italia", page_icon="🔊", layout="wide")

st.title("🔊 Techno Radar Italia")
st.subheader("Tutti gli eventi underground in tempo reale")

# --- SIMULAZIONE DATABASE EVENTI (In un'app reale qui avremmo lo scraper) ---
@st.cache_data
def carica_eventi():
    # Simuliamo i dati che il bot troverebbe su Resident Advisor o Shotgun
    data = {
        'Evento': ['Dystopian Milan', 'Hard Techno Gate', 'Industrial Roma', 'Acid Napoli', 'Techno Warehouse', 'Tunnel Club Night'],
        'Città': ['Milano', 'Torino', 'Roma', 'Napoli', 'Bologna', 'Milano'],
        'DJ': ['Rødhåd', 'Klangkuenstler', 'Anetha', '999999999', 'I Hate Models', 'Kobosil'],
        'Genere': ['Techno', 'Hard Techno', 'Industrial', 'Acid Techno', 'Hardcore', 'Techno'],
        'lat': [45.4642, 45.0703, 41.8919, 40.8518, 44.4949, 45.4800],
        'lon': [9.1900, 7.6868, 12.5113, 14.2681, 11.3426, 9.2100],
        'Data': ['2026-05-01', '2026-05-02', '2026-05-05', '2026-05-10', '2026-05-12', '2026-05-15']
    }
    return pd.DataFrame(data)

df_eventi = carica_eventi()

# --- SIDEBAR FILTRI ---
st.sidebar.header("Filtra la Serata")
citta_scelta = st.sidebar.multiselect("Seleziona Città", options=df_eventi['Città'].unique(), default=df_eventi['Città'].unique())
genere_scelto = st.sidebar.multiselect("Genere", options=df_eventi['Genere'].unique(), default=df_eventi['Genere'].unique())

# Filtriamo i dati in base alle scelte
df_filtrato = df_eventi[(df_eventi['Città'].isin(citta_scelta)) & (df_eventi['Genere'].isin(genere_scelto))]

# --- LAYOUT PRINCIPALE ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🗺️ Mappa degli Eventi")
    # Mostra la mappa dell'Italia con i punti degli eventi
    st.map(df_filtrato[['lat', 'lon']])

with col2:
    st.markdown("### 🗓️ Prossimi Eventi")
    if not df_filtrato.empty:
        for i, row in df_filtrato.iterrows():
            with st.expander(f"{row['Evento']} - {row['Città']}"):
                st.write(f"**📍 Dove:** {row['Città']}")
                st.write(f"**🎧 DJ:** {row['DJ']}")
                st.write(f"**📅 Data:** {row['Data']}")
                st.write(f"**🔊 Genere:** {row['Genere']}")
                st.button("Acquista Biglietto", key=i)
    else:
        st.warning("Nessun evento trovato con questi filtri.")

# --- SEZIONE AGGIORNAMENTO AUTOMATICO ---
st.divider()
st.info("🔄 Il Bot sta scansionando: Resident Advisor, Shotgun, DICE, Xceed...")
if st.button("Aggiorna Database ora"):
    st.toast("Scansione dei club in corso...")
    st.success("Database aggiornato con 3 nuovi eventi a Milano e Roma!")
