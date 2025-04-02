from dataclasses import dataclass
@dataclass
class Contato:
    nome: str
    sobrenome: str
    email: str
    telefone: str
@dataclass
class ControleContatos:
    arquivo: str
    def adicionar_contato(self, contato):
        with open(self.arquivo, "a") as f:
            f.write(f"{contato.nome},{contato.sobrenome},{contato.email},{contato.telefone}\n")
    def buscar_contato(self, email_busca):
        with open(self.arquivo, "r") as f:
            for linha in f:
                nome, sobrenome, email, telefone = linha.strip().split(",")
                if email == email_busca:
                    return Contato(nome, sobrenome, email, telefone)
                else:
                    return "Contato não encontrado"
            
    def remover_contato(self, email_busca):
        linhas = []
        encontrado = False
        with open(self.arquivo, "r") as f:
            for linha in f:
                _, _, email, _ = linha.strip().split(",")
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
def main():
    agenda = ControleContatos(arquivo="contatos.txt")
    contato1 = Contato("Raphael", "Jesus", "raphael.jesus@estacio.br", "123456789")
    contato2 = Contato("Caroline", "Castro", "carol@email.com", "987654321")
    agenda.adicionar_contato(contato1)
    agenda.adicionar_contato(contato2)
    print(agenda.buscar_contato("raphael.jesus@estacio.br").nome)
    agenda.remover_contato("carol@email.com")
    email_busca = "raphael.jesus@estacio.br"
    contato_encontrado = agenda.buscar_contato(email_busca)
    if isinstance(contato_encontrado, Contato):
        print(f"Nome: {contato_encontrado.nome}, Sobrenome: {contato_encontrado.sobrenome}, Email: {contato_encontrado.email}, Telefone: {contato_encontrado.telefone}")
    else:
        print(contato_encontrado)
    agenda.remover_contato("carol@email.com")
if __name__ == "__main__":
    main()
