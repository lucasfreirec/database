from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    cidade = Column(String, nullable=False)

    veterinarios = relationship("Veterinario", back_populates="clinica", cascade="all, delete-orphan")