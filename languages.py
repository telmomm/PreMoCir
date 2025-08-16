# languages.py - Sistema de internacionalización para PreMoCir

LANGUAGES = {
    "es": {
        "name": "Español",
        "flag": "🇪🇸",
        "translations": {
            # Título y navegación
            "app_title": "Predicción de la Mortalidad en Cirugía Cardíaca",
            "language_selector": "Idioma",
            
            # Formulario de entrada
            "hematocrit_label": "Hematocrito preoperatorio (%)",
            "creatinine_label": "Creatinina preoperatoria (mg/dL)",
            "edmonton_label": "Fragilidad Edmonton",
            "edmonton_button": "Abrir evaluación Edmonton",
            "admission_date": "Fecha de ingreso",
            "days_hospitalized": "Días hospitalizado",
            "mace_complications": "Complicaciones MACE",
            "all_complications": "Complicaciones Todas",
            
            # Botones y acciones
            "predict_button": "🔄 Realizar predicción",
            "prediction_results": "🎯 Resultado de la Predicción",
            "shap_explanation": "📊 Explicación de la Predicción (SHAP)",
            "shap_description": "Esta gráfica muestra qué variables contribuyeron más a la predicción:",
            
            # Resultados
            "mortality_risk": "Riesgo de Mortalidad",
            "mortality_probability": "Probabilidad de Mortalidad",
            "survival_probability": "Probabilidad de Supervivencia",
            "vs_average": "vs promedio",
            "below_average": "bajo promedio",
            
            # Errores y mensajes
            "model_unavailable": "Modelo no disponible",
            "model_no_probabilities": "El modelo no soporta la predicción de probabilidades.",
            "prediction_error": "Error en la predicción",
            "shap_error": "No se pudo generar el gráfico de explicación SHAP",
            "missing_feature": "Falta la característica requerida",
            
            # Modal Edmonton
            "edmonton_modal_title": "Escala de Fragilidad de Edmonton",
            
            # Sidebar
            "sidebar_about_title": "❓ ¿Qué es PreMoCir?",
            "sidebar_about_content": """**PreMoCir** (Predicción de Mortalidad en Cirugía Cardíaca) es una herramienta de ayuda a la decisión clínica que estima la probabilidad de mortalidad de un paciente sometido a cirugía cardíaca, basándose en variables clínicas preoperatorias y datos de evolución hospitalaria. Utiliza modelos de aprendizaje automático desarrollados a partir de datos reales.""",
            
            "sidebar_manual_title": "📘 Manual de Usuario",
            "sidebar_manual_content": """### 1. Introducción de datos
- Introduce los siguientes valores en los campos visibles:
    - **Hematocrito preoperatorio (%)**
    - **Creatinina preoperatoria (mg/dL)**
    - **Fragilidad Edmonton (0–17)**
    - **Fecha de ingreso hospitalario**
    - **Complicaciones MACE** (toggle): si el paciente ha tenido eventos cardiovasculares graves.
    - **Complicaciones TODAS** (toggle): si ha tenido cualquier tipo de complicación médica relevante.

### 2. Realizar predicción
- Pulsa el botón **🔄 Realizar predicción**.
- La aplicación mostrará la **probabilidad de mortalidad estimada** en porcentaje.""",

            "sidebar_warnings_title": "⚠️ Advertencias",
            "sidebar_warnings_content": """- Esta aplicación es **una herramienta de apoyo** y **no sustituye el criterio clínico profesional**.
- Los datos procesados **no se almacenan ni se transmiten**, garantizando privacidad y anonimato.
- El modelo es probabilístico y puede estar sujeto a errores inherentes al aprendizaje automático.
- Los resultados deben interpretarse en contexto clínico.""",

            "sidebar_github_button": "🔗 GitHub",
            
            # Footer
            "footer_developed_by": "Desarrollado por",
            
            # Variables para SHAP (nombres legibles)
            "var_creatinine": "Creatinina",
            "var_stay_length": "Días Hospitalización",
            "var_hematocrit": "Hematocrito",
            "var_mace": "MACE",
            "var_complications": "Complicaciones",
            "var_edmonton": "Escala Edmonton"
        }
    },
    "en": {
        "name": "English",
        "flag": "🇺🇸",
        "translations": {
            # Título y navegación
            "app_title": "Cardiac Surgery Mortality Prediction",
            "language_selector": "Language",
            
            # Formulario de entrada
            "hematocrit_label": "Preoperative Hematocrit (%)",
            "creatinine_label": "Preoperative Creatinine (mg/dL)",
            "edmonton_label": "Edmonton Frailty",
            "edmonton_button": "Open Edmonton Assessment",
            "admission_date": "Admission Date",
            "days_hospitalized": "Days Hospitalized",
            "mace_complications": "MACE Complications",
            "all_complications": "All Complications",
            
            # Botones y acciones
            "predict_button": "🔄 Make Prediction",
            "prediction_results": "🎯 Prediction Results",
            "shap_explanation": "📊 Prediction Explanation (SHAP)",
            "shap_description": "This chart shows which variables contributed most to the prediction:",
            
            # Resultados
            "mortality_risk": "Mortality Risk",
            "mortality_probability": "Mortality Probability",
            "survival_probability": "Survival Probability",
            "vs_average": "vs average",
            "below_average": "below average",
            
            # Errores y mensajes
            "model_unavailable": "Model unavailable",
            "model_no_probabilities": "The model does not support probability prediction.",
            "prediction_error": "Prediction error",
            "shap_error": "Could not generate SHAP explanation chart",
            "missing_feature": "Missing required feature",
            
            # Modal Edmonton
            "edmonton_modal_title": "Edmonton Frailty Scale",
            
            # Sidebar
            "sidebar_about_title": "❓ What is PreMoCir?",
            "sidebar_about_content": """**PreMoCir** (Cardiac Surgery Mortality Prediction) is a clinical decision support tool that estimates the mortality probability of a patient undergoing cardiac surgery, based on preoperative clinical variables and hospital evolution data. It uses machine learning models developed from real data.""",
            
            "sidebar_manual_title": "📘 User Manual",
            "sidebar_manual_content": """### 1. Data Input
- Enter the following values in the visible fields:
    - **Preoperative Hematocrit (%)**
    - **Preoperative Creatinine (mg/dL)**
    - **Edmonton Frailty (0–17)**
    - **Hospital admission date**
    - **MACE Complications** (toggle): if the patient has had severe cardiovascular events.
    - **All Complications** (toggle): if they have had any type of relevant medical complication.

### 2. Make Prediction
- Click the **🔄 Make Prediction** button.
- The application will show the **estimated mortality probability** as a percentage.""",

            "sidebar_warnings_title": "⚠️ Warnings",
            "sidebar_warnings_content": """- This application is **a support tool** and **does not replace professional clinical judgment**.
- Processed data **is not stored or transmitted**, ensuring privacy and anonymity.
- The model is probabilistic and may be subject to errors inherent to machine learning.
- Results should be interpreted in clinical context.""",

            "sidebar_github_button": "🔗 GitHub",
            
            # Footer
            "footer_developed_by": "Developed by",
            
            # Variables para SHAP (nombres legibles)
            "var_creatinine": "Creatinine",
            "var_stay_length": "Hospital Stay",
            "var_hematocrit": "Hematocrit",
            "var_mace": "MACE",
            "var_complications": "Complications",
            "var_edmonton": "Edmonton Scale"
        }
    }
}

