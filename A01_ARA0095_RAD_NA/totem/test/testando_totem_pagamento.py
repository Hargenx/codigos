import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import json
import os
import logging
import uuid
import random
import string
from typing import Dict, List, Optional

# —— Configurações de arquivos ——
TICKETS_JSON    = "tickets.json"
LOG_FILE        = "log_estacionamento.log"
COMPROVANTES_DIR = "comprovantes"

# —— Logger ——
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

# —— Funções de persistência ——
def inicializar_json() -> None:
    if not os.path.exists(TICKETS_JSON):
        with open(TICKETS_JSON, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def carregar_tickets() -> List[Dict]:
    inicializar_json()
    with open(TICKETS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tickets(dados: List[Dict]) -> None:
    with open(TICKETS_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# —— Lógica de emissão de ticket (teste) ——
def gerar_placa_aleatoria() -> str:
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits,       k=4))
    return letras + numeros

def emitir_ticket(placa: Optional[str] = None) -> str:
    dados = carregar_tickets()
    if not placa:
        placa = gerar_placa_aleatoria()
    ticket_id = str(uuid.uuid4())[:8].upper()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = {
        "ticket_id": ticket_id,
        "placa":      placa.upper(),
        "hora_entrada": now,
        "pago":       False,
        "hora_pagamento": "",
        "valor":      0.0,
        "liberado_ate": ""
    }
    dados.append(registro)
    salvar_tickets(dados)
    logging.info(f"Entrada registrada: Ticket {ticket_id}, Placa {placa.upper()}")
    return ticket_id

# —— Cálculo de preço e tolerância ——
def calcular_valor_e_tolerancia(hora_entrada: str) -> (float, int):
    ent = datetime.strptime(hora_entrada, "%Y-%m-%d %H:%M:%S")
    diff_min = int((datetime.now() - ent).total_seconds() // 60)
    if diff_min <= 15:
        return 5.0, 15
    if diff_min <= 30:
        return 8.0, 15
    if diff_min <= 60:
        return 12.0, 20
    if diff_min <= 120:
        return 18.0, 20
    return 25.0, 30

# —— Geração de comprovante ——
def gerar_comprovante(ticket: Dict) -> None:
    os.makedirs(COMPROVANTES_DIR, exist_ok=True)
    nome = f"comprovante_{ticket['ticket_id']}.txt"
    path = os.path.join(COMPROVANTES_DIR, nome)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("====== Estacionamento Central ======\n")
            f.write(f"Ticket: {ticket['ticket_id']}\n")
            f.write(f"Placa:  {ticket['placa']}\n")
            f.write(f"Entrada:   {ticket['hora_entrada']}\n")
            f.write(f"Pagamento: {ticket['hora_pagamento']}\n")
            f.write(f"Valor pago: R$ {ticket['valor']:.2f}\n")
            f.write(f"Liberado até: {ticket['liberado_ate']}\n")
            f.write("====================================\n")
            f.write("Obrigado por usar nosso serviço!\n")
        logging.info(f"Comprovante gerado em {path}")
    except Exception as e:
        logging.error(f"Falha ao gerar comprovante: {e}")

# —— GUI Tkinter ——
class PagamentoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Totem de Pagamento")
        self.geometry("480x400")
        self.resizable(False, False)
        self._build_widgets()
    
    def _build_widgets(self):
        # Entrada de ticket
        tk.Label(self, text="Código do Ticket:", font=("Arial", 12)).pack(pady=10)
        self.ticket_entry = tk.Entry(self, font=("Arial", 16), justify="center")
        self.ticket_entry.pack(pady=5)
        tk.Button(self, text="Buscar", width=10, command=self._buscar_ticket).pack(pady=5)
        
        # Frame de detalhes
        self.details_frame = tk.Frame(self)
        self.details_frame.pack(pady=10)
        
        # Botões de pagamento
        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack(pady=10)
        self.btn_cartao = tk.Button(self.btn_frame, text="💳 Cartão",  width=12, command=lambda: self._pagar("Cartão"))
        self.btn_pix    = tk.Button(self.btn_frame, text="📱 PIX",     width=12, command=lambda: self._pagar("PIX"))
        for btn in (self.btn_cartao, self.btn_pix):
            btn.pack(side="left", padx=10)
        self._toggle_payment_buttons(False)
    
    def _toggle_payment_buttons(self, enable: bool):
        state = "normal" if enable else "disabled"
        self.btn_cartao.config(state=state)
        self.btn_pix.config(state=state)
    
    def _buscar_ticket(self):
        tid = self.ticket_entry.get().strip().upper()
        tickets = carregar_tickets()
        for t in tickets:
            if t["ticket_id"] == tid:
                if t["pago"]:
                    messagebox.showinfo("Info", "Ticket já pago.")
                    return
                self.current_ticket = t
                self._mostrar_detalhes(t)
                return
        messagebox.showerror("Erro", "Ticket não encontrado.")
    
    def _mostrar_detalhes(self, ticket: Dict):
        for w in self.details_frame.winfo_children():
            w.destroy()
        valor, tol = calcular_valor_e_tolerancia(ticket["hora_entrada"])
        minutos = int((datetime.now() - datetime.strptime(ticket["hora_entrada"], "%Y-%m-%d %H:%M:%S")).total_seconds() // 60)
        
        info = (
            f"Placa: {ticket['placa']}\n"
            f"Estadia: {minutos} min\n"
            f"Valor: R$ {valor:.2f}\n"
            f"Tolerância: {tol} min"
        )
        tk.Label(self.details_frame, text=info, font=("Arial", 12), justify="left").pack()
        self.current_valor     = valor
        self.current_tolerancia = tol
        self._toggle_payment_buttons(True)
    
    def _pagar(self, metodo: str):
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            liberado = (datetime.now() + timedelta(minutes=self.current_tolerancia)).strftime("%Y-%m-%d %H:%M:%S")
            # Atualiza dados
            self.current_ticket.update({
                "pago": True,
                "hora_pagamento": now,
                "valor": self.current_valor,
                "liberado_ate": liberado
            })
            tickets = carregar_tickets()
            for i, t in enumerate(tickets):
                if t["ticket_id"] == self.current_ticket["ticket_id"]:
                    tickets[i] = self.current_ticket
                    break
            salvar_tickets(tickets)
            logging.info(f"Pagamento {metodo} para ticket {self.current_ticket['ticket_id']} - R$ {self.current_valor:.2f}")
            gerar_comprovante(self.current_ticket)
            
            messagebox.showinfo("Sucesso",
                f"Pagamento efetuado!\nValor: R$ {self.current_valor:.2f}\n"
                f"Liberado até: {liberado}")
            self._toggle_payment_buttons(False)
            self._clear_all()
        except Exception as e:
            logging.error(f"Erro no pagamento: {e}")
            messagebox.showerror("Erro", f"Falha ao processar pagamento.\n{e}")
    
    def _clear_all(self):
        self.ticket_entry.delete(0, tk.END)
        for w in self.details_frame.winfo_children():
            w.destroy()

if __name__ == "__main__":
    # Emissão de ticket de teste (pode comentar em produção)
    print("Ticket de exemplo:", emitir_ticket())
    app = PagamentoGUI()
    app.mainloop()
