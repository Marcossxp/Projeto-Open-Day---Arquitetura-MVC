import streamlit as st

# Importa a view principal da aplicação
from view.lista_musicas import main as render_karaoke_page

# Configuração da página
st.set_page_config(
    page_title="Karaoke Music Application",
    page_icon="🎤",
    layout="wide",
)


def main():
    st.title("Karaoke Music Application")
    st.caption("Navegue pelo catálogo completo e encontre a próxima música para soltar a voz.")
    render_karaoke_page()


if __name__ == "__main__":
    main()