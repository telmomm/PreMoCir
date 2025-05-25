import streamlit as st

def show_footer():
    footer = """
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
        Desarrollado por <b>Telmo Miguel Medina</b> | © 2025
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
