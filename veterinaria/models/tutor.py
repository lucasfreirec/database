from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    telefone = Column(String)
 
    pets = relationship("Pet", back_populates="tutor", cascade="all, delete-orphan") 