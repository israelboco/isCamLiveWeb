from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Abonnement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    max_users = db.Column(db.Integer, nullable=False)
    max_cameras_per_session = db.Column(db.Integer, nullable=False)
    max_sessions_per_user = db.Column(db.Integer, nullable=False)

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('abonnement.id'), nullable=False)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    session_name = db.Column(db.String(100), nullable=False)

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    camera_name = db.Column(db.String(100), nullable=False)
    camera_url = db.Column(db.String(200), nullable=False)
