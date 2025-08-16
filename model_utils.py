import joblib
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt

@st.cache_resource
def load_model(path='model.joblib'):
    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None

def load_train_data(path='train_dataset.joblib'):
    """
    Carga datos de entrenamiento para usar como background en SHAP
    """
    try:
        return joblib.load(path)
      
    except Exception as e:
        st.warning(f"No se pudieron cargar datos de entrenamiento para SHAP: {e}")
        return None

def load_explainer():
    
    """Cargar explainer de SHAP, crearlo si no existe o hay incompatibilidad"""
    try:
        explainer = joblib.load('explainer.joblib')
        return explainer
    except (FileNotFoundError, Exception) as e:
        st.warning(f"No se pudo cargar el explainer guardado: {str(e)}")
        return None
    
def model_predict(X):
    """Función para hacer predicciones con el modelo"""
    model = load_model()
    if model is None:
        return None

    # Si el modelo es un Pipeline, usa el preprocesador y el regressor
    if hasattr(model, 'named_steps'):
        preprocessor = model.named_steps.get('preprocessor', None)
        final_model = model.named_steps.get('regressor', model)
        if preprocessor is not None:
            X_transformed = preprocessor.transform(X)
            return final_model.predict_proba(X_transformed)
        else:
            return final_model.predict_proba(X)
    else:
        # Si el modelo es un estimador directo (RandomForest, etc.)
        return model.predict_proba(X)
    
def generate_shap_plot(explainer, paciente_df, probabilidad_morir, language_code='es'):
    """
    Genera un gráfico SHAP waterfall para explicar la predicción
    
    Args:
        explainer: Explainer de SHAP cargado
        paciente_df: DataFrame con los datos del paciente
        probabilidad_morir: Probabilidad de mortalidad calculada
        language_code: Código del idioma ('es' o 'en')
    
    Returns:
        fig: Figura de matplotlib con el gráfico SHAP
    """
    try:
        from languages import get_variable_names, get_translation
        
        # Obtener nombres de variables en el idioma especificado
        nombre_variables = get_variable_names(language_code)
        
        # Generar valores SHAP
        shap_values_paciente = explainer(paciente_df)
        
        # Renombrar columnas para visualización
        paciente_df_viz = paciente_df.rename(columns=nombre_variables)
        feature_names_viz = list(paciente_df_viz.columns)
        
        # Crear la figura de SHAP
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Generar gráfico waterfall
        shap.plots._waterfall.waterfall_legacy(
            expected_value=shap_values_paciente.base_values[0, 1],
            shap_values=shap_values_paciente.values[0, :, 1],
            feature_names=feature_names_viz,
            features=paciente_df_viz.iloc[0].values
        )
        
        # Título traducido
        title_text = f'{get_translation(language_code, "shap_explanation")} - {get_translation(language_code, "mortality_probability")}: {probabilidad_morir:.2f}%'
        plt.title(title_text, fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        return fig
        
    except Exception as e:
        st.error(f"Error al generar gráfico SHAP: {str(e)}")
        return None