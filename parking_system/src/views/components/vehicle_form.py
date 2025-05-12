import tkinter as tk
from tkinter import ttk
from typing import Callable


class VehicleForm(ttk.Frame):
    def __init__(self, parent, on_submit: Callable, on_exit: Callable, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.on_submit = on_submit
        self.on_exit = on_exit
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface do formulário"""
        self.grid_columnconfigure(1, weight=1)

        # Labels e Entradas
        ttk.Label(self, text="Placa:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.plate_entry = ttk.Entry(self)
        self.plate_entry.grid(row=0, column=1, sticky=tk.EW, pady=2)

        ttk.Label(self, text="Modelo:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.model_entry = ttk.Entry(self)
        self.model_entry.grid(row=1, column=1, sticky=tk.EW, pady=2)

        ttk.Label(self, text="Cor:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.color_entry = ttk.Entry(self)
        self.color_entry.grid(row=2, column=1, sticky=tk.EW, pady=2)

        ttk.Label(self, text="Tipo:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.type_combobox = ttk.Combobox(
            self, values=["Carro", "Moto", "Caminhão", "Ônibus"]
        )
        self.type_combobox.grid(row=3, column=1, sticky=tk.EW, pady=2)
        self.type_combobox.current(0)

        # Botões
        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.EW)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

        self.entry_btn = ttk.Button(
            btn_frame,
            text="Registrar Entrada",
            command=self.handle_submit,
            style="Success.TButton",
        )
        self.entry_btn.grid(row=0, column=0, padx=2, sticky=tk.EW)

        self.exit_btn = ttk.Button(
            btn_frame,
            text="Registrar Saída",
            command=self.handle_exit,
            style="Danger.TButton",
        )
        self.exit_btn.grid(row=0, column=1, padx=2, sticky=tk.EW)

    def handle_submit(self):
        """Lida com o envio do formulário de entrada"""
        data = {
            "plate": self.plate_entry.get().strip().upper(),
            "model": self.model_entry.get().strip(),
            "color": self.color_entry.get().strip(),
            "type": self.type_combobox.get(),
        }
        self.on_submit(data)

    def handle_exit(self):
        """Lida com o registro de saída"""
        plate = self.plate_entry.get().strip().upper()
        self.on_exit(plate)

    def clear_form(self):
        """Limpa os campos do formulário"""
        self.plate_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.type_combobox.current(0)

    def set_focus(self):
        """Define o foco no campo de placa"""
        self.plate_entry.focus_set()
