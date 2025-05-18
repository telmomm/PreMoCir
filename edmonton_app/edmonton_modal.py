import streamlit as st

questions = [
    {"text": "¿Qué día de la semana es hoy?", "options": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], "score": lambda x: 0 if x == "correcto" else 1},
    {"text": "¿Cómo describiría su estado general de salud?", "options": ["Excelente", "Buena", "Regular", "Mala"], "score": lambda x: ["Excelente", "Buena", "Regular", "Mala"].index(x)},
    {"text": "¿Puede realizar compras de alimentos de forma independiente?", "options": ["Sí", "No"], "score": lambda x: 0 if x == "Sí" else 1},
    {"text": "¿Tiene alguien que le apoye regularmente?", "options": ["Sí", "No"], "score": lambda x: 0 if x == "Sí" else 1},
    {"text": "¿Cuántos medicamentos toma diariamente?", "options": ["0-4", "5 o más"], "score": lambda x: 0 if x == "0-4" else 1},
    {"text": "¿Ha perdido peso en los últimos 6 meses sin intención?", "options": ["Sí", "No"], "score": lambda x: 1 if x == "Sí" else 0},
    {"text": "¿Se siente deprimido o triste frecuentemente?", "options": ["Sí", "No"], "score": lambda x: 1 if x == "Sí" else 0},
    {"text": "¿Tiene dificultades para subir escaleras o caminar?", "options": ["Sí", "No"], "score": lambda x: 1 if x == "Sí" else 0},
    {"text": "¿Puede levantarse de una silla sin usar los brazos?", "options": ["Sí", "No"], "score": lambda x: 0 if x == "Sí" else 1},
    {"text": "¿Ha tenido pérdidas de orina o heces?", "options": ["Sí", "No"], "score": lambda x: 1 if x == "Sí" else 0}
]

def edmonton_questionnaire():
    if "edmonton_current" not in st.session_state:
        st.session_state.edmonton_current = 0
    if "edmonton_answers" not in st.session_state:
        st.session_state.edmonton_answers = []
    if "edmonton_result" not in st.session_state:
        st.session_state.edmonton_result = None

    q_index = st.session_state.edmonton_current

    if q_index < len(questions):
        question = questions[q_index]
        st.subheader(f"Pregunta {q_index + 1}")
        selected = st.radio(question["text"], question["options"], key=f"q_{q_index}")

        if st.button("Siguiente", key=f"next_{q_index}"):
            st.session_state.edmonton_answers.append(selected)
            st.session_state.edmonton_current += 1
            st.rerun()
    else:
        total_score = sum(
            questions[i]["score"](ans) for i, ans in enumerate(st.session_state.edmonton_answers)
        )
        st.session_state.edmonton_result = total_score

        # Mostrar resumen
        st.markdown(f"### Puntaje total: `{total_score}` / {len(questions)}")

        if total_score <= 4:
            st.info("Estado: No frágil o prefrágil")
        elif total_score <= 7:
            st.warning("Estado: Frágil moderado")
        else:
            st.error("Estado: Frágil severo")

        # Reset de preguntas pero mantenemos resultado
        st.session_state.edmonton_current = 0
        st.session_state.edmonton_answers = []
