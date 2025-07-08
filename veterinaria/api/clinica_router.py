from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.clinica_schema import ClinicaCreate, ClinicaResponse
from schemas.veterinario_schema import VeterinarioResponse
from services.clinica_service import ClinicaService
from repositories.clinica_repository import ClinicaRepository
from database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_clinica_service(db: Session = Depends(get_db)):
    return ClinicaService(ClinicaRepository(db))

@router.post("/clinicas", response_model=ClinicaResponse, status_code=201)
def create_clinica(
    clinica: ClinicaCreate, 
    service: ClinicaService = Depends(get_clinica_service)
):
    """
    Cria uma nova clínica.
    """
    try:
        nova_clinica = service.create_clinica(nome=clinica.nome, cidade=clinica.cidade)
        return nova_clinica
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/clinicas", response_model=List[ClinicaResponse])
def get_all_clinicas(service: ClinicaService = Depends(get_clinica_service)):
    """
    [cite_start]Lista todas as clínicas. [cite: 1]
    """
    return service.get_all_clinicas()

@router.get("/clinicas/{id}", response_model=ClinicaResponse)
def get_clinica_by_id(id: int, service: ClinicaService = Depends(get_clinica_service)):
    """
    [cite_start]Busca uma clínica específica pelo ID. [cite: 1]
    """
    clinica = service.get_clinica_by_id(id)
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return clinica

@router.get("/clinicas/{id}/veterinarios", response_model=List[VeterinarioResponse])
def get_veterinarios_of_clinica(id: int, service: ClinicaService = Depends(get_clinica_service)):
    """
    [cite_start]Lista todos os veterinários de uma clínica específica. [cite: 1]
    """
    veterinarios = service.get_veterinarios_of_clinica(id)
    if veterinarios is None:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return veterinarios