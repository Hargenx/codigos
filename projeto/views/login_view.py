import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import DatabaseManager

class LoginView(ttk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.parent = parent
        self.on_login_success = on_login_success
        self.db_manager = DatabaseManager()
        
        self.configure(padding="20")
        
        # Criar variáveis de controle
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.reg_username_var = tk.StringVar()
        self.reg_email_var = tk.StringVar()
        self.reg_password_var = tk.StringVar()
        self.reg_confirm_password_var = tk.StringVar()
        
        # Notebook para alternar entre login e registro
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Frame de login
        self.login_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.login_frame, text="Login")
        
        # Frame de registro
        self.register_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.register_frame, text="Registro")
        
        self._create_login_form()
        self._create_register_form()
        
    def _create_login_form(self):
        """Cria o formulário de login"""
        # Título
        ttk.Label(
            self.login_frame, 
            text="PurchasePal", 
            font=("Helvetica", 24)
        ).pack(pady=(0, 20))
        
        # Formulário
        form_frame = ttk.Frame(self.login_frame)
        form_frame.pack(fill=tk.BOTH, pady=20)
        
        # Usuário
        ttk.Label(form_frame, text="Nome de Usuário:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.username_var, width=40).pack(fill=tk.X, pady=(0, 15))
        
        # Senha
        ttk.Label(form_frame, text="Senha:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.password_var, show="*", width=40).pack(fill=tk.X)
        
        # Botão de login
        ttk.Button(
            form_frame, 
            text="Entrar",
            command=self._handle_login
        ).pack(pady=20)
        
    def _create_register_form(self):
        """Cria o formulário de registro"""
        # Título
        ttk.Label(
            self.register_frame, 
            text="Registrar Conta", 
            font=("Helvetica", 18)
        ).pack(pady=(0, 20))
        
        # Formulário
        form_frame = ttk.Frame(self.register_frame)
        form_frame.pack(fill=tk.BOTH, pady=10)
        
        # Usuário
        ttk.Label(form_frame, text="Nome de Usuário:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.reg_username_var, width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Email
        ttk.Label(form_frame, text="Email:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.reg_email_var, width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Senha
        ttk.Label(form_frame, text="Senha:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.reg_password_var, show="*", width=40).pack(fill=tk.X, pady=(0, 10))
        
        # Confirmação de Senha
        ttk.Label(form_frame, text="Confirmar Senha:").pack(anchor=tk.W, pady=(0, 5))
        ttk.Entry(form_frame, textvariable=self.reg_confirm_password_var, show="*", width=40).pack(fill=tk.X)
        
        # Botão de registro
        ttk.Button(
            form_frame, 
            text="Registrar",
            command=self._handle_register
        ).pack(pady=20)
    
    def _handle_login(self):
        """Processa o login do usuário"""
        username = self.username_var.get()
        password = self.password_var.get()
        
        if not username or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        user, message = self.db_manager.authenticate_user(username, password)
        
        if user:
            messagebox.showinfo("Sucesso", message)
            self.on_login_success(user[0], user[1])  # Passa id e username
        else:
            messagebox.showerror("Erro", message)
    
    def _handle_register(self):
        """Processa o registro de um novo usuário"""
        username = self.reg_username_var.get()
        email = self.reg_email_var.get()
        password = self.reg_password_var.get()
        confirm_password = self.reg_confirm_password_var.get()
        
        if not username or not email or not password or not confirm_password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem")
            return
        
        success, message = self.db_manager.register_user(username, email, password)
        
        if success:
            messagebox.showinfo("Sucesso", message)
            self.notebook.select(0)  # Volta para a aba de login
            
            # Limpa os campos de registro
            self.reg_username_var.set("")
            self.reg_email_var.set("")
            self.reg_password_var.set("")
            self.reg_confirm_password_var.set("")
        else:
            messagebox.showerror("Erro", message)