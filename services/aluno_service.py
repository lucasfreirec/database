# services/aluno_service.py

from sqlalchemy.orm import Session
from models import Aluno

class AlunoService:
    def __init__(self, db_session: Session):
        """
        Inicializa o serviço com uma sessão do banco de dados.
        """
        self.db_session = db_session

    def criar_aluno(self, nome: str, matricula: int, email: str, curso: str) -> Aluno:
        """
        Cria um novo aluno no banco de dados.
        Usa session.add() e session.commit().
        """
        # Verifica se a matrícula já existe
        aluno_existente = self.buscar_aluno_por_matricula(matricula)
        if aluno_existente:
            raise ValueError(f"Aluno com a matrícula {matricula} já existe.")
            
        novo_aluno = Aluno(
            matricula=matricula,
            nome=nome,
            email=email,
            curso=curso
        )
        self.db_session.add(novo_aluno)
        self.db_session.commit()
        self.db_session.refresh(novo_aluno)
        return novo_aluno

    def listar_alunos(self) -> list[Aluno]:
        """
        Retorna uma lista de todos os alunos.
        Usa session.query().
        """
        return self.db_session.query(Aluno).all()

    def buscar_aluno_por_matricula(self, matricula: int) -> Aluno | None:
        """
        Busca um aluno pela sua matrícula (chave primária).
        Usa session.query().
        """
        return self.db_session.query(Aluno).filter(Aluno.matricula == matricula).first()

    def atualizar_aluno(self, matricula: int, nome: str = None, email: str = None, curso: str = None) -> Aluno | None:
        """
        Atualiza os dados de um aluno existente.
        """
        aluno = self.buscar_aluno_por_matricula(matricula)
        if not aluno:
            return None

        if nome is not None:
            aluno.nome = nome
        if email is not None:
            aluno.email = email
        if curso is not None:
            aluno.curso = curso
        
        self.db_session.commit()
        self.db_session.refresh(aluno)
        return aluno

    def remover_aluno(self, matricula: int) -> bool:
        """
        Remove um aluno do banco de dados.
        """
        aluno = self.buscar_aluno_por_matricula(matricula)
        if not aluno:
            return False
            
        self.db_session.delete(aluno)
        self.db_session.commit()
        return True