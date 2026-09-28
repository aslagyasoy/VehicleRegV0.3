import sqlite3

from database.database import Database
from .model import Vehicle


class VehicleRepository:
    def __init__(self, database: Database):
        self.database = database

    def add(self, vehicle: Vehicle) -> Vehicle:
        try:
            with self.database.connect() as connection:
                cursor = connection.execute(
                    """
                    INSERT INTO vehicles (
                        plate_number, owner_name, vehicle_type, brand, model,
                        year, color, engine_number, chassis_number,
                        registration_date, expiry_date, status
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        vehicle.plate_number,
                        vehicle.owner_name,
                        vehicle.vehicle_type,
                        vehicle.brand,
                        vehicle.model,
                        vehicle.year,
                        vehicle.color,
                        vehicle.engine_number,
                        vehicle.chassis_number,
                        vehicle.registration_date,
                        vehicle.expiry_date,
                        vehicle.status,
                    ),
                )
                vehicle.id = cursor.lastrowid
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Plate number, engine number, or chassis number already exists."
            ) from error

        return vehicle

    def update(self, vehicle: Vehicle) -> Vehicle:
        if vehicle.id is None:
            raise ValueError("Vehicle record has no ID.")

        try:
            with self.database.connect() as connection:
                connection.execute(
                    """
                    UPDATE vehicles
                    SET plate_number = ?, owner_name = ?, vehicle_type = ?,
                        brand = ?, model = ?, year = ?, color = ?,
                        engine_number = ?, chassis_number = ?,
                        registration_date = ?, expiry_date = ?, status = ?
                    WHERE id = ?
                    """,
                    (
                        vehicle.plate_number,
                        vehicle.owner_name,
                        vehicle.vehicle_type,
                        vehicle.brand,
                        vehicle.model,
                        vehicle.year,
                        vehicle.color,
                        vehicle.engine_number,
                        vehicle.chassis_number,
                        vehicle.registration_date,
                        vehicle.expiry_date,
                        vehicle.status,
                        vehicle.id,
                    ),
                )
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Plate number, engine number, or chassis number already exists."
            ) from error

        return vehicle

    def delete(self, vehicle_id: int) -> None:
        with self.database.connect() as connection:
            connection.execute(
                "DELETE FROM vehicles WHERE id = ?",
                (vehicle_id,),
            )

    def list(self, search: str = "") -> list[Vehicle]:
        with self.database.connect() as connection:
            if search:
                term = f"%{search.strip()}%"
                rows = connection.execute(
                    """
                    SELECT id, plate_number, owner_name, vehicle_type, brand,
                           model, year, color, engine_number, chassis_number,
                           registration_date, expiry_date, status
                    FROM vehicles
                    WHERE plate_number LIKE ?
                       OR owner_name LIKE ?
                       OR brand LIKE ?
                       OR model LIKE ?
                       OR engine_number LIKE ?
                       OR chassis_number LIKE ?
                    ORDER BY id DESC
                    """,
                    (term, term, term, term, term, term),
                ).fetchall()
            else:
                rows = connection.execute(
                    """
                    SELECT id, plate_number, owner_name, vehicle_type, brand,
                           model, year, color, engine_number, chassis_number,
                           registration_date, expiry_date, status
                    FROM vehicles
                    ORDER BY id DESC
                    """
                ).fetchall()

        return [
            Vehicle(
                id=row[0],
                plate_number=row[1],
                owner_name=row[2],
                vehicle_type=row[3],
                brand=row[4],
                model=row[5],
                year=row[6],
                color=row[7],
                engine_number=row[8],
                chassis_number=row[9],
                registration_date=row[10],
                expiry_date=row[11],
                status=row[12],
            )
            for row in rows
        ]
