from database.database import Database
from .model import Vehicle
from .repository import VehicleRepository


class VehicleService:
    def __init__(self, database: Database):
        self.repository = VehicleRepository(database)

    def add_vehicle(self, vehicle: Vehicle) -> Vehicle:
        return self.repository.add(vehicle)

    def update_vehicle(self, vehicle: Vehicle) -> Vehicle:
        return self.repository.update(vehicle)

    def delete_vehicle(self, vehicle_id: int) -> None:
        self.repository.delete(vehicle_id)

    def get_vehicles(self, search: str = "") -> list[Vehicle]:
        return self.repository.list(search)
