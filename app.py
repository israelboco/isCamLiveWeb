from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def init_db():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, client_id TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')  # Page d'accueil

@app.route('/abonnement')
def abonnement():
    return render_template('abonnement.html')  # Page d'abonnement

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Page contact


@app.route('/abonnement/save', methods=['POST'])
def saveAbonnement():
    if request.method == 'POST':
        email = request.form['email']
        # Sauvegarder l'email dans la base de données ou envoyer un email de confirmation
        flash('Abonnement réussi ! Merci de vous être abonné.')
        return redirect(url_for('home'))
    return render_template('view/abonnement.html')

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
    
    # Envoyer une notification au client
    emit('notification', {'message': 'Image analysée'})


if __name__ == '__main__':
    # app.run(debug=True)
    init_db()
    socketio.run(app, debug=True)
