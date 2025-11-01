import streamlit as st 
import pandas as pd

st.title("Oficina OpenDay ADS")

# Chama a view lista_musicas
from view.lista_musicas import lista_musicas_view

st.set_page_config(
    page_title="lista music",
    page_icon="🎸",
    layout="wide",
)


def main():
    st.title("App Principal")
    lista_musicas_view()
    

if __name__ == "__main__":
    main()