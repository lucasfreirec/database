from sqlalchemy.orm import Session
from models import Exemplar, Livro

class ExemplarService:
    def __init__(self, db_session: Session):
        """
        Inicializa o serviço com a sessão do banco de dados.
        """
        self.db_session = db_session

    def criar_exemplar(self, tombo: int, codigo_livro: int) -> Exemplar:
        """
        Cria um novo exemplar, associando-o a um livro existente.
        """
        livro = self.db_session.get(Livro, codigo_livro)
        if not livro:
            raise ValueError(f"Não foi encontrado um livro com o código {codigo_livro}.")

        exemplar_existente = self.buscar_exemplar_por_tombo(tombo)
        if exemplar_existente:
            raise ValueError(f"Exemplar com o tombo {tombo} já existe.")

        novo_exemplar = Exemplar(tombo=tombo, codigo_livro=codigo_livro)
        self.db_session.add(novo_exemplar)
        self.db_session.commit()
        self.db_session.refresh(novo_exemplar)
        return novo_exemplar

    def listar_exemplares(self) -> list[Exemplar]:
        """
        Retorna uma lista de todos os exemplares.
        """
        return self.db_session.query(Exemplar).all()

    def buscar_exemplar_por_tombo(self, tombo: int) -> Exemplar | None:
        """
        Busca um exemplar pelo seu tombo (chave primária).
        """
        return self.db_session.get(Exemplar, tombo)
    
    def atualizar_exemplar(self, tombo: int, codigo_livro: int) -> Exemplar | None:
        """
        Atualiza o livro ao qual um exemplar pertence.
        """
        exemplar = self.buscar_exemplar_por_tombo(tombo)
        if not exemplar:
            return None
            
        # Validação: o novo livro deve existir
        novo_livro = self.db_session.get(Livro, codigo_livro)
        if not novo_livro:
            raise ValueError(f"Não foi encontrado um livro com o código {codigo_livro} para a atualização.")
            
        exemplar.codigo_livro = codigo_livro
        self.db_session.commit()
        self.db_session.refresh(exemplar)
        return exemplar


    def remover_exemplar(self, tombo: int) -> bool:
        """
        Remove um exemplar do banco de dados.
        """
        exemplar = self.buscar_exemplar_por_tombo(tombo)
        if not exemplar:
            return False
            
        if exemplar.emprestimos:
            raise ValueError("Não é possível remover um exemplar que está ou já esteve em um empréstimo.")

        self.db_session.delete(exemplar)
        self.db_session.commit()
        return True