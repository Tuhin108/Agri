import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "best_price_forecast_model.pkl")

model = joblib.load(MODEL_PATH)

def get_forecast():
    forecast = model.get_forecast(steps=12).predicted_mean
    return forecast.tolist()
