from tkinter import messagebox
import tkinter as tk

janela = tk.Tk()
canvas = tk.Canvas(janela, width=200, height=100)
canvas.create_rectangle(50, 20, 150, 80, fill="blue")
canvas.pack()

janela.mainloop()
messagebox.showinfo("Título", "Mensagem para o usuário")