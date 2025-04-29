import logging
import os

caminho = os.path.dirname(os.path.abspath(__file__))
# Verifica se o diretório de logs existe, caso contrário, cria um novo
if not os.path.exists(caminho):
    os.makedirs(caminho)
nome = "app.log"
log = os.path.join(caminho, nome)
# Configuração básica do logger
logging.basicConfig(
    filename=log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
