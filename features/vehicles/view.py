
from collections import Counter

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QFont
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
    QDialog,
    QFrame,
    QSizePolicy,
)

from .dialog import VehicleDialog


class VehicleTypeChart(QWidget):
    def __init__(self):
        super().__init__()

        self.counts = {}
        self.setMinimumHeight(150)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

    def set_counts(self, counts):
        self.counts = counts
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )
        painter.fillRect(
            self.rect(),
            QColor("#ffffff"),
        )

        rect = self.rect().adjusted(18, 12, -18, -12)

        if not self.counts:
            painter.setPen(QColor("#64748b"))
            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                "No vehicle records yet",
            )
            painter.end()
            return

        data = sorted(
            self.counts.items(),
            key=lambda item: (-item[1], item[0]),
        )

        max_count = max(
            1,
            max(self.counts.values()),
        )

        row_height = max(
            25,
            min(38, rect.height() // len(data)),
        )

        label_width = 105
        count_width = 45

        bar_width = max(
            20,
            rect.width() - label_width - count_width - 10,
        )

        painter.setFont(QFont("Segoe UI", 9))

        for i, (name, count) in enumerate(data):
            y = rect.top() + i * row_height

            painter.setPen(QColor("#1e293b"))
            painter.drawText(
                rect.left(),
                y,
                label_width - 8,
                row_height,
                Qt.AlignmentFlag.AlignVCenter,
                name,
            )

            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor("#e2e8f0"))

            painter.drawRoundedRect(
                rect.left() + label_width,
                y + 7,
                bar_width,
                row_height - 14,
                5,
                5,
            )

            painter.setBrush(QColor("#2563eb"))

            painter.drawRoundedRect(
                rect.left() + label_width,
                y + 7,
                max(
                    2,
                    round(bar_width * count / max_count),
                ),
                row_height - 14,
                5,
                5,
            )

            painter.setPen(QColor("#1e293b"))
            painter.drawText(
                rect.left() + label_width + bar_width + 7,
                y,
                count_width - 7,
                row_height,
                Qt.AlignmentFlag.AlignVCenter,
                str(count),
            )

        painter.end()


