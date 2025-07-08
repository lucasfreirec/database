# services/pet_service.py

from repositories.pet_repository import PetRepository
from models.pet import Pet
from models.atendimento import Atendimento

class PetService:
    def __init__(self, pet_repository: PetRepository):
        """
        Inicializa o serviço com uma instância do repositório de pets.
        """
        self.pet_repository = pet_repository

    def create_pet(self, nome: str, especie: str, idade: int, tutor_id: int) -> Pet:
        """
        Cria um novo pet.
        Este método atende ao endpoint: POST /pets 
        """
        return self.pet_repository.create(
            nome=nome,
            especie=especie,
            idade=idade,
            tutor_id=tutor_id
        )

    def get_all_pets(self) -> list[Pet]:
        """
        Retorna todos os pets.
        Este método atende ao endpoint: GET /pets
        """
        return self.pet_repository.get_all()

    def get_pet_by_id(self, id_pet: int) -> Pet | None:
        """
        Busca um pet pelo seu ID.
        """
        return self.pet_repository.get_by_id(id_pet)

    def get_atendimentos_of_pet(self, id_pet: int) -> list[Atendimento] | None:
        """
        Busca um pet e retorna sua lista de atendimentos.
        Este método atende diretamente ao endpoint: GET /pets/{id}/atendimentos 
        """
        pet = self.pet_repository.get_by_id(id_pet)
        if pet:
            return pet.atendimentos
        return None

    def delete_pet(self, id_pet: int) -> bool:
        """
        Deleta um pet.
        """
        return self.pet_repository.delete(id_pet)

    def update_pet(self, id_pet: int, nome: str = None, especie: str = None, idade: int = None, tutor_id: int = None) -> Pet | None:
        """
        Atualiza os dados de um pet.
        """
        return self.pet_repository.update(id_pet, nome, especie, idade, tutor_id)