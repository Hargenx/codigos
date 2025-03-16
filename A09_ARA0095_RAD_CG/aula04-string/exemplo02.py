# Lista de linhas a serem escritas no arquivo
linhas = [
    "Esta é a primeira linha.\n",
    "Esta é a segunda linha.\n",
    "Esta é a terceira linha.\n"
]
with open("./A09_ARA0095_RAD_CG/aula04-string/exemplo_writelines.txt", "w", encoding="utf-8") as arquivo:
    # Escreve todas as linhas de uma vez no arquivo
    arquivo.writelines(linhas)

with open("./A09_ARA0095_RAD_CG/aula04-string/exemplo_writelines.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
