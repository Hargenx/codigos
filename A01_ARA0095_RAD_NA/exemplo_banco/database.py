import sqlite3
import csv
from pathlib import Path
from typing import List, Tuple
from models.Pessoa import Pessoa
from models.Marca import Marca
from models.Veiculo import Veiculo
from logger import log_info, log_error

# Define o diretório base dinamicamente
BASE_DIR = Path(__file__).resolve().parent


class ConexaoBanco:
    def __init__(self) -> None:
        try:
            # Banco de dados na raiz do projeto
            db_path = BASE_DIR / "veiculos.sqlite"
            self.conexao = sqlite3.connect(db_path)
            self.cursor = self.conexao.cursor()
            log_info(f"Conectado ao banco SQLite em {db_path}.")
            self.criar_tabelas()
        except sqlite3.Error as e:
            log_error(f"Erro ao conectar ao banco: {e}")
            raise

    def criar_tabelas(self) -> None:
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS pessoa (
                    cpf TEXT PRIMARY KEY,
                    nome TEXT,
                    nascimento TEXT,
                    oculos BOOLEAN
                )
            """
            )
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS marca (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    sigla TEXT
                )
            """
            )
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS veiculo (
                    placa TEXT PRIMARY KEY,
                    cor TEXT,
                    proprietario_cpf TEXT,
                    marca_id INTEGER,
                    FOREIGN KEY (proprietario_cpf) REFERENCES pessoa(cpf),
                    FOREIGN KEY (marca_id) REFERENCES marca(id)
                )
            """
            )
            self.conexao.commit()
            log_info("Tabelas criadas com sucesso.")
        except sqlite3.Error as e:
            log_error(f"Erro ao criar tabelas: {e}")
            raise

    def inserir_pessoa(self, pessoa: Pessoa) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)",
                (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos),
            )
            self.conexao.commit()
            log_info("Pessoa inserida com sucesso.")
        except sqlite3.Error as e:
            log_error(f"Erro ao inserir pessoa: {e}")
            raise

    def inserir_marca(self, marca: Marca) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO marca (nome, sigla) VALUES (?, ?)",
                (marca.nome, marca.sigla),
            )
            self.conexao.commit()
            log_info("Marca inserida com sucesso.")
        except sqlite3.Error as e:
            log_error(f"Erro ao inserir marca: {e}")
            raise

    def inserir_veiculo(self, veiculo: Veiculo) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO veiculo (placa, cor, proprietario_cpf, marca_id) VALUES (?, ?, ?, ?)",
                (
                    veiculo.placa,
                    veiculo.cor,
                    veiculo.proprietario_cpf,
                    veiculo.marca_id,
                ),
            )
            self.conexao.commit()
            log_info("Veículo inserido com sucesso.")
        except sqlite3.Error as e:
            log_error(f"Erro ao inserir veículo: {e}")
            raise

        def atualizar_pessoa(self, cpf: str, novo_nome: str, novo_oculos: bool) -> None:
        try:
            self.cursor.execute(
                """
                UPDATE pessoa
                SET nome = ?, oculos = ?
                WHERE cpf = ?
                """,
                (novo_nome, novo_oculos, cpf),
            )
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                log_info(f"Pessoa com CPF {cpf} atualizada com sucesso.")
            else:
                log_info(f"Nenhuma pessoa encontrada com o CPF {cpf}. Nenhuma alteração feita.")
        except sqlite3.Error as e:
            log_error(f"Erro ao atualizar pessoa com CPF {cpf}: {e}")
            raise
        
    def remover_pessoa(self, cpf: str) -> None:
        try:
            self.cursor.execute(
                "DELETE FROM pessoa WHERE cpf = ?",
                (cpf,)
            )
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                log_info(f"Pessoa com CPF {cpf} removida com sucesso.")
            else:
                log_info(f"Nenhuma pessoa encontrada com o CPF {cpf}. Nenhuma remoção realizada.")
        except sqlite3.Error as e:
            log_error(f"Erro ao remover pessoa com CPF {cpf}: {e}")
            raise


    def buscar_veiculos(self) -> List[Tuple]:
        try:
            self.cursor.execute(
                """
                SELECT v.placa, v.cor, p.nome, m.nome
                FROM veiculo v
                JOIN pessoa p ON v.proprietario_cpf = p.cpf
                JOIN marca m ON v.marca_id = m.id
            """
            )
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            log_error(f"Erro ao buscar veículos: {e}")
            raise

    def exportar_veiculos_csv(self) -> None:
        try:
            veiculos = self.buscar_veiculos()
            export_dir = BASE_DIR / "export"
            export_dir.mkdir(exist_ok=True)

            export_path = export_dir / "veiculos.csv"
            with open(
                export_path, mode="w", newline="", encoding="utf-8"
            ) as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerow(["Placa", "Cor", "Proprietário", "Marca"])
                writer.writerows(veiculos)

            log_info(
                f"Exportação de veículos para CSV concluída com sucesso em {export_path}."
            )
        except sqlite3.Error as e:
            log_error(f"Erro ao exportar veículos para CSV: {e}")
            raise
        except OSError as e:
            log_error(f"Erro de sistema de arquivos ao exportar CSV: {e}")
            raise

    def close(self) -> None:
        try:
            self.cursor.close()
            self.conexao.close()
            log_info("Conexão SQLite encerrada.")
        except sqlite3.Error as e:
            log_error(f"Erro ao fechar a conexão SQLite: {e}")
            raise
