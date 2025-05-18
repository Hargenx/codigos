from tkinter import Tk, Label, Button

class ExemploSimples:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Exemplo simples")
        self.janela.geometry("300x200")
        self.label = Label(self.janela, text="Olá mundo!")
        self.label.pack()
        self.botao = Button(self.janela, text="Botão")
        self.botao.pack()
        self.janela.mainloop()

if __name__ == "__main__":
    ExemploSimples()