from sqlalchemy.orm import Session
from models.veterinario import Veterinario
from models.clinica import Clinica

class VeterinarioRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, nome: str, especialidade: str, clinica_id: int) -> Veterinario:
        """
        Cria um novo veterinário, associado a uma clínica existente.
        """
        clinica = self.db_session.get(Clinica, clinica_id)
        if not clinica:
            raise ValueError(f"Clínica com ID {clinica_id} não encontrada.")

        novo_veterinario = Veterinario(
            nome=nome,
            especialidade=especialidade,
            clinica_id=clinica_id
        )
        self.db_session.add(novo_veterinario)
        self.db_session.commit()
        self.db_session.refresh(novo_veterinario)
        return novo_veterinario

    def get_all(self) -> list[Veterinario]:
        """
        Retorna todos os veterinários cadastrados.
        """
        return self.db_session.query(Veterinario).all()

    def get_by_id(self, id_veterinario: int) -> Veterinario | None:
        """
        Busca um veterinário pelo seu ID.
        """
        return self.db_session.get(Veterinario, id_veterinario)

    def delete(self, id_veterinario: int) -> bool:
        """
        Deleta um veterinário pelo seu ID.
        """
        veterinario = self.get_by_id(id_veterinario)
        if veterinario:
            self.db_session.delete(veterinario)
            self.db_session.commit()
            return True
        return False
        
    def update(self, id_veterinario: int, nome: str = None, especialidade: str = None, clinica_id: int = None) -> Veterinario | None:
        """
        Atualiza os dados de um veterinário.
        """
        veterinario = self.get_by_id(id_veterinario)
        if veterinario:
            if nome:
                veterinario.nome = nome
            if especialidade:
                veterinario.especialidade = especialidade
            if clinica_id:
                clinica = self.db_session.get(Clinica, clinica_id)
                if not clinica:
                    raise ValueError(f"Clínica com ID {clinica_id} não encontrada para atualização.")
                veterinario.clinica_id = clinica_id
            
            self.db_session.commit()
            self.db_session.refresh(veterinario)
        return veterinario