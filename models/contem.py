from sqlalchemy import Column, BigInteger, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from db import Base

#Base = declarative_base()

class Contem(Base):
    __tablename__ = "contem"

    id_emp = Column(BigInteger, ForeignKey("emprestimo.id"), primary_key=True)

    tombo_emp = Column(BigInteger, ForeignKey("exemplar.tombo"), primary_key=True)

    data_devol = Column(Date)

    emprestimo = relationship("Emprestimo", back_populates="exemplares")

    exemplar = relationship("Exemplar", back_populates="emprestimos")