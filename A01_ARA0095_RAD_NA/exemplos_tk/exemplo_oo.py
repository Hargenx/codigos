import tkinter as tk
from tkinter import ttk
class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Exemplo OO")
        self.pack(padx=20, pady=20)
        ttk.Label(self, text="Digite algo:").pack()
        self.entrada = ttk.Entry(self)
        self.entrada.pack()
        ttk.Button(self, text="Mostrar", command=self.exibir).pack()
    def exibir(self):
        print("Entrada:", self.entrada.get())
        self.entrada.delete(0, tk.END)
        self.entrada.focus()

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
