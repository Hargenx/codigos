from pathlib import Path
import json
from typing import List, Dict


class Aluno:
    """
    Representa um aluno com nome e nota.

    Attributes:
        nome (str): Nome do aluno.
        nota (float): Nota do aluno.
    """

    def __init__(self, nome: str, nota: float):
        """
        Inicializa uma nova instância de Aluno.

        Args:
            nome (str): O nome do aluno.
            nota (float): A nota do aluno.
        """
        self.nome = nome.strip().title()
        self.nota = float(nota)

    def to_dict(self) -> Dict[str, float]:
        """
        Retorna o aluno como um dicionário com nome e nota.

        Returns:
            dict: Um dicionário {nome: nota}.
        """
        return {self.nome: self.nota}

    def __str__(self) -> str:
        """
        Representação em string do aluno no formato CSV.

        Returns:
            str: Nome e nota separados por vírgula.
        """
        return f"{self.nome},{self.nota:.1f}"


class GerenciadorAlunos:
    """
    Classe responsável pelo gerenciamento de alunos e persistência dos dados.

    Attributes:
        csv_path (Path): Caminho do arquivo CSV.
        json_path (Path): Caminho do arquivo JSON.
        txt_path (Path): Caminho do arquivo TXT.
        alunos (Dict[str, float]): Dicionário com os dados dos alunos.
    """

    def __init__(self, base_dir: Path):
        """
        Inicializa o gerenciador e carrega os dados existentes.

        Args:
            base_dir (Path): Diretório base onde os arquivos serão armazenados.
        """
        self.csv_path = base_dir / "alunos.csv"
        self.json_path = base_dir / "alunos.json"
        self.txt_path = base_dir / "alunos.txt"
        self.alunos: Dict[str, float] = self._carregar()

    def _carregar(self) -> Dict[str, float]:
        """
        Carrega os dados dos alunos a partir do arquivo CSV, se existir. (_ == Método protegido ou interno)

        Returns:
            dict: Dicionário com os dados dos alunos.
        """
        if self.csv_path.exists():
            try:
                with open(self.csv_path, "r") as f:
                    return {
                        nome: float(nota)
                        for nome, nota in (linha.strip().split(",") for linha in f)
                    }
            except FileNotFoundError:
                print("Arquivo CSV não encontrado.")
            except ValueError as ve:
                print(f"Erro ao converter nota para float: {ve}")
            except OSError as oe:
                print(f"Erro de sistema ao acessar o arquivo: {oe}")
        return {}

    def salvar(self) -> None:
        """
        Salva os dados dos alunos nos formatos CSV, TXT e JSON.
        """
        try:
            with open(self.csv_path, "w") as f_csv, open(
                self.txt_path, "w"
            ) as f_txt, open(self.json_path, "w") as f_json:

                for nome, nota in self.alunos.items():
                    linha = f"{nome},{nota:.1f}\n"
                    f_csv.write(linha)
                    f_txt.write(f"{nome} tem nota {nota:.1f}\n")

                json.dump(self.alunos, f_json, indent=4)

        except Exception as e:
            print(f"Erro ao salvar os arquivos: {e}")

    def cadastrar(self, aluno: Aluno) -> bool:
        """
        Cadastra ou atualiza um aluno no dicionário e salva os dados.

        Args:
            aluno (Aluno): Instância da classe Aluno.

        Returns:
            bool: True se o cadastro foi bem-sucedido.
        """
        self.alunos[aluno.nome] = aluno.nota
        self.salvar()
        return True

    def remover(self, nome: str) -> bool:
        """
        Remove um aluno pelo nome.

        Args:
            nome (str): Nome do aluno a ser removido.

        Returns:
            bool: True se o aluno foi removido, False caso contrário.
        """
        if nome in self.alunos:
            del self.alunos[nome]
            self.salvar()
            return True
        return False

    def alterar_nota(self, nome: str, nova_nota: float) -> bool:
        """
        Altera a nota de um aluno existente.

        Args:
            nome (str): Nome do aluno.
            nova_nota (float): Nova nota a ser atribuída.

        Returns:
            bool: True se a nota foi alterada, False caso o aluno não exista.
        """
        if nome in self.alunos:
            self.alunos[nome] = nova_nota
            self.salvar()
            return True
        return False

    def listar(self) -> List[str]:
        """
        Lista todos os alunos cadastrados.

        Returns:
            list: Lista de strings no formato "nome,nota".
        """
        return [f"{nome},{nota:.1f}" for nome, nota in self.alunos.items()]

    def buscar(self, nome: str) -> str:
        """
        Busca um aluno pelo nome.

        Args:
            nome (str): Nome do aluno.

        Returns:
            str: Informação do aluno no formato "nome,nota" ou mensagem de erro.
        """
        if nome in self.alunos:
            return f"{nome},{self.alunos[nome]:.1f}"
        return "Aluno não encontrado."

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
