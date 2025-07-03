from datetime import date
from sqlalchemy.orm import Session
from models import Contem

class ContemService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def registrar_devolucao(self, id_emp: int, tombo_emp: int) -> Contem | None:
        """
        Registra a data de devolução de um exemplar específico em um empréstimo.
        """
        item_contem = self.db_session.get(Contem, (id_emp, tombo_emp))
        
        if not item_contem:
            return None
            
        if item_contem.data_devol is not None:
            raise ValueError("Este exemplar já foi devolvido.")
            
        item_contem.data_devol = date.today()
        self.db_session.commit()
        self.db_session.refresh(item_contem)
        return item_contem