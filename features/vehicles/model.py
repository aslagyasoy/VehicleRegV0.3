from dataclasses import dataclass
from datetime import date


@dataclass
class Vehicle:
    plate_number: str
    owner_name: str
    vehicle_type: str
    brand: str
    model: str
    year: int
    color: str
    engine_number: str
    chassis_number: str
    registration_date: str
    expiry_date: str
    status: str
    id: int | None = None

    def __post_init__(self) -> None:
        self.plate_number = self.plate_number.strip().upper()
        self.owner_name = self.owner_name.strip()
        self.vehicle_type = self.vehicle_type.strip()
        self.brand = self.brand.strip()
        self.model = self.model.strip()
        self.color = self.color.strip()
        self.engine_number = self.engine_number.strip().upper()
        self.chassis_number = self.chassis_number.strip().upper()
        self.status = self.status.strip()

        if not self.plate_number:
            raise ValueError("Plate number is required.")

        if not self.owner_name:
            raise ValueError("Owner name is required.")

        if not self.vehicle_type:
            raise ValueError("Vehicle type is required.")

        if not self.brand:
            raise ValueError("Brand is required.")

        if not self.model:
            raise ValueError("Model is required.")

        current_year = date.today().year
        if self.year < 1900 or self.year > current_year + 1:
            raise ValueError("Enter a valid vehicle year.")

        if not self.color:
            raise ValueError("Color is required.")

        if not self.engine_number:
            raise ValueError("Engine number is required.")

        if not self.chassis_number:
            raise ValueError("Chassis number is required.")

        if self.status not in ("Active", "Expired", "Suspended"):
            raise ValueError("Invalid registration status.")
