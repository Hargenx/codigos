from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Vehicle:
    plate: str
    model: str
    color: str
    vehicle_type: str
    entry_time: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    exit_time: Optional[str] = None

    def is_parked(self) -> bool:
        return self.exit_time is None

    def register_exit(self):
        self.exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "plate": self.plate,
            "model": self.model,
            "color": self.color,
            "type": self.vehicle_type,
            "entry_time": self.entry_time,
            "exit_time": self.exit_time,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vehicle":
        return cls(
            plate=data.get("plate", ""),
            model=data.get("model", ""),
            color=data.get("color", ""),
            vehicle_type=data.get("type", "Carro"),
            entry_time=data.get("entry_time"),
            exit_time=data.get("exit_time"),
        )
