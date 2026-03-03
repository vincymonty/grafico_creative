import streamlit as st
import os
from PIL import Image

# Configurações para esconder TUDO
st.set_page_config(page_title="Monitor", layout="wide")

st.markdown("""
    <style>
    /* Esconde avisos, erros, menus e cabeçalhos */
    .stAlert, .stException, footer, header, #MainMenu {display: none !important;}
    .reportview-container { background: black; }
    body { background-color: black; margin: 0; padding: 0; }
    .stImage > img { width: 100vw; height: auto; }
    </style>
    """, unsafe_allow_html=True)

IMAGEM = "grafico.jpg"

if os.path.exists(IMAGEM):
    img = Image.open(IMAGEM)
    st.image(img, use_container_width=True)
else:
    st.write("Aguardando arquivo...")