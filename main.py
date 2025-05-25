import streamlit as st
import pandas as pd
from model_utils import load_model
from prediction import make_prediction
from sidebar import show_sidebar
from footer import show_footer
from streamlit_modal import Modal
from edmonton_modal import edmonton_questionnaire


st.set_page_config(
    page_title="PreMoCir", 
    layout="wide", 
    page_icon="🛌",
    initial_sidebar_state="collapsed"
)

st.title("Predicción de la Mortalidad en Cirugía Cardíaca")
show_sidebar()

# --- Lógica del formulario ---
# ... tus inputs ...

model = load_model()
    #st.header("📝 Datos del paciente (Modelo Extendido)")
    
modal = Modal("Escala de Fragilidad de Edmonton", key="edmonton_modal", max_width=600)


col1, col2 = st.columns(2)
with col1:
        htopre = st.number_input("Hematocrito preoperatorio (%)", 0.0, 100.0, 40.0, 0.5)
        creatinina = st.number_input("Creatinina preoperatoria (mg/dL)", 0.0, 20.0, 1.0, 0.1)
        col1_1, col1_2 = st.columns(2)

        with col1_1:
            edmonton = st.select_slider("Fragilidad Edmonton", options=list(range(18)), value=5)
        with col1_2:
            if st.button("Abrir evaluación Edmonton"):
                modal.open()
if modal.is_open():
    with modal.container():
        edmonton_questionnaire()
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
   
        #convertir complicaciones-mcae a numermero en una sola linea
       
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


show_footer()

