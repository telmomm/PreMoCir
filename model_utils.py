import joblib
import streamlit as st

@st.cache_resource
def load_model(path='model.joblib'):
    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None
