# Vehicle Registration System

**Project Version:** VehicleRegV0.3  
**Author:** Nikko Lim  
**Section:** CS26L (3581)

## Project Description

The Vehicle Registration System is a desktop application developed using Python, PyQt6, and SQLite3. It provides a graphical interface where authorized users can create accounts, log in, and manage vehicle registration records.

The system allows users to add, view, search, update, and delete vehicle information such as plate number, owner name, vehicle type, brand, model, year, color, engine number, chassis number, registration date, expiry date, and registration status.

The project addresses the need for a more organized and persistent way to manage vehicle registration records. Instead of keeping information in temporary program variables or manually maintaining records, the application stores data in an SQLite database so records remain available after the application is closed and reopened. It also separates the graphical interface, business logic, data models, and database operations to make the project easier to maintain and extend.

## Project Objectives

The main objectives of the project are:

- Develop a desktop-based vehicle registration management system using Python.
- Provide user registration, login, and logout functionality.
- Store user and vehicle records persistently using SQLite3.
- Implement Create, Read, Update, Delete, and Search operations for vehicle records.
- Validate important vehicle information before saving it.
- Prevent duplicate plate numbers, engine numbers, and chassis numbers through database constraints.
- Provide a simple and user-friendly graphical interface using PyQt6.
- Apply object-oriented programming and modular programming principles.
- Separate the user interface, business logic, database operations, and data models into organized modules.
- Create a resizable interface that adapts to different window sizes.

## Features

### User Registration

Users can create an account by providing a username and password. The authentication feature validates the information before the account is stored.

### User Login

Registered users can log in before accessing the vehicle registration management interface.

### Logout

The logged-in user can safely log out of the system and return to the authentication screen.

### Add Vehicle

Users can register a vehicle by entering its required information and saving it to the SQLite database.

### View Vehicle Records

Saved vehicle registrations are displayed in a table inside the application.

### Update Vehicle

A user can select an existing vehicle record, load its information into the form, edit the values, and save the changes.

### Delete Vehicle

A selected vehicle record can be deleted after the user confirms the operation.

### Search Vehicle Records

The system supports searching vehicle records using information such as plate number, owner, brand, model, engine number, or chassis number.

### Registration and Expiry Dates

The system records the vehicle's registration date and expiration date using date input controls.

### Registration Status

Each vehicle can have a registration status such as Active, Expired, or Suspended.

### Persistent Storage

User and vehicle data are stored in SQLite3 and remain available after the application is restarted.

### Resizable GUI

The PyQt6 interface uses layouts so the form and vehicle table can adapt when the application window is resized.

## Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| PyQt6 | Desktop graphical user interface |
| SQLite3 | Local relational database |
| QSS | Styling for the PyQt6 interface |
| `sqlite3` | Python database library |
| `hashlib` | Password hashing used by the authentication service |
| `dataclasses` | Structured application models |
| `pathlib` | File and path handling |
| Git | Version control |
| GitHub | Source-code hosting |

## Project Structure

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

### Important Files and Folders

| File / Folder | Purpose |
| --- | --- |
| `main.py` | Application entry point. Initializes the database, services, authentication flow, and main window. |
| `style.qss` | Main application styling. |
| `requirements.txt` | Lists required third-party Python packages. |
| `.gitignore` | Prevents local/generated files such as the virtual environment and database from being committed. |
| `database/` | Contains database connection and table-creation logic. |
| `database/database.py` | Creates SQLite connections and the `users` and `vehicles` tables. |
| `features/authentication/` | Contains all authentication-related modules. |
| `authentication/model.py` | Defines the User data model and validation. |
| `authentication/repository.py` | Performs user-related SQLite operations. |
| `authentication/service.py` | Contains registration, login, logout, and password hashing logic. |
| `authentication/view.py` | Contains the PyQt6 login and registration interface. |
| `features/vehicles/` | Contains all vehicle-management modules. |
| `vehicles/model.py` | Defines the Vehicle data model and vehicle validation. |
| `vehicles/repository.py` | Performs vehicle CRUD and search SQL operations. |
| `vehicles/service.py` | Provides vehicle-management operations to the GUI. |
| `vehicles/view.py` | Contains the vehicle form, buttons, search field, and records table. |

## Installation and Setup

### Requirements

Before running the application, install:

- Python 3.10 or newer
- Git, if cloning from GitHub
- PyQt6

SQLite3 is included with standard Python installations.

### 1. Clone the Repository

```bash
git clone https://github.com/aslagyasoy/vehicle-registration-app.git
```

### 2. Open the Project Folder

```bash
cd vehicle-registration-app
```

If your repository/folder uses the `VehicleRegV0.3` name instead, open that folder instead.

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment on Windows

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If PyQt6 is not already listed or installed:

```bash
python -m pip install PyQt6
```

### 6. Run the Application

```bash
python main.py
```

The application automatically initializes the SQLite database tables when it starts.

## How to Use the System

