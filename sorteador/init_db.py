import sqlite3
import os
from pathlib import Path


DB_PATH = Path(__file__).parent / 'banco.db'
caminho = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(caminho, "banco.db")

def init_db():
    with sqlite3.connect(caminho) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS turmas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT UNIQUE NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS grupos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        turma_id INTEGER,
                        nome TEXT,
                        alunos TEXT,
                        tema TEXT,
                        FOREIGN KEY(turma_id) REFERENCES turmas(id))''')
        conn.commit()

if __name__ == '__main__':
    init_db()
    print('Banco criado com sucesso!')
