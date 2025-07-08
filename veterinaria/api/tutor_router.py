from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.tutor_schema import TutorCreate, TutorResponse
from schemas.pet_schema import PetResponse
from services.tutor_service import TutorService
from repositories.tutor_repository import TutorRepository
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_tutor_service(db: Session = Depends(get_db)):
    return TutorService(TutorRepository(db))

@router.post("/tutores", response_model=TutorResponse, status_code=201)
def create_tutor(tutor: TutorCreate, service: TutorService = Depends(get_tutor_service)):
    return service.create_tutor(nome=tutor.nome, telefone=tutor.telefone)

@router.get("/tutores/{id}/pets", response_model=List[PetResponse])
def get_pets_of_tutor(id: int, service: TutorService = Depends(get_tutor_service)):
    pets = service.get_pets_of_tutor(id)
    if pets is None:
        raise HTTPException(status_code=404, detail="Tutor não encontrado")
    return pets