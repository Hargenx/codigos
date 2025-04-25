class Dre:
    def __init__(self, numero):
        self.numero = [self.funcao(numero)]

    def funcao(self, numero):
        return numero * 2


d = Dre(2)
print(d.funcao(2))