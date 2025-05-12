import tkinter as tk
from tkinter import ttk

# Janela principal
root = tk.Tk()
root.title("Exemplo com ttk")

# Aplicar tema moderno
style = ttk.Style()
style.theme_use("classic")

# Estilizar botão padrão TButton (cor do fundo afeta apenas em alguns temas e sistemas)
style.configure(
    "TButton",
    background="red",
    foreground="black",
    padding=6,
    font=("Helvetica", 12, "bold"),
)

# Criar botão estilizado
botao = ttk.Button(root, text="Clique Aqui")
botao.pack(padx=20, pady=20)

root.mainloop()
