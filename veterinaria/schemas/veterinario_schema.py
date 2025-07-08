from pydantic import BaseModel
from typing import List
from .atendimento_schema import AtendimentoResponse

class VeterinarioBase(BaseModel):
    nome: str
    especialidade: str

class VeterinarioCreate(VeterinarioBase):
    clinica_id: int

class VeterinarioResponse(VeterinarioBase):
    id: int
    clinica_id: int
    atendimentos: List[AtendimentoResponse] = []

    class Config:
        orm_mode = True