class VehicleView(QWidget):
    HEADERS = [
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

    def __init__(self, service):
        super().__init__()

        self.service = service
        self.all_vehicles = []

        self.setObjectName("vehicleDashboard")

        self.build_ui()
        self.apply_styles()
        self.refresh()

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget#vehicleDashboard {
                background-color: #f4f6fb;
            }

            QWidget#vehicleDashboard QLabel {
                color: #172b4d;
                background: transparent;
            }

            QWidget#vehicleDashboard QLineEdit {
                background-color: #ffffff;
                color: #172b4d;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 8px 12px;
                min-height: 20px;
            }

            QWidget#vehicleDashboard QLineEdit:focus {
                border: 1px solid #2563eb;
            }

            QWidget#vehicleDashboard QPushButton {
                background-color: #e2e8f0;
                color: #172b4d;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                padding: 9px 18px;
                font-weight: 600;
                min-height: 20px;
            }

            QWidget#vehicleDashboard QPushButton:hover {
                background-color: #cbd5e1;
            }

            QWidget#vehicleDashboard QPushButton#primaryButton {
                background-color: #2563eb;
                color: #ffffff;
                border: none;
            }

            QWidget#vehicleDashboard QPushButton#primaryButton:hover {
                background-color: #1d4ed8;
            }

            QWidget#vehicleDashboard QPushButton#dangerButton {
                background-color: #dc2626;
                color: #ffffff;
                border: none;
            }

            QWidget#vehicleDashboard QPushButton#dangerButton:hover {
                background-color: #b91c1c;
            }

            QWidget#vehicleDashboard QPushButton:disabled {
                background-color: #e5e7eb;
                color: #64748b;
                border: 1px solid #d1d5db;
            }

            QWidget#vehicleDashboard QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f8fafc;
                color: #172b4d;
                gridline-color: #e2e8f0;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
                selection-background-color: #dbeafe;
                selection-color: #172b4d;
            }

            QWidget#vehicleDashboard QHeaderView::section {
                background-color: #eaf0f8;
                color: #172b4d;
                padding: 8px;
                border: none;
                border-right: 1px solid #d1dbe8;
                border-bottom: 1px solid #d1dbe8;
                font-weight: 600;
            }

            QWidget#vehicleDashboard QTableWidget::item {
                padding: 5px;
            }
        """)

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(4, 4, 4, 4)
        root.setSpacing(12)

        title = QLabel("Vehicle Overview")
        title.setStyleSheet(
            "font-size: 19px;"
            "font-weight: 700;"
            "color: #152a47;"
        )
        root.addWidget(title)

        stats = QHBoxLayout()
        stats.setSpacing(12)

        self.total_label = self.make_stat(
            stats, "Total Vehicles"
        )
        self.car_label = self.make_stat(
            stats, "Cars"
        )
        self.motorcycle_label = self.make_stat(
            stats, "Motorcycles"
        )
        self.other_label = self.make_stat(
            stats, "Other Types"
        )

        root.addLayout(stats)

        chart_title = QLabel("Vehicles by Type")
        chart_title.setStyleSheet(
            "font-size: 15px;"
            "font-weight: 600;"
            "color: #152a47;"
        )
        root.addWidget(chart_title)

        self.chart = VehicleTypeChart()
        root.addWidget(self.chart)

        toolbar = QHBoxLayout()
        toolbar.setSpacing(12)

        self.search = QLineEdit()
        self.search.setPlaceholderText(
            "Search plate, owner, brand, model, engine or chassis..."
        )
        self.search.setMinimumHeight(38)
        self.search.textChanged.connect(
            self.refresh_table
        )

        toolbar.addWidget(self.search, 1)

        self.add_button = QPushButton("+ Add Vehicle")
        self.add_button.setObjectName("primaryButton")
        self.add_button.setMinimumWidth(150)
        self.add_button.setMinimumHeight(38)
        self.add_button.clicked.connect(
            self.add_vehicle
        )

        toolbar.addWidget(self.add_button)
        root.addLayout(toolbar)

        self.table = QTableWidget(
            0,
            len(self.HEADERS),
        )
        self.table.setHorizontalHeaderLabels(
            self.HEADERS
        )

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.horizontalHeader().setMinimumSectionSize(55)

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(True)
        self.table.setWordWrap(False)
        self.table.setTextElideMode(
            Qt.TextElideMode.ElideRight
        )
        self.table.setMinimumHeight(250)
        self.table.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        root.addWidget(self.table, 1)

        actions = QHBoxLayout()
        actions.setSpacing(10)

        self.update_button = QPushButton(
            "Update Selected"
        )
        self.update_button.setMinimumWidth(150)
        self.update_button.setMinimumHeight(38)
        self.update_button.clicked.connect(
            self.update_vehicle
        )

        self.delete_button = QPushButton(
            "Delete Selected"
        )
        self.delete_button.setObjectName(
            "dangerButton"
        )
        self.delete_button.setMinimumWidth(150)
        self.delete_button.setMinimumHeight(38)
        self.delete_button.clicked.connect(
            self.delete_vehicle
        )

        actions.addStretch()
        actions.addWidget(self.update_button)
        actions.addWidget(self.delete_button)

        root.addLayout(actions)

        self.table.itemSelectionChanged.connect(
            self.selection_changed
        )
        self.selection_changed()

    def make_stat(self, layout, label):
        card = QFrame()
        card.setObjectName("statCard")

        card.setStyleSheet("""
            QFrame#statCard {
                background-color: #ffffff;
                border: 1px solid #dbe3ed;
                border-radius: 9px;
            }
        """)

        box = QVBoxLayout(card)
        box.setContentsMargins(14, 10, 14, 10)

        name = QLabel(label)
        name.setStyleSheet(
            "border: none;"
            "color: #64748b;"
            "font-size: 12px;"
        )

        value = QLabel("0")
        value.setStyleSheet(
            "border: none;"
            "color: #1e40af;"
            "font-size: 25px;"
            "font-weight: 700;"
        )

        box.addWidget(name)
        box.addWidget(value)

        layout.addWidget(card, 1)

        return value

    def selected_vehicle(self):
        row = self.table.currentRow()

        if row < 0 or not self.table.item(row, 0):
            return None

        vehicle_id = int(
            self.table.item(row, 0).text()
        )

        return next(
            (
                vehicle
                for vehicle in self.all_vehicles
                if vehicle.id == vehicle_id
            ),
            None,
        )

    def selection_changed(self):
        selected = (
            self.selected_vehicle() is not None
        )

        self.update_button.setEnabled(selected)
        self.delete_button.setEnabled(selected)

    def refresh(self):
        try:
            self.all_vehicles = list(
                self.service.get_vehicles("")
            )
        except Exception as exc:
            QMessageBox.critical(
                self,
                "Loading Error",
                str(exc),
            )
            return

        counts = Counter(
            vehicle.vehicle_type
            for vehicle in self.all_vehicles
        )

        self.total_label.setText(
            str(len(self.all_vehicles))
        )
        self.car_label.setText(
            str(counts.get("Car", 0))
        )
        self.motorcycle_label.setText(
            str(counts.get("Motorcycle", 0))
        )

        other_count = sum(
            count
            for vehicle_type, count in counts.items()
            if vehicle_type not in (
                "Car",
                "Motorcycle",
            )
        )

        self.other_label.setText(
            str(other_count)
        )

        self.chart.setMinimumHeight(
            max(150, 40 * len(counts) + 22)
        )
        self.chart.set_counts(dict(counts))

        self.refresh_table()

    def refresh_table(self):
        query = (
            self.search.text()
            .strip()
            .casefold()
        )

        filtered = [
            vehicle
            for vehicle in self.all_vehicles
            if not query or any(
                query in str(value).casefold()
                for value in (
                    vehicle.plate_number,
                    vehicle.owner_name,
                    vehicle.brand,
                    vehicle.model,
                    vehicle.engine_number,
                    vehicle.chassis_number,
                )
            )
        ]

        self.table.setRowCount(
            len(filtered)
        )

        for row, vehicle in enumerate(filtered):
            fields = [
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

            for column, value in enumerate(fields):
                item = QTableWidgetItem(
                    str(value)
                )
                item.setToolTip(str(value))

                if column == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        vehicle.id,
                    )

                self.table.setItem(
                    row,
                    column,
                    item,
                )

        self.table.clearSelection()
        self.selection_changed()

    def add_vehicle(self):
        dialog = VehicleDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                self.service.add_vehicle(
                    dialog.result_vehicle
                )
            except Exception as exc:
                QMessageBox.warning(
                    self,
                    "Save Failed",
                    str(exc),
                )
                return

            self.refresh()

            QMessageBox.information(
                self,
                "Saved",
                "Vehicle added successfully.",
            )

    def update_vehicle(self):
        vehicle = self.selected_vehicle()

        if vehicle is None:
            QMessageBox.warning(
                self,
                "Selection Required",
                "Select a vehicle first.",
            )
            return

        dialog = VehicleDialog(
            self,
            vehicle,
        )

        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                self.service.update_vehicle(
                    dialog.result_vehicle
                )
            except Exception as exc:
                QMessageBox.warning(
                    self,
                    "Update Failed",
                    str(exc),
                )
                return

            self.refresh()

            QMessageBox.information(
                self,
                "Updated",
                "Vehicle updated successfully.",
            )

    def delete_vehicle(self):
        vehicle = self.selected_vehicle()

        if vehicle is None:
            QMessageBox.warning(
                self,
                "Selection Required",
                "Select a vehicle first.",
            )
            return

        answer = QMessageBox.question(
            self,
            "Delete Vehicle",
            f"Delete vehicle {vehicle.plate_number}?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            try:
                self.service.delete_vehicle(
                    vehicle.id
                )
            except Exception as exc:
                QMessageBox.warning(
                    self,
                    "Delete Failed",
                    str(exc),
                )
                return

            self.refresh()

            QMessageBox.information(
                self,
                "Deleted",
                "Vehicle deleted successfully.",
            )
