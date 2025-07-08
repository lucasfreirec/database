from repositories.atendimento_repository import AtendimentoRepository
from models.atendimento import Atendimento

class AtendimentoService:
    def __init__(self, atendimento_repository: AtendimentoRepository):
        """
        Inicializa o serviço com uma instância do repositório de atendimentos.
        """
        self.atendimento_repository = atendimento_repository

    def create_atendimento(self, descricao: str, pet_id: int, veterinario_id: int) -> Atendimento:
        """
        Cria um novo atendimento.
        Este método atende ao endpoint: POST /atendimentos
        """
        return self.atendimento_repository.create(
            descricao=descricao,
            pet_id=pet_id,
            veterinario_id=veterinario_id
        )

    def get_all_atendimentos(self) -> list[Atendimento]:
        """
        Retorna todos os atendimentos.
        Este método atende ao endpoint: GET /atendimentos
        """
        return self.atendimento_repository.get_all()

    def get_atendimento_by_id(self, id_atendimento: int) -> Atendimento | None:
        """
        Busca um atendimento pelo seu ID.
        """
        return self.atendimento_repository.get_by_id(id_atendimento)

    def get_atendimentos_by_veterinario_id(self, id_veterinario: int) -> list[Atendimento]:
        """
        Retorna os atendimentos de um veterinário específico.
        Este método atende ao endpoint: GET /veterinarios/{id}/atendimentos
        """
        return self.atendimento_repository.get_by_veterinario_id(id_veterinario)

    def get_atendimentos_by_pet_id(self, id_pet: int) -> list[Atendimento]:
        """
        Retorna os atendimentos de um pet específico.
        Este método atende ao endpoint: GET /pets/{id}/atendimentos
        """
        return self.atendimento_repository.get_by_pet_id(id_pet)
    
    def delete_atendimento(self, id_atendimento: int) -> bool:
        """
        Deleta um atendimento.
        """
        return self.atendimento_repository.delete(id_atendimento)