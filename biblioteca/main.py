from db import SessionLocal
from services.aluno_service import AlunoService
from services.livro_service import LivroService
from services.exemplar_service import ExemplarService
from services.emprestimo_service import EmprestimoService
from services.contem_service import ContemService

def exibir_menu():
    print("\n--- Sistema de Gerenciamento da Biblioteca ---")
    print("Opções de Aluno:")
    print("  1. Cadastrar Novo Aluno")
    print("  2. Listar Todos os Alunos")
    print("Opções de Livro e Exemplar:")
    print("  3. Cadastrar Novo Livro")
    print("  4. Listar Todos os Livros")
    print("  5. Cadastrar Novo Exemplar de um Livro")
    print("  6. Listar Todos os Exemplares")
    print("Opções de Empréstimo:")
    print("  7. Realizar Novo Empréstimo")
    print("  8. Registrar Devolução de um Exemplar")
    print("  9. Listar Todos os Empréstimos")
    print("---------------------------------------------")
    print("  0. Sair do Programa")
    print("---------------------------------------------")

def main():
    session = SessionLocal()
    
    # Instancia todos os serviços com a mesma sessão
    aluno_service = AlunoService(db_session=session)
    livro_service = LivroService(db_session=session)
    exemplar_service = ExemplarService(db_session=session)
    emprestimo_service = EmprestimoService(db_session=session)
    contem_service = ContemService(db_session=session)

    while True:
        exibir_menu()
        escolha = input("Digite o número da opção desejada: ")

        try:
            if escolha == '1':
                # --- Cadastrar Aluno ---
                print("\n--- Cadastrar Novo Aluno ---")
                matricula = int(input("Matrícula: "))
                nome = input("Nome completo: ")
                email = input("Email: ")
                curso = input("Curso: ")
                aluno = aluno_service.criar_aluno(matricula=matricula, nome=nome, email=email, curso=curso)
                print(f"\n[SUCESSO] Aluno '{aluno.nome}' cadastrado com matrícula {aluno.matricula}.")

            elif escolha == '2':
                # --- Listar Alunos ---
                print("\n--- Lista de Alunos Cadastrados ---")
                alunos = aluno_service.listar_alunos()
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                for aluno in alunos:
                    print(f"- Matrícula: {aluno.matricula}, Nome: {aluno.nome}, Curso: {aluno.curso}")

            elif escolha == '3':
                # --- Cadastrar Livro ---
                print("\n--- Cadastrar Novo Livro ---")
                codigo = int(input("Código do Livro: "))
                titulo = input("Título: ")
                autor = input("Autor: ")
                editora = input("Editora: ")
                ano_pub = int(input("Ano de Publicação: "))
                livro = livro_service.criar_livro(codigo=codigo, titulo=titulo, autor=autor, editora=editora, ano_pub=ano_pub)
                print(f"\n[SUCESSO] Livro '{livro.titulo}' cadastrado com código {livro.codigo}.")

            elif escolha == '4':
                # --- Listar Livros ---
                print("\n--- Lista de Livros Cadastrados ---")
                livros = livro_service.listar_livros()
                if not livros:
                    print("Nenhum livro cadastrado.")
                for livro in livros:
                    print(f"- Código: {livro.codigo}, Título: '{livro.titulo}', Autor: {livro.autor}")

            elif escolha == '5':
                # --- Cadastrar Exemplar ---
                print("\n--- Cadastrar Novo Exemplar ---")
                tombo = int(input("Tombo do Exemplar: "))
                codigo_livro = int(input("Código do Livro ao qual pertence: "))
                exemplar = exemplar_service.criar_exemplar(tombo=tombo, codigo_livro=codigo_livro)
                print(f"\n[SUCESSO] Exemplar de tombo {exemplar.tombo} do livro '{exemplar.livro.titulo}' cadastrado.")
            
            elif escolha == '6':
                # --- Listar Exemplares ---
                print("\n--- Lista de Exemplares Cadastrados ---")
                exemplares = exemplar_service.listar_exemplares()
                if not exemplares:
                    print("Nenhum exemplar cadastrado.")
                for exemplar in exemplares:
                    print(f"- Tombo: {exemplar.tombo}, Título: '{exemplar.livro.titulo}'")

            elif escolha == '7':
                # --- Realizar Empréstimo ---
                print("\n--- Realizar Novo Empréstimo ---")
                mat_aluno = int(input("Matrícula do Aluno: "))
                tombos_str = input("Digite os tombos dos exemplares, separados por vírgula (ex: 9001,9002): ")
                tombos = [int(t.strip()) for t in tombos_str.split(',')]
                emprestimo = emprestimo_service.criar_emprestimo(mat_aluno=mat_aluno, tombos_exemplares=tombos)
                print(f"\n[SUCESSO] Empréstimo ID {emprestimo.id} criado para o aluno '{emprestimo.aluno.nome}'.")

            elif escolha == '8':
                # --- Registrar Devolução ---
                print("\n--- Registrar Devolução de Exemplar ---")
                id_emp = int(input("ID do Empréstimo: "))
                tombo_emp = int(input("Tombo do Exemplar a ser devolvido: "))
                devolucao = contem_service.registrar_devolucao(id_emp=id_emp, tombo_emp=tombo_emp)
                print(f"\n[SUCESSO] Devolução do exemplar {devolucao.tombo_emp} registrada em {devolucao.data_devol}.")
            
            elif escolha == '9':
                # --- Listar Empréstimos ---
                print("\n--- Lista de Empréstimos ---")
                emprestimos = emprestimo_service.listar_emprestimos()
                if not emprestimos:
                    print("Nenhum empréstimo realizado.")
                for emp in emprestimos:
                    print(f"ID: {emp.id}, Aluno: {emp.aluno.nome}, Data: {emp.data_emprestimo}")
                    for item in emp.exemplares:
                        status = f"Devolvido em {item.data_devol}" if item.data_devol else "Pendente"
                        print(f"  -> Exemplar Tombo: {item.tombo_emp}, Status: {status}")

            elif escolha == '0':
                print("Encerrando o programa...")
                break
            
            else:
                print("[ERRO] Opção inválida. Por favor, tente novamente.")

        except ValueError as e:
            print(f"\n[ERRO DE VALOR] {e}")
        except Exception as e:
            print(f"\n[ERRO INESPERADO] Ocorreu um erro: {e}")

        input("\nPressione Enter para continuar...")

    session.close()

if __name__ == "__main__":
    main()