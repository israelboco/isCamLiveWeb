from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('view/index.html')  # Page d'accueil

@app.route('/abonnement')
def abonnement():
    return render_template('view/abonnement.html')  # Page d'abonnement

@app.route('/contact')
def contact():
    return render_template('view/contact.html')  # Page contact


@app.route('/abonnement/save', methods=['POST'])
def saveAbonnement():
    if request.method == 'POST':
        email = request.form['email']
        # Sauvegarder l'email dans la base de données ou envoyer un email de confirmation
        flash('Abonnement réussi ! Merci de vous être abonné.')
        return redirect(url_for('home'))
    return render_template('view/abonnement.html')


if __name__ == '__main__':
    app.run(debug=True)
