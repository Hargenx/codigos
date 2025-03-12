arquivo = open('./dados.txt')
print('Nome do arquivo: ', arquivo.name)
print('Tamanho do arquivo (em bytes): ', arquivo.tell())
print('Modo do arquivo: ', arquivo.mode)
print('Arquivo está fechado? ', arquivo.closed)
arquivo.close()
print('Arquivo está fechado? ', arquivo.closed)
import os
# Diretório base
diretorio_base = 'D:\\Estacio\\2025_01\\codigos\\04_ARA0095_RAD_NA'
# Subdiretório e nome do arquivo
subdiretorio = 'manipulando_arquivo'
nome_arquivo = 'dados.txt'
# Construir o caminho relativo
caminho_relativo = os.path.join(diretorio_base, subdiretorio, nome_arquivo)
# Obter o caminho absoluto
caminho_absoluto = os.path.abspath(caminho_relativo)
# Exibir os resultados
print(f'Caminho relativo: {caminho_relativo}')
print(f'Caminho absoluto: {caminho_absoluto}')
