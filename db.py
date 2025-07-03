import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# O endereço do banco de dados agora usa o nome do serviço 'db' do docker-compose
# Em vez de 'localhost'
DATABASE_URL = "postgresql+psycopg2://meu_usuario:minha_senha@db/biblioteca_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()