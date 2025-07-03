# services/livro_service.py

from sqlalchemy.orm import Session
from models import Livro

class LivroService:
    def __init__(self, db_session: Session):
        """
        Inicializa o serviço com a sessão do banco de dados. 
        """
        self.db_session = db_session

    def criar_livro(self, codigo: int, titulo: str, autor: str, editora: str, ano_pub: int) -> Livro:
        """
        Cria um novo livro no banco de dados. 
        """
        # Verifica se um livro com o mesmo código já existe
        livro_existente = self.buscar_livro_por_codigo(codigo)
        if livro_existente:
            raise ValueError(f"Livro com o código {codigo} já existe.")

        novo_livro = Livro(
            codigo=codigo,
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano_pub=ano_pub
        )
        self.db_session.add(novo_livro)
        self.db_session.commit()
        self.db_session.refresh(novo_livro)
        return novo_livro

    def listar_livros(self) -> list[Livro]:
        """
        Retorna uma lista de todos os livros. 
        """
        return self.db_session.query(Livro).all()

    def buscar_livro_por_codigo(self, codigo: int) -> Livro | None:
        """
        Busca um livro pelo seu código (chave primária). 
        """
        # .get() é otimizado para busca por chave primária
        return self.db_session.get(Livro, codigo)

    def atualizar_livro(self, codigo: int, titulo: str = None, autor: str = None, editora: str = None, ano_pub: int = None) -> Livro | None:
        """
        Atualiza os dados de um livro existente. 
        """
        livro = self.buscar_livro_por_codigo(codigo)
        if not livro:
            return None

        if titulo is not None:
            livro.titulo = titulo
        if autor is not None:
            livro.autor = autor
        if editora is not None:
            livro.editora = editora
        if ano_pub is not None:
            livro.ano_pub = ano_pub
        
        self.db_session.commit()
        self.db_session.refresh(livro)
        return livro

    def remover_livro(self, codigo: int) -> bool:
        """
        Remove um livro do banco de dados. 
        """
        livro = self.buscar_livro_por_codigo(codigo)
        if not livro:
            return False
        
        # Lógica de negócio: não permitir exclusão se houver exemplares
        if livro.exemplares:
            raise ValueError("Não é possível remover um livro que possui exemplares cadastrados.")
            
        self.db_session.delete(livro)
        self.db_session.commit()
        return True