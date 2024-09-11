from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models_01 import t_tb_pedidos_eliminados

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Akira91@localhost/enviexpress"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()

res =  session.query(t_tb_pedidos_eliminados).all()


