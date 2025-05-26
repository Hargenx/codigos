# incluir.py
import tkinter as tk
from tkinter import messagebox

class AddUserWindow(tk.Toplevel):
    """Janela para adicionar um novo usuário."""
    def __init__(self, master, database, on_success=None):
        """
        :param master: janela-pai (Tk)
        :param database: instância da classe Database
        :param on_success: callback sem argumentos, chamado após inclusão
        """
        super().__init__(master)
        self.title("Incluir Usuário")
        self.resizable(False, False)
        self.database = database
        self.on_success = on_success

        # Layout
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_email = tk.Entry(self, width=30)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Salvar",   command=self.salvar).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.destroy).pack(side="right", padx=5)

        # Centraliza a janela sobre a principal
        self.transient(master)
        self.grab_set()
        master.wait_window(self)

    def salvar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        if not nome or not email:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            self.database.add_user(nome, email)
        except Exception as e:
            # Espera sqlite3.IntegrityError para e-mail duplicado
            messagebox.showerror("Erro ao adicionar", str(e))
            return

        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
        if callable(self.on_success):
            self.on_success()
        self.destroy()
