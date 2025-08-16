import streamlit as st
from languages import get_translation

def show_footer():
    # Obtener idioma actual
    if 'language' not in st.session_state:
        st.session_state.language = 'es'
    
    # Función para obtener traducción
    def t(key):
        return get_translation(st.session_state.language, key)
    
    footer = f"""
    <div style="
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
        color: gray;
        font-size: small;
        z-index: 1000;">
        {t("footer_developed_by")} <b>Telmo Miguel Medina</b> | © 2025
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
