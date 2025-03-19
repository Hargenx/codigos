# Exemplo com return: retorna uma lista completa
def get_coxinhas(*pedidos):
    return [f'{pedido} coxinhas' for pedido in pedidos]

salgados_return = get_coxinhas(4, 6, 8)
print("Usando return:")
print(salgados_return)  # Imprime: ['4 coxinhas', '6 coxinhas', '8 coxinhas']

# Exemplo com yield: gera os itens um a um
def get_joelho(*pedidos):
    for pedido in pedidos:
        yield f'{pedido} joelho(s)'

print("\nUsando yield:")
for salgado in get_joelho(4, 6, 8):
    print(salgado)
