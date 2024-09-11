from fastapi import FastAPI
from src.database import res
from fastapi.encoders import jsonable_encoder
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def leer_items():
    json_items  = jsonable_encoder(res)
    return json_items