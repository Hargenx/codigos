from view.view import Visao
from database import ConexaoBanco
from models.Pessoa import Pessoa
from models.Marca import Marca
from models.Veiculo import Veiculo
from logger import log_info


class Controlador:
    def __init__(self, tipo_banco: str = "sqlite") -> None:
        self.visao = Visao()
        self.banco = ConexaoBanco(tipo_banco)
        self.banco.conectar()
        self.banco.criar_tabelas()

    def executar(self) -> None:
        while True:
            opcao = self.visao.exibir_menu()

            match opcao:
                case "1":
                    self.cadastrar_pessoa()
                case '2':
                    self.cadastrar_marca()
                case '3':
                    self.cadastrar_veiculo()
                case '4':
                    self.listar_veiculos()
                case '5':
                    self.visao.exibir_mensagem("Encerrando o programa. Até logo!")
                    self.banco.close()
                    break
                case _:
                    self.visao.exibir_mensagem("Opção inválida. Tente novamente.")

    def cadastrar_pessoa(self) -> None:
        cpf, nome, nascimento, oculos = self.visao.obter_dados_pessoa()
        pessoa = Pessoa(cpf, nome, nascimento, oculos)
        self.banco.inserir_pessoa(pessoa)
        self.visao.exibir_mensagem("Pessoa cadastrada com sucesso!")
        log_info(f"Pessoa cadastrada: {pessoa}")

    def cadastrar_marca(self) -> None:
        nome, sigla = self.visao.obter_dados_marca()
        marca = Marca(0, nome, sigla)  # ID será auto incrementado
        self.banco.inserir_marca(marca)
        self.visao.exibir_mensagem("Marca cadastrada com sucesso!")
        log_info(f"Marca cadastrada: {marca}")

    def cadastrar_veiculo(self) -> None:
        placa, cor, cpf_proprietario, id_marca = self.visao.obter_dados_veiculo()
        veiculo = Veiculo(placa, cor, cpf_proprietario, id_marca)
        self.banco.inserir_veiculo(veiculo)
        self.visao.exibir_mensagem("Veículo cadastrado com sucesso!")
        log_info(f"Veículo cadastrado: {veiculo}")

    def listar_veiculos(self) -> None:
        veiculos = self.banco.buscar_veiculos()
        self.visao.exibir_veiculos(veiculos)
