from pydantic import BaseModel
from datetime import datetime

class PetMinimalResponse(BaseModel):
    id: int
    nome: str
    class Config: orm_mode = True

class VetMinimalResponse(BaseModel):
    id: int
    nome: str
    class Config: orm_mode = True

class AtendimentoCreate(BaseModel):
    descricao: str
    pet_id: int
    veterinario_id: int

class AtendimentoResponse(BaseModel):
    id: int
    data: datetime
    descricao: str
    pet: PetMinimalResponse
    veterinario: VetMinimalResponse
    
    class Config:
        orm_mode = True