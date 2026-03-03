import streamlit as st
import os
from PIL import Image

# Configuração de página para ocupar tudo
st.set_page_config(page_title="DISPLAY MONITOR", layout="wide")

# CSS para esconder o aviso amarelo e deixar o fundo 100% limpo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    /* Remove o aviso de depreciação da tela */
    .stAlert {display: none;} 
    body {background-color: black;}
    .stImage > img {
        width: 100%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

IMAGEM_NOME = "grafico.jpg"

if os.path.exists(IMAGEM_NOME):
    img = Image.open(IMAGEM_NOME)
    
    # Atualizado para o novo padrão que o Streamlit pediu
    st.image(img, use_container_width=True) 
else:
    st.error(f"Arquivo '{IMAGEM_NOME}' não encontrado.")