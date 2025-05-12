import tkinter.ttk as ttk


class StyleManager:
    def __init__(self):
        self.style = ttk.Style()
        self.setup_styles()

    def setup_styles(self):
        """Configura os estilos visuais da aplicação"""
        self.style.theme_use("clam")

        # Cores
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.accent_color = "#3498db"
        self.success_color = "#2ecc71"
        self.warning_color = "#f39c12"
        self.danger_color = "#e74c3c"
        self.card_bg = "#34495e"

        # Configurar estilos
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure(
            "TLabel",
            background=self.bg_color,
            foreground=self.fg_color,
            font=("Helvetica", 10),
        )
        self.style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))
        self.style.configure("TButton", font=("Helvetica", 10), padding=6)
        self.style.configure(
            "Accent.TButton", background=self.accent_color, foreground="white"
        )
        self.style.configure(
            "Success.TButton", background=self.success_color, foreground="white"
        )
        self.style.configure(
            "Danger.TButton", background=self.danger_color, foreground="white"
        )
        self.style.configure("TEntry", font=("Helvetica", 10), padding=5)
        self.style.configure("TCombobox", font=("Helvetica", 10), padding=5)
        self.style.map("Accent.TButton", background=[("active", "#2980b9")])
        self.style.map("Success.TButton", background=[("active", "#27ae60")])
        self.style.map("Danger.TButton", background=[("active", "#c0392b")])

    def get_bg_color(self):
        return self.bg_color

    def get_fg_color(self):
        return self.fg_color

    def get_card_bg(self):
        return self.card_bg
