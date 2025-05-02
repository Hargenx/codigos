import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import DatabaseManager

class DashboardView(ttk.Frame):
    def __init__(self, parent, user_id, username, logout_callback):
        super().__init__(parent)
        self.parent = parent
        self.user_id = user_id
        self.username = username
        self.logout_callback = logout_callback
        self.db_manager = DatabaseManager()
        
        self.current_list_id = None
        self.current_list_name = None
        self.current_list_is_owned = True
        self.current_list_can_edit = True
        
        self._create_widgets()
        self._load_user_lists()
    
    def _create_widgets(self):
        """Cria os widgets da tela principal"""
        # Frame principal com duas colunas
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Coluna esquerda - listas
        self.lists_frame = ttk.Frame(self.main_frame, padding="10")
        self.lists_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5, pady=5)
        
        # Coluna direita - itens da lista
        self.items_frame = ttk.Frame(self.main_frame, padding="10")
        self.items_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barra superior
        self._create_top_bar()
        
        # Frame das listas
        self._create_lists_section()
        
        # Frame dos itens
        self._create_items_section()
    
    def _create_top_bar(self):
        """Cria a barra superior do dashboard"""
        top_bar = ttk.Frame(self)
        top_bar.pack(fill=tk.X, pady=10, padx=10)
        
        # Boas-vindas ao usuário
        welcome_text = f"Bem-vindo, {self.username}!"
        welcome_label = ttk.Label(top_bar, text=welcome_text, font=("Helvetica", 12, "bold"))
        welcome_label.pack(side=tk.LEFT)
        
        # Botão de logout
        logout_btn = ttk.Button(top_bar, text="Sair", command=self.logout_callback)
        logout_btn.pack(side=tk.RIGHT)
    
    def _create_lists_section(self):
        """Cria a seção de listas de compras"""
        # Título
        ttk.Label(
            self.lists_frame,
            text="Minhas Listas",
            font=("Helvetica", 14, "bold")
        ).pack(fill=tk.X, pady=(0, 10))
        
        # Botão para adicionar nova lista
        ttk.Button(
            self.lists_frame,
            text="Nova Lista",
            command=self._show_add_list_dialog
        ).pack(fill=tk.X, pady=(0, 10))
        
        # Frame para as listas
        lists_container = ttk.LabelFrame(self.lists_frame, text="Listas Próprias")
        lists_container.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.lists_treeview = ttk.Treeview(
            lists_container,
            columns=("name",),
            show="headings",
            height=10
        )
        self.lists_treeview.heading("name", text="Nome da Lista")
        self.lists_treeview.column("name", width=150)
        self.lists_treeview.pack(fill=tk.BOTH, expand=True, pady=5)
        self.lists_treeview.bind("<<TreeviewSelect>>", self._on_list_selected)
        
        # Frame para listas compartilhadas
        shared_lists_container = ttk.LabelFrame(self.lists_frame, text="Listas Compartilhadas")
        shared_lists_container.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.shared_lists_treeview = ttk.Treeview(
            shared_lists_container,
            columns=("name", "can_edit"),
            show="headings",
            height=10
        )
        self.shared_lists_treeview.heading("name", text="Nome da Lista")
        self.shared_lists_treeview.heading("can_edit", text="Pode Editar")
        self.shared_lists_treeview.column("name", width=150)
        self.shared_lists_treeview.column("can_edit", width=80)
        self.shared_lists_treeview.pack(fill=tk.BOTH, expand=True, pady=5)
        self.shared_lists_treeview.bind("<<TreeviewSelect>>", self._on_shared_list_selected)
        
        # Botões de ações com listas
        actions_frame = ttk.Frame(self.lists_frame)
        actions_frame.pack(fill=tk.X, pady=10)
        
        self.share_btn = ttk.Button(
            actions_frame,
            text="Compartilhar",
            command=self._show_share_list_dialog,
            state=tk.DISABLED
        )
        self.share_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            actions_frame,
            text="Excluir",
            command=self._delete_selected_list,
            style="Danger.TButton"
        ).pack(side=tk.RIGHT, padx=5)
    
    def _create_items_section(self):
        """Cria a seção de itens da lista"""
        # Título
        self.items_title = ttk.Label(
            self.items_frame,
            text="Selecione uma lista",
            font=("Helvetica", 14, "bold")
        )
        self.items_title.pack(fill=tk.X, pady=(0, 10))
        
        # Frame para adicionar item
        self.add_item_frame = ttk.LabelFrame(self.items_frame, text="Adicionar Item")
        self.add_item_frame.pack(fill=tk.X, pady=10)
        
        # Variáveis de controle para o novo item
        self.new_item_name = tk.StringVar()
        self.new_item_qty = tk.IntVar(value=1)
        self.new_item_category = tk.StringVar(value="Geral")
        
        # Grid de formulário para novo item
        form_frame = ttk.Frame(self.add_item_frame)
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(form_frame, textvariable=self.new_item_name).grid(row=0, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(form_frame, text="Quantidade:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Spinbox(form_frame, from_=1, to=100, textvariable=self.new_item_qty).grid(row=1, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(form_frame, text="Categoria:").grid(row=2, column=0, sticky=tk.W, pady=5)
        categories = ["Geral", "Frutas/Vegetais", "Carnes", "Laticínios", "Limpeza", "Higiene", "Outros"]
        ttk.Combobox(form_frame, textvariable=self.new_item_category, values=categories).grid(row=2, column=1, sticky=tk.EW, padx=5)
        
        form_frame.columnconfigure(1, weight=1)
        
        # Botão para adicionar item
        self.add_item_btn = ttk.Button(
            self.add_item_frame,
            text="Adicionar Item",
            command=self._add_new_item,
            state=tk.DISABLED
        )
        self.add_item_btn.pack(pady=10)
        
        # Tabela de itens
        items_list_frame = ttk.LabelFrame(self.items_frame, text="Itens da Lista")
        items_list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.items_treeview = ttk.Treeview(
            items_list_frame,
            columns=("name", "quantity", "category", "completed"),
            show="headings",
            height=15
        )
        self.items_treeview.heading("name", text="Nome")
        self.items_treeview.heading("quantity", text="Qtd")
        self.items_treeview.heading("category", text="Categoria")
        self.items_treeview.heading("completed", text="Comprado")
        
        self.items_treeview.column("name", width=150)
        self.items_treeview.column("quantity", width=50)
        self.items_treeview.column("category", width=100)
        self.items_treeview.column("completed", width=80)
        
        self.items_treeview.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Scrollbar para a tabela de itens
        items_scrollbar = ttk.Scrollbar(items_list_frame, orient=tk.VERTICAL, command=self.items_treeview.yview)
        self.items_treeview.configure(yscrollcommand=items_scrollbar.set)
        items_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        
        # Frame de ações para os itens
        items_actions_frame = ttk.Frame(self.items_frame)
        items_actions_frame.pack(fill=tk.X, pady=10)
        
        self.toggle_completed_btn = ttk.Button(
            items_actions_frame,
            text="Marcar como Comprado",
            command=self._toggle_item_completed,
            state=tk.DISABLED
        )
        self.toggle_completed_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_item_btn = ttk.Button(
            items_actions_frame,
            text="Excluir Item",
            command=self._delete_selected_item,
            state=tk.DISABLED
        )
        self.delete_item_btn.pack(side=tk.RIGHT, padx=5)
        
        # Configurar evento de seleção de item
        self.items_treeview.bind("<<TreeviewSelect>>", self._on_item_selected)
    
    def _load_user_lists(self):
        """Carrega as listas do usuário"""
        # Limpar as listas atuais
        for item in self.lists_treeview.get_children():
            self.lists_treeview.delete(item)
            
        for item in self.shared_lists_treeview.get_children():
            self.shared_lists_treeview.delete(item)
        
        # Buscar listas do banco de dados
        lists_data = self.db_manager.get_user_lists(self.user_id)
        
        # Adicionar listas próprias
        for list_data in lists_data["own_lists"]:
            list_id, name, is_shared, created_at, updated_at = list_data
            self.lists_treeview.insert("", tk.END, iid=list_id, values=(name,))
        
        # Adicionar listas compartilhadas
        for list_data in lists_data["shared_lists"]:
            list_id, name, is_shared, created_at, updated_at, can_edit = list_data
            edit_status = "Sim" if can_edit else "Não"
            self.shared_lists_treeview.insert("", tk.END, iid=list_id, values=(name, edit_status))
    
    def _load_list_items(self):
        """Carrega os itens da lista selecionada"""
        if not self.current_list_id:
            return
            
        # Limpar os itens atuais
        for item in self.items_treeview.get_children():
            self.items_treeview.delete(item)
        
        # Buscar itens do banco de dados
        items = self.db_manager.get_list_items(self.current_list_id)
        
        # Adicionar itens à tabela
        for item in items:
            item_id, name, quantity, category, completed = item
            completed_text = "✓" if completed else ""
            self.items_treeview.insert("", tk.END, iid=item_id, values=(name, quantity, category, completed_text))
    
    def _show_add_list_dialog(self):
        """Exibe diálogo para adicionar uma nova lista"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("Nova Lista")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Centralizar a janela
        dialog.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (dialog.winfo_width() // 2)
        y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Conteúdo do diálogo
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Nome da lista
        ttk.Label(frame, text="Nome da Lista:").pack(anchor=tk.W)
        list_name_var = tk.StringVar()
        list_name_entry = ttk.Entry(frame, textvariable=list_name_var, width=40)
        list_name_entry.pack(fill=tk.X, pady=10)
        list_name_entry.focus()
        
        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(
            btn_frame,
            text="Cancelar",
            command=dialog.destroy
        ).pack(side=tk.RIGHT)
        
        ttk.Button(
            btn_frame,
            text="Criar",
            command=lambda: self._create_new_list(list_name_var.get(), dialog)
        ).pack(side=tk.RIGHT, padx=10)
    
    def _create_new_list(self, list_name, dialog):
        """Cria uma nova lista de compras"""
        if not list_name:
            messagebox.showerror("Erro", "Por favor, digite um nome para a lista", parent=dialog)
            return
        
        success, message = self.db_manager.create_shopping_list(list_name, self.user_id)
        
        if success:
            dialog.destroy()
            self._load_user_lists()
            messagebox.showinfo("Sucesso", message)
        else:
            messagebox.showerror("Erro", message, parent=dialog)
    
    def _show_share_list_dialog(self):
        """Exibe diálogo para compartilhar uma lista"""
        if not self.current_list_id or not self.current_list_is_owned:
            return
        
        dialog = tk.Toplevel(self.parent)
        dialog.title(f"Compartilhar Lista: {self.current_list_name}")
        dialog.geometry("350x200")
        dialog.resizable(False, False)
        dialog.transient(self.parent)
        dialog.grab_set()
        
        # Centralizar a janela
        dialog.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (dialog.winfo_width() // 2)
        y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Conteúdo do diálogo
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Email do usuário
        ttk.Label(frame, text="Email do usuário:").pack(anchor=tk.W)
        user_email_var = tk.StringVar()
        user_email_entry = ttk.Entry(frame, textvariable=user_email_var, width=40)
        user_email_entry.pack(fill=tk.X, pady=10)
        user_email_entry.focus()
        
        # Permissões
        can_edit_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            frame,
            text="Permitir que o usuário edite a lista",
            variable=can_edit_var
        ).pack(anchor=tk.W, pady=10)
        
        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(
            btn_frame,
            text="Cancelar",
            command=dialog.destroy
        ).pack(side=tk.RIGHT)
        
        ttk.Button(
            btn_frame,
            text="Compartilhar",
            command=lambda: self._share_list_with_user(
                user_email_var.get(),
                can_edit_var.get(),
                dialog
            )
        ).pack(side=tk.RIGHT, padx=10)
    
    def _share_list_with_user(self, user_email, can_edit, dialog):
        """Compartilha a lista com outro usuário"""
        if not user_email:
            messagebox.showerror("Erro", "Por favor, digite o email do usuário", parent=dialog)
            return
        
        success, message = self.db_manager.share_list(self.current_list_id, user_email, can_edit)
        
        if success:
            dialog.destroy()
            self._load_user_lists()
            messagebox.showinfo("Sucesso", message)
        else:
            messagebox.showerror("Erro", message, parent=dialog)
    
    def _on_list_selected(self, event):
        """Trata a seleção de uma lista própria"""
        # Limpar seleção da outra lista
        self.shared_lists_treeview.selection_remove(self.shared_lists_treeview.selection())
        
        selection = self.lists_treeview.selection()
        if selection:
            list_id = selection[0]
            list_name = self.lists_treeview.item(list_id, "values")[0]
            
            self.current_list_id = list_id
            self.current_list_name = list_name
            self.current_list_is_owned = True
            self.current_list_can_edit = True
            
            # Atualiza título
            self.items_title.config(text=f"Lista: {list_name}")
            
            # Habilita botões de ação
            self.share_btn.config(state=tk.NORMAL)
            self.add_item_btn.config(state=tk.NORMAL)
            
            # Carrega itens da lista
            self._load_list_items()
    
    def _on_shared_list_selected(self, event):
        """Trata a seleção de uma lista compartilhada"""
        # Limpar seleção da outra lista
        self.lists_treeview.selection_remove(self.lists_treeview.selection())
        
        selection = self.shared_lists_treeview.selection()
        if selection:
            list_id = selection[0]
            values = self.shared_lists_treeview.item(list_id, "values")
            list_name = values[0]
            can_edit = values[1] == "Sim"
            
            self.current_list_id = list_id
            self.current_list_name = list_name
            self.current_list_is_owned = False
            self.current_list_can_edit = can_edit
            
            # Atualiza título
            self.items_title.config(text=f"Lista: {list_name} (Compartilhada)")
            
            # Configura botões de ação
            self.share_btn.config(state=tk.DISABLED)
            self.add_item_btn.config(state=tk.NORMAL if can_edit else tk.DISABLED)
            
            # Carrega itens da lista
            self._load_list_items()
    
    def _on_item_selected(self, event):
        """Trata a seleção de um item da lista"""
        selection = self.items_treeview.selection()
        if selection:
            # Habilita botões de ação para itens
            can_edit = self.current_list_is_owned or self.current_list_can_edit
            self.toggle_completed_btn.config(state=tk.NORMAL if can_edit else tk.DISABLED)
            self.delete_item_btn.config(state=tk.NORMAL if can_edit else tk.DISABLED)
            
            # Verifica se o item está marcado como comprado
            item_id = selection[0]
            values = self.items_treeview.item(item_id, "values")
            is_completed = values[3] == "✓"
            
            # Atualiza o texto do botão de acordo com o status
            btn_text = "Desmarcar como Comprado" if is_completed else "Marcar como Comprado"
            self.toggle_completed_btn.config(text=btn_text)
    
    def _add_new_item(self):
        """Adiciona um novo item à lista atual"""
        if not self.current_list_id:
            return
        
        name = self.new_item_name.get()
        quantity = self.new_item_qty.get()
        category = self.new_item_category.get()
        
        if not name:
            messagebox.showerror("Erro", "Por favor, digite um nome para o item")
            return
        
        success, message = self.db_manager.add_list_item(
            self.current_list_id,
            name,
            quantity,
            category
        )
        
        if success:
            # Limpa os campos
            self.new_item_name.set("")
            self.new_item_qty.set(1)
            self.new_item_category.set("Geral")
            
            # Recarrega os itens
            self._load_list_items()
        else:
            messagebox.showerror("Erro", message)
    
    def _toggle_item_completed(self):
        """Marca ou desmarca um item como comprado"""
        selection = self.items_treeview.selection()
        if not selection:
            return
        
        item_id = selection[0]
        values = self.items_treeview.item(item_id, "values")
        is_completed = values[3] == "✓"
        
        success, message = self.db_manager.toggle_item_completed(
            item_id,
            not is_completed
        )
        
        if success:
            self._load_list_items()
        else:
            messagebox.showerror("Erro", message)
    
    def _delete_selected_item(self):
        """Remove o item selecionado"""
        selection = self.items_treeview.selection()
        if not selection:
            return
        
        item_id = selection[0]
        item_name = self.items_treeview.item(item_id, "values")[0]
        
        confirm = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o item '{item_name}'?"
        )
        
        if confirm:
            success, message = self.db_manager.delete_list_item(item_id)
            
            if success:
                self._load_list_items()
            else:
                messagebox.showerror("Erro", message)
    
    def _delete_selected_list(self):
        """Remove a lista selecionada"""
        # Esta função seria implementada em uma versão mais completa do sistema
        pass