1. Run `main.py`.
2. The authentication window will appear.
3. Create an account if you do not already have one.
4. Log in using your registered username and password.
5. The Vehicle Registration System window will open.
6. Enter the vehicle information in the registration form.
7. Click **Add Vehicle** to save a new vehicle.
8. Use the search box to locate an existing vehicle.
9. Click a row in the table to load that vehicle into the form.
10. Modify the information and click **Update Vehicle** to save changes.
11. Select a record and click **Delete Selected** to remove it.
12. Confirm the deletion when prompted.
13. Click **Clear** to reset the form.
14. Click **Log Out** when finished.

## OOP Implementation

The project uses object-oriented programming to organize the application into classes with specific responsibilities.

### Important Classes

#### `Database`

Manages SQLite database connections and creates the required database tables.

#### `User`

Represents a registered application user.

Example object:

```python
user = User(
    id=1,
    username="nikko"
)
```

#### `Vehicle`

Represents one vehicle registration record.

A Vehicle object contains information such as:

- ID
- Plate number
- Owner name
- Vehicle type
- Brand
- Model
- Year
- Color
- Engine number
- Chassis number
- Registration date
- Expiry date
- Status

#### `AuthenticationRepository`

Handles direct database operations involving user accounts.

#### `AuthenticationService`

Contains authentication-related application logic such as registration, login, logout, and password hashing.

#### `AuthenticationView`

Provides the PyQt6 graphical interface for user login and registration.

#### `VehicleRepository`

Handles direct SQLite operations involving vehicle records.

#### `VehicleService`

Acts as the application layer between the VehicleView and VehicleRepository.

#### `VehicleView`

Provides the graphical interface for creating, searching, updating, deleting, and viewing vehicle records.

### Encapsulation

Encapsulation is applied by grouping related data and behavior into focused classes.

For example:

- `Vehicle` contains vehicle data and validation.
- `VehicleRepository` contains vehicle database operations.
- `VehicleService` exposes vehicle-management operations.
- `VehicleView` contains vehicle GUI behavior.
- `AuthenticationService` contains authentication logic.

The GUI does not need to directly execute SQL because database operations are encapsulated inside repository classes.

### Inheritance

Inheritance is mainly used in the PyQt6 graphical interface.

For example:

```python
class VehicleView(QWidget):
```

`VehicleView` inherits the behavior and capabilities of PyQt6's `QWidget`.

The application's dialog windows similarly inherit from `QDialog`.

The current version does not use a custom domain hierarchy such as `Car(Vehicle)` or `Motorcycle(Vehicle)`.

### Polymorphism

The current project does not implement a major custom polymorphic domain hierarchy. Therefore, custom polymorphism is not a primary feature of this version.

PyQt6 itself uses object-oriented framework behavior, but the project does not claim a custom `Vehicle` subclass polymorphism implementation.

### Composition and Separation of Responsibilities

The project also uses object relationships where views receive services and services use repositories.

```text
User
  |
  v
View
  |
  v
Service
  |
  v
Repository
  |
  v
Database
  |
  v
SQLite3
```

This keeps the GUI separate from database-specific code.

## Database

The application uses an SQLite3 database.

```text
vehicle_registration.db
├── users
└── vehicles
```

### Users Table

| Field | Description |
| --- | --- |
| `id` | Unique user ID |
| `username` | Unique login username |
| `password` | Hashed password value |

### Vehicles Table

| Field | Description |
| --- | --- |
| `id` | Unique vehicle record ID |
| `plate_number` | Vehicle plate number |
| `owner_name` | Registered owner |
| `vehicle_type` | Vehicle type |
| `brand` | Vehicle manufacturer/brand |
| `model` | Vehicle model |
| `year` | Vehicle year |
| `color` | Vehicle color |
| `engine_number` | Unique engine identifier |
| `chassis_number` | Unique chassis identifier |
| `registration_date` | Registration date |
| `expiry_date` | Registration expiration date |
| `status` | Registration status |

The database uses unique constraints for important identifying fields such as the username, plate number, engine number, and chassis number.

## Database Operations

### Create

The system performs `INSERT` operations when a new user or vehicle record is created.

Example process:

```text
Vehicle Form
    ↓
Vehicle Object
    ↓
VehicleService
    ↓
VehicleRepository
    ↓
INSERT
    ↓
SQLite3
```

### Read

Vehicle records are retrieved from SQLite and displayed in the PyQt6 table.

### Update

When the user selects a record, the vehicle ID is stored and its values are loaded into the form. Saving the edited form updates the existing database row.

### Delete

The system deletes the selected vehicle record after the user confirms the action.

### Search

Search text is passed through the service to the repository. The repository searches multiple vehicle fields and returns matching records.

The search includes fields such as:

- Plate number
- Owner name
- Brand
- Model
- Engine number
- Chassis number

Parameterized SQL queries are used so user-supplied values are handled separately from the SQL statement.

## Screenshots

Add the screenshots from the working application to a folder named `screenshots` in the project.

Recommended structure:

```text
VehicleRegV0.3/
└── screenshots/
    ├── login.png
    ├── registration.png
    ├── vehicle-dashboard.png
    ├── add-vehicle.png
    └── search-update.png
```

