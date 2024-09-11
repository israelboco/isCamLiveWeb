from app import db
from datetime import datetime, timezone
import uuid


# Modèle pour gérer les formules d'abonnement
class Abonnement(db.Model):
    __tablename__ = 'abonnement'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Basic, Pro, Entreprise
    price = db.Column(db.Float, nullable=False)
    max_users = db.Column(db.Integer, nullable=False)
    max_cameras_per_session = db.Column(db.Integer, nullable=False)
    max_sessions_per_user = db.Column(db.Integer, nullable=False)
    secure_streaming = db.Column(db.Boolean, default=False)
    custom_options = db.Column(db.Boolean, default=False)  # Options supplémentaires pour entreprise

    def __repr__(self):
        return f'<Abonnement {self.name}>'


# Modèle pour les utilisateurs
class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('abonnement.id'), nullable=False)
    activation_key = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))  # Clé unique
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    subscription = db.relationship('Abonnement', backref='utilisateurs', lazy=True)

    def __repr__(self):
        return f'<Utilisateur {self.email}>'

# Modèle pour les contact support
class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<contact {self.email}>'


# Modèle pour les sessions utilisateur
class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    session_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    utilisateur = db.relationship('Utilisateur', backref='sessions', lazy=True)

    def __repr__(self):
        return f'<Session {self.session_name}>'


# Modèle pour les caméras connectées par session
class Camera(db.Model):
    __tablename__ = 'camera'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    camera_name = db.Column(db.String(100), nullable=False)
    camera_url = db.Column(db.String(255), nullable=False)  # URL ou IP de la caméra

    session = db.relationship('Session', backref='cameras', lazy=True)

    def __repr__(self):
        return f'<Camera {self.camera_name}>'
