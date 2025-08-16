# edmonton_multilingual.py - Cuestionario de Edmonton multiidioma

import streamlit as st
from languages import get_translation

# Preguntas del cuestionario Edmonton en múltiples idiomas
EDMONTON_QUESTIONS = {
    "es": [
        {
            "text": "¿Qué día de la semana es hoy?", 
            "options": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], 
            "score": lambda x: 0 if x == "correcto" else 1
        },
        {
            "text": "¿Cómo describiría su estado general de salud?", 
            "options": ["Excelente", "Buena", "Regular", "Mala"], 
            "score": lambda x: ["Excelente", "Buena", "Regular", "Mala"].index(x)
        },
        {
            "text": "¿Puede realizar compras de alimentos de forma independiente?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 0 if x == "Sí" else 1
        },
        {
            "text": "¿Tiene alguien que le apoye regularmente?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 0 if x == "Sí" else 1
        },
        {
            "text": "¿Cuántos medicamentos toma diariamente?", 
            "options": ["0-4", "5 o más"], 
            "score": lambda x: 0 if x == "0-4" else 1
        },
        {
            "text": "¿Ha perdido peso en los últimos 6 meses sin intención?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 1 if x == "Sí" else 0
        },
        {
            "text": "¿Se siente deprimido o triste frecuentemente?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 1 if x == "Sí" else 0
        },
        {
            "text": "¿Tiene dificultades para subir escaleras o caminar?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 1 if x == "Sí" else 0
        },
        {
            "text": "¿Puede levantarse de una silla sin usar los brazos?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 0 if x == "Sí" else 1
        },
        {
            "text": "¿Ha tenido pérdidas de orina o heces?", 
            "options": ["Sí", "No"], 
            "score": lambda x: 1 if x == "Sí" else 0
        }
    ],
    "en": [
        {
            "text": "What day of the week is it today?", 
            "options": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 
            "score": lambda x: 0 if x == "correct" else 1
        },
        {
            "text": "How would you describe your general health?", 
            "options": ["Excellent", "Good", "Fair", "Poor"], 
            "score": lambda x: ["Excellent", "Good", "Fair", "Poor"].index(x)
        },
        {
            "text": "Can you shop for groceries independently?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 0 if x == "Yes" else 1
        },
        {
            "text": "Do you have someone who regularly supports you?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 0 if x == "Yes" else 1
        },
        {
            "text": "How many medications do you take daily?", 
            "options": ["0-4", "5 or more"], 
            "score": lambda x: 0 if x == "0-4" else 1
        },
        {
            "text": "Have you lost weight in the last 6 months unintentionally?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 1 if x == "Yes" else 0
        },
        {
            "text": "Do you feel depressed or sad frequently?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 1 if x == "Yes" else 0
        },
        {
            "text": "Do you have difficulty climbing stairs or walking?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 1 if x == "Yes" else 0
        },
        {
            "text": "Can you get up from a chair without using your arms?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 0 if x == "Yes" else 1
        },
        {
            "text": "Have you had losses of urine or feces?", 
            "options": ["Yes", "No"], 
            "score": lambda x: 1 if x == "Yes" else 0
        }
    ]
}

# Textos adicionales para el cuestionario
EDMONTON_TEXTS = {
    "es": {
        "question_label": "Pregunta",
        "next_button": "Siguiente",
        "total_score": "Puntaje total",
        "state_label": "Estado",
        "not_frail": "No frágil o prefrágil",
        "moderate_frail": "Frágil moderado",
        "severe_frail": "Frágil severo"
    },
    "en": {
        "question_label": "Question",
        "next_button": "Next",
        "total_score": "Total Score",
        "state_label": "State",
        "not_frail": "Not frail or pre-frail",
        "moderate_frail": "Moderately frail",
        "severe_frail": "Severely frail"
    }
}

def get_edmonton_text(language_code, key):
    """Obtiene texto específico del cuestionario Edmonton en el idioma dado"""
    try:
        return EDMONTON_TEXTS[language_code][key]
    except KeyError:
        return key

def edmonton_questionnaire_multilingual(language_code='es'):
    """
    Cuestionario de Edmonton multiidioma
    
    Args:
        language_code (str): Código del idioma ('es' o 'en')
    """
    if "edmonton_current" not in st.session_state:
        st.session_state.edmonton_current = 0
    if "edmonton_answers" not in st.session_state:
        st.session_state.edmonton_answers = []
    if "edmonton_result" not in st.session_state:
        st.session_state.edmonton_result = None

    questions = EDMONTON_QUESTIONS[language_code]
    q_index = st.session_state.edmonton_current

    if q_index < len(questions):
        question = questions[q_index]
        st.subheader(f"{get_edmonton_text(language_code, 'question_label')} {q_index + 1}")
        selected = st.radio(question["text"], question["options"], key=f"q_{q_index}")

        if st.button(get_edmonton_text(language_code, "next_button"), key=f"next_{q_index}"):
            st.session_state.edmonton_answers.append(selected)
            st.session_state.edmonton_current += 1
            st.rerun()
    else:
        total_score = sum(
            questions[i]["score"](ans) for i, ans in enumerate(st.session_state.edmonton_answers)
        )
        st.session_state.edmonton_result = total_score

        # Mostrar resumen
        st.markdown(f"### {get_edmonton_text(language_code, 'total_score')}: `{total_score}` / {len(questions)}")

        if total_score <= 4:
            st.info(f"{get_edmonton_text(language_code, 'state_label')}: {get_edmonton_text(language_code, 'not_frail')}")
        elif total_score <= 7:
            st.warning(f"{get_edmonton_text(language_code, 'state_label')}: {get_edmonton_text(language_code, 'moderate_frail')}")
        else:
            st.error(f"{get_edmonton_text(language_code, 'state_label')}: {get_edmonton_text(language_code, 'severe_frail')}")

        # Reset de preguntas pero mantenemos resultado
        st.session_state.edmonton_current = 0
        st.session_state.edmonton_answers = []
