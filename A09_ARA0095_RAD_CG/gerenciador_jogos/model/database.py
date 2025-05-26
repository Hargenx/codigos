import sqlite3
from typing import List, Optional
import os

class Database:
    def __init__(self, db_path: str = "data/jogos.db") -> None:
        os.makedirs("data", exist_ok=True)
        self.db_path = db_path
        self._criar_tabelas()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _criar_tabelas(self) -> None:
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jogos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    nota REAL NOT NULL
                )
            """)
            conn.commit()

    def inserir_usuario(self, usuario: str, senha: str) -> bool:
        try:
            with self._conectar() as conn:
                conn.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
                return True
        except sqlite3.IntegrityError:
            return False

    def buscar_usuario(self, usuario: str, senha: str) -> Optional[tuple]:
        with self._conectar() as conn:
            cursor = conn.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            return cursor.fetchone()

    def inserir_jogo(self, titulo: str, genero: str, nota: float) -> bool:
        try:
            with self._conectar() as conn:
                conn.execute("INSERT INTO jogos (titulo, genero, nota) VALUES (?, ?, ?)", (titulo, genero, nota))
                return True
        except sqlite3.Error:
            return False

    def buscar_jogos(self) -> List[tuple]:
        with self._conectar() as conn:
            cursor = conn.execute("SELECT id, titulo, genero, nota FROM jogos")
            return cursor.fetchall()

    def excluir_jogo(self, jogo_id: int) -> bool:
        with self._conectar() as conn:
            cursor = conn.execute("DELETE FROM jogos WHERE id = ?", (jogo_id,))
            return cursor.rowcount > 0

    def editar_jogo(self, jogo_id: int, titulo: str, genero: str, nota: float) -> bool:
        try:
            with self._conectar() as conn:
                cursor = conn.execute(
                    "UPDATE jogos SET titulo = ?, genero = ?, nota = ? WHERE id = ?",
                    (titulo, genero, nota, jogo_id)
                )
                return cursor.rowcount > 0
        except sqlite3.Error:
            return False
