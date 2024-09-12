import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

USER = dotenv_values('.env')['USER']
PASSWORD = dotenv_values('.env')['PASSWORD'] 
DB_NAME = dotenv_values('.env')['DB_NAME']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@localhost/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
query_pedidos_eliminados = sa.select(sa.text('*')).select_from(sa.text('tb_pedidos_eliminados'))
pedidos_cabecera= session.execute(query_pedidos_eliminados).keys()
pedidos_all = session.execute(query_pedidos_eliminados).all()
