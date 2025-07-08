from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, server_default=func.now()) 
    descricao = Column(String, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))

    pet = relationship("Pet", back_populates="atendimentos")
    veterinario = relationship("Veterinario", back_populates="atendimentos")