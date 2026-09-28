# VehicleRegV0.3

A desktop Vehicle Registration System built with **Python**, **PyQt6**, and **SQLite3**.

## Features

- User registration and login
- Vehicle registration management
- Add vehicle records
- View vehicle records
- Update vehicle records
- Delete vehicle records
- Search vehicle records
- Registration and expiration dates
- Registration status
- SQLite3 data persistence
- PyQt6 graphical user interface

## Project Architecture

```text
VehicleRegV0.3/
├── main.py
├── style.qss
├── README.md
├── requirements.txt
├── .gitignore
├── database/
│   ├── __init__.py
│   └── database.py
└── features/
    ├── __init__.py
    ├── authentication/
    │   ├── __init__.py
    │   ├── model.py
    │   ├── repository.py
    │   ├── service.py
    │   ├── view.py
    │   └── style.qss
    └── vehicles/
        ├── __init__.py
        ├── model.py
        ├── repository.py
        ├── service.py
        ├── view.py
        └── style.qss
```

## Architecture

The project separates responsibilities into four layers.

### Model

`model.py` defines application data objects and validation rules.

Examples:

- `User`
- `Vehicle`

### Repository

`repository.py` handles communication with SQLite3.

It contains database operations such as:

- INSERT
- SELECT
- UPDATE
- DELETE

### Service

`service.py` contains application/business logic and connects the user interface to the repository.

```text
View
  ↓
Service
  ↓
Repository
  ↓
SQLite3
```

### View

`view.py` contains the PyQt6 graphical user interface, including forms, buttons, tables, input fields, and dialogs.

## Database

The application uses one SQLite database containing separate tables.

```text
vehicle_registration.db
├── users
└── vehicles
```

### Users Table

| Field | Description |
| --- | --- |
| id | Unique user ID |
| username | Login username |
| password | Stored password |

### Vehicles Table

| Field | Description |
| --- | --- |
| id | Vehicle record ID |
| plate_number | Vehicle plate number |
| owner_name | Registered owner |
| vehicle_type | Vehicle type |
| brand | Vehicle manufacturer |
| model | Vehicle model |
| year | Vehicle year |
| color | Vehicle color |
| engine_number | Engine identifier |
| chassis_number | Chassis identifier |
| registration_date | Registration date |
| expiry_date | Registration expiration date |
| status | Registration status |

The database file is generated locally and excluded from Git through `.gitignore`.

## Application Flow

```text
Start Application
       |
       v
Initialize SQLite Database
       |
       v
Login / Registration
       |
       v
Vehicle Registration System
       |
       +---- Add Vehicle
       |
       +---- Update Vehicle
       |
       +---- Delete Vehicle
       |
       +---- Search Vehicles
       |
       v
SQLite Database
```

## Technologies

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| PyQt6 | Desktop GUI |
| SQLite3 | Database |
| QSS | GUI styling |
| Git | Version control |
| GitHub | Source-code hosting |

## Requirements

- Python 3.10 or newer
- PyQt6
- SQLite3 (included with Python)

## Installation

Clone the repository:

```bash
git clone https://github.com/aslagyasoy/VehicleRegV0.3.git
```

Open the project:

```bash
cd VehicleRegV0.3
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## GitHub Files

The following local/generated files should not be uploaded:

- `.idea/`
- `.venv/`
- `__pycache__/`
- SQLite `.db` files

They are excluded by `.gitignore`.

## Programming Concepts Used

- Object-Oriented Programming
- Classes and objects
- Modular programming
- SQLite database management
- CRUD operations
- Exception handling
- Input validation
- GUI programming
- Authentication
- Separation of concerns

## Version

**VehicleRegV0.3**

Current functionality includes authentication, SQLite storage, vehicle CRUD operations, search, and a PyQt6 graphical interface.

## License

Created for educational purposes.
