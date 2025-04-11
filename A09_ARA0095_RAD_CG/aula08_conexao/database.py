import sqlite3
import psycopg2
import mysql.connector

class DatabaseConnection:
    def __init__(self, db_type="sqlite"):
        self.db_type = db_type
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.db_type == "sqlite":
            self.conn = sqlite3.connect("books.db")
        elif self.db_type == "postgres":
            self.conn = psycopg2.connect(
                dbname="book_exemplo",
                user="postgres",
                password="postgress",
                host="localhost",
                port="5432"
            )
        elif self.db_type == "mysql":
            self.conn = mysql.connector.connect(
                host="localhost",
                user=root",
                password="123456",
                database="book_exemplo"
            )
        else:
            raise ValueError("Unsupported database type")
        self.cursor = self.conn.cursor()
        print(f"Connected to {self.db_type} database.")

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(255),
            author VARCHAR(255),
            year INTEGER
        )
        """
        if self.db_type == "sqlite":
            create_table_sql = create_table_sql.replace("AUTO_INCREMENT", "AUTOINCREMENT")
        elif self.db_type == "postgres":
            create_table_sql = create_table_sql.replace("AUTO_INCREMENT", "SERIAL")

        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_book(self, title, author, year):
        sql = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
        params = (title, author, year)

        # SQLite usa ?
        if self.db_type == "sqlite":
            sql = sql.replace("%s", "?")

        self.cursor.execute(sql, params)
        self.conn.commit()

    def fetch_books(self):
        self.cursor.execute("SELECT title, author, year FROM books")
        return self.cursor.fetchall()

    def remove_book(self, title):
        sql = "DELETE FROM books WHERE title = %s"
        if self.db_type == "sqlite":
            sql = sql.replace("%s", "?")
        self.cursor.execute(sql, (title,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
        print(f"{self.db_type} connection closed.")
