from controller.controller import Controlador


def main() -> None:
    print("Iniciando o sistema com banco de dados SQLite...")

    # Cria a instância do controlador, que automaticamente cria e conecta ao banco
    controlador = Controlador()

    # Executa o fluxo principal da aplicação (menu interativo)
    controlador.executar()


if __name__ == "__main__":
    main()


'''def main() -> None:
    # Seleção do banco de dados na inicialização da aplicação
    print("Selecione o banco de dados que deseja utilizar:")
    print("1. SQLite (padrão)")
    print("2. PostgreSQL")
    print("3. MySQL")

    escolha_banco: str = input("Opção escolhida: ")

    tipo_banco: str = "sqlite"
    if escolha_banco == "2":
        tipo_banco = "postgres"
    elif escolha_banco == "3":
        tipo_banco = "mysql"

    # Instancia o controlador da aplicação, que cuida da inicialização do banco e do fluxo do sistema
    controlador = Controlador(tipo_banco)

    # Executa o fluxo principal da aplicação (menu interativo)
    controlador.executar()


if __name__ == "__main__":
    main()
'''
