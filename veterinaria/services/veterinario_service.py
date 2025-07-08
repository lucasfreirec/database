from repositories.veterinario_repository import VeterinarioRepository
from models.veterinario import Veterinario
from models.atendimento import Atendimento

class VeterinarioService:
    def __init__(self, veterinario_repository: VeterinarioRepository):
        """
        Inicializa o serviço com uma instância do repositório de veterinários.
        """
        self.veterinario_repository = veterinario_repository

    def create_veterinario(self, nome: str, especialidade: str, clinica_id: int) -> Veterinario:
        """
        Cria um novo veterinário.
        Este método atende ao endpoint: POST /veterinarios [c
        """
        return self.veterinario_repository.create(
            nome=nome,
            especialidade=especialidade,
            clinica_id=clinica_id
        )

    def get_all_veterinarios(self) -> list[Veterinario]:
        """
        Retorna todos os veterinários.
        Este método atende ao endpoint: GET /veterinarios [cite: 71]
        """
        return self.veterinario_repository.get_all()

    def get_veterinario_by_id(self, id_veterinario: int) -> Veterinario | None:
        """
        Busca um veterinário pelo seu ID.
        """
        return self.veterinario_repository.get_by_id(id_veterinario)

    def get_atendimentos_of_veterinario(self, id_veterinario: int) -> list[Atendimento] | None:
        """
        Busca um veterinário e retorna sua lista de atendimentos.
        Este método atende diretamente ao endpoint: GET /veterinarios/{id}/atendimentos [cite: 82]
        """
        veterinario = self.veterinario_repository.get_by_id(id_veterinario)
        if veterinario:
            return veterinario.atendimentos
        return None

    def delete_veterinario(self, id_veterinario: int) -> bool:
        """
        Deleta um veterinário.
        """
        return self.veterinario_repository.delete(id_veterinario)
        
    def update_veterinario(self, id_veterinario: int, nome: str = None, especialidade: str = None, clinica_id: int = None) -> Veterinario | None:
        """
        Atualiza os dados de um veterinário.
        """
        return self.veterinario_repository.update(id_veterinario, nome, especialidade, clinica_id)