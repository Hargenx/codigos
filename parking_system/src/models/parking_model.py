from typing import List, Dict, Optional
from .vehicle_model import Vehicle
from datetime import datetime
import json
import csv


class ParkingModel:
    def __init__(self):
        self.vehicles: List[Vehicle] = []
        self.log_file = "parking_logs.txt"
        self.data_file = "parking_data.json"
        self.load_data()

    def add_vehicle(self, vehicle: Vehicle) -> bool:
        """Adiciona um veículo ao estacionamento se não estiver já estacionado"""
        if self.is_vehicle_parked(vehicle.plate):
            return False
        self.vehicles.append(vehicle)
        self.save_data()
        return True

    def register_exit(self, plate: str) -> bool:
        """Registra a saída de um veículo"""
        vehicle = self.find_parked_vehicle(plate)
        if vehicle:
            vehicle.register_exit()
            self.save_data()
            return True
        return False

    def find_parked_vehicle(self, plate: str) -> Optional[Vehicle]:
        """Encontra um veículo estacionado pela placa"""
        for vehicle in self.vehicles:
            if vehicle.plate == plate and vehicle.is_parked():
                return vehicle
        return None

    def is_vehicle_parked(self, plate: str) -> bool:
        """Verifica se um veículo está estacionado"""
        return self.find_parked_vehicle(plate) is not None

    def get_parked_vehicles(self) -> List[Vehicle]:
        """Retorna lista de veículos estacionados"""
        return [v for v in self.vehicles if v.is_parked()]

    def get_vehicle_stats(self) -> Dict[str, int]:
        """Retorna estatísticas dos veículos"""
        stats = {
            "total": len(self.vehicles),
            "parked": len(self.get_parked_vehicles()),
            "cars": len([v for v in self.vehicles if v.vehicle_type == "Carro"]),
            "motorcycles": len([v for v in self.vehicles if v.vehicle_type == "Moto"]),
            "trucks": len([v for v in self.vehicles if v.vehicle_type == "Caminhão"]),
            "buses": len([v for v in self.vehicles if v.vehicle_type == "Ônibus"]),
        }
        return stats

    def log_activity(self, message: str):
        """Registra uma atividade no log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def get_recent_logs(self, filter_type: str = "Todos", limit: int = 50) -> List[str]:
        """Obtém os logs recentes com filtro opcional"""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                logs = f.readlines()
        except FileNotFoundError:
            return []

        if filter_type == "Entradas":
            logs = [log for log in logs if "Entrada registrada" in log]
        elif filter_type == "Saídas":
            logs = [log for log in logs if "Saída registrada" in log]

        return logs[-limit:] if limit else logs

    def load_data(self):
        """Carrega os dados salvos"""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.vehicles = [Vehicle.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.vehicles = []

    def save_data(self):
        """Salva os dados no arquivo"""
        data = [vehicle.to_dict() for vehicle in self.vehicles]
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def export_to_csv(self, file_path: str) -> bool:
        """Exporta os dados para CSV"""
        try:
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Placa", "Modelo", "Cor", "Tipo", "Entrada", "Saída"])

                for vehicle in self.vehicles:
                    writer.writerow(
                        [
                            vehicle.plate,
                            vehicle.model,
                            vehicle.color,
                            vehicle.vehicle_type,
                            vehicle.entry_time,
                            vehicle.exit_time or "Estacionado",
                        ]
                    )
            return True
        except Exception:
            return False
