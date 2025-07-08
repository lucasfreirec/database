from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.atendimento_schema import AtendimentoCreate, AtendimentoResponse
from services.atendimento_service import AtendimentoService
from repositories.atendimento_repository import AtendimentoRepository
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def get_atendimento_service(db: Session = Depends(get_db)):
    return AtendimentoService(AtendimentoRepository(db))

@router.post("/atendimentos", response_model=AtendimentoResponse, status_code=201)
def create_atendimento(atendimento: AtendimentoCreate, service: AtendimentoService = Depends(get_atendimento_service)):
    try:
        return service.create_atendimento(
            descricao=atendimento.descricao, 
            pet_id=atendimento.pet_id, 
            veterinario_id=atendimento.veterinario_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/atendimentos", response_model=List[AtendimentoResponse])
def get_all_atendimentos(service: AtendimentoService = Depends(get_atendimento_service)):
    return service.get_all_atendimentos()