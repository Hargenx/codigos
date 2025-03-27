def dividir(numerador, denominador):
    # Se o denominador for zero, levanta uma exceção do tipo ValueError
    if denominador == 0:
        raise ValueError("Divisão por zero não é permitida!")
    return numerador / denominador

try:
    # Tentamos realizar uma divisão
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except ValueError as erro:
    # Capturamos a exceção e exibimos a mensagem de erro
    print("Ocorreu um erro:", erro)
