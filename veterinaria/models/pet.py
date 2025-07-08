from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(Integer)

    tutor_id = Column(Integer, ForeignKey("tutores.id")) # 

    tutor = relationship("Tutor", back_populates="pets")

    atendimentos = relationship("Atendimento", back_populates="pet", cascade="all, delete-orphan")