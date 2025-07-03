from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import declarative_base, relationship
from db import Base

class Aluno(Base):
    __tablename__ = "aluno"

    matricula = Column(BigInteger, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    curso = Column(String, nullable=False)

    emprestimos = relationship("Emprestimo", back_populates="aluno")