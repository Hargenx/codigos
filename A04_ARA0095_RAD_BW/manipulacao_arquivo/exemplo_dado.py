import os

arquivo = open('dados.txt', 'w', encoding='utf-8')

for i in range(1, 1100):
    arquivo.write(f'Esta é a linha {i}.\n')

tamanho = os.path.getsize('dados.txt')
print('Nome do arquivo: ', arquivo.name)
print('Tamanho do arquivo (em bytes):', tamanho)
print('Modo do arquivo: ', arquivo.mode)
print('Arquivo está fechado? ', arquivo.closed)
arquivo.close()
print('Arquivo está fechado? ', arquivo.closed)
