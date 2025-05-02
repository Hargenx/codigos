import tkinter as tk
from tkinter import messagebox
from views.login_view import LoginView
from database.db_manager import DatabaseManager

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("PurchasePal - Sistema de Controle de Compras")
        self.geometry("800x600")
        self.configure(bg="#f5f5f5")
        
        # Inicializa o banco de dados
        self.db_manager = DatabaseManager()
        self.db_manager.setup_database()
        
        # Configura o frame atual como login
        self.current_frame = None
        self.show_login()
        
    def show_login(self):
        """Exibe a tela de login"""
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = LoginView(self, self.switch_to_dashboard)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def switch_to_dashboard(self, user_id, username):
        """Muda para o dashboard após o login bem-sucedido"""
        from views.dashboard_view import DashboardView
        
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = DashboardView(self, user_id, username, self.show_login)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop()