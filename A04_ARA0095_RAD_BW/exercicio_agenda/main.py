from agenda import Contato, ControleContatos
from pathlib import Path
def main():
    caminho_arquivo = Path(__file__).parent / "contatos.txt"
    agenda = ControleContatos(arquivo=caminho_arquivo)

    contato1 = Contato("Raphael", "Jesus", "raphael.jesus@estacio.br", "123456789")
    contato2 = Contato("Caroline", "Castro", "carol@email.com", "987654321")

    agenda.adicionar_contato(contato1)
    agenda.adicionar_contato(contato2)

    contato = agenda.buscar_contato("raphael.jesus@estacio.br")
    if contato:
        print(f"\n📌 Contato encontrado: {contato.nome} {contato.sobrenome} - {contato.telefone}")
    else:
        print("Contato não encontrado.")

    agenda.remover_contato("carol@email.com")
    agenda.remover_contato("carol@email.com")  # testando remoção de um já removido


if __name__ == "__main__":
    main()