### Screenshot 1 - Login Screen

<img width="426" height="446" alt="Screenshot 2026-10-04 180319" src="https://github.com/user-attachments/assets/507ec9e9-53a3-41ab-b9df-495474bd6680" />

**Description:** The Vehicle Registration System login screen where registered users enter their username and password. It also provides a **Create an Account** option for new users.

### Screenshot 2 - User Registration

<img width="419" height="445" alt="Screenshot 2026-10-04 182612" src="https://github.com/user-attachments/assets/1641be70-0358-44ad-9dda-fcda23405f51" />

**Description:** The user registration screen where a new user creates an account by entering a username, password, and password confirmation. The form shows the minimum username and password requirements and provides a **Back to Login** option.

### Screenshot 3 - Vehicle Registration Dashboard

<img width="1205" height="834" alt="Screenshot 2026-10-04 182703" src="https://github.com/user-attachments/assets/3de3f9e1-009a-4869-bb59-6e9322b96869" />

**Description:** The main Vehicle Registration System dashboard after a successful login. It contains the complete vehicle registration form, registration and expiry dates, status selection, Add Vehicle, Clear, and Delete Selected controls, a vehicle search field, and the table of saved vehicle registration records. The header also displays the currently logged-in user and provides a Log Out button.

### Screenshot 4 - Adding a Vehicle

<img width="1183" height="517" alt="Screenshot 2026-10-04 182752" src="https://github.com/user-attachments/assets/232da2aa-d714-42ec-8523-4bac20eae000" />

**Description:** The vehicle registration form used to enter a new vehicle record. It includes fields for plate number, owner name, vehicle type, brand, model, year, color, engine number, chassis number, registration date, expiry date, and status. The **Add Vehicle** button saves the completed record, **Clear** resets the form, and **Delete Selected** removes a selected existing record.

### Screenshot 5 - Search and Update

<img width="1194" height="703" alt="Screenshot 2026-10-04 182829" src="https://github.com/user-attachments/assets/86d59c97-d841-4e36-9acc-274069617a29" />

**Description:** The search and update workflow of the Vehicle Registration System. The search field filters the vehicle table using the entered value. After a matching record is selected, its saved information is loaded into the form and the **Add Vehicle** button changes to **Update Vehicle**, allowing the user to edit and save the existing registration record.

> Replace or add screenshot files in the `screenshots` folder using the filenames above so they display correctly on GitHub.

## Testing

The current version was tested primarily through manual functional testing.

| Test Case | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Start application | Application starts and database tables are initialized | Application starts successfully and displays authentication screen | Passed |
| Register valid user | New account is created | Account is created successfully | Passed |
| Register duplicate username | Duplicate account is rejected | User cannot register the same username again | Passed |
| Password shorter than required length | Validation message is displayed | Invalid password is rejected | Passed |
| Login with correct credentials | Main application opens | Vehicle Registration System opens | Passed |
| Login with incorrect credentials | Login is rejected | Error message is displayed | Passed |
| Add valid vehicle | Vehicle is stored and displayed | Vehicle appears in the records table | Passed |
| Submit invalid/missing vehicle data | Validation error is displayed | Invalid record is not saved | Passed |
| Add duplicate unique vehicle information | Duplicate data is rejected | Database prevents duplicate unique values | Passed |
| Search vehicle | Matching records are displayed | Table updates to matching records | Passed |
| Select vehicle | Vehicle information loads into form | Selected row values appear in form | Passed |
| Update vehicle | Existing record is changed | Updated information appears in table/database | Passed |
| Delete vehicle | Record is removed after confirmation | Selected record is deleted | Passed |
| Restart application | Existing records remain available | SQLite records remain after restart | Passed |
| Resize window | Interface adjusts to available size | Form and table resize with the window | Passed |
| Logout | Current session ends | User returns to authentication flow | Passed |

## Known Issues / Limitations

The current version has the following limitations:

- There is no role-based access control. Authenticated users currently have the same vehicle-management permissions.
- Password hashing currently uses SHA-256. A production application should use a password-specific salted algorithm such as Argon2, bcrypt, or PBKDF2.
- There is no forgot-password or password-reset feature.
- Vehicle registration status is selected manually and is not automatically changed to Expired based on the expiry date.
- The current model does not automatically enforce that the expiry date must be later than the registration date.
- There is no audit log showing which user created, updated, or deleted a vehicle.
- The vehicle table does not currently use pagination.
- The system is a local desktop application and does not provide multi-computer synchronization.
- The SQLite database is local to the computer running the program.
- The project currently relies mainly on manual functional testing rather than a complete automated unit-test suite.

## Author

**Name:** Nikko Lim  
**Section:** CS26L (3581)

## Version

**VehicleRegV0.3**

Current functionality includes authentication, SQLite3 persistence, vehicle CRUD operations, search, validation, registration and expiry dates, registration status, and a PyQt6 graphical interface.

## License

Created for educational purposes.
