import tkinter as tk
from tkinter import ttk
from typing import Dict


class Dashboard(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface do dashboard"""
        self.grid_columnconfigure(0, weight=1)

        # Cabeçalho
        ttk.Label(self, text="Dashboard", style="Header.TLabel").grid(
            row=0, column=0, pady=(0, 15), sticky=tk.W
        )

        # Métricas
        self.metrics_frame = ttk.Frame(self)
        self.metrics_frame.grid(row=1, column=0, sticky=tk.EW, pady=5)

        self.metric_labels = {}
        metrics = [
            ("total", "Total Veículos"),
            ("parked", "Estacionados"),
            ("cars", "Carros"),
            ("motorcycles", "Motos"),
            ("trucks", "Caminhões"),
            ("buses", "Ônibus"),
        ]

        for i, (key, title) in enumerate(metrics):
            frame = ttk.Frame(self.metrics_frame)
            frame.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky=tk.NSEW)
            self.metrics_frame.grid_columnconfigure(i % 3, weight=1)

            ttk.Label(frame, text=title).pack(pady=(5, 0))
            label = ttk.Label(frame, text="0", font=("Helvetica", 18, "bold"))
            label.pack(pady=(0, 5))

            self.metric_labels[key] = label

        # Gráfico
        self.chart_frame = ttk.Frame(self)
        self.chart_frame.grid(row=2, column=0, sticky=tk.NSEW, pady=10)
        self.grid_rowconfigure(2, weight=1)

        self.canvas = tk.Canvas(
            self.chart_frame, bg=self.master.cget("background"), highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def update_metrics(self, stats: Dict[str, int]):
        """Atualiza as métricas do dashboard"""
        for key, label in self.metric_labels.items():
            label.config(text=str(stats.get(key, 0)))

    def update_chart(self, stats: Dict[str, int]):
        """Atualiza o gráfico de distribuição"""
        self.canvas.delete("all")

        # Dados para o gráfico
        types = ["Carros", "Motos", "Caminhões", "Ônibus"]
        counts = [
            stats.get("cars", 0),
            stats.get("motorcycles", 0),
            stats.get("trucks", 0),
            stats.get("buses", 0),
        ]
        total = sum(counts) or 1  # Evitar divisão por zero
        colors = ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]

        # Dimensões
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) * 0.4

        # Desenhar gráfico de pizza
        start_angle = 0
        for count, color in zip(counts, colors):
            if count == 0:
                continue

            extent = 360 * (count / total)
            self.canvas.create_arc(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                start=start_angle,
                extent=extent,
                fill=color,
                outline="",
            )
            start_angle += extent

        # Legenda
        legend_x = 20
        legend_y = 20
        for type_name, color, count in zip(types, colors, counts):
            self.canvas.create_rectangle(
                legend_x, legend_y, legend_x + 20, legend_y + 20, fill=color, outline=""
            )
            self.canvas.create_text(
                legend_x + 30,
                legend_y + 10,
                text=f"{type_name}: {count}",
                anchor=tk.W,
                fill=self.style.lookup("TLabel", "foreground"),
                font=("Helvetica", 10),
            )
            legend_y += 25
