from tkinter import Tk, Label, Entry, Button, Toplevel, END, StringVar
import os
import hashlib


def registro() -> None:
    """Janela de registro."""
    global tela_de_registro
    tela_de_registro = Toplevel(janela_principal)
    tela_de_registro.title("Registro")
    tela_de_registro.geometry("300x250")

    global usuario
    global senha
    global usuario_entry
    global senha_entry
    usuario = StringVar()
    senha = StringVar()

    Label(
        tela_de_registro, text="Por favor, preencha os dados abaixo", bg="blue", pady=10
    ).pack()
    Label(tela_de_registro, text="").pack()
    Label(tela_de_registro, text="Usuário * ").pack()
    usuario_entry = Entry(tela_de_registro, textvariable=usuario)
    usuario_entry.pack()
    Label(tela_de_registro, text="Senha * ").pack()
    senha_entry = Entry(tela_de_registro, textvariable=senha, show="*")
    senha_entry.pack()
    Label(tela_de_registro, text="").pack()
    Button(
        tela_de_registro,
        text="Registrar",
        width=10,
        height=1,
        bg="blue",
        command=registro_de_usuario,
    ).pack()


def login() -> None:
    """Janela de login."""
    global janela_de_login
    janela_de_login = Toplevel(janela_principal)
    janela_de_login.title("Login")
    janela_de_login.geometry("300x250")

    global usuario_verificacao
    global senha_verificacao

    usuario_verificacao = StringVar()
    senha_verificacao = StringVar()

    global usuario_login_entry
    global senha_login_entry

    Label(janela_de_login, text="Por favor, entre com os dados de login").pack()
    Label(janela_de_login, text="").pack()
    Label(janela_de_login, text="Usuário * ").pack()
    usuario_login_entry = Entry(janela_de_login, textvariable=usuario_verificacao)
    usuario_login_entry.pack()
    Label(janela_de_login, text="Senha * ").pack()
    senha_login_entry = Entry(janela_de_login, textvariable=senha_verificacao, show="*")
    senha_login_entry.pack()
    Label(janela_de_login, text="").pack()
    Button(
        janela_de_login, text="Login", width=10, height=1, command=login_verificacao
    ).pack()


def registro_de_usuario() -> None:
    """Registro de novo usuário."""
    usuario_info = usuario.get()
    senha_info = senha.get()
    senha_hash = hashlib.sha256(senha_info.encode()).hexdigest()

    if not os.path.exists("usuarios"):
        os.makedirs("usuarios")
    with open(f"usuarios/{usuario_info}.txt", "w") as arquivo:
        arquivo.write(usuario_info + "\n")
        arquivo.write(senha_hash)

    usuario_entry.delete(0, END)
    senha_entry.delete(0, END)

    Label(
        tela_de_registro,
        text="Registrado com sucesso",
        fg="green",
        font=("Calibri", 11),
    ).pack()


def login_verificacao() -> None:
    """Login de usuário."""
    usuario1 = usuario_verificacao.get()
    senha1 = senha_verificacao.get()
    senha_hash1 = hashlib.sha256(senha1.encode()).hexdigest()

    usuario_login_entry.delete(0, END)
    senha_login_entry.delete(0, END)

    if os.path.exists(f"./usuarios/{usuario1}.txt"):
        with open(f"./usuarios/{usuario1}.txt", "r") as arquivo1:
            verificacao = arquivo1.read().splitlines()
            if senha_hash1 == verificacao[1]:
                login_sucesso()
            else:
                senha_nao_reconhecida()
    else:
        usuario_nao_encontrado()


def login_sucesso() -> None:
    """Login com sucesso."""
    global login_tela_de_sucesso
    login_tela_de_sucesso = Toplevel(janela_de_login)
    login_tela_de_sucesso.title("Sucesso")
    login_tela_de_sucesso.geometry("150x100")
    Label(login_tela_de_sucesso, text="Login com Sucesso").pack()
    Button(
        login_tela_de_sucesso,
        text="OK",
        command=lambda: fechar_janela(login_tela_de_sucesso),
    ).pack()


def senha_nao_reconhecida() -> None:
    """Senha não reconhecida."""
    global senha_tela_nao_reconhecida
    senha_tela_nao_reconhecida = Toplevel(janela_de_login)
    senha_tela_nao_reconhecida.title("Erro")
    senha_tela_nao_reconhecida.geometry("150x100")
    Label(senha_tela_nao_reconhecida, text="Senha inválida").pack()
    Button(
        senha_tela_nao_reconhecida,
        text="OK",
        command=lambda: fechar_janela(senha_tela_nao_reconhecida),
    ).pack()


def usuario_nao_encontrado() -> None:
    """Usuário não encontrado."""
    global tela_usuario_nao_encontrado
    tela_usuario_nao_encontrado = Toplevel(janela_de_login)
    tela_usuario_nao_encontrado.title("Erro")
    tela_usuario_nao_encontrado.geometry("150x100")
    Label(tela_usuario_nao_encontrado, text="Usuário não encontrado").pack()
    Button(
        tela_usuario_nao_encontrado,
        text="OK",
        command=lambda: fechar_janela(tela_usuario_nao_encontrado),
    ).pack()


def fechar_janela(janela: Toplevel) -> None:
    """Fecha uma janela."""
    janela.destroy()


def janela_da_conta() -> None:
    """Janela principal."""
    global janela_principal
    janela_principal = Tk()
    janela_principal.geometry("300x250")
    janela_principal.title("Login da conta")
    Label(
        text="Escolha sua opção",
        bg="blue",
        width="300",
        height="2",
        font=("Calibri", 13),
    ).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Registrar", height="2", width="30", command=registro).pack()

    janela_principal.mainloop()


if __name__ == "__main__":
    janela_da_conta()
