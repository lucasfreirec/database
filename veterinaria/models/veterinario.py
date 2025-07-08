from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    especialidade = Column(String, nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"))

    clinica = relationship("Clinica", back_populates="veterinarios")
    atendimentos = relationship("Atendimento", back_populates="veterinario", cascade="all, delete-orphan")