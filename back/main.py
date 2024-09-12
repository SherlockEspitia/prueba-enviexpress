from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import pedidos_all,pedidos_cabecera
from fastapi.encoders import jsonable_encoder
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def leer_items():
    json_items  = jsonable_encoder(pedidos_all)
    return json_items