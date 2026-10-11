
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QDateEdit,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QScrollArea,
    QWidget,
    QLabel,
)


class VehicleDialog(QDialog):
    def __init__(self, parent=None, vehicle=None):
        super().__init__(parent)

        self.vehicle = vehicle
        self.result_vehicle = None

        self.setObjectName("vehicleDialog")
        self.setWindowTitle(
            "Update Vehicle" if vehicle else "Add Vehicle"
        )

        self.resize(620, 690)
        self.setMinimumSize(500, 500)

        self.build_ui()
        self.apply_styles()

        if vehicle:
            self.load_vehicle(vehicle)

    def build_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(22, 20, 22, 20)
        outer.setSpacing(14)

        title = QLabel(
            "Update Vehicle" if self.vehicle else "Add New Vehicle"
        )
        title.setObjectName("dialogTitle")
        outer.addWidget(title)

        subtitle = QLabel(
            "Edit the registration information below."
            if self.vehicle
            else "Enter the vehicle details to create a new registration."
        )
        subtitle.setObjectName("dialogSubtitle")
        outer.addWidget(subtitle)

        scroll = QScrollArea()
        scroll.setObjectName("formScroll")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)

        body = QWidget()
        body.setObjectName("formBody")

        form = QFormLayout(body)
        form.setContentsMargins(2, 8, 2, 8)
        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(12)

        self.plate = QLineEdit()
        self.owner = QLineEdit()

        self.vehicle_type = QComboBox()
        self.vehicle_type.addItems([
            "Car",
            "Motorcycle",
            "Truck",
            "Van",
            "Bus",
            "Other",
        ])

        self.brand = QLineEdit()
        self.model = QLineEdit()

        self.year = QSpinBox()
        self.year.setRange(1900, 2100)
        self.year.setValue(QDate.currentDate().year())

        self.color = QLineEdit()
        self.engine = QLineEdit()
        self.chassis = QLineEdit()

        self.registered = QDateEdit()
        self.registered.setCalendarPopup(True)
        self.registered.setDisplayFormat("yyyy-MM-dd")
        self.registered.setDate(QDate.currentDate())

        self.expires = QDateEdit()
        self.expires.setCalendarPopup(True)
        self.expires.setDisplayFormat("yyyy-MM-dd")
        self.expires.setDate(
            QDate.currentDate().addYears(1)
        )

        self.status = QComboBox()
        self.status.addItems([
            "Active",
            "Expired",
            "Suspended",
        ])

        fields = [
            ("Plate Number", self.plate),
            ("Owner Name", self.owner),
            ("Vehicle Type", self.vehicle_type),
            ("Brand", self.brand),
            ("Model", self.model),
            ("Year", self.year),
            ("Color", self.color),
            ("Engine Number", self.engine),
            ("Chassis Number", self.chassis),
            ("Registration Date", self.registered),
            ("Expiry Date", self.expires),
            ("Status", self.status),
        ]

        for label, widget in fields:
            form.addRow(label, widget)

        scroll.setWidget(body)
        outer.addWidget(scroll, 1)

        actions = QHBoxLayout()
        actions.setSpacing(12)

        save = QPushButton(
            "Update Vehicle" if self.vehicle else "Add Vehicle"
        )
        save.setObjectName("saveVehicleButton")
        save.setMinimumHeight(42)
        save.clicked.connect(self.submit)

        cancel = QPushButton("Cancel")
        cancel.setObjectName("cancelVehicleButton")
        cancel.setMinimumHeight(42)
        cancel.clicked.connect(self.reject)

        actions.addWidget(save, 1)
        actions.addWidget(cancel, 1)

        outer.addLayout(actions)

    def apply_styles(self):
        self.setStyleSheet("""
            QDialog#vehicleDialog {
                background-color: #f4f6fb;
                color: #172b4d;
            }

            QLabel {
                background: transparent;
                color: #172b4d;
                font-size: 12px;
                font-weight: 500;
            }

            QLabel#dialogTitle {
                color: #102a4c;
                font-size: 22px;
                font-weight: 700;
            }

            QLabel#dialogSubtitle {
                color: #64748b;
                font-size: 12px;
                font-weight: 400;
            }

            QScrollArea#formScroll {
                background: transparent;
                border: none;
            }

            QWidget#formBody {
                background-color: #f4f6fb;
            }

            QLineEdit,
            QComboBox,
            QSpinBox,
            QDateEdit {
                background-color: #ffffff;
                color: #172b4d;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 7px 10px;
                min-height: 23px;
                font-size: 12px;
            }

            QLineEdit:focus,
            QComboBox:focus,
            QSpinBox:focus,
            QDateEdit:focus {
                border: 1px solid #2563eb;
            }

            QComboBox QAbstractItemView {
                background-color: #ffffff;
                color: #172b4d;
                selection-background-color: #dbeafe;
                selection-color: #172b4d;
                border: 1px solid #cbd5e1;
            }

            QComboBox::drop-down {
                background-color: #ffffff;
                border: none;
                width: 26px;
            }

            QSpinBox::up-button,
            QSpinBox::down-button,
            QDateEdit::drop-down {
                background-color: #edf2f8;
                border: none;
                width: 22px;
            }

            QCalendarWidget {
                background-color: #ffffff;
                color: #172b4d;
            }

            QCalendarWidget QWidget {
                background-color: #ffffff;
                color: #172b4d;
            }

            QPushButton#saveVehicleButton {
                background-color: #2563eb;
                color: #ffffff;
                border: none;
                border-radius: 7px;
                font-size: 13px;
                font-weight: 600;
                padding: 9px 16px;
            }

            QPushButton#saveVehicleButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton#cancelVehicleButton {
                background-color: #e2e8f0;
                color: #172b4d;
                border: 1px solid #cbd5e1;
                border-radius: 7px;
                font-size: 13px;
                font-weight: 600;
                padding: 9px 16px;
            }

            QPushButton#cancelVehicleButton:hover {
                background-color: #cbd5e1;
            }
        """)

    def load_vehicle(self, vehicle):
        self.plate.setText(vehicle.plate_number)
        self.owner.setText(vehicle.owner_name)
        self.vehicle_type.setCurrentText(
            vehicle.vehicle_type
        )
        self.brand.setText(vehicle.brand)
        self.model.setText(vehicle.model)
        self.year.setValue(vehicle.year)
        self.color.setText(vehicle.color)
        self.engine.setText(vehicle.engine_number)
        self.chassis.setText(vehicle.chassis_number)

        registered_date = QDate.fromString(
            vehicle.registration_date,
            "yyyy-MM-dd",
        )

        expiry_date = QDate.fromString(
            vehicle.expiry_date,
            "yyyy-MM-dd",
        )

        if registered_date.isValid():
            self.registered.setDate(registered_date)

        if expiry_date.isValid():
            self.expires.setDate(expiry_date)

        self.status.setCurrentText(vehicle.status)

    def submit(self):
        from .model import Vehicle

        try:
            if self.expires.date() < self.registered.date():
                raise ValueError(
                    "Expiry date cannot be earlier than registration date."
                )

            self.result_vehicle = Vehicle(
                id=self.vehicle.id if self.vehicle else None,
                plate_number=self.plate.text().strip(),
                owner_name=self.owner.text().strip(),
                vehicle_type=self.vehicle_type.currentText(),
                brand=self.brand.text().strip(),
                model=self.model.text().strip(),
                year=self.year.value(),
                color=self.color.text().strip(),
                engine_number=self.engine.text().strip(),
                chassis_number=self.chassis.text().strip(),
                registration_date=self.registered.date().toString(
                    "yyyy-MM-dd"
                ),
                expiry_date=self.expires.date().toString(
                    "yyyy-MM-dd"
                ),
                status=self.status.currentText(),
            )

            self.accept()

        except (ValueError, TypeError) as exc:
            QMessageBox.warning(
                self,
                "Invalid Vehicle",
                str(exc),
            )
