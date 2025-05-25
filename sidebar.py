import streamlit as st

def show_sidebar():

    with st.sidebar.expander("❓ ¿Qué es PreMoCir?"):
        st.markdown("""

        **PreMoCir** (Predicción de Mortalidad en Cirugía Cardíaca) es una herramienta de ayuda a la decisión clínica que estima la probabilidad de mortalidad de un paciente sometido a cirugía cardíaca, basándose en variables clínicas preoperatorias y datos de evolución hospitalaria. Utiliza modelos de aprendizaje automático desarrollados a partir de datos reales.
        """)

    with st.sidebar.expander("📘 Manual de Usuario"):
        st.markdown("""
        ### 1. Introducción de datos
        - Introduce los siguientes valores en los campos visibles:
            - **Hematocrito preoperatorio (%)**
            - **Creatinina preoperatoria (mg/dL)**
            - **Fragilidad Edmonton (0–13)**
            - **Fecha de ingreso hospitalario**
            - **Complicaciones MACE** (toggle): si el paciente ha tenido eventos cardiovasculares graves.
            - **Complicaciones TODAS** (toggle): si ha tenido cualquier tipo de complicación médica relevante.

        ### 2. Realizar predicción
        - Pulsa el botón **🔄 Realizar predicción**.
        - La aplicación mostrará la **probabilidad de mortalidad estimada** en porcentaje.

        """)

    with st.sidebar.expander("⚠️ Advertencias"):
        st.markdown("""
        - Esta aplicación es **una herramienta de apoyo** y **no sustituye el criterio clínico profesional**.
        - Los datos procesados **no se almacenan ni se transmiten**, garantizando privacidad y anonimato.
        - El modelo es probabilístico y puede estar sujeto a errores inherentes al aprendizaje automático.
        - Los resultados deben interpretarse en contexto clínico.


        """)
    st.sidebar.link_button("🔗 GitHub", "https://github.com/telmomm/PreMoCir/tree/main")
