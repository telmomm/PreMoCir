import streamlit as st
from streamlit_modal import Modal
from edmonton_modal import edmonton_questionnaire

st.set_page_config(page_title="Evaluación Edmonton", layout="centered")

st.title("Evaluación Clínica")

# Botón y modal
modal = Modal("Escala de Fragilidad de Edmonton", key="edmonton_modal", max_width=600)

if st.button("Abrir evaluación Edmonton"):
    modal.open()

if modal.is_open():
    with modal.container():
        edmonton_questionnaire()

# Mostrar resultado fuera del modal si ya fue completado
if "edmonton_result" in st.session_state and st.session_state.edmonton_result is not None:
    st.markdown("---")
    st.subheader("Resultado Edmonton final:")
    st.metric(label="Puntaje de Fragilidad", value=st.session_state.edmonton_result)
