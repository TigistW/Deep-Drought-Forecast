from fastapi import FastAPI
from app.models.predictor import load_model, run_inference
from app.models.explainer import explain_prediction
from app.services.gee_fetcher import get_latest_data
import json

app = FastAPI(title="Drought Prediction API")

# Load model once
model = load_model("model/cnn_lstm_model.pt")

@app.get("/")
def root():
    return {"msg": "Drought Prediction API running!"}

@app.get("/predict")
def predict():
    # Load pre-fetched SPEI data (last 24x12 values)
    with open("app/data/latest_spei.json", "r") as f:
        data = json.load(f)

    prediction = run_inference(model, data)
    explanation = explain_prediction(model, data)

    return {
        "input_data": data,
        "prediction": prediction,
        "shap_values": explanation
    }
