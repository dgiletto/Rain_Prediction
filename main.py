from fastapi import FASTAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import train_and_predict_rainfall

app = FASTAPI()

# Allow CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class WeatherInput(BaseModel):
    temperature: float
    humidity: float
    windSpeed: float
    precipitation: float
    cloudCover: float
    preesure: float

@app.post("/api/post")
def predict(input: WeatherInput):
    result = train_and_predict_rainfall([
        input.temperature,
        input.humidity,
        input.windSpeed,
        input.precipitation,
        input.cloudCover,
        input.pressure
    ])
    return result

