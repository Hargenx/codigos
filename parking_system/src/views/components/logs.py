import tkinter as tk
from tkinter import ttk
from typing import List


class LogViewer(ttk.Frame):
    def __init__(self, parent, on_filter_change=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.on_filter_change = on_filter_change
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface do visualizador de logs"""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Cabeçalho e filtros
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, sticky=tk.EW, pady=(0, 5))

        ttk.Label(
            header_frame, text="Registro de Atividades", style="Header.TLabel"
        ).pack(side=tk.LEFT)

        filter_frame = ttk.Frame(header_frame)
        filter_frame.pack(side=tk.RIGHT, padx=5)

        ttk.Label(filter_frame, text="Filtrar por:").pack(side=tk.LEFT, padx=5)

        self.filter_combobox = ttk.Combobox(
            filter_frame,
            values=["Todos", "Entradas", "Saídas"],
            width=10,
            state="readonly",
        )
        self.filter_combobox.pack(side=tk.LEFT, padx=5)
        self.filter_combobox.current(0)
        self.filter_combobox.bind("<<ComboboxSelected>>", self.handle_filter_change)

        # Área de logs
        self.logs_text = tk.Text(
            self,
            height=10,
            bg=self.style.lookup("TFrame", "background"),
            fg=self.style.lookup("TLabel", "foreground"),
            font=("Consolas", 10),
            padx=10,
            pady=10,
            wrap=tk.WORD,
        )
        self.logs_text.grid(row=1, column=0, sticky=tk.NSEW)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.logs_text.yview
        )
        scrollbar.grid(row=1, column=1, sticky=tk.NS)
        self.logs_text.config(yscrollcommand=scrollbar.set)

    def handle_filter_change(self, event=None):
        """Lida com a mudança de filtro"""
        if self.on_filter_change:
            self.on_filter_change(self.filter_combobox.get())

    def update_logs(self, logs: List[str]):
        """Atualiza a exibição dos logs"""
        self.logs_text.config(state=tk.NORMAL)
        self.logs_text.delete(1.0, tk.END)
        self.logs_text.insert(tk.END, "".join(logs))
        self.logs_text.config(state=tk.DISABLED)
        self.logs_text.see(tk.END)

    def get_current_filter(self) -> str:
        """Retorna o filtro atual"""
        return self.filter_combobox.get()
