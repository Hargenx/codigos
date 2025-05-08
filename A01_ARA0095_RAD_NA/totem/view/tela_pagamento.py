import tkinter as tk
from tkinter import messagebox
from controller.controlador_totem import ControladorTotem
from model.ticket import Ticket


class TelaTotemPagamento(tk.Tk):
    """
    Interface gráfica do totem de pagamento.
    """

    def __init__(self):
        super().__init__()
        self.title("Totem de Pagamento")
        self.geometry("500x450")
        self.resizable(False, False)

        self.controlador = ControladorTotem()
        self.ticket_encontrado: Ticket = None

        self._tela_inicial()

    def _tela_inicial(self):
        self._limpar_tela()
        tk.Label(self, text="Insira o código do ticket", font=("Arial", 16)).pack(pady=20)

        self.entry_ticket = tk.Entry(self, font=("Arial", 18), justify="center")
        self.entry_ticket.pack(pady=10)

        tk.Button(self, text="Consultar", font=("Arial", 14), command=self._consultar_ticket).pack(pady=20)

    def _consultar_ticket(self):
        codigo = self.entry_ticket.get().strip().upper()
        ticket = self.controlador.buscar_ticket_valido(codigo)

        if ticket:
            self.ticket_encontrado = ticket
            self._mostrar_detalhes()
        else:
            messagebox.showerror("Erro", "Ticket inválido ou já pago.")

    def _mostrar_detalhes(self):
        self._limpar_tela()

        permanencia = self.ticket_encontrado.calcular_permanencia()
        valor, tolerancia = self._calcular_valor(permanencia)
        self.ticket_encontrado.valor = f"{valor:.2f}"

        tk.Label(self, text=f"Placa: {self.ticket_encontrado.placa}", font=("Arial", 16)).pack(pady=5)
        tk.Label(self, text=f"Tempo: {permanencia} min", font=("Arial", 14)).pack(pady=5)
        tk.Label(self, text=f"Valor: R$ {valor:.2f}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text="Escolha a forma de pagamento", font=("Arial", 12)).pack(pady=10)

        botoes = tk.Frame(self)
        botoes.pack(pady=10)
        tk.Button(botoes, text="💳 Cartão", width=10, height=2,
                  command=lambda: self._confirmar_pagamento("Cartão")).pack(side="left", padx=10)
        tk.Button(botoes, text="📱 PIX", width=10, height=2,
                  command=lambda: self._confirmar_pagamento("PIX")).pack(side="left", padx=10)

        tk.Button(self, text="Cancelar", font=("Arial", 12), command=self._tela_inicial).pack(pady=20)

    def _confirmar_pagamento(self, metodo: str):
        ticket_pago = self.controlador.realizar_pagamento(self.ticket_encontrado, metodo)
        messagebox.showinfo("Pagamento concluído", f"Pagamento via {metodo} realizado com sucesso!\n"
                                                   f"Valor: R$ {ticket_pago.valor}\n"
                                                   f"Liberado até: {ticket_pago.liberado_ate}")
        self._tela_inicial()

    def _limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _calcular_valor(self, tempo_min: int) -> tuple[float, int]:
        match tempo_min:
            case tempo if tempo <= 15:
                return 5.0, 15
            case tempo if tempo <= 30:
                return 8.0, 15
            case tempo if tempo <= 60:
                return 12.0, 20
            case tempo if tempo <= 120:
                return 18.0, 20
            case _:
                return 25.0, 30
