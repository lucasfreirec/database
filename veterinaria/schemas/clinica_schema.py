from pydantic import BaseModel
from typing import List
from .veterinario_schema import VeterinarioResponse

class ClinicaCreate(BaseModel):
    nome: str
    cidade: str

class ClinicaResponse(ClinicaCreate):
    id: int
    veterinarios: List[VeterinarioResponse] = []

    class Config:
        orm_mode = True