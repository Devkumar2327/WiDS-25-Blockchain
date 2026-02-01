import joblib
import pandas as pd

model = joblib.load("xgb_fraud_model.pkl")

def predict_wallet(features: dict):
    df = pd.DataFrame([features])
    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])
    return prediction, probability
