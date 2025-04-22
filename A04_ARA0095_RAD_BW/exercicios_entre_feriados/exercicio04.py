import exercicio01
import exercicio02
import exercicio03

if __name__ == '__main__':
    while True:
        print("Escolha um exercício:")
        print("1. Criar banco de produtos")
        print("2. Criar banco de livros")
        print("3. Criar arquivo de nomes")
        print("4. Ler arquivo de nomes")
        print("5. Criar banco de nomes")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                exercicio01.criar_banco_produtos()
            case "2":
                exercicio02.criar_banco_livros()
            case "3":
                exercicio03.criar_arquivo_nomes()
            case "4":
                exercicio03.ler_arquivo_nomes()
            case '5':
                exercicio03.criar_banco_nomes()
            case '6':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")
                continue