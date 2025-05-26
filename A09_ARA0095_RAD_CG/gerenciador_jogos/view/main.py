import logging
from tkinter import Tk, StringVar, messagebox
from tkinter.ttk import Label, Entry, Button, Frame, Treeview, Combobox, Style
from controller.controller import Controller
from model.database import Database

class Aplicacao(Frame):
    def __init__(self, master: Tk, controller: Controller):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.pack(padx=10, pady=10)
        self.usuario_var = StringVar()
        self.senha_var = StringVar()
        self.editando_id = None
        self.criar_tela_login()

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def criar_tela_login(self):
        self.limpar_tela()
        Label(self, text="Usuário").pack()
        Entry(self, textvariable=self.usuario_var).pack()
        Label(self, text="Senha").pack()
        Entry(self, textvariable=self.senha_var, show="*").pack()
        Button(self, text="Entrar", command=self.login).pack(pady=5)
        Button(self, text="Cadastrar-se", command=self.registrar).pack()

    def login(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()
        if not usuario or not senha:
            messagebox.showerror("Erro", "Preencha usuário e senha.")
            return
        if self.controller.autenticar_usuario(usuario, senha):
            self.criar_tela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def registrar(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()
        if len(usuario) < 3 or len(senha) < 3:
            messagebox.showwarning("Aviso", "Usuário e senha devem ter no mínimo 3 caracteres.")
            return
        if self.controller.registrar_usuario(usuario, senha):
            messagebox.showinfo("Sucesso", "Usuário registrado.")
        else:
            messagebox.showwarning("Aviso", "Usuário já existe.")

    def criar_tela_principal(self):
        self.limpar_tela()
        self.titulo_var = StringVar()
        self.genero_var = StringVar()
        self.nota_var = StringVar()

        Label(self, text="Título do Jogo").pack()
        Entry(self, textvariable=self.titulo_var).pack()
        Label(self, text="Gênero").pack()
        Combobox(self, textvariable=self.genero_var,
                 values=["RPG", "Ação", "Aventura", "Corrida", "Puzzle"],
                 state="readonly").pack()
        Label(self, text="Nota (0-10)").pack()
        Entry(self, textvariable=self.nota_var).pack()
        Button(self, text="Adicionar Jogo", command=self.adicionar_ou_editar_jogo).pack(pady=5)

        self.tree = Treeview(self, columns=("ID", "Título", "Gênero", "Nota"), show="headings")
        for col in ("ID", "Título", "Gênero", "Nota"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)
        Button(self, text="Editar Selecionado", command=self.carregar_jogo_para_edicao).pack(pady=2)
        Button(self, text="Remover Selecionado", command=self.remover_jogo).pack()
        self.atualizar_lista()

    def adicionar_ou_editar_jogo(self):
        try:
            titulo = self.titulo_var.get().strip()
            genero = self.genero_var.get().strip()
            nota = float(self.nota_var.get())
            if not titulo or not genero or not (0 <= nota <= 10):
                raise ValueError("Preencha corretamente todos os campos.")
            if self.editando_id:
                self.controller.editar_jogo(self.editando_id, titulo, genero, nota)
                self.editando_id = None
            else:
                self.controller.cadastrar_jogo(titulo, genero, nota)
            self.titulo_var.set("")
            self.genero_var.set("")
            self.nota_var.set("")
            self.atualizar_lista()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def carregar_jogo_para_edicao(self):
        item = self.tree.selection()
        if item:
            valores = self.tree.item(item, "values")
            self.editando_id = int(valores[0])
            self.titulo_var.set(valores[1])
            self.genero_var.set(valores[2])
            self.nota_var.set(valores[3])

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for jogo in self.controller.listar_jogos():
            self.tree.insert("", "end", values=jogo)

    def remover_jogo(self):
        item = self.tree.selection()
        if item:
            jogo_id = int(self.tree.item(item, "values")[0])
            if self.controller.remover_jogo(jogo_id):
                self.atualizar_lista()
            else:
                messagebox.showerror("Erro", "Erro ao remover jogo.")

def main():
    logging.basicConfig(filename="data/relatorio.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    root = Tk()
    root.title("🎮 Gerenciador de Jogos")
    root.geometry("520x600")
    Style().theme_use("clam")
    db = Database()
    controller = Controller(db)
    app = Aplicacao(root, controller)
    app.mainloop()

if __name__ == "__main__":
    main()
