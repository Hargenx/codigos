import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os
import logging
from typing import Dict, List

# Arquivos usados
ARQUIVO_JSON = "pagamentos.json"
ARQUIVO_LOG = "registro.log"

# Configuração do log
logging.basicConfig(
    filename=ARQUIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def inicializar_json() -> None:
    """Cria o arquivo JSON se não existir."""
    if not os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, mode="w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
        except OSError as e:
            logging.error(f"Erro ao criar arquivo JSON: {e}")
            raise

def registrar_pagamento(placa: str) -> None:
    """Salva a placa no JSON e registra no log."""
    pagamento: Dict[str, str] = {
        "placa": placa.upper(),
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(ARQUIVO_JSON, mode="r+", encoding="utf-8") as f:
            dados: List[Dict[str, str]] = json.load(f)
            dados.append(pagamento)
            f.seek(0)
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except (OSError, json.JSONDecodeError) as e:
        logging.error(f"Erro ao registrar pagamento: {e}")
        raise

    logging.info(f"Pagamento registrado para placa {placa.upper()}")

class TotemApp(tk.Tk):
    """Simulador de Totem de Estacionamento com teclado virtual."""
    def __init__(self) -> None:
        super().__init__()
        self.title("Simulador de Totem")
        self.geometry("500x500")
        self.resizable(False, False)
        inicializar_json()
        self.placa_digitada = ""
        self._tela_inicial()

    def _tela_inicial(self) -> None:
        self._limpar_tela()
        tk.Label(self, text="Estacionamento Inteligente", font=("Arial", 18)).pack(pady=30)
        tk.Button(self, text="Iniciar", font=("Arial", 14), command=self._tela_teclado).pack(pady=10)

    def _tela_teclado(self) -> None:
        self._limpar_tela()
        self.placa_digitada = ""
        self.display = tk.Label(self, text="", font=("Arial", 22), relief="sunken", width=15)
        self.display.pack(pady=10)

        teclado_qwerty = [
            "1234567890",
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"
        ]

        for linha in teclado_qwerty:
            frame = tk.Frame(self)
            frame.pack(pady=2)
            for letra in linha:
                tk.Button(
                    frame, text=letra, width=4, height=2,
                    font=("Arial", 12),
                    command=lambda l=letra: self._adicionar_letra(l)
                ).pack(side="left", padx=2)

        botoes_frame = tk.Frame(self)
        botoes_frame.pack(pady=15)

        tk.Button(botoes_frame, text="Corrigir", width=10, command=self._corrigir).pack(side="left", padx=10)
        tk.Button(botoes_frame, text="Cancelar", width=10, command=self._tela_inicial).pack(side="left", padx=10)
        tk.Button(botoes_frame, text="Confirmar", width=10, command=self._confirmar).pack(side="left", padx=10)

    def _adicionar_letra(self, letra: str) -> None:
        if len(self.placa_digitada) < 7:
            self.placa_digitada += letra
            self.display.config(text=self.placa_digitada)

    def _corrigir(self) -> None:
        self.placa_digitada = self.placa_digitada[:-1]
        self.display.config(text=self.placa_digitada)

    def _confirmar(self) -> None:
        placa = self.placa_digitada.strip().upper()
        if not self._validar_placa(placa):
            messagebox.showerror("Erro", "Placa inválida. Digite 7 ou mais caracteres.")
            return
        try:
            registrar_pagamento(placa)
            messagebox.showinfo("Sucesso", f"Pagamento registrado para: {placa}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar pagamento: {e}")
        self._tela_inicial()

    def _limpar_tela(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()

    @staticmethod
    def _validar_placa(placa: str) -> bool:
        return len(placa) >= 7 and placa.isalnum()

if __name__ == "__main__":
    app = TotemApp()
    app.mainloop()
