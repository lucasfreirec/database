from sqlalchemy import Column, BigInteger, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from db import Base

class Emprestimo(Base):
    __tablename__ = "emprestimo"
    
    id = Column(BigInteger, primary_key=True)
    data_emprestimo = Column(Date)
    previsao_devolucao = Column(Date)
    dias_atraso = Column(Integer)
    
    mat_aluno = Column(BigInteger, ForeignKey("aluno.matricula"))
    
    aluno = relationship("Aluno", back_populates="emprestimos")
    
    exemplares = relationship("Contem", back_populates="emprestimo")