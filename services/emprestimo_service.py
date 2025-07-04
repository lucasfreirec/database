from datetime import date
from sqlalchemy.orm import Session
from models import Emprestimo, Aluno, Exemplar, Contem

class EmprestimoService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def criar_emprestimo(self, mat_aluno: int, tombos_exemplares: list[int]) -> Emprestimo:
        """
        Cria um novo registro de empréstimo e associa os exemplares a ele.
        Esta é uma operação atômica: ou tudo funciona, ou nada é salvo.
        """
        if not tombos_exemplares:
            raise ValueError("A lista de exemplares não pode estar vazia.")

        aluno = self.db_session.get(Aluno, mat_aluno)
        if not aluno:
            raise ValueError(f"Aluno com matrícula {mat_aluno} não encontrado.")

        novo_emprestimo = Emprestimo(
            mat_aluno=mat_aluno,
            data_emprestimo=date.today(),
            previsao_devolucao=date.today() 
        )
        self.db_session.add(novo_emprestimo)

        for tombo in tombos_exemplares:
            exemplar = self.db_session.get(Exemplar, tombo)
            if not exemplar:
                raise ValueError(f"Exemplar com tombo {tombo} não encontrado.")
            
            item_contem = Contem(
                emprestimo=novo_emprestimo, # Associa o empréstimo ao item
                exemplar=exemplar         # Associa o exemplar ao item
            )
            self.db_session.add(item_contem)

        self.db_session.commit()
        self.db_session.refresh(novo_emprestimo)
        return novo_emprestimo

    def listar_emprestimos(self) -> list[Emprestimo]:
        """Lista todos os empréstimos."""
        return self.db_session.query(Emprestimo).all()
        
    def buscar_emprestimo_por_id(self, id_emp: int) -> Emprestimo | None:
        """Busca um empréstimo pelo seu ID."""
        return self.db_session.get(Emprestimo, id_emp)