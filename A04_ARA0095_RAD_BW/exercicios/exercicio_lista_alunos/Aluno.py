class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nNotas: {self.notas}\nMédia: {self.calcular_media()}"