from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import pedidos_all, pedidos_cabecera
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
from src.data_to_excel import convert_to_df, save_to_excel

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

@app.get('/download-excel')
def download_excel():
    df = convert_to_df(pedidos_all,pedidos_cabecera)
    file_path = save_to_excel(df)
    return FileResponse(path=file_path, filename="pedidos_eliminados.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")