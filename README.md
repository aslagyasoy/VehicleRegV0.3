
# Vehicle Registration System

**Project Version:** VehicleRegV0.3  
**Author:** Nikko Lim  
**Section:** CS26L (3581)

## Project Description

The Vehicle Registration System is a desktop application developed using Python, PyQt6, and SQLite3. It allows authorized users to register, manage, search, update, and delete vehicle registration records through a graphical user interface.

The system provides a dashboard displaying vehicle statistics and a graph showing the number of registered vehicles by type. It also includes user authentication, vehicle registration popup forms, and a searchable vehicle records table.

The project addresses the need for an organized and reliable way to manage vehicle registration information. Instead of manually recording vehicle details or storing information temporarily, the application uses an SQLite database to preserve records even after the program is closed.

The application follows a modular architecture that separates data models, database operations, business logic, and graphical interfaces.

## Project Objectives

The main objectives of the project are:

1. Develop a desktop-based Vehicle Registration System using Python.
2. Implement user registration, login, and logout functionality.
3. Provide a user-friendly graphical interface using PyQt6.
4. Store user and vehicle records permanently using SQLite3.
5. Implement Create, Read, Update, Delete, and Search operations.
6. Provide a dashboard displaying vehicle registration statistics.
7. Visualize vehicle records using a graph grouped by vehicle type.
8. Allow users to add and update vehicles through popup forms.
9. Validate important vehicle registration information.
10. Apply object-oriented programming and modular programming principles.
11. Separate the interface, business logic, and database operations.
12. Create a responsive interface that adjusts when the application window is resized.

## Features

The Vehicle Registration System is organized into two main functional modules: **Authentication** and **Vehicle Management**.

Each module follows a modular structure consisting of a Model, Repository, Service, and View.

### 1. Authentication Module

**Location:** `features/authentication/`

The Authentication module manages user access to the system.

- **User Registration:** Allows new users to create an account using a username and password.
- **User Login:** Authenticates registered users before granting access to the application.
- **Logout:** Allows users to exit their current session and return to the login screen.
- **Input Validation:** Validates usernames and passwords during account registration and login.
- **Password Hashing:** Uses SHA-256 hashing before storing passwords in the database.

### 2. Vehicle Management Module

**Location:** `features/vehicles/`

The Vehicle Management module handles vehicle registration records and provides the main application dashboard.

- **Vehicle Dashboard:** Displays an overview of registered vehicles.
- **Vehicle Statistics:** Shows the total number of vehicles, cars, motorcycles, and other vehicle types.
- **Vehicle Type Graph:** Displays a horizontal bar graph of registered vehicles grouped by type.
- **Add Vehicle:** Opens a popup form where users can enter and save vehicle registration information.
- **View Vehicle Records:** Displays saved vehicle registrations in a searchable and responsive table.
- **Update Vehicle:** Allows users to select an existing vehicle and modify its information using a prefilled popup form.
- **Delete Vehicle:** Removes a selected vehicle record after confirmation.
- **Search Vehicle Records:** Filters records using plate number, owner name, brand, model, engine number, or chassis number.
- **Registration and Expiry Dates:** Stores and manages vehicle registration and expiration dates.
- **Registration Status:** Tracks vehicle status, including Active, Expired, and Suspended.
- **Automatic Dashboard Refresh:** Updates the table, statistics, and graph after successful additions, updates, or deletions.

### 3. Shared System Features

- **SQLite Database:** Stores user accounts and vehicle registration records locally.
- **Persistent Storage:** Preserves saved information when the application is closed and reopened.
- **Input Validation:** Helps prevent invalid or incomplete vehicle information.
- **Responsive Interface:** Adjusts the dashboard, table, and controls when the application window is resized.
- **Modular Architecture:** Separates models, repositories, services, and views for easier maintenance.

## Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| PyQt6 | Desktop graphical user interface |
| SQLite3 | Local relational database |
| QSS | Styling for the PyQt6 interface |
| sqlite3 | Python database library |
| hashlib | Password hashing |
| dataclasses | Structured application models |
| pathlib | File and path handling |
| collections.Counter | Counting vehicles by type |
| QPainter | Drawing the dashboard graph |
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
├── screenshots/
│   ├── login.png
│   ├── registration.png
│   ├── vehicle-dashboard.png
│   ├── add-vehicle.png
│   └── search-update.png
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
        ├── dialog.py
        └── style.qss
