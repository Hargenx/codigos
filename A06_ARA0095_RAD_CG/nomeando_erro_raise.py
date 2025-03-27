# Definindo uma exceção personalizada
class MeuErro(Exception):
    pass

def dividir(numerador, denominador):
    if denominador == 0:
        # Lança a exceção personalizada com uma mensagem de erro
        raise MeuErro("Divisão por zero não é permitida!")
    return numerador / denominador

try:
    # Tentativa de realizar a divisão
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except MeuErro as erro:
    # Captura e trata a exceção personalizada
    print("Ocorreu um erro personalizado:", erro)
