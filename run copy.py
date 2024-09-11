from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Changer avec votre propre clé secrète

# Initialiser Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Vue de redirection si non connecté

# Exemple de base de données d'utilisateurs en mémoire (à remplacer par une vraie base de données)
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

# Classe User
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f'<User: {self.id}>'

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Route de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Vous êtes connecté avec succès.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'danger')
    return render_template('login.html')

# Route de dashboard (page protégée)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.id)

# Route de déconnexion
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
