from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from db import Base

class Exemplar(Base):
    __tablename__ = "exemplar"
    
    tombo = Column(BigInteger, primary_key=True)
    
    codigo_livro = Column(BigInteger, ForeignKey("livro.codigo"), nullable=False)
    
    livro = relationship("Livro", back_populates="exemplares")
    
    emprestimos = relationship("Contem", back_populates="exemplar")