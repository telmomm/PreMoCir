import pandas as pd

def make_prediction(model, input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    return prediction, probabilities
