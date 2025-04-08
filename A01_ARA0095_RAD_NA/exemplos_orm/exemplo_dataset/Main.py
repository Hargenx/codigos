# Importando a biblioteca
import dataset
from pathlib import Path
base_dir = Path(__file__).parent
# Criando a classe de gerenciamento de contatos
class GerenciadorContatos:

    def __init__(self, db_url=None):
        if db_url is None:
            db_path = base_dir / "contatos.db"
            db_url = f"sqlite:///{db_path}"
            # Conectando ao banco de dados
        self.db = dataset.connect(db_url)
        # Criando (ou acessando) a tabela de contatos
        self.contatos = self.db["contatos"]

    def criar_contato(self, nome, telefone):
        """Adiciona um novo contato."""
        self.contatos.insert(dict(nome=nome, telefone=telefone))
        print(f"Contato {nome} adicionado com sucesso!")

    def listar_contato(self):
        """Lista todos os contatos."""
        print("Lista de Contatos:")
        for contato in self.contatos.all():
            print(
                f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}"
            )

    def atualizar_contato(self, contato_id, nome=None, telefone=None):
        """Atualiza um contato existente."""
        contato = dict(id=contato_id)
        if nome:
            contato["nome"] = nome
        if telefone:
            contato["telefone"] = telefone
        self.contatos.update(contato, ["id"])
        print(f"Contato ID {contato_id} atualizado.")

    def apagar_contato(self, contato_id):
        """Remove um contato pelo ID."""
        self.contatos.delete(id=contato_id)
        print(f"Contato ID {contato_id} removido.")


# Testando a classe
if __name__ == "__main__":
    gerenciar = GerenciadorContatos()

    # Adicionando contatos
    gerenciar.criar_contato("Caarol", "1234-5678")
    gerenciar.criar_contato("Raphael", "9876-5432")

    # Listando contatos
    gerenciar.listar_contato()

    # Atualizando um contato
    gerenciar.atualizar_contato(contato_id=1, telefone="1111-2222")

    # Listando novamente
    gerenciar.listar_contato()

    # Removendo um contato
    gerenciar.apagar_contato(contato_id=2)

    # Listando para conferir
    gerenciar.listar_contato()
