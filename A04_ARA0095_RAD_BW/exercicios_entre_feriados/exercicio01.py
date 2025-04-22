'''📝 Exercício 1 – Criação de Banco com Tabela de Produtos
Objetivo: Criar um banco SQLite com uma tabela chamada produtos.'''

import sqlite3

def criar_banco_produtos():
    """Cria um banco SQLite com uma tabela chamada produtos."""
    try:
        conexao = sqlite3.connect("./A04_ARA0095_RAD_BW/exercicios_entre_feriados/mercado.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                preco REAL
            )
        """)

        print("Tabela 'produtos' criada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)
    finally:
        conexao.close()
