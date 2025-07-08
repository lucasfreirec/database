from sqlalchemy.orm import Session
from models.pet import Pet
from models.tutor import Tutor

class PetRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, nome: str, especie: str, idade: int, tutor_id: int) -> Pet:
        """
        Cria um novo pet, associado a um tutor existente.
        """
        tutor = self.db_session.get(Tutor, tutor_id)
        if not tutor:
            raise ValueError(f"Tutor com ID {tutor_id} não encontrado.")

        novo_pet = Pet(
            nome=nome,
            especie=especie,
            idade=idade,
            tutor_id=tutor_id
        )
        self.db_session.add(novo_pet)
        self.db_session.commit()
        self.db_session.refresh(novo_pet)
        return novo_pet

    def get_all(self) -> list[Pet]:
        """
        Retorna todos os pets cadastrados.
        """
        return self.db_session.query(Pet).all()

    def get_by_id(self, id_pet: int) -> Pet | None:
        """
        Busca um pet pelo seu ID.
        """
        return self.db_session.get(Pet, id_pet)

    def delete(self, id_pet: int) -> bool:
        """
        Deleta um pet pelo seu ID.
        """
        pet = self.get_by_id(id_pet)
        if pet:
            if pet.atendimentos:
                raise ValueError("Não é possível remover um pet que possui atendimentos registrados.")
            
            self.db_session.delete(pet)
            self.db_session.commit()
            return True
        return False

    def update(self, id_pet: int, nome: str = None, especie: str = None, idade: int = None, tutor_id: int = None) -> Pet | None:
        """
        Atualiza os dados de um pet.
        """
        pet = self.get_by_id(id_pet)
        if pet:
            if nome:
                pet.nome = nome
            if especie:
                pet.especie = especie
            if idade:
                pet.idade = idade
            if tutor_id:
                tutor = self.db_session.get(Tutor, tutor_id)
                if not tutor:
                    raise ValueError(f"Tutor com ID {tutor_id} não encontrado para atualização.")
                pet.tutor_id = tutor_id
                
            self.db_session.commit()
            self.db_session.refresh(pet)
        return pet