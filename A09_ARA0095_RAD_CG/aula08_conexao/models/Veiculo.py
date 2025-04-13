class Veiculo:
    def __init__(self, placa: str, cor: str, proprietario_cpf: str, marca_id: int) -> None:
        self.placa = placa
        self.cor = cor
        self.proprietario_cpf = proprietario_cpf
        self.marca_id = marca_id

    def __str__(self) -> str:
        return (f"Placa: {self.placa} - Cor: {self.cor} - "
                f"Proprietário CPF: {self.proprietario_cpf} - Marca ID: {self.marca_id}")
