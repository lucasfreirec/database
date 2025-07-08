from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.pet_schema import PetCreate, PetResponse
from services.pet_service import PetService
from repositories.pet_repository import PetRepository
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def get_pet_service(db: Session = Depends(get_db)):
    return PetService(PetRepository(db))

@router.post("/pets", response_model=PetResponse, status_code=201)
def create_pet(pet: PetCreate, service: PetService = Depends(get_pet_service)):
    try:
        return service.create_pet(nome=pet.nome, especie=pet.especie, idade=pet.idade, tutor_id=pet.tutor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/pets", response_model=List[PetResponse])
def get_all_pets(service: PetService = Depends(get_pet_service)):
    return service.get_all_pets()