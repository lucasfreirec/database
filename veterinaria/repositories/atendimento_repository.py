from sqlalchemy.orm import Session
from models.atendimento import Atendimento
from models.pet import Pet
from models.veterinario import Veterinario

class AtendimentoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, descricao: str, pet_id: int, veterinario_id: int) -> Atendimento:
        """
        Cria um novo atendimento, associando um pet e um veterinário.
        """
        pet = self.db_session.get(Pet, pet_id)
        if not pet:
            raise ValueError(f"Pet com ID {pet_id} não encontrado.")

        veterinario = self.db_session.get(Veterinario, veterinario_id)
        if not veterinario:
            raise ValueError(f"Veterinário com ID {veterinario_id} não encontrado.")

        novo_atendimento = Atendimento(
            descricao=descricao,
            pet_id=pet_id,
            veterinario_id=veterinario_id
        )
        
        self.db_session.add(novo_atendimento)
        self.db_session.commit()
        self.db_session.refresh(novo_atendimento)
        return novo_atendimento

    def get_all(self) -> list[Atendimento]:
        """
        Retorna todos os atendimentos cadastrados.
        """
        return self.db_session.query(Atendimento).all()

    def get_by_id(self, id_atendimento: int) -> Atendimento | None:
        """
        Busca um atendimento pelo seu ID.
        """
        return self.db_session.get(Atendimento, id_atendimento)
    
    def get_by_veterinario_id(self, id_veterinario: int) -> list[Atendimento]:
        """
        Retorna todos os atendimentos realizados por um veterinário específico.
        """
        return self.db_session.query(Atendimento).filter(Atendimento.veterinario_id == id_veterinario).all()

    def get_by_pet_id(self, id_pet: int) -> list[Atendimento]:
        """
        Retorna todos os atendimentos de um pet específico.
        """
        return self.db_session.query(Atendimento).filter(Atendimento.pet_id == id_pet).all()

    def delete(self, id_atendimento: int) -> bool:
        """
        Deleta um atendimento pelo seu ID.
        """
        atendimento = self.get_by_id(id_atendimento)
        if atendimento:
            self.db_session.delete(atendimento)
            self.db_session.commit()
            return True
        return False