```

### Important Files and Folders

| File / Folder | Purpose |
| --- | --- |
| `main.py` | Initializes the application, database, services, authentication flow, and main window. |
| `style.qss` | Main application styling. |
| `README.md` | Project documentation. |
| `requirements.txt` | Lists the required Python dependencies. |
| `.gitignore` | Excludes generated files and local environment files from Git. |
| `screenshots/` | Contains screenshots of the working application. |
| `database/` | Contains database-related functionality. |
| `database/database.py` | Creates SQLite connections and database tables. |
| `features/authentication/` | Contains user authentication modules. |
| `authentication/model.py` | Defines the User data model. |
| `authentication/repository.py` | Performs database operations involving user accounts. |
| `authentication/service.py` | Handles registration, login, and password hashing logic. |
| `authentication/view.py` | Provides the login and registration interface. |
| `features/vehicles/` | Contains vehicle registration management modules. |
| `vehicles/model.py` | Defines the Vehicle data model and validation. |
| `vehicles/repository.py` | Performs vehicle CRUD and search operations. |
| `vehicles/service.py` | Connects vehicle business logic with the repository. |
| `vehicles/view.py` | Provides the vehicle dashboard, statistics, graph, search, table, and action buttons. |
| `vehicles/dialog.py` | Provides the Add Vehicle and Update Vehicle popup forms. |
| `vehicles/style.qss` | Contains vehicle interface styling. |

## Installation and Setup

### System Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- Git
- PyQt6
- SQLite3

SQLite3 is included with standard Python installations.

### Step 1: Clone the Repository

```bash
git clone https://github.com/aslagyasoy/VehicleRegV0.3.git
```

### Step 2: Open the Project Folder

```bash
cd VehicleRegV0.3
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```cmd
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If PyQt6 is not installed:

```bash
python -m pip install PyQt6
```

### Step 6: Run the Application

```bash
python main.py
```

The application automatically initializes the required SQLite database tables when it starts.

## How to Use the System

### 1. User Registration

1. Launch the application.
2. Click **Create an Account**.
3. Enter a username.
4. Enter a password.
5. Confirm the password.
6. Click **Register**.
7. Return to the login screen.

### 2. User Login

1. Enter the registered username.
2. Enter the correct password.
3. Click **Log In**.
4. The Vehicle Registration Dashboard will open.

### 3. View Dashboard

After logging in, the dashboard displays:

- Total registered vehicles
- Total cars
- Total motorcycles
- Total other vehicle types
- Vehicle-type distribution graph
- Searchable vehicle records table

The dashboard statistics are calculated using the records stored in SQLite.

### 4. Add Vehicle

1. Click **+ Add Vehicle**.
2. The Add Vehicle popup will appear.
3. Enter the required vehicle information.
4. Select the vehicle type.
5. Enter the registration and expiry dates.
6. Select the registration status.
7. Click **Add Vehicle**.
8. The vehicle will be saved to the database.

The dashboard statistics, graph, and table will automatically refresh.

### 5. Search Vehicle

1. Locate the search bar above the table.
2. Enter a plate number, owner name, brand, model, engine number, or chassis number.
3. The table will automatically display matching records.

### 6. Update Vehicle

1. Select an existing vehicle from the table.
2. Click **Update Selected**.
3. The Update Vehicle popup will appear with the saved information.
4. Modify the necessary details.
5. Click **Update Vehicle**.
6. The system will save the changes and refresh the dashboard.

### 7. Delete Vehicle

1. Select a vehicle from the table.
2. Click **Delete Selected**.
3. A confirmation dialog will appear.
4. Confirm the deletion.
5. The record will be removed from the database.

The table, statistics, and graph will automatically update.

### 8. Logout

1. Click **Log Out**.
2. The current session will end.
3. The application will return to the authentication screen.

## OOP Implementation

The project applies object-oriented programming to organize the system into reusable classes with specific responsibilities.

### Important Classes

#### Database

The `Database` class manages SQLite connections and initializes the required database tables.

#### User

The `User` class represents a registered application user.

It stores user information such as:

- User ID
- Username
- Password hash

#### Vehicle

The `Vehicle` class represents a vehicle registration record.

It contains:

- Vehicle ID
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

#### AuthenticationRepository

Handles database operations involving user accounts.

#### AuthenticationService

Handles user registration, login, password hashing, and authentication-related business logic.

#### AuthenticationView

Provides the PyQt6 interface for login and registration.

#### VehicleRepository

Handles database operations for vehicle registration records.

#### VehicleService

Acts as the business logic layer between the vehicle interface and repository.

#### VehicleView

Provides the main dashboard interface, including:

- Vehicle statistics
- Vehicle-type graph
- Search functionality
- Vehicle records table
- Add, Update, and Delete controls

#### VehicleDialog

Provides the popup form used to add and update vehicle information.

#### VehicleTypeChart

Uses PyQt6's `QPainter` to draw a horizontal bar graph showing the number of registered vehicles by type.

### Encapsulation

Encapsulation is applied by organizing related data and behavior into separate classes.

Examples:

- `Vehicle` contains vehicle information and validation.
- `VehicleRepository` contains vehicle database operations.
- `VehicleService` manages vehicle-related application logic.
- `VehicleView` manages the dashboard and table interface.
- `VehicleDialog` manages the Add and Update popup forms.
- `AuthenticationService` handles authentication logic.

This organization prevents the graphical interface from directly managing SQL queries.

### Inheritance

Inheritance is used primarily through PyQt6.

Examples:

```python
class VehicleView(QWidget):
    pass
