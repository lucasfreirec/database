from sqlalchemy.orm import Session
from models.tutor import Tutor

class TutorRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, nome: str, telefone: str) -> Tutor:
        """
        Cria um novo tutor no banco de dados.
        """
        novo_tutor = Tutor(nome=nome, telefone=telefone)
        self.db_session.add(novo_tutor)
        self.db_session.commit()
        self.db_session.refresh(novo_tutor)
        return novo_tutor

    def get_all(self) -> list[Tutor]:
        """
        Retorna todos os tutores cadastrados.
        """
        return self.db_session.query(Tutor).all()

    def get_by_id(self, id_tutor: int) -> Tutor | None:
        """
        Busca um tutor pelo seu ID.
        """
        return self.db_session.get(Tutor, id_tutor)
    
    def delete(self, id_tutor: int) -> bool:
        """
        Deleta um tutor pelo seu ID.
        """
        tutor = self.get_by_id(id_tutor)
        if tutor:
            self.db_session.delete(tutor)
            self.db_session.commit()
            return True
        return False

    def update(self, id_tutor: int, nome: str = None, telefone: str = None) -> Tutor | None:
        """
        Atualiza os dados de um tutor.
        """
        tutor = self.get_by_id(id_tutor)
        if tutor:
            if nome:
                tutor.nome = nome
            if telefone:
                tutor.telefone = telefone
            self.db_session.commit()
            self.db_session.refresh(tutor)
        return tutor