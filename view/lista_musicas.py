import pandas as pd
import streamlit as st

from controller.musicaskaraokecontroller import (
    SEARCH_STATE_KEY,
    clear_search_value,
    ensure_search_state,
    get_filtered_catalog,
    get_full_catalog,
    get_search_value,
)


def main():
    """Montagem da tela principal da aplicação."""
    _inject_styles()
    ensure_search_state()  # Garante que o campo de busca tenha um valor inicial.

    search_text = _render_search_area()
    full_df, visible_full = get_full_catalog()
    filtered_df, visible_filtered = get_filtered_catalog(search_text, full_df)

    _render_summary_metrics(total=len(visible_full), filtered=len(visible_filtered), query=search_text)
    _render_dataframe(visible_filtered)


def _inject_styles() -> None:
    """Insere CSS simples para destacar o campo de busca e os números das músicas."""
    st.markdown(
        """
        <style>
        div[data-testid="stTextInput"] > label {
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.04rem;
            text-transform: uppercase;
            color: #1c355e;
        }
        div[data-testid="stTextInput"] input {
            font-size: 1.2rem;
            font-weight: 600;
            padding: 0.85rem 1rem;
            border-radius: 0.8rem;
            border: 2px solid #1c75bc;
            background-color: #f5fbff;
            color: #0b1f33;
        }
        div[data-testid="stMetricValue"] {
            font-weight: 700 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_search_area() -> str:
    """Exibe o campo de busca e retorna o texto digitado."""
    st.markdown("#### 🔎 Encontre sua música em segundos")
    st.caption("Pesquise por número do catálogo, nome da música, artista ou gênero.")

    search_col, clear_col = st.columns([6, 1])

    with search_col:
        # O Streamlit cuida de atualizar st.session_state automaticamente por causa da chave (key).
        st.text_input(
            "Busca no catálogo",
            key=SEARCH_STATE_KEY,
            placeholder="Ex.: 01039, Todo Azul do Mar, 14 Bis...",
            label_visibility="collapsed",
        )

    with clear_col:
        st.button("Limpar", on_click=clear_search_value, use_container_width=True)

    return get_search_value()


def _render_summary_metrics(total: int, filtered: int, query: str) -> None:
    """Mostra indicadores rápidos para o usuário entender o resultado da busca."""
    col1, col2, col3 = st.columns([1, 1, 2])
    col1.metric("Total no catálogo", f"{total:,}".replace(",", "."))
    col2.metric("Resultados", f"{filtered:,}".replace(",", "."))

    if query:
        col3.success(f"Mostrando resultados para “{query}”.")
    else:
        col3.info("Use o campo de busca para filtrar rapidamente o catálogo.")


def _render_dataframe(display_df: pd.DataFrame) -> None:
    """Exibe o catálogo final já filtrado, com destaque para número e nome da música."""
    st.markdown("#### 🎵 Catálogo de músicas")

    if display_df.empty:
        st.warning("Nenhuma música corresponde à sua busca. Tente ajustar os termos.")
        return

    # Destaca número e nome para facilitar leitura.
    styled_df = display_df.style.set_properties(
        subset=["numero", "musica"], **{"font-weight": "bold"}
    )

    # Controla a altura da tabela para evitar scroll infinito (máx. 20 linhas de cada vez).
    max_visible_rows = min(len(display_df), 20)
    table_height = 70 + max_visible_rows * 33

    st.dataframe(
        styled_df,
        use_container_width=True,
        height=table_height,
        hide_index=True,
        column_config={
            "numero": st.column_config.TextColumn("Número", width="small"),
            "musica": st.column_config.TextColumn("Música", width="large"),
            "artista": st.column_config.TextColumn("Artista"),
            "genero": st.column_config.TextColumn("Gênero"),
        },
    )