```

```python
class VehicleDialog(QDialog):
    pass
```

```python
class VehicleTypeChart(QWidget):
    pass
```

These classes inherit existing functionality from PyQt6 components.

The project does not currently implement a custom vehicle inheritance hierarchy such as `Car(Vehicle)` or `Motorcycle(Vehicle)`.

### Polymorphism

The application uses PyQt6 framework methods that can be overridden by subclasses.

For example, `VehicleTypeChart` implements `paintEvent()` to provide custom drawing behavior.

This is an example of method overriding.

The project does not currently implement a separate custom domain polymorphism hierarchy.

### Composition

The system uses composition to connect components.

```text
VehicleView
    |
    +-- VehicleDialog
    |
    +-- VehicleTypeChart
    |
    +-- VehicleService
            |
            +-- VehicleRepository
                    |
                    +-- Database
                            |
                            +-- SQLite3
```

This architecture separates the interface, business logic, and database operations.

## Database

The application uses SQLite3 for persistent data storage.

### Database Name

```text
vehicle_registration.db
```

### Database Tables

```text
vehicle_registration.db
├── users
└── vehicles
```

### Users Table

| Field | Description |
| --- | --- |
| id | Unique user identifier |
| username | Unique username |
| password | Hashed user password |

### Vehicles Table

| Field | Description |
| --- | --- |
| id | Unique vehicle record identifier |
| plate_number | Vehicle plate number |
| owner_name | Registered owner |
| vehicle_type | Type of vehicle |
| brand | Vehicle manufacturer |
| model | Vehicle model |
| year | Vehicle year |
| color | Vehicle color |
| engine_number | Engine identifier |
| chassis_number | Chassis identifier |
| registration_date | Date of registration |
| expiry_date | Registration expiration date |
| status | Current registration status |

### Database Operations

#### Create

The system inserts a new record when a user registers an account or adds a vehicle.

#### Read

The system retrieves stored vehicle information and displays it in the dashboard table.

#### Update

The system updates an existing vehicle record when the user saves changes through the Update Vehicle popup.

#### Delete

The system removes a selected vehicle record after confirmation.

#### Search

The system searches vehicle records using information such as:

- Plate number
- Owner name
- Brand
- Model
- Engine number
- Chassis number

### Database Constraints

The database uses unique constraints for important identifiers such as:

- Username
- Plate number
- Engine number
- Chassis number

These constraints help prevent duplicate records.

## Screenshots

The following screenshots demonstrate the important interfaces and functions of the application.

### Screenshot 1 - Login Screen

<img width="427" height="445" alt="Screenshot 2026-10-11 230849" src="https://github.com/user-attachments/assets/cbc1572b-e50a-487b-b8cb-3e211b8d39aa" />

**Description:** The login screen where registered users enter their username and password to access the Vehicle Registration System. It also provides a Create an Account option for new users.

### Screenshot 2 - User Registration

<img width="423" height="445" alt="Screenshot 2026-10-11 230912" src="https://github.com/user-attachments/assets/ad4e8294-42e0-4071-b7dc-bf267530dba7" />

**Description:** The user registration screen where new users create an account by entering a username, password, and password confirmation.

### Screenshot 3 - Vehicle Registration Dashboard

<img width="1200" height="835" alt="Screenshot 2026-10-11 230539" src="https://github.com/user-attachments/assets/0c0cebbc-8836-461e-bd02-e5656ad1de83" />

**Description:** The main application dashboard displaying vehicle registration records and the controls available to authenticated users.

The updated dashboard also includes vehicle statistics, a vehicle-type graph, a searchable table, and an Add Vehicle popup button.

### Screenshot 4 - Adding a Vehicle

<img width="1197" height="829" alt="Screenshot 2026-10-11 230658" src="https://github.com/user-attachments/assets/74d4fc6a-eee8-4397-aa60-8142f6668a87" />

**Description:** The vehicle registration form used to enter the information required for a new vehicle record.

In the updated application, this form is displayed in a separate popup instead of directly on the main dashboard.

### Screenshot 5 - Search and Update

<img width="1190" height="388" alt="Screenshot 2026-10-11 230737" src="https://github.com/user-attachments/assets/77b4c054-d9f1-4a0c-8a20-6860805c837d" />

**Description:** The vehicle search and update workflow. Users can locate an existing record, select it, and modify its saved information.

In the updated application, the selected vehicle's information is loaded into an Update Vehicle popup.

**Note:** Screenshots 3–5 document the earlier form-based interface. They should be replaced with new screenshots of the dashboard and popup interface to reflect the latest version accurately.

## Testing

The application is evaluated through manual functional testing.

The following table lists the expected behavior and the results that should be verified when testing the latest version.

| Test Case | Expected Result | Actual Result | Status |
| --- | --- | --- | --- |
| Launch application | Authentication window appears | To be verified | Pending |
| Register valid user | Account is created | To be verified | Pending |
| Register duplicate username | Duplicate registration is rejected | To be verified | Pending |
| Login with valid credentials | Dashboard opens | To be verified | Pending |
| Login with invalid credentials | Login is rejected | To be verified | Pending |
| Load dashboard | Vehicle statistics and graph appear | Dashboard displayed in provided screenshot | Observed |
| Count vehicle types | Statistics match SQLite records | Four vehicles displayed: two cars and two motorcycles | Observed |
| Add Vehicle button | Registration popup opens | Popup displayed in provided screenshot | Observed |
| Add valid vehicle | Record is saved | To be verified | Pending |
| Submit incomplete vehicle information | Validation message appears | To be verified | Pending |
| Search vehicle | Table displays matching records | To be verified | Pending |
| Update selected vehicle | Popup opens with existing information | To be verified | Pending |
| Save updated vehicle | Database record is updated | To be verified | Pending |
| Delete selected vehicle | Record is removed after confirmation | To be verified | Pending |
| Refresh dashboard | Statistics and graph update | To be verified | Pending |
| Resize application | Dashboard and table adjust to window size | Full-width table update implemented | Pending verification |
| Restart application | Saved records remain available | To be verified | Pending |
| Logout | User returns to authentication screen | To be verified | Pending |

## Known Issues / Limitations

The current version has the following limitations:

1. **Local Database:** SQLite records are stored locally and are not synchronized across multiple computers.
2. **No Role-Based Access:** The system does not currently provide separate Administrator and Staff permissions.
3. **Password Security:** Authentication uses SHA-256 hashing. A production application should use a password-specific salted algorithm such as Argon2, bcrypt, or PBKDF2.
4. **No Password Recovery:** The system does not include a forgot-password feature.
5. **Manual Registration Status:** Registration status is selected manually rather than automatically calculated from the expiry date.
6. **No Audit Logs:** The system does not record which user created, updated, or deleted a vehicle.
7. **No Export Feature:** Vehicle records cannot currently be exported directly to PDF or Excel.
8. **No Cloud Synchronization:** The system does not currently support online database synchronization.
9. **No Pagination:** The vehicle table does not currently use pagination.
10. **Limited Automated Testing:** The application primarily relies on manual functional testing.
11. **Screenshot Updates:** Some existing screenshots show the earlier version of the interface and need to be replaced.

## Future Improvements

Possible improvements include:

- Administrator and Staff roles
- Password recovery
- Automated registration expiration monitoring
- Dashboard filtering by date
- PDF and Excel export
- Vehicle registration renewal reminders
- Audit logs for record changes
- Advanced search and filtering
- Database backup and restoration
- Automated unit testing
- Cloud database synchronization
- Printable vehicle registration reports

## Author

**Name:** Nikko Lim  
**Section:** CS26L (3581)

## Version

**VehicleRegV0.3**

The current version includes:

- User authentication
- Vehicle registration management
- SQLite3 persistence
- Add and Update Vehicle popup forms
- Vehicle dashboard
- Vehicle statistics
- Vehicle-type graph
- Searchable vehicle records table
- Create, Read, Update, and Delete operations
- Responsive table layout
- Input validation

## License

Created for educational purposes.
