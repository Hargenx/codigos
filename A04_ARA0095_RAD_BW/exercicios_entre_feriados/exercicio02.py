'''📚 Exercício 2 – Criação de Banco com Campos de Texto e Inteiro
Objetivo: Criar uma tabela chamada livros com os campos titulo, autor e ano.'''

import sqlite3

def criar_banco_livros():
    """Cria um banco SQLite com uma tabela chamada livros."""
    try:
        conexao = sqlite3.connect("./A04_ARA0095_RAD_BW/exercicios_entre_feriados/biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                ano INTEGER
            )
        """)

        print("Tabela 'livros' criada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)
    finally:
        conexao.close()
