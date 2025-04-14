import sqlite3
import psycopg2
import mysql.connector
from typing import Union, List, Tuple
from models.Pessoa import Pessoa
from models.Marca import Marca
from models.Veiculo import Veiculo
from logger import log_info, log_error


class ConexaoBanco:
    def __init__(self, tipo_banco: str = "sqlite") -> None:
        self.tipo_banco = tipo_banco
        self.conexao: Union[
            sqlite3.Connection,
            psycopg2.extensions.connection,
            mysql.connector.MySQLConnection,
            None,
        ] = None
        self.cursor: Union[
            sqlite3.Cursor,
            psycopg2.extensions.cursor,
            mysql.connector.cursor.MySQLCursor,
            None,
        ] = None

        # Cria o banco antes de conectar, se necessário
        self.criar_banco_de_dados()
        self.conectar()
        self.criar_tabelas()

    def criar_banco_de_dados(self) -> None:
        try:
            if self.tipo_banco == "postgres":
                temp_conn = psycopg2.connect(
                    dbname="veiculos.db",
                    user="postgres",
                    password="123456",
                    host="localhost",
                    port="5432",
                )
                temp_conn.autocommit = True
                temp_cursor = temp_conn.cursor()
                temp_cursor.execute(
                    f"SELECT 1 FROM pg_database WHERE datname = {self.dbname}"
                )
                exists = temp_cursor.fetchone()
                if not exists:
                    temp_cursor.execute(f"CREATE DATABASE {self.dbname}")
                    log_info("Banco de dados PostgreSQL criado com sucesso.")
                temp_cursor.close()
                temp_conn.close()

            elif self.tipo_banco == "mysql":
                temp_conn = mysql.connector.connect(
                    host="localhost", user="root", password="1234"
                )
                temp_cursor = temp_conn.cursor()
                temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.dbname}")
                log_info("Banco de dados MySQL criado com sucesso.")
                temp_cursor.close()
                temp_conn.close()

            # SQLite cria automaticamente ao conectar, não precisa ação manual
        except Exception as e:
            log_error(f"Erro ao criar banco de dados: {e}")
            raise e

    def conectar(self) -> None:
        try:
            if self.tipo_banco == "sqlite":
                self.conexao = sqlite3.connect("veiculos.db")
            elif self.tipo_banco == "postgres":
                self.conexao = psycopg2.connect(
                    dbname="veiculos.db",
                    user="postgres",
                    password="123456",
                    host="localhost",
                    port="5432",
                )
            elif self.tipo_banco == "mysql":
                self.conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="veiculos.db",
                )
            else:
                raise ValueError("Tipo de banco de dados não suportado.")

            self.cursor = self.conexao.cursor()
            log_info(f"Conectado ao banco de dados: {self.tipo_banco}")
            print(f"[INFO] Conectado ao banco de dados: {self.tipo_banco}")

        except Exception as e:
            log_error(f"Erro ao conectar ao banco de dados: {e}")
            raise e

    def criar_tabelas(self) -> None:
        try:
            # Definições corretas para chaves primárias auto-incrementadas
            if self.tipo_banco == "postgres":
                id_definicao = "SERIAL PRIMARY KEY"
            elif self.tipo_banco == "mysql":
                id_definicao = "INTEGER PRIMARY KEY AUTO_INCREMENT"
            else:  # SQLite
                id_definicao = "INTEGER PRIMARY KEY"

            tabelas = [
                (
                    "CREATE TABLE IF NOT EXISTS pessoa ("
                    "cpf VARCHAR(14) PRIMARY KEY,"
                    "nome VARCHAR(255),"
                    "nascimento DATE,"
                    "oculos BOOLEAN"
                    ")"
                ),
                (
                    f"CREATE TABLE IF NOT EXISTS marca ("
                    f"id {id_definicao},"
                    f"nome VARCHAR(255),"
                    f"sigla VARCHAR(10)"
                    ")"
                ),
                (
                    "CREATE TABLE IF NOT EXISTS veiculo ("
                    "placa VARCHAR(20) PRIMARY KEY,"
                    "cor VARCHAR(50),"
                    "proprietario_cpf VARCHAR(14),"
                    "marca_id INTEGER,"
                    "FOREIGN KEY (proprietario_cpf) REFERENCES pessoa(cpf),"
                    "FOREIGN KEY (marca_id) REFERENCES marca(id)"
                    ")"
                ),
            ]

            for tabela in tabelas:
                self.cursor.execute(tabela)

            self.conexao.commit()
            log_info("Tabelas criadas com sucesso.")

        except Exception as e:
            log_error(f"Erro ao criar tabelas: {e}")
            raise e

    # 🧩 Métodos de inserção e busca — mantenho parametrizados, seguro e limpo
    def inserir_pessoa(self, pessoa: Pessoa) -> None:
        try:
            sql = "INSERT INTO pessoa (cpf, nome, nascimento, oculos) VALUES (%s, %s, %s, %s)"
            params = (pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos)

            if self.tipo_banco == "sqlite":
                sql = sql.replace("%s", "?")

            self.cursor.execute(sql, params)
            self.conexao.commit()
            log_info("Pessoa inserida com sucesso.")

        except Exception as e:
            log_error(f"Erro ao inserir pessoa: {e}")
            raise e

    def inserir_marca(self, marca: Marca) -> None:
        try:
            sql = "INSERT INTO marca (nome, sigla) VALUES (%s, %s)"
            params = (marca.nome, marca.sigla)

            if self.tipo_banco == "sqlite":
                sql = sql.replace("%s", "?")

            self.cursor.execute(sql, params)
            self.conexao.commit()
            log_info("Marca inserida com sucesso.")

        except Exception as e:
            log_error(f"Erro ao inserir marca: {e}")
            raise e

    def inserir_veiculo(self, veiculo: Veiculo) -> None:
        try:
            sql = "INSERT INTO veiculo (placa, cor, proprietario_cpf, marca_id) VALUES (%s, %s, %s, %s)"
            params = (
                veiculo.placa,
                veiculo.cor,
                veiculo.proprietario_cpf,
                veiculo.marca_id,
            )

            if self.tipo_banco == "sqlite":
                sql = sql.replace("%s", "?")

            self.cursor.execute(sql, params)
            self.conexao.commit()
            log_info("Veículo inserido com sucesso.")

        except Exception as e:
            log_error(f"Erro ao inserir veículo: {e}")
            raise e

    def buscar_veiculos(self) -> List[Tuple]:
        try:
            self.cursor.execute(
                "SELECT placa, cor, proprietario_cpf, marca_id FROM veiculo"
            )
            resultados = self.cursor.fetchall()
            log_info("Consulta de veículos realizada com sucesso.")
            return resultados

        except Exception as e:
            log_error(f"Erro ao consultar veículos: {e}")
            raise e

    def close(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
        log_info(f"Conexão com o banco de dados {self.tipo_banco} encerrada.")
        print(f"[INFO] Conexão com o banco de dados {self.tipo_banco} encerrada.")
