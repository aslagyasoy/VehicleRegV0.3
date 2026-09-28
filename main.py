import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from database.database import Database
from features.authentication.service import AuthenticationService
from features.authentication.view import AuthenticationView
from features.vehicles.service import VehicleService
from features.vehicles.view import VehicleView


class VehicleRegistrationWindow(QDialog):
    def __init__(self, vehicles, authentication):
        super().__init__()
        self.authentication = authentication
        self.logged_out = False

        self.setWindowTitle("Vehicle Registration System")
        self.resize(1100, 700)
        self.setObjectName("mainContent")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 24)
        layout.setSpacing(14)

        header = QWidget()
        header.setObjectName("appHeader")
        header.setMinimumHeight(78)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(22, 14, 18, 14)
        header_layout.setSpacing(16)

        title_group = QVBoxLayout()
        title_group.setSpacing(2)

        title = QLabel("Vehicle Registration System")
        title.setObjectName("appTitle")

        subtitle = QLabel("Manage vehicle registration records")
        subtitle.setObjectName("appSubtitle")

        title_group.addWidget(title)
        title_group.addWidget(subtitle)
        header_layout.addLayout(title_group, 1)

        current_user = self.authentication.current_user
        username = current_user.username if current_user else "User"

        user_label = QLabel(f"Logged in as: {username}")
        user_label.setObjectName("userLabel")
        header_layout.addWidget(user_label)

        logout_button = QPushButton("Log Out")
        logout_button.setObjectName("logoutButton")
        logout_button.setFixedHeight(36)
        logout_button.clicked.connect(self.logout)
        header_layout.addWidget(logout_button)

        layout.addWidget(header)

        tabs = QTabWidget()
        tabs.addTab(VehicleView(vehicles), "Vehicle Registrations")
        layout.addWidget(tabs)

    def logout(self):
        answer = QMessageBox.question(
            self,
            "Log Out",
            "Are you sure you want to log out?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.authentication.logout()
            self.logged_out = True
            self.close()


def main():
    database = Database()
    database.create_tables()

    app = QApplication(sys.argv)
    app.setStyleSheet((Path(__file__).with_name("style.qss")).read_text())

    authentication = AuthenticationService(database)
    vehicles = VehicleService(database)

    while True:
        login_dialog = AuthenticationView(authentication)
        if login_dialog.exec() != QDialog.DialogCode.Accepted:
            return 0

        window = VehicleRegistrationWindow(vehicles, authentication)
        window.exec()

        if not window.logged_out:
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
