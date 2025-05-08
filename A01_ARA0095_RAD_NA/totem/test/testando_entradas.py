import json
import os
import logging
from datetime import datetime
import uuid
import random
import string
from typing import Dict, List

ARQUIVO_TICKETS = "tickets.json"
ARQUIVO_LOG = "log_estacionamento.log"

# Configuração de log
logging.basicConfig(
    filename=ARQUIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def inicializar_json() -> None:
    if not os.path.exists(ARQUIVO_TICKETS):
        with open(ARQUIVO_TICKETS, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def gerar_placa_aleatoria() -> str:
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return f"{letras}{numeros}"

def emitir_ticket(placa: str = "") -> str:
    inicializar_json()

    if not placa:
        placa = gerar_placa_aleatoria()

    ticket_id = str(uuid.uuid4())[:8].upper()
    hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro: Dict[str, str] = {
        "ticket_id": ticket_id,
        "placa": placa.upper(),
        "hora_entrada": hora_entrada,
        "pago": "nao",
        "hora_pagamento": "",
        "valor": "",
        "liberado_ate": ""
    }

    try:
        with open(ARQUIVO_TICKETS, "r+", encoding="utf-8") as f:
            dados: List[Dict] = json.load(f)
            dados.append(registro)
            f.seek(0)
            json.dump(dados, f, indent=4, ensure_ascii=False)
        logging.info(f"Entrada registrada: Ticket {ticket_id}, Placa {placa.upper()}")
    except Exception as e:
        logging.error(f"Erro ao registrar entrada: {e}")
        raise

    return ticket_id

# Teste manual
if __name__ == "__main__":
    print("Teste de emissão de ticket:")
    placa = input("Digite a placa (ou pressione Enter para gerar aleatoriamente): ").strip()
    ticket = emitir_ticket(placa)
    print(f"Ticket gerado com sucesso: {ticket}")
