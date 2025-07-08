from repositories.tutor_repository import TutorRepository
from models.tutor import Tutor
from models.pet import Pet

class TutorService:
    def __init__(self, tutor_repository: TutorRepository):
        """
        Inicializa o serviço com uma instância do repositório de tutores.
        """
        self.tutor_repository = tutor_repository

    def create_tutor(self, nome: str, telefone: str) -> Tutor:
        """
        Cria um novo tutor.
        Este método atende ao endpoint: POST /tutores [cite: 164]
        """
        return self.tutor_repository.create(nome=nome, telefone=telefone)

    def get_all_tutores(self) -> list[Tutor]:
        """
        Retorna todos os tutores.
        """
        return self.tutor_repository.get_all()

    def get_tutor_by_id(self, id_tutor: int) -> Tutor | None:
        """
        Busca um tutor pelo seu ID.
        """
        return self.tutor_repository.get_by_id(id_tutor)

    def get_pets_of_tutor(self, id_tutor: int) -> list[Pet] | None:
        """
        Busca um tutor e retorna a lista de pets associados.
        Este método atende diretamente ao endpoint: GET /tutores/{id}/pets 
        """
        tutor = self.tutor_repository.get_by_id(id_tutor)
        if tutor:
            return tutor.pets
        return None

    def delete_tutor(self, id_tutor: int) -> bool:
        """
        Deleta um tutor.
        """
        return self.tutor_repository.delete(id_tutor)

    def update_tutor(self, id_tutor: int, nome: str = None, telefone: str = None) -> Tutor | None:
        """
        Atualiza os dados de um tutor.
        """
        return self.tutor_repository.update(id_tutor, nome, telefone)