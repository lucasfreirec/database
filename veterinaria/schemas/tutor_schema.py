from pydantic import BaseModel
from typing import List, Optional
from .pet_schema import PetResponse 

class TutorBase(BaseModel):
    nome: str
    telefone: Optional[str] = None

class TutorCreate(TutorBase):
    pass

class TutorResponse(TutorBase):
    id: int
    pets: List[PetResponse] = []

    class Config:
        orm_mode = True