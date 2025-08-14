from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("ml_model/model.joblib")

# Define request body schema
class Transaction(BaseModel):
    amount: float
    time: float
    v1: float  # PCA features (from dataset)
    v2: float
    # ... (add all 28 PCA features)

# Initialize FastAPI
app = FastAPI(title="Fraud Detection API")

# Health check endpoint
@app.get("/")
def home():
    return {"status": "API is running 🚀"}

# Fraud prediction endpoint
@app.post("/predict")
def predict(transaction: Transaction):
    # Convert transaction data to numpy array
    features = np.array([[
        transaction.time,
        transaction.amount,
        transaction.v1,
        transaction.v2,
        # ... (all features)
    ]])

    # Predict fraud probability
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "fraud_prediction": int(prediction),
        "fraud_probability": float(probability),
    }