import streamlit as st
st.set_page_config(layout="wide")
import besoin_individuel
import besoincollectif
PAGES = {
    "Besoins individuels": besoin_individuel,
    "Besoins collectifs": besoincollectif,
    }

st.sidebar.header('Liste des outils :gear:', )
selection = st.sidebar.radio("  ", list(PAGES.keys()))
page = PAGES[selection]
page.main()