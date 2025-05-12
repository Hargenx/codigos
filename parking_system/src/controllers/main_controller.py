from ..views.main_view import MainView
from .parking_controller import ParkingController
from ..models.parking_model import ParkingModel


class MainController:
    def __init__(self, root):
        self.root = root
        self.model = ParkingModel()
        self.parking_controller = ParkingController(self.model)
        self.view = MainView(root)
        self.view.set_controller(self)
        self.update_all()

    def handle_vehicle_entry(self, vehicle_data):
        """Lida com o registro de entrada de veículo"""
        success = self.parking_controller.register_vehicle_entry(vehicle_data)
        if success:
            self.view.clear_form()
            self.update_all()
            self.view.show_message(
                "Sucesso",
                f"Entrada do veículo {vehicle_data['plate']} registrada com sucesso!",
            )
        else:
            self.view.show_error(
                "Erro", f"Veículo com placa {vehicle_data['plate']} já está estacionado"
            )

    def handle_vehicle_exit(self, plate):
        """Lida com o registro de saída de veículo"""
        success = self.parking_controller.register_vehicle_exit(plate)
        if success:
            self.view.clear_form()
            self.update_all()
            self.view.show_message(
                "Sucesso", f"Saída do veículo {plate} registrada com sucesso!"
            )
        else:
            self.view.show_error(
                "Erro", f"Veículo com placa {plate} não encontrado ou já saiu"
            )

    def handle_log_filter(self, filter_type):
        """Lida com a mudança de filtro de logs"""
        self.update_logs()

    def handle_export_data(self):
        """Lida com a exportação de dados"""
        file_path = self.view.ask_save_file(
            "Salvar dados como", [("CSV Files", "*.csv"), ("All Files", "*.*")]
        )

        if file_path:
            success = self.parking_controller.export_data(file_path)
            if success:
                self.view.show_message(
                    "Sucesso", f"Dados exportados com sucesso para:\n{file_path}"
                )
            else:
                self.view.show_error("Erro", "Falha ao exportar dados")

    def update_all(self):
        """Atualiza todos os componentes da view"""
        self.update_parked_list()
        self.update_dashboard()
        self.update_logs()

    def update_parked_list(self):
        """Atualiza a lista de veículos estacionados"""
        parked_vehicles = self.parking_controller.get_parked_vehicles()
        self.view.update_parked_list(parked_vehicles)

    def update_dashboard(self):
        """Atualiza o dashboard"""
        stats = self.parking_controller.get_vehicle_stats()
        self.view.update_dashboard(stats)

    def update_logs(self):
        """Atualiza os logs"""
        filter_type = self.view.log_viewer.get_current_filter()
        logs = self.parking_controller.get_filtered_logs(filter_type)
        self.view.update_logs(logs)
