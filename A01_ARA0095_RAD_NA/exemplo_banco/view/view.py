from typing import Tuple


class Visao:
    def exibir_menu(self) -> str:
        print("\n=== Menu Principal ===")
        print("1. Cadastrar pessoa")
        print("2. Cadastrar marca")
        print("3. Cadastrar veículo")
        print("4. Listar veículos")
        print("5. Exportar veículos para CSV")
        print("6. Sair")
        return input("Escolha uma opção: ")

    def obter_dados_pessoa(self) -> Tuple[str, str, str, bool]:
        cpf = input("Informe o CPF: ")
        nome = input("Informe o nome: ")
        nascimento = input("Informe a data de nascimento (YYYY-MM-DD): ")
        oculos = input("Usa óculos? (sim/nao): ").strip().lower() == "sim"
        return cpf, nome, nascimento, oculos

    def obter_dados_marca(self) -> Tuple[str, str]:
        nome = input("Informe o nome da marca: ")
        sigla = input("Informe a sigla da marca: ")
        return nome, sigla

    def obter_dados_veiculo(self) -> Tuple[str, str, str, int]:
        placa = input("Informe a placa do veículo: ")
        cor = input("Informe a cor do veículo: ")
        cpf_proprietario = input("Informe o CPF do proprietário: ")
        id_marca = int(input("Informe o ID da marca: "))
        return placa, cor, cpf_proprietario, id_marca

    def exibir_mensagem(self, mensagem: str) -> None:
        print(mensagem)

    def exibir_veiculos(self, veiculos: list) -> None:
        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n=== Lista de Veículos ===")
            for veiculo in veiculos:
                print(veiculo)
