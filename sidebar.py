import streamlit as st
from languages import get_translation, get_available_languages

def show_sidebar():
    # Obtener idioma actual
    if 'language' not in st.session_state:
        st.session_state.language = 'es'
    
    # Función para obtener traducción
    def t(key):
        return get_translation(st.session_state.language, key)

    with st.sidebar.expander(t("sidebar_about_title")):
        st.markdown(t("sidebar_about_content"))

    with st.sidebar.expander(t("sidebar_manual_title")):
        st.markdown(t("sidebar_manual_content"))

    with st.sidebar.expander(t("sidebar_warnings_title")):
        st.markdown(t("sidebar_warnings_content"))
    
    st.sidebar.link_button(t("sidebar_github_button"), "https://github.com/telmomm/PreMoCir/tree/main")
    
    # Separador
    st.sidebar.divider()
    
    # Selector de idioma al final del sidebar
    st.sidebar.subheader(t("language_selector"))
    
    languages = get_available_languages()
    current_lang_index = next((i for i, (code, _, _) in enumerate(languages) if code == st.session_state.language), 0)
    
    # Crear opciones para el selector
    language_options = [f"{flag} {name}" for code, name, flag in languages]
    language_codes = [code for code, _, _ in languages]
    
    selected_index = st.sidebar.selectbox(
        label="",
        options=range(len(language_options)),
        format_func=lambda x: language_options[x],
        index=current_lang_index,
        key="language_selector"
    )
    
    # Actualizar idioma si cambió
    if language_codes[selected_index] != st.session_state.language:
        st.session_state.language = language_codes[selected_index]
        st.rerun()
