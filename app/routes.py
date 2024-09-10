from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Abonnement, Utilisateur, Session, Camera
from . import socketio
import sqlite3
import cv2
import numpy as np
from flask_socketio import emit

# Create a blueprint for the routes
bp = Blueprint('main', __name__)

def setup_routes(app):
    app.register_blueprint(bp)

@bp.route('/admin')
def index():
    return render_template('admin/index.html')

@bp.route('/admin/admin_dashboard')
def admin_dashboard():
    abonnements = Abonnement.query.all()
    utilisateurs = Utilisateur.query.all()
    return render_template('admin/admin_dashboard.html', abonnements=abonnements, utilisateurs=utilisateurs)

# Route pour gérer les abonnements
@bp.route('/admin/abonnements')
def manage_abonnements():
    abonnements = Abonnement.query.all()
    return render_template('admin/abonnements.html', abonnements=abonnements)

# Route pour gérer les utilisateurs
@bp.route('/admin/utilisateurs')
def manage_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    return render_template('admin/utilisateurs.html', utilisateurs=utilisateurs)

# Ajouter des routes pour CRUD des Sessions et des Caméras

@bp.route('/')
def home():
    return render_template('index.html')  # Page d'accueil

@bp.route('/indes')
def indes():
    return render_template('indes.html')  # Page indes

@bp.route('/tarifs')
def tarifs():
    return render_template('tarifs.html')  # Page tarifs

@bp.route('/inscription')
def inscription():
    return render_template('inscription.html')  # Page inscription

@bp.route('/contact')
def contact():
    return render_template('contact.html')  # Page contact

@bp.route('/socket')
def socket():
    return render_template('socket.html')  # Page socket

@bp.route('/abonnement/save', methods=['POST'])
def save_abonnement():
    if request.method == 'POST':
        email = request.form['email']
        # Sauvegarder l'email dans la base de données ou envoyer un email de confirmation
        flash('Abonnement réussi ! Merci de vous être abonné.')
        return redirect(url_for('home'))
    return render_template('view/abonnement.html')

    

def setup_socketio():
    @socketio.on('connect')
    def handle_connect():
        client_id = request.sid
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()
        c.execute("INSERT INTO clients (client_id) VALUES (?)", (client_id,))
        conn.commit()
        conn.close()
        print('Client connected:', client_id)

    @socketio.on('disconnect')
    def handle_disconnect():
        client_id = request.sid
        conn = sqlite3.connect('clients.db')
        c = conn.cursor()
        c.execute("DELETE FROM clients WHERE client_id=?", (client_id,))
        conn.commit()
        conn.close()
        print('Client disconnected:', client_id)

    @socketio.on('image')
    def handle_image(data):
        # Convertir les données d'image en format utilisable par OpenCV
        nparr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Analyse de l'image avec OpenCV (exemple de détection de mouvement)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        print('Image analysée')

        # Envoyer une notification au client
        emit('notification', {'message': 'Image analysée'})

    @socketio.event
    def connect_error(data):
        print("Connection failed:", data)

# Configurer les événements SocketIO
setup_socketio()

# Démarrer l'application
# if __name__ == '__main__':
#     bp.run(debug=True)
