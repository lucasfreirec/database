from sqlalchemy.orm import Session
from models.clinica import Clinica

class ClinicaRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, nome: str, cidade: str) -> Clinica:
        """
        Cria uma nova clínica no banco de dados.
        """
        nova_clinica = Clinica(nome=nome, cidade=cidade)
        self.db_session.add(nova_clinica)
        self.db_session.commit()
        self.db_session.refresh(nova_clinica)
        return nova_clinica

    def get_all(self) -> list[Clinica]:
        """
        Retorna todas as clínicas cadastradas.
        """
        return self.db_session.query(Clinica).all()

    def get_by_id(self, id_clinica: int) -> Clinica | None:
        """
        Busca uma clínica pelo seu ID.
        """
        return self.db_session.get(Clinica, id_clinica)

    def delete(self, id_clinica: int) -> bool:
        """
        Deleta uma clínica pelo seu ID.
        """
        clinica = self.get_by_id(id_clinica)
        if clinica:
            self.db_session.delete(clinica)
            self.db_session.commit()
            return True
        return False
        
    def update(self, id_clinica: int, nome: str = None, cidade: str = None) -> Clinica | None:
        """
        Atualiza os dados de uma clínica.
        """
        clinica = self.get_by_id(id_clinica)
        if clinica:
            if nome:
                clinica.nome = nome
            if cidade:
                clinica.cidade = cidade
            self.db_session.commit()
            self.db_session.refresh(clinica)
        return clinica