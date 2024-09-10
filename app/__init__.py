# /app/__init__.py

from flask_socketio import SocketIO
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Importer les routes et les modèles après l'initialisation de db
# from app import routes, models  # noqa: E402

# Initialiser la base de données
db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///camlive.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    socketio.init_app(app)

    # Import routes here to avoid circular imports
    with app.app_context():
        from .routes import setup_routes
        setup_routes(app)

    return app

def init_db():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, client_id TEXT)''')
    conn.commit()
    conn.close()
