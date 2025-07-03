from sqlalchemy import Column, String, Integer, BigInteger 
from sqlalchemy.orm import declarative_base, relationship
from db import Base

#Base = declarative_base()

class Livro(Base):
    __tablename__ = "livro"
    
    codigo = Column(BigInteger, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    ano_pub = Column(Integer, nullable=False)

    exemplares = relationship("Exemplar", back_populates="livro")