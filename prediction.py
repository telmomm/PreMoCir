import pandas as pd
import shap
import matplotlib.pyplot as plt
import streamlit as st

def make_prediction(model, input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    return prediction, probabilities

def generate_shap_plot(model, train_data):
    """
    Genera una gráfica SHAP para explicar la predicción específica
    Funciona con pipelines de scikit-learn
    """
    model = model_predict_proba(model, train_data)
    explainer = shap.Explainer(model, train_data)

   
        
        # Función wrapper para el pipeline
def model_predict_proba(model, X):
    preprocessor = model.named_steps['preprocessor']
    final_model = model.named_steps['regressor']

    X_transformed = preprocessor.transform(X)
    return final_model.predict_proba(X_transformed)
        
    


