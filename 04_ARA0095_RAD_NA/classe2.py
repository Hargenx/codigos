from dataclasses import dataclass
@dataclass
class Aluno:
    nome: str
    idade: int
    notas: list
    def calcular_media(self: object) -> float:
        '''
        Método para calcular a média das notas do aluno
        :return: float -> Média das notas do aluno
        '''
        return sum(self.notas) / len(self.notas)
    
if __name__ == "__main__":
    aluno1 = Aluno("Raphael", 39, [9.5, 8.7, 7.2])
    aluno2 = Aluno("Caroline", 30, [6.8, 7.5, 8.9])
    lista_alunos = [aluno1, aluno2]
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome}, Média: {aluno.calcular_media():.2f}")
