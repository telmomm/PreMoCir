import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Configuración de la página ---
st.set_page_config(
    page_title="Predicción de Mortalidad a 30 días", 
    layout="wide", 
    page_icon="🛌",
    initial_sidebar_state="expanded"
)

st.title("📊 Predicción de Mortalidad a 30 días")

# --- Cargar el modelo ---
@st.cache_resource
def load_model_simple():
    try:
        model = joblib.load('model.joblib')
        return model
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None
    
@st.cache_resource
def load_model_extended():
    try:
        model = joblib.load('model.joblib')
        return model
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None
    
# --- Selección del modelo ---
#model_type = st.radio("Selecciona el tipo de modelo:", ["Simple", "Extendido"])
extended = st.toggle("Modelo Extendido", value=False)
if extended:
    model_type = "Extendido"
else:
    model_type = "Simple"

if model_type == "Simple":
    model = load_model_simple()
    #st.header("📝 Datos del paciente (Modelo Simple)")
    
    # Inputs para el modelo simple
    col1, col2 = st.columns(2)
    with col1:
        htopre = st.number_input("Hematocrito preoperatorio (%)", 0.0, 100.0, 40.0, 0.5)
        creatinina = st.number_input("Creatinina preoperatoria (mg/dL)", 0.0, 20.0, 1.0, 0.1)
        edmonton = st.select_slider("Fragilidad Edmonton", options=list(range(14)), value=5)

    with col2:
        fecha_ingreso = st.date_input("Fecha de ingreso", pd.to_datetime("today"))
        complicaciones_mace = st.toggle("Complicaciones MACE", value=False)
        complicaciones_todas = st.toggle("Complicaciones Todas", value=False)

else:
    model = load_model_extended()
    #st.header("📝 Datos del paciente (Modelo Extendido)")
    
    # Inputs para el modelo extendido
    col1, col2 = st.columns(2)
    with col1:
        htopre = st.number_input("Hematocrito preoperatorio (%)", 0.0, 100.0, 40.0, 0.5)
        creatinina = st.number_input("Creatinina preoperatoria (mg/dL)", 0.0, 20.0, 1.0, 0.1)
        edmonton = st.select_slider("Fragilidad Edmonton", options=list(range(14)), value=5)
        #test5metros = st.number_input("Test de 5 metros (segundos)", 0.0, 100.0, 10.0, 0.1)
    with col2:
        fecha_ingreso = st.date_input("Fecha de ingreso", pd.to_datetime("today"))
        # Calcular la estancia hospitalaria con fecha de ingreso y dia actual
        fecha_ingreso = pd.to_datetime(fecha_ingreso)
        fecha_actual = pd.to_datetime("today")
        dias_hospitalizados = (fecha_actual - fecha_ingreso).days
        st.write(f"Dias hospitalizado: {dias_hospitalizados}")
        complicaciones_mace = st.toggle("Complicaciones MACE", value=False)
        complicaciones_todas = st.toggle("Complicaciones Todas", value=False)

# --- Predicción ---
if st.button("🔄 Realizar predicción", type="primary"):#
    if model is None:
        st.error("Modelo no disponible")
    else:

        #Calcular la estacia hospitalaria con fecha de ingreso y dia actual
        #fecha_ingreso = pd.to_datetime(fecha_ingreso)
        #fecha_actual = pd.to_datetime("today")
        #dias_hospitalizados = (fecha_actual - fecha_ingreso).days

        # Crear un diccionario con los datos de entrada
        input_data = {}
        if model_type == "Simple":
            input_data.update({
                'Creatininapre': creatinina,
                'Htopre': htopre,
                'Edmonton': edmonton,
                'Estanciahospitalariacalculada':dias_hospitalizados,
                'ComplicacionesMACE':1 if complicaciones_mace else 0,
                'ComplicacionesTODAS':1 if complicaciones_todas else 0,
                
            })
        #convertir complicaciones-mcae a numermero en una sola linea
        if model_type == "Extendido":
            input_data.update({
                'Creatininapre': creatinina,
                'Htopre': htopre,
                'Edmonton': edmonton,
                'Estanciahospitalariacalculada':dias_hospitalizados,
                'ComplicacionesMACE':1 if complicaciones_mace else 0,
                'ComplicacionesTODAS':1 if complicaciones_todas else 0,
                
            })
        # Datos de la preddicción
        try:
            #st.write("Datos de entrada:")
            #st.write(input_data)
            prediction = model.predict(pd.DataFrame([input_data]))[0]
            probabilities = model.predict_proba(pd.DataFrame([input_data]))[0]
            #st.success(f"Predicción: {prediction}")
            probabilidad_vivir = probabilities[0]*100
            probabilidad_morir = probabilities[1]*100
            #st.success(f"Probabilidad Sobrevivir: {probabilidad_vivir:.4f}%")
            st.success(f"Probabilidad Mortalidad: {probabilidad_morir:.4f}%")
        except AttributeError:
            st.error("El modelo no soporta la predicción de probabilidades.")

# ...existing code...

# --- Footer ---
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