def get_translation(language_code, key):
    """
    Obtiene la traducción para una clave específica en el idioma dado.
    
    Args:
        language_code (str): Código del idioma ('es' o 'en')
        key (str): Clave de la traducción
    
    Returns:
        str: Texto traducido o la clave si no se encuentra la traducción
    """
    try:
        return LANGUAGES[language_code]["translations"][key]
    except KeyError:
        # Si no se encuentra la traducción, devolver la clave como fallback
        return key

def get_available_languages():
    """
    Devuelve una lista de idiomas disponibles.
    
    Returns:
        list: Lista de tuplas (código, nombre, bandera)
    """
    return [(code, lang["name"], lang["flag"]) for code, lang in LANGUAGES.items()]

def get_variable_names(language_code):
    """
    Devuelve el diccionario de nombres de variables para SHAP en el idioma especificado.
    
    Args:
        language_code (str): Código del idioma
    
    Returns:
        dict: Diccionario con nombres de variables traducidos
    """
    t = LANGUAGES[language_code]["translations"]
    return {
        'Creatininapre': t["var_creatinine"],
        'Estanciahospitalariacalculada': t["var_stay_length"],
        'Htopre': t["var_hematocrit"],
        'ComplicacionesMACE': t["var_mace"],
        'ComplicacionesTODAS': t["var_complications"],
        'Edmonton': t["var_edmonton"]
    }
