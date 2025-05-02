import sqlite3
import os
import hashlib
from datetime import datetime

caminho = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(caminho, "purchasepal.db")
class DatabaseManager:
    def __init__(self, db_name=caminho):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
            
    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            
    def setup_database(self):
        """Configura o banco de dados e cria tabelas se não existirem"""
        if not self.connect():
            return False
            
        try:
            # Tabela de usuários
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Tabela de listas de compras
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS shopping_lists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    owner_id INTEGER NOT NULL,
                    is_shared BOOLEAN DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (owner_id) REFERENCES users (id)
                )
            ''')
            
            # Tabela de itens das listas
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS list_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    list_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    quantity INTEGER DEFAULT 1,
                    category TEXT DEFAULT 'Geral',
                    completed BOOLEAN DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (list_id) REFERENCES shopping_lists (id)
                )
            ''')
            
            # Tabela para controle de compartilhamento de listas
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS shared_users (
                    list_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    can_edit BOOLEAN DEFAULT 0,
                    PRIMARY KEY (list_id, user_id),
                    FOREIGN KEY (list_id) REFERENCES shopping_lists (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao configurar o banco de dados: {e}")
            return False
        finally:
            self.close()
            
    def register_user(self, username, email, password):
        """Registra um novo usuário no sistema"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            # Verifica se o usuário já existe
            self.cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
            if self.cursor.fetchone():
                return False, "Nome de usuário ou email já existe"
                
            # Hash da senha para armazenamento seguro
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Insere o novo usuário
            self.cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )
            self.conn.commit()
            return True, "Usuário registrado com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro no registro: {e}"
        finally:
            self.close()
            
    def authenticate_user(self, username, password):
        """Autentica um usuário no sistema"""
        if not self.connect():
            return None, "Erro ao conectar ao banco de dados"
            
        try:
            # Hash da senha para comparação
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Busca o usuário
            self.cursor.execute(
                "SELECT id, username FROM users WHERE username = ? AND password = ?", 
                (username, hashed_password)
            )
            user = self.cursor.fetchone()
            
            if user:
                return user, "Login bem-sucedido"
            else:
                return None, "Nome de usuário ou senha incorretos"
        except sqlite3.Error as e:
            return None, f"Erro na autenticação: {e}"
        finally:
            self.close()
    
    def get_user_lists(self, user_id):
        """Obtém todas as listas de compras de um usuário"""
        if not self.connect():
            return []
            
        try:
            # Busca listas próprias do usuário
            self.cursor.execute("""
                SELECT id, name, is_shared, created_at, updated_at 
                FROM shopping_lists 
                WHERE owner_id = ?
                ORDER BY updated_at DESC
            """, (user_id,))
            own_lists = self.cursor.fetchall()
            
            # Busca listas compartilhadas com o usuário
            self.cursor.execute("""
                SELECT sl.id, sl.name, sl.is_shared, sl.created_at, sl.updated_at, su.can_edit 
                FROM shopping_lists sl
                JOIN shared_users su ON sl.id = su.list_id
                WHERE su.user_id = ?
                ORDER BY sl.updated_at DESC
            """, (user_id,))
            shared_lists = self.cursor.fetchall()
            
            return {"own_lists": own_lists, "shared_lists": shared_lists}
        except sqlite3.Error as e:
            print(f"Erro ao buscar listas: {e}")
            return {"own_lists": [], "shared_lists": []}
        finally:
            self.close()
    
    def create_shopping_list(self, name, owner_id):
        """Cria uma nova lista de compras"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                "INSERT INTO shopping_lists (name, owner_id, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (name, owner_id, now, now)
            )
            self.conn.commit()
            return True, "Lista criada com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro ao criar lista: {e}"
        finally:
            self.close()
    
    def share_list(self, list_id, user_email, can_edit):
        """Compartilha uma lista com outro usuário"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            # Verifica se o usuário existe
            self.cursor.execute("SELECT id FROM users WHERE email = ?", (user_email,))
            user = self.cursor.fetchone()
            
            if not user:
                return False, "Usuário não encontrado"
            
            user_id = user[0]
            
            # Atualiza status de compartilhamento da lista
            self.cursor.execute(
                "UPDATE shopping_lists SET is_shared = 1 WHERE id = ?", 
                (list_id,)
            )
            
            # Adiciona o compartilhamento
            self.cursor.execute(
                "INSERT OR REPLACE INTO shared_users (list_id, user_id, can_edit) VALUES (?, ?, ?)",
                (list_id, user_id, 1 if can_edit else 0)
            )
            self.conn.commit()
            return True, "Lista compartilhada com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro ao compartilhar lista: {e}"
        finally:
            self.close()
    
    def get_list_items(self, list_id):
        """Obtém todos os itens de uma lista de compras"""
        if not self.connect():
            return []
            
        try:
            self.cursor.execute("""
                SELECT id, name, quantity, category, completed
                FROM list_items
                WHERE list_id = ?
                ORDER BY completed, category, name
            """, (list_id,))
            
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar itens: {e}")
            return []
        finally:
            self.close()
    
    def add_list_item(self, list_id, name, quantity, category):
        """Adiciona um item à lista de compras"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                """INSERT INTO list_items 
                   (list_id, name, quantity, category, created_at, updated_at) 
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (list_id, name, quantity, category, now, now)
            )
            self.conn.commit()
            return True, "Item adicionado com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro ao adicionar item: {e}"
        finally:
            self.close()
    
    def toggle_item_completed(self, item_id, completed):
        """Marca ou desmarca um item como comprado"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                "UPDATE list_items SET completed = ?, updated_at = ? WHERE id = ?",
                (1 if completed else 0, now, item_id)
            )
            self.conn.commit()
            return True, "Item atualizado com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro ao atualizar item: {e}"
        finally:
            self.close()
    
    def delete_list_item(self, item_id):
        """Remove um item da lista de compras"""
        if not self.connect():
            return False, "Erro ao conectar ao banco de dados"
            
        try:
            self.cursor.execute("DELETE FROM list_items WHERE id = ?", (item_id,))
            self.conn.commit()
            return True, "Item removido com sucesso"
        except sqlite3.Error as e:
            return False, f"Erro ao remover item: {e}"
        finally:
            self.close()