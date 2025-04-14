from datetime import date

class Pessoa:
    def __init__(self, cpf: str, nome: str, nascimento: date, oculos: bool) -> None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos

    def __str__(self) -> str:
        return f"{self.nome} (CPF: {self.cpf}) - Nasc: {self.nascimento} - Óculos: {'Sim' if self.oculos else 'Não'}"
