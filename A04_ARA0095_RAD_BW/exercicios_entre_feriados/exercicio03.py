'''📂 Exercício 3 – Criar Banco com Nomes Lidos de um TXT
Objetivo: Ler nomes de um arquivo .txt (um por linha) e exibir na tela. Em seguida, criar uma tabela nomes para armazenar esses dados futuramente (sem inserir ainda).

Arquivo nomes.txt:

Raphael
Caroline
Vanessa
Cristina
Gilson
Gabriel
Sara
'''
import sqlite3

def criar_arquivo_nomes():
    '''Cria um arquivo .txt com uma lista de nomes.'''
    lista_nomes = [ "Raphael", "Caroline", "Vanessa", "Cristina", "Gilson", "Gabriel", "Sara" ]
    try:
        with open("./A04_ARA0095_RAD_BW/exercicios_entre_feriados/nomes.txt", "w", encoding="utf-8") as arquivo:
            for nome in lista_nomes:
                arquivo.write(nome + "\n")
        print("Nomes escritos no arquivo 'nomes.txt' com sucesso.")
    except Exception as erro:
        print("Erro ao escrever no arquivo:", erro)

def ler_arquivo_nomes():
    '''Leitura de um arquivo .txt com uma lista de nomes.'''
    try:
        with open("./A04_ARA0095_RAD_BW/exercicios_entre_feriados/nomes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            print("Nomes lidos do arquivo:")
            for nome in linhas:
                print(nome.strip())
    except FileNotFoundError:
        print("Arquivo 'nomes.txt' não encontrado.")
    except Exception as erro:
        print("Erro ao ler o arquivo:", erro)

def criar_banco_nomes():
    '''Cria um banco SQLite com uma tabela chamada nomes.'''
    try:
        conexao = sqlite3.connect("./A04_ARA0095_RAD_BW/exercicios_entre_feriados/cadastro.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nomes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
        """)

        print("Tabela 'nomes' criada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao criar banco:", erro)
    finally:
        conexao.close()
