# main.py
import tkinter as tk
from tkinter import messagebox
import os
from incluir import AddUserWindow

class Database:
    """Classe responsável pelo acesso ao SQLite."""
    def __init__(self, db_filename: str):
        self.db_file = os.path.join(os.path.dirname(__file__), db_filename)
        self._ensure_table()

    def _connect(self):
        import sqlite3
        return sqlite3.connect(self.db_file)

    def _ensure_table(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome  TEXT    NOT NULL,
                email TEXT    NOT NULL UNIQUE
            )
        """)
        conn.commit()
        conn.close()

    def add_user(self, nome: str, email: str) -> None:
        """Tenta inserir um novo usuário; lança sqlite3.IntegrityError se o e-mail já existir."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()

    def list_users(self):
        """Retorna lista de tuplas (id, nome, email)."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return rows


class MainApp:
    """Janela principal que lista usuários e abre a janela de inclusão."""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CRUD OO com Tkinter e SQLite")
        self.root.geometry("450x400")

        # Instância de Database
        self.db = Database("usuarios.db")

        # Widgets
        self.btn_novo = tk.Button(root, text="Novo Usuário", command=self.abrir_janela_inclusão)
        self.btn_novo.pack(pady=10)

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(padx=10, pady=10)

        # Carrega lista inicial
        self.refresh_list()

    def refresh_list(self):
        """Limpa e preenche o Listbox com os usuários do banco."""
        self.listbox.delete(0, tk.END)
        for uid, nome, email in self.db.list_users():
            self.listbox.insert(tk.END, f"ID:{uid:03d} — {nome} <{email}>")

    def abrir_janela_inclusão(self):
        """Abre a janela de inclusão, passando callback para atualização."""
        AddUserWindow(self.root, self.db, on_success=self.refresh_list)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
