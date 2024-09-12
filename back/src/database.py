import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

USER = dotenv_values('.env')['USER']
PASSWORD = dotenv_values('.env')['PASSWORD'] 
DB_NAME = dotenv_values('.env')['DB_NAME']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@localhost/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
# se usa sqlalchemy para crear una query que tenga todos campos de la tabla tb_pedidos_eliminados
query_pedidos_eliminados = sa.select(sa.text('*')).select_from(sa.text('tb_pedidos_eliminados'))
pedidos_cabecera= session.execute(query_pedidos_eliminados).keys()#estas son las cabeceras pero no fueron utilizadas al final
pedidos_all = session.execute(query_pedidos_eliminados).all()# variable que contiene todos los campos de la tabla tb_pedidos_eliminados
