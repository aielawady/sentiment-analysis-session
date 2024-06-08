from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, confloat

from sntm_webapp.core import sum2nums
from sntm_webapp.sentiment_analysis import predict, load_model

app = FastAPI()

@app.get("/")
def home():
    return "Hello"

@app.on_event("startup")
def startup_event():
    load_model()

@app.get("/sum/{a}/{b}")
def sum2(a: float, b: float, c: str="sum"):
    if c == "mul":
        return a * b
    else:
        return sum2nums(a, b)
    
class RequestModel(BaseModel):
    text: str
    threshold: confloat(gt=0, le=1)

class ResponseModel(BaseModel):
    classification: Literal["negative", "positive"]
    score: float

@app.post("/inference") # , response_model=ResponseModel)
def inference(data: RequestModel):
    prediction = predict(data.text)
    return prediction
    return {"classification": "negative", "score": 0.5}