from pathlib import Path

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .model import Vehicle


class VehicleView(QWidget):
    def __init__(self, service):
        super().__init__()
        self.setObjectName("vehicleView")
        self.service = service
        self.selected_vehicle_id = None

        self.build_ui()
        self.setStyleSheet(Path(__file__).with_name("style.qss").read_text())
        self.refresh()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        form = QFormLayout()

        self.plate_input = QLineEdit()
        self.owner_input = QLineEdit()

        self.type_input = QComboBox()
        self.type_input.addItems(
            ["Car", "Motorcycle", "Truck", "Van", "Bus", "Other"]
        )

        self.brand_input = QLineEdit()
        self.model_input = QLineEdit()

        self.year_input = QSpinBox()
        self.year_input.setRange(1900, 2100)
        self.year_input.setValue(QDate.currentDate().year())

        self.color_input = QLineEdit()
        self.engine_input = QLineEdit()
        self.chassis_input = QLineEdit()

        self.registration_date_input = QDateEdit()
        self.registration_date_input.setCalendarPopup(True)
        self.registration_date_input.setDisplayFormat("yyyy-MM-dd")
        self.registration_date_input.setDate(QDate.currentDate())

        self.expiry_date_input = QDateEdit()
        self.expiry_date_input.setCalendarPopup(True)
        self.expiry_date_input.setDisplayFormat("yyyy-MM-dd")
        self.expiry_date_input.setDate(QDate.currentDate().addYears(1))

        self.status_input = QComboBox()
        self.status_input.addItems(["Active", "Expired", "Suspended"])

        form.addRow("Plate Number", self.plate_input)
        form.addRow("Owner Name", self.owner_input)
        form.addRow("Vehicle Type", self.type_input)
        form.addRow("Brand", self.brand_input)
        form.addRow("Model", self.model_input)
        form.addRow("Year", self.year_input)
        form.addRow("Color", self.color_input)
        form.addRow("Engine Number", self.engine_input)
        form.addRow("Chassis Number", self.chassis_input)
        form.addRow("Registration Date", self.registration_date_input)
        form.addRow("Expiry Date", self.expiry_date_input)
        form.addRow("Status", self.status_input)

        layout.addLayout(form)

        button_layout = QHBoxLayout()

        self.save_button = QPushButton("Add Vehicle")
        self.save_button.setObjectName("primaryButton")
        self.save_button.clicked.connect(self.save_vehicle)
        button_layout.addWidget(self.save_button)

        clear_button = QPushButton("Clear")
        clear_button.setObjectName("secondaryButton")
        clear_button.clicked.connect(self.clear_form)
        button_layout.addWidget(clear_button)

        delete_button = QPushButton("Delete Selected")
        delete_button.setObjectName("dangerButton")
        delete_button.clicked.connect(self.delete_selected)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by plate, owner, brand, model, engine, or chassis..."
        )
        self.search_input.textChanged.connect(self.refresh)

        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        self.table = QTableWidget(0, 13)
        self.table.setHorizontalHeaderLabels(
            [
                "ID",
                "Plate",
                "Owner",
                "Type",
                "Brand",
                "Model",
                "Year",
                "Color",
                "Engine No.",
                "Chassis No.",
                "Registered",
                "Expires",
                "Status",
            ]
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellClicked.connect(self.load_selected_row)

        layout.addWidget(self.table)

    def build_vehicle_from_form(self) -> Vehicle:
        return Vehicle(
            id=self.selected_vehicle_id,
            plate_number=self.plate_input.text(),
            owner_name=self.owner_input.text(),
            vehicle_type=self.type_input.currentText(),
            brand=self.brand_input.text(),
            model=self.model_input.text(),
            year=self.year_input.value(),
            color=self.color_input.text(),
            engine_number=self.engine_input.text(),
            chassis_number=self.chassis_input.text(),
            registration_date=self.registration_date_input.date().toString("yyyy-MM-dd"),
            expiry_date=self.expiry_date_input.date().toString("yyyy-MM-dd"),
            status=self.status_input.currentText(),
        )

    def save_vehicle(self):
        try:
            vehicle = self.build_vehicle_from_form()

            if self.selected_vehicle_id is None:
                self.service.add_vehicle(vehicle)
                QMessageBox.information(
                    self,
                    "Saved",
                    "Vehicle registration added successfully.",
                )
            else:
                self.service.update_vehicle(vehicle)
                QMessageBox.information(
                    self,
                    "Updated",
                    "Vehicle registration updated successfully.",
                )

        except ValueError as error:
            QMessageBox.warning(self, "Invalid Vehicle", str(error))
            return

        self.clear_form()
        self.refresh()

    def load_selected_row(self, row, _column):
        self.selected_vehicle_id = int(self.table.item(row, 0).text())

        self.plate_input.setText(self.table.item(row, 1).text())
        self.owner_input.setText(self.table.item(row, 2).text())
        self.type_input.setCurrentText(self.table.item(row, 3).text())
        self.brand_input.setText(self.table.item(row, 4).text())
        self.model_input.setText(self.table.item(row, 5).text())
        self.year_input.setValue(int(self.table.item(row, 6).text()))
        self.color_input.setText(self.table.item(row, 7).text())
        self.engine_input.setText(self.table.item(row, 8).text())
        self.chassis_input.setText(self.table.item(row, 9).text())

        reg_date = QDate.fromString(self.table.item(row, 10).text(), "yyyy-MM-dd")
        expiry_date = QDate.fromString(self.table.item(row, 11).text(), "yyyy-MM-dd")

        if reg_date.isValid():
            self.registration_date_input.setDate(reg_date)

        if expiry_date.isValid():
            self.expiry_date_input.setDate(expiry_date)

        self.status_input.setCurrentText(self.table.item(row, 12).text())
        self.save_button.setText("Update Vehicle")

    def delete_selected(self):
        if self.selected_vehicle_id is None:
            QMessageBox.warning(
                self,
                "No Selection",
                "Select a vehicle record first.",
            )
            return

        answer = QMessageBox.question(
            self,
            "Delete Vehicle",
            "Are you sure you want to delete the selected vehicle registration?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.service.delete_vehicle(self.selected_vehicle_id)
            self.clear_form()
            self.refresh()

    def clear_form(self):
        self.selected_vehicle_id = None

        self.plate_input.clear()
        self.owner_input.clear()
        self.type_input.setCurrentIndex(0)
        self.brand_input.clear()
        self.model_input.clear()
        self.year_input.setValue(QDate.currentDate().year())
        self.color_input.clear()
        self.engine_input.clear()
        self.chassis_input.clear()
        self.registration_date_input.setDate(QDate.currentDate())
        self.expiry_date_input.setDate(QDate.currentDate().addYears(1))
        self.status_input.setCurrentIndex(0)

        self.save_button.setText("Add Vehicle")
        self.table.clearSelection()

    def refresh(self):
        search = self.search_input.text() if hasattr(self, "search_input") else ""
        vehicles = self.service.get_vehicles(search)

        self.table.setRowCount(len(vehicles))

        for row, vehicle in enumerate(vehicles):
            values = [
                vehicle.id,
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
            ]

            for column, value in enumerate(values):
                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value)),
                )
