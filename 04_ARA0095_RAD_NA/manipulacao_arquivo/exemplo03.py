caminho_arquivo = 'nomes.txt'

arquivo = open("nomes.txt", 'w')
arquivo.write("Raphael")
arquivo.writelines(["\nCaroline", "\nVanessa", "\nCristina"])
arquivo.close()
arquivo = open(caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i, linha in enumerate(linhas, start=1):
    print(f'Linha {i}: {linha}')
