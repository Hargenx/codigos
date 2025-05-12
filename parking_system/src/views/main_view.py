import tkinter as tk
from tkinter import ttk, filedialog
from .components.vehicle_form import VehicleForm
from .components.dashboard import Dashboard
from .components.logs import LogViewer
from .styles import StyleManager

class MainView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.style_manager = StyleManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Configura a interface principal"""
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Painel esquerdo (controle)
        self.control_frame = ttk.Frame(self.main_frame, width=300)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        self.control_frame.pack_propagate(False)
        
        # Painel direito (dashboard e logs)
        self.dashboard_frame = ttk.Frame(self.main_frame)
        self.dashboard_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Componentes
        self.setup_control_section()
        self.setup_dashboard_section()
    
    def setup_control_section(self):
        """Configura a seção de controle"""
        # Formulário de veículos
        self.vehicle_form = VehicleForm(
            self.control_frame, 
            on_submit=lambda data: self.controller.handle_vehicle_entry(data),
            on_exit=lambda plate: self.controller.handle_vehicle_exit(plate)
        )
        self.vehicle_form.pack(fill=tk.X, pady=5)
        
        # Lista de veículos estacionados
        ttk.Label(self.control_frame, text="Veículos no Estacionamento", style='Header.TLabel').pack(pady=(20, 5))
        
        self.parked_tree = ttk.Treeview(
            self.control_frame, 
            columns=('plate', 'model', 'type'), 
            show='headings', 
            height=10
        )
        self.parked_tree.heading('plate', text='Placa')
        self.parked_tree.heading('model', text='Modelo')
        self.parked_tree.heading('type', text='Tipo')
        self.parked_tree.column('plate', width=80)
        self.parked_tree.column('model', width=100)
        self.parked_tree.column('type', width=70)
        self.parked_tree.pack(fill=tk.BOTH, expand=True)
        
        # Botão para exportar dados
        export_btn = ttk.Button(
            self.control_frame, 
            text="Exportar Dados", 
            command=self.controller.handle_export_data,
            style='Accent.TButton'
        )
        export_btn.pack(fill=tk.X, pady=(10, 0))
    
    def setup_dashboard_section(self):
        """Configura a seção de dashboard e logs"""
        # Dashboard
        self.dashboard = Dashboard(self.dashboard_frame)
        self.dashboard.pack(fill=tk.BOTH, expand=True)
        
        # Logs
        self.log_viewer = LogViewer(
            self.dashboard_frame,
            on_filter_change=lambda filter_type: self.controller.handle_log_filter(filter_type)
        )
        self.log_viewer.pack(fill=tk.BOTH, expand=True)
    
    def set_controller(self, controller):
        """Define o controlador para esta view"""
        self.controller = controller
    
    def update_parked_list(self, vehicles):
        """Atualiza a lista de veículos estacionados"""
        self.parked_tree.delete(*self.parked_tree.get_children())
        for vehicle in vehicles:
            self.parked_tree.insert('', tk.END, values=(
                vehicle.plate, 
                vehicle.model, 
                vehicle.vehicle_type
            ))
    
    def update_dashboard(self, stats):
        """Atualiza o dashboard com novas estatísticas"""
        self.dashboard.update_metrics(stats)
        self.dashboard.update_chart(stats)
    
    def update_logs(self, logs):
        """Atualiza a exibição dos logs"""
        self.log_viewer.update_logs(logs)
    
    def clear_form(self):
        """Limpa o formulário de veículo"""
        self.vehicle_form.clear_form()
    
    def show_message(self, title, message):
        """Exibe uma mensagem ao usuário"""
        tk.messagebox.showinfo(title, message)
    
    def show_error(self, title, message):
        """Exibe uma mensagem de erro ao usuário"""
        tk.messagebox.showerror(title, message)
    
    def ask_save_file(self, title, filetypes):
        """Mostra diálogo para salvar arquivo"""
        return filedialog.asksaveasfilename(title=title, filetypes=filetypes)