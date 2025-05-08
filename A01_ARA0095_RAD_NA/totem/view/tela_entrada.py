import tkinter as tk
from controller.controlador_entrada import ControladorEntrada


class TelaEntrada(tk.Tk):
    """
    Interface gráfica para entrada de veículos no estacionamento.
    """

    def __init__(self):
        super().__init__()
        self.title("Entrada de Veículos")
        self.geometry("400x300")
        self.resizable(False, False)
        self.controlador = ControladorEntrada()

        self._criar_interface()

    def _criar_interface(self):
        self._limpar_tela()
        tk.Label(self, text="🚗 Bem-vindo ao Estacionamento", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Gerar Ticket", font=("Arial", 14), command=self._gerar_ticket).pack(pady=30)

        self.resultado = tk.Label(self, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def _gerar_ticket(self):
        ticket = self.controlador.gerar_ticket()
        self.resultado.config(
            text=f"Ticket: {ticket.ticket_id}\nPlaca: {ticket.placa}\nEntrada: {ticket.hora_entrada}"
        )

    def _limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()
