from pathlib import Path
from Aluno import Aluno
from GerenciadorAlunos import GerenciadorAlunos

def exibir_menu():
    print("\n=== MENU GERENCIAMENTO DE ALUNOS ===")
    print("1. Cadastrar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por nome")
    print("4. Remover aluno")
    print("5. Alterar nota de aluno")
    print("0. Sair")
if __name__ == "__main__":
    base_dir = Path(__file__).parent
    gerenciador = GerenciadorAlunos(base_dir)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                nome = input("Nome do aluno: ").strip()
                try:
                    nota = float(input("Nota do aluno (0 a 10): ").strip())
                    if 0 <= nota <= 10:
                        aluno = Aluno(nome, nota)
                        gerenciador.cadastrar(aluno)
                        print(f"Aluno {nome} cadastrado com sucesso.")
                    else:
                        print("Nota fora do intervalo permitido.")
                except ValueError:
                    print("Erro: a nota deve ser um número.")

            case "2":
                alunos = gerenciador.listar()
                print("\n--- Lista de Alunos ---")
                for linha in alunos:
                    print(linha)
                if not alunos:
                    print("Nenhum aluno cadastrado.")

            case "3":
                nome = input("Nome do aluno: ").strip()
                resultado = gerenciador.buscar(nome.title())
                print(f"Resultado: {resultado}")

            case "4":
                nome = input("Nome do aluno a remover: ").strip()
                if gerenciador.remover(nome.title()):
                    print(f"Aluno {nome} removido com sucesso.")
                else:
                    print("Aluno não encontrado.")

            case "5":
                nome = input("Nome do aluno: ").strip()
                try:
                    nova_nota = float(input("Nova nota: ").strip())
                    if gerenciador.alterar_nota(nome.title(), nova_nota):
                        print(f"Nota de {nome} atualizada para {nova_nota}.")
                    else:
                        print("Aluno não encontrado.")
                except ValueError:
                    print("Erro: a nota deve ser um número.")

            case "0":
                print("Encerrando o programa...")
                break

            case _:
                print("Opção inválida. Tente novamente.")


    '''print("Cadastrando:", gerenciador.cadastrar(Aluno("Raphael", 8.0)))
    print("Lendo:", gerenciador.buscar("Raphael"))
    print("Lista completa:", gerenciador.listar())
    print("Removendo:", gerenciador.remover("Raphael"))
    print("Lista após remoção:", gerenciador.listar())
    print("Novo cadastro:", gerenciador.cadastrar(Aluno("Raphael", 7.0)))
    print("Alterando nota:", gerenciador.alterar_nota("Raphael", 10.0))
    print("Lista final:", gerenciador.listar())'''
