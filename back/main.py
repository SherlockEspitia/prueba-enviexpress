from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import pedidos_all
from fastapi.encoders import jsonable_encoder
app = FastAPI()

origins = ['*']
# Se agregan cabeceras para el envio cruzados de datos 'CORS'
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

#Endpoint que envia todos los campos de la tabla tb_pedidos eliminados como un json
@app.get("/items/")
async def leer_items():
    json_items  = jsonable_encoder(pedidos_all)
    return json_items