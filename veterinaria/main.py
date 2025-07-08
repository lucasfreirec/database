from fastapi import FastAPI
from api import clinica_router, veterinario_router, tutor_router, pet_router, atendimento_router
from database import engine, Base

app = FastAPI(
    title="Sistema de Gerenciamento de Clínicas Veterinárias",
    description="API para gerenciar clínicas, veterinários, tutores, pets e atendimentos.",
    version="1.0.0"
)

app.include_router(clinica_router.router, prefix="/api/v1", tags=["Clínicas"])
app.include_router(veterinario_router.router, prefix="/api/v1", tags=["Veterinários"])
app.include_router(tutor_router.router, prefix="/api/v1", tags=["Tutores"])
app.include_router(pet_router.router, prefix="/api/v1", tags=["Pets"])
app.include_router(atendimento_router.router, prefix="/api/v1", tags=["Atendimentos"])


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Clínica Veterinária"}