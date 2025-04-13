from datetime import date

class Pessoa:
    def __init__(self, cpf: str, nome: str, nascimento: date, oculos: bool) -> None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos

    def __str__(self) -> str:
        return f"{self.nome} (CPF: {self.cpf}) - Nasc: {self.nascimento} - Óculos: {'Sim' if self.oculos else 'Não'}"

    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.nascimento.year
        if hoje.month < self.nascimento.month or (hoje.month == self.nascimento.month and hoje.day < self.nascimento.day):
            idade -= 1
        return idade

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'nascimento': self.nascimento,
            'oculos': self.oculos
        }