from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.veterinario_schema import VeterinarioCreate, VeterinarioResponse
from services.veterinario_service import VeterinarioService
from repositories.veterinario_repository import VeterinarioRepository
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_veterinario_service(db: Session = Depends(get_db)):
    return VeterinarioService(VeterinarioRepository(db))

@router.post("/veterinarios", response_model=VeterinarioResponse, status_code=201)
def create_veterinario(
    veterinario: VeterinarioCreate,
    service: VeterinarioService = Depends(get_veterinario_service)
):
    """
    Cadastra um novo veterinário.
    """
    try:
        return service.create_veterinario(
            nome=veterinario.nome,
            especialidade=veterinario.especialidade,
            clinica_id=veterinario.clinica_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/veterinarios", response_model=List[VeterinarioResponse])
def get_all_veterinarios(service: VeterinarioService = Depends(get_veterinario_service)):
    """
    Lista todos os veterinários.
    """
    return service.get_all_veterinarios()