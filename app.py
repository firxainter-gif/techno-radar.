
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 1. IL "CERVELLO" (Lo Scraper per trovare eventi reali)
def scrape_techno():
    # URL di Shotgun Milano (uno dei siti più semplici per iniziare)
    url = "https://shotgun.live/it/cities/milan" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        eventi_reali = []
        # Cerchiamo i titoli degli eventi (tag h3 su Shotgun)
        for item in soup.find_all('h3')[:15]: 
            nome_evento = item.text.strip()
            if nome_evento:
                eventi_reali.append({
                    'Evento': nome_evento,
                    'Città': 'Milano',
                    'Genere': 'Techno / Electronic',
                    'lat': 45.4642, 
                    'lon': 9.1900
                })
        return pd.DataFrame(eventi_reali)
    except Exception as e:
        return pd.DataFrame([{'Evento': f'Errore: {e}', 'Città': 'Milano', 'Genere': 'N/A', 'lat': 45.46, 'lon': 9.19}])

# 2. L'INTERFACCIA DELL'APP
st.set_page_config(page_title="Techno Radar PRO", page_icon="🔊", layout="wide")

st.title("🔊 Techno Radar Real-Time")
st.markdown("Questa app scansiona automaticamente il web alla ricerca di eventi Techno.")

# Pulsante per attivare lo scraper
if st.button('🔄 AVVIA SCANSIONE WEB ORA'):
    with st.spinner('Il bot sta setacciando i club... attendi...'):
        df = scrape_techno()
        
        if not df.empty and 'Evento' in df.columns:
            st.success(f'Trovati {len(df)} eventi potenziali!')
            
            # Mostra la mappa
            st.subheader("📍 Mappa degli eventi")
            st.map(df[['lat', 'lon']])
            
            # Mostra la lista
            st.subheader("🗓️ Lista Eventi Trovati")
            st.table(df[['Evento', 'Città', 'Genere']])
        else:
            st.error("Il sito è protetto o non ci sono eventi al momento. Riprova più tardi.")

st.sidebar.info("Bot Status: Online 🟢")
st.sidebar.markdown("Scansione attiva su: **Shotgun.live**")
