from repositories.clinica_repository import ClinicaRepository
from models.clinica import Clinica
from models.veterinario import Veterinario

class ClinicaService:
    def __init__(self, clinica_repository: ClinicaRepository):
        """
        Inicializa o serviço com uma instância do repositório de clínicas.
        """
        self.clinica_repository = clinica_repository

    def create_clinica(self, nome: str, cidade: str) -> Clinica:
        """
        Lógica de negócio para criar uma nova clínica.
        """
        clinicas_existentes = self.clinica_repository.get_all()
        for c in clinicas_existentes:
            if c.nome == nome and c.cidade == cidade:
                raise ValueError("Uma clínica com este nome já existe nesta cidade.")
        
        return self.clinica_repository.create(nome=nome, cidade=cidade)

    def get_all_clinicas(self) -> list[Clinica]:
        """
        Retorna todas as clínicas.
        """
        return self.clinica_repository.get_all()

    def get_clinica_by_id(self, id_clinica: int) -> Clinica | None:
        """
        Busca uma clínica específica pelo seu ID.
        """
        return self.clinica_repository.get_by_id(id_clinica)

    def get_veterinarios_of_clinica(self, id_clinica: int) -> list[Veterinario] | None:
        """
        Busca uma clínica e retorna a lista de veterinários associados.
        Este método atende diretamente ao endpoint: GET /clinicas/{id}/veterinarios 
        """
        clinica = self.clinica_repository.get_by_id(id_clinica)
        if clinica:
            return clinica.veterinarios
        return None

    def delete_clinica(self, id_clinica: int) -> bool:
        """
        Deleta uma clínica.
        """
        return self.clinica_repository.delete(id_clinica)
        
    def update_clinica(self, id_clinica: int, nome: str = None, cidade: str = None) -> Clinica | None:
        """
        Atualiza os dados de uma clínica.
        """
        return self.clinica_repository.update(id_clinica, nome, cidade)