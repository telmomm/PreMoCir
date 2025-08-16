import streamlit as st
import pandas as pd
from model_utils import load_model, load_train_data, load_explainer, model_predict, generate_shap_plot as generate_shap_waterfall
from prediction import make_prediction
from sidebar import show_sidebar
from footer import show_footer
from streamlit_modal import Modal
from edmonton_multilingual import edmonton_questionnaire_multilingual
from languages import get_translation, get_available_languages
import shap
import matplotlib.pyplot as plt
import joblib

st.set_page_config(
    page_title="PreMoCir", 
    layout="wide", 
    page_icon="🛌",
    initial_sidebar_state="collapsed"
)

# Inicializar idioma en session state
if 'language' not in st.session_state:
    st.session_state.language = 'es'

# Función helper para traducir
def t(key):
    return get_translation(st.session_state.language, key)

st.title(t("app_title"))
show_sidebar()

import model_utils
explainer = model_utils.load_explainer()
model = joblib.load('model.joblib')
# El modelo cargado es un RandomForestClassifier, no un Pipeline
preprocessor = None  # Si necesitas preprocesar, hazlo manualmente antes de predecir
final_model = model  # Usar el modelo directamente


modal = Modal(t("edmonton_modal_title"), key="edmonton_modal", max_width=600)

col1, col2 = st.columns(2)
with col1:
    htopre = st.number_input(t("hematocrit_label"), 0.0, 100.0, 34.2, 0.5)
    creatinina = st.number_input(t("creatinine_label"), 0.0, 20.0, 1.01, 0.1)
    col1_1, col1_2 = st.columns(2)

    with col1_1:
        edmonton = st.select_slider(t("edmonton_label"), options=list(range(18)), value=7)
    with col1_2:
        if st.button(t("edmonton_button")):
            modal.open()

if modal.is_open():
    with modal.container():
        edmonton_questionnaire_multilingual(st.session_state.language)

with col2:
    fecha_ingreso = st.date_input(t("admission_date"), pd.to_datetime("today"))
    fecha_ingreso = pd.to_datetime(fecha_ingreso)
    fecha_actual = pd.to_datetime("today")
    dias_hospitalizados = (fecha_actual - fecha_ingreso).days
    st.write(f"{t('days_hospitalized')}: {dias_hospitalizados}")
    complicaciones_mace = st.toggle(t("mace_complications"), value=True)
    complicaciones_todas = st.toggle(t("all_complications"), value=True)

# --- Predicción ---
if st.button(t("predict_button"), type="primary"):
    if model is None:
        st.error(t("model_unavailable"))
    else:
        # Crear un diccionario con los datos de entrada
        input_data = {
            'Creatininapre': creatinina,
            'Htopre': htopre,
            'Edmonton': edmonton,
            'Estanciahospitalariacalculada': dias_hospitalizados,
            'ComplicacionesMACE': 1 if complicaciones_mace else 0,
            'ComplicacionesTODAS': 1 if complicaciones_todas else 0,
        }
        
        paciente_df = pd.DataFrame([input_data])
        
        # Datos de la predicción
        try:
            prediction = model.predict(pd.DataFrame([input_data]))[0]
            probabilities = model.predict_proba(pd.DataFrame([input_data]))[0]
            probabilidad_vivir = probabilities[0]*100
            probabilidad_morir = probabilities[1]*100
            
            # Preparar datos para SHAP
            caracteristicas_requeridas = [
                'Creatininapre', 'Estanciahospitalariacalculada', 'Htopre',
                'ComplicacionesMACE', 'ComplicacionesTODAS', 'Edmonton'
            ]
            
            caracteristicas_paciente = {
                'Creatininapre': creatinina,
                'Estanciahospitalariacalculada': dias_hospitalizados,
                'Htopre': htopre,
                'ComplicacionesMACE': 1 if complicaciones_mace else 0,
                'ComplicacionesTODAS': 1 if complicaciones_todas else 0,
                'Edmonton': edmonton
            }
            
            # Verificar que tenemos todas las características
            for caracteristica in caracteristicas_requeridas:
                if caracteristica not in caracteristicas_paciente:
                    raise ValueError(f"{t('missing_feature')}: {caracteristica}")

            # DataFrame para el explainer
            paciente_df = pd.DataFrame([caracteristicas_paciente])
            paciente_df = paciente_df[caracteristicas_requeridas]
            
            st.subheader(t("prediction_results"))

            # Layout en dos columnas para resultados
            col_resultado1, col_resultado2 = st.columns(2)
            with col_resultado1:
                
                # Métrica visual
                vs_avg_text = f" {t('vs_average')}" if probabilidad_morir > 50 else f" {t('below_average')}"
                delta_value = f"{probabilidad_morir - 50:.2f}%" + vs_avg_text if probabilidad_morir > 50 else f"{50 - probabilidad_morir:.2f}%" + vs_avg_text
                
                st.metric(
                    label=t("mortality_risk"), 
                    value=f"{probabilidad_morir:.2f}%",
                    delta=delta_value
                )
            
            with col_resultado2:
                # Generar y mostrar gráfico SHAP con idioma
                shap_fig = generate_shap_waterfall(explainer, paciente_df, probabilidad_morir, st.session_state.language)
                if shap_fig is not None:
                    st.pyplot(shap_fig)
                    plt.close(shap_fig)  # Cerrar figura para liberar memoria
                else:
                    st.error(t("shap_error"))


        except AttributeError:
            st.error(t("model_no_probabilities"))
        except Exception as e:
            st.error(f"{t('prediction_error')}: {str(e)}")

show_footer()