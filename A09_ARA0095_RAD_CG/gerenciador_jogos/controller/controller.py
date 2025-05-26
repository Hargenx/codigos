import logging
from model.database import Database

class Controller:
    def __init__(self, db: Database):
        self.db = db

    def autenticar_usuario(self, usuario: str, senha: str) -> bool:
        user = self.db.buscar_usuario(usuario, senha)
        logging.info(f"Login de '{usuario}' - {'OK' if user else 'Falha'}")
        return user is not None

    def registrar_usuario(self, usuario: str, senha: str) -> bool:
        sucesso = self.db.inserir_usuario(usuario, senha)
        logging.info(f"Registro de '{usuario}' - {'OK' if sucesso else 'Falha'}")
        return sucesso

    def cadastrar_jogo(self, titulo: str, genero: str, nota: float) -> bool:
        sucesso = self.db.inserir_jogo(titulo, genero, nota)
        logging.info(f"Cadastro jogo '{titulo}' - {'OK' if sucesso else 'Erro'}")
        return sucesso

    def listar_jogos(self):
        return self.db.buscar_jogos()

    def remover_jogo(self, jogo_id: int) -> bool:
        sucesso = self.db.excluir_jogo(jogo_id)
        logging.info(f"Remocao jogo ID {jogo_id} - {'OK' if sucesso else 'Erro'}")
        return sucesso

    def editar_jogo(self, jogo_id: int, titulo: str, genero: str, nota: float) -> bool:
        sucesso = self.db.editar_jogo(jogo_id, titulo, genero, nota)
        logging.info(f"Edicao jogo ID {jogo_id} - {'OK' if sucesso else 'Erro'}")
        return sucesso
