from pydantic import BaseModel
from typing import List, Optional
from .atendimento_schema import AtendimentoResponse

class PetBase(BaseModel):
    nome: str
    especie: str
    idade: Optional[int] = None

class PetCreate(PetBase):
    tutor_id: int

class PetResponse(PetBase):
    id: int
    tutor_id: int
    atendimentos: List[AtendimentoResponse] = []

    class Config:
        orm_mode = True