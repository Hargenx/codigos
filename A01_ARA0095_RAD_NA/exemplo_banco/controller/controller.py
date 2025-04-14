from view.view import Visao
from database import ConexaoBanco
from models.Pessoa import Pessoa
from models.Marca import Marca
from models.Veiculo import Veiculo
from logger import log_info


class Controlador:
    def __init__(self) -> None:
        self.visao = Visao()
        self.banco = ConexaoBanco()  # SQLite fixo
        log_info("Controlador inicializado com sucesso.")

    def executar(self) -> None:
        while True:
            opcao = self.visao.exibir_menu()

            match opcao:
                case "1":
                    self.cadastrar_pessoa()
                case "2":
                    self.cadastrar_marca()
                case "3":
                    self.cadastrar_veiculo()
                case "4":
                    self.listar_veiculos()
                case "5":
                    self.exportar_veiculos_csv()
                case "6":
                    self.encerrar_programa()
                    break
                case _:
                    self.visao.exibir_mensagem("Opção inválida. Tente novamente.")

    def cadastrar_pessoa(self) -> None:
        try:
            cpf, nome, nascimento, oculos = self.visao.obter_dados_pessoa()
            pessoa = Pessoa(cpf, nome, nascimento, oculos)
            self.banco.inserir_pessoa(pessoa)
            self.visao.exibir_mensagem("Pessoa cadastrada com sucesso!")
            log_info(f"Pessoa cadastrada: {pessoa}")
        except Exception as e:
            self.visao.exibir_mensagem(f"Erro ao cadastrar pessoa: {e}")

    def cadastrar_marca(self) -> None:
        try:
            nome, sigla = self.visao.obter_dados_marca()
            marca = Marca(0, nome, sigla)  # ID será auto incrementado pelo SQLite
            self.banco.inserir_marca(marca)
            self.visao.exibir_mensagem("Marca cadastrada com sucesso!")
            log_info(f"Marca cadastrada: {marca}")
        except Exception as e:
            self.visao.exibir_mensagem(f"Erro ao cadastrar marca: {e}")

    def cadastrar_veiculo(self) -> None:
        try:
            placa, cor, cpf_proprietario, id_marca = self.visao.obter_dados_veiculo()
            veiculo = Veiculo(placa, cor, cpf_proprietario, id_marca)
            self.banco.inserir_veiculo(veiculo)
            self.visao.exibir_mensagem("Veículo cadastrado com sucesso!")
            log_info(f"Veículo cadastrado: {veiculo}")
        except Exception as e:
            self.visao.exibir_mensagem(f"Erro ao cadastrar veículo: {e}")

    def listar_veiculos(self) -> None:
        try:
            veiculos = self.banco.buscar_veiculos()
            self.visao.exibir_veiculos(veiculos)
        except Exception as e:
            self.visao.exibir_mensagem(f"Erro ao listar veículos: {e}")

    def exportar_veiculos_csv(self) -> None:
        try:
            self.banco.exportar_veiculos_csv()
            self.visao.exibir_mensagem("Veículos exportados para CSV com sucesso!")
        except Exception as e:
            self.visao.exibir_mensagem(f"Erro ao exportar veículos: {e}")

    def encerrar_programa(self) -> None:
        self.banco.close()
        self.visao.exibir_mensagem("Programa encerrado. Conexão com o banco fechada.")
        log_info("Programa encerrado.")
