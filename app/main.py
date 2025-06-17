
from fastapi import FastAPI
from app.schema import RatingRequest, RatingResponse
from app.model_loader import load_model


from app.utils import preprocess

import logging

app = FastAPI()
model = load_model()

@app.get("/health")
def health():
    return {"status": "Movie rating API is running"}

@app.post("/predict", response_model=RatingResponse)
def predict_rating(data: RatingRequest):
    try:
        features = [data.User_Id, data.Movie_Name, data.Genre]
        processed = preprocess(features)
        prediction = model.predict(processed)[0]
        return {"predicted_rating": round(float(prediction), 2)}
    except Exception as e:
        logging.exception("Prediction error")
        return {"predicted_rating": -1.0}
