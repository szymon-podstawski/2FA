# Two-Factor Authentication (2FA) for Admins

This project implements a backend application with two-factor authentication (2FA) for admin users. The application ensures secure login with role-based access control and OTP-based 2FA.

## Features
- User authentication with roles (`admin` and `user`).
- Two-factor authentication for admin users.
- Secure password storage using hashing (`bcrypt` or `Django auth`).
- Dockerized deployment with database support (PostgreSQL/MySQL).

## Technologies Used
- **Backend Framework**: Flask or Django.
- **Database**: PostgreSQL/MySQL.
- **2FA**: Libraries like `pyotp` or `django-otp`.
- **Deployment**: Docker and Docker Compose.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/enable-2fa-for-admins.git
   cd enable-2fa-for-admins
Install Dependencies:

Create and activate a virtual environment:
bash
Kopiuj
Edytuj
python3 -m venv venv
source venv/bin/activate
Install required packages:
bash
Kopiuj
Edytuj
pip install -r requirements.txt
Run Locally:

Flask:
bash
Kopiuj
Edytuj
python app.py
Django:
bash
Kopiuj
Edytuj
python manage.py runserver
Run with Docker:

bash
Kopiuj
Edytuj
docker-compose up --build
How to Enable 2FA
Admin users can generate a QR code using an endpoint.
Scan the QR code with an app like Google Authenticator.
Use the generated OTP during login.
Tests
Includes unit and integration tests:
User registration and login tests.
OTP verification tests.
Role-based access tests.
Run tests:
bash
Kopiuj
Edytuj
pytest
Example Admin User
Username: admin
Password: admin123
2FA: Enabled (use the provided QR code or OTP generator for testing).
Future Improvements
Frontend integration.
Support for additional 2FA methods.
Advanced error handling and logging.
Feel free to contribute by submitting issues or pull requests. For detailed information, check the documentation in the repository.
