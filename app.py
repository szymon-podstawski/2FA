from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Ładowanie zmiennych środowiskowych
load_dotenv()

# Inicjalizacja aplikacji
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja rozszerzeń
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Import i rejestracja blueprintów
from app.routes.auth import auth_bp
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)