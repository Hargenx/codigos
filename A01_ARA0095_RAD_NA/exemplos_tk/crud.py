import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from pathlib import Path

# Definindo o caminho do banco de dados
base_dir = Path(__file__).resolve().parent
DB_NAME = base_dir / "pessoas.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    return conn


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


class AplicativoCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD com Tkinter + TTK + SQLite")
        self.root.geometry("335x370")
        self.root.resizable(False, False)

        self.estilo()
        self.criar_widgets()
        self.listar()

    def estilo(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6)
        style.configure("TEntry", padding=6)

    def criar_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entry_nome = ttk.Entry(frame, width=30)
        self.entry_nome.grid(row=0, column=1, columnspan=2, pady=5)

        ttk.Label(frame, text="Idade:").grid(row=1, column=0, sticky="w")
        self.entry_idade = ttk.Entry(frame, width=30)
        self.entry_idade.grid(row=1, column=1, columnspan=2, pady=5)

        ttk.Button(frame, text="Cadastrar", command=self.inserir).grid(
            row=2, column=0, pady=10
        )
        ttk.Button(frame, text="Atualizar", command=self.atualizar).grid(
            row=2, column=1
        )
        ttk.Button(frame, text="Excluir", command=self.deletar).grid(row=2, column=2)

        self.lista = tk.Listbox(frame, height=10, width=50)
        self.lista.grid(row=3, column=0, columnspan=3, pady=10)
        ttk.Button(frame, text="Listar", command=self.listar).grid(row=4, column=1)

    def inserir(self):
        nome = self.entry_nome.get().strip()
        idade = self.entry_idade.get().strip()
        if nome and idade.isdigit():
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, int(idade))
            )
            conn.commit()
            conn.close()
            self.limpar_campos()
            self.listar()
        else:
            messagebox.showwarning("Erro", "Preencha nome e idade válidos!")

    def listar(self):
        self.lista.delete(0, tk.END)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas")
        for pessoa in cursor.fetchall():
            self.lista.insert(tk.END, f"{pessoa[0]} - {pessoa[1]} - {pessoa[2]} anos")
        conn.close()

    def deletar(self):
        selecao = self.lista.curselection()
        if selecao:
            item = self.lista.get(selecao[0])
            id = item.split(" - ")[0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))
            conn.commit()
            conn.close()
            self.listar()
        else:
            messagebox.showinfo("Atenção", "Selecione um item para excluir.")

    def atualizar(self):
        selecao = self.lista.curselection()
        nome = self.entry_nome.get().strip()
        idade = self.entry_idade.get().strip()
        if selecao and nome and idade.isdigit():
            item = self.lista.get(selecao[0])
            id = item.split(" - ")[0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE pessoas SET nome = ?, idade = ? WHERE id = ?",
                (nome, int(idade), id),
            )
            conn.commit()
            conn.close()
            self.limpar_campos()
            self.listar()
        else:
            messagebox.showinfo("Atenção", "Selecione um item e preencha nome e idade.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)


if __name__ == "__main__":
    criar_tabela()
    root = tk.Tk()
    app = AplicativoCRUD(root)
    root.mainloop()
