from typing import Dict, List
from ..models.parking_model import ParkingModel
from ..models.vehicle_model import Vehicle


class ParkingController:
    def __init__(self, model: ParkingModel):
        self.model = model

    def register_vehicle_entry(self, vehicle_data: Dict) -> bool:
        """Registra a entrada de um veículo"""
        plate = vehicle_data.get("plate", "").strip().upper()
        if not plate:
            return False

        vehicle = Vehicle(
            plate=plate,
            model=vehicle_data.get("model", "").strip(),
            color=vehicle_data.get("color", "").strip(),
            vehicle_type=vehicle_data.get("type", "Carro"),
        )

        success = self.model.add_vehicle(vehicle)
        if success:
            self.model.log_activity(
                f"Entrada registrada: {plate} ({vehicle.vehicle_type})"
            )
        return success

    def register_vehicle_exit(self, plate: str) -> bool:
        """Registra a saída de um veículo"""
        plate = plate.strip().upper()
        if not plate:
            return False

        success = self.model.register_exit(plate)
        if success:
            self.model.log_activity(f"Saída registrada: {plate}")
        return success

    def get_parked_vehicles(self) -> List[Vehicle]:
        """Obtém a lista de veículos estacionados"""
        return self.model.get_parked_vehicles()

    def get_vehicle_stats(self) -> Dict[str, int]:
        """Obtém estatísticas dos veículos"""
        return self.model.get_vehicle_stats()

    def get_filtered_logs(self, filter_type: str = "Todos") -> List[str]:
        """Obtém logs filtrados"""
        return self.model.get_recent_logs(filter_type)

    def export_data(self, file_path: str) -> bool:
        """Exporta os dados para um arquivo"""
        success = self.model.export_to_csv(file_path)
        if success:
            self.model.log_activity(f"Dados exportados para {file_path}")
        return success
