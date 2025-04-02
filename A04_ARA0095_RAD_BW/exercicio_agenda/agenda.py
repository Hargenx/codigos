from dataclasses import dataclass
from typing import Optional

@dataclass
class Contato:
    """
    Representa um contato com nome, sobrenome, email e telefone.
    """
    nome: str
    sobrenome: str
    email: str
    telefone: str

    def __str__(self):
        return f"{self.nome},{self.sobrenome},{self.email},{self.telefone}"


@dataclass
class ControleContatos:
    """
    Classe para gerenciar contatos em um arquivo de texto.
    """
    arquivo: str

    def adicionar_contato(self, contato: Contato) -> None:
        """
        Adiciona um contato ao arquivo.

        Args:
            contato (Contato): O contato a ser adicionado.
        """
        try:
            with open(self.arquivo, "a") as f:
                f.write(f"{contato}\n")
        except OSError as e:
            print(f"Erro ao salvar contato: {e}")

    def buscar_contato(self, email_busca: str) -> Optional[Contato]:
        """
        Busca um contato pelo email.

        Args:
            email_busca (str): O email a ser buscado.

        Returns:
            Contato se encontrado, ou None.
        """
        try:
            with open(self.arquivo, "r") as f:
                for linha in f:
                    nome, sobrenome, email, telefone = linha.strip().split(",")
                    if email == email_busca:
                        return Contato(nome, sobrenome, email, telefone)
        except FileNotFoundError:
            print("Arquivo de contatos não encontrado.")
        except ValueError:
            print("Erro ao ler uma linha do arquivo (formato inválido).")
        except OSError as e:
            print(f"Erro ao acessar o arquivo: {e}")
        return None

    def remover_contato(self, email_busca: str) -> bool:
        """
        Remove um contato com o email especificado.

        Args:
            email_busca (str): Email do contato a ser removido.

        Returns:
            bool: True se contato foi removido, False se não encontrado.
        """
        linhas = []
        encontrado = False
        try:
            with open(self.arquivo, "r") as f:
                for linha in f:
                    campos = linha.strip().split(",")
                    if len(campos) != 4:
                        continue  # ignora linhas inválidas
                    _, _, email, _ = campos
                    if email == email_busca:
                        encontrado = True
                    else:
                        linhas.append(linha)
            if encontrado:
                with open(self.arquivo, "w") as f:
                    f.writelines(linhas)
                print(f"Contato com email '{email_busca}' foi removido.")
            else:
                print(f"Contato com email '{email_busca}' não encontrado.")
            return encontrado
        except FileNotFoundError:
            print("Arquivo de contatos não encontrado.")
        except OSError as e:
            print(f"Erro ao acessar o arquivo: {e}")
        return False