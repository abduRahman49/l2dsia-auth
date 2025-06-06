# Import des dépendances
from flask import request, Flask, render_template, session, redirect, url_for
from database import StudentDAL, UtilisateurDAL
from forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt


# Instation de l'application Flask
app = Flask(__name__)
# Définit la classe Bcrypt pour la gestion de la cryptographie
bcrypt = Bcrypt(app)
app.debug = True
app.secret_key = "eflekljfkfljsl" # Clé à changer en production


# Définition des routes de notre application avec les contrôleurs (views)
@app.route("/etudiants")
def liste_edudiants():
    Etudiant = StudentDAL()
    etudiants = Etudiant.get_all()
    return render_template("etudiants.html", etudiants=etudiants)

@app.route("/delete/<int:id>")
def delete_etudiant(id):
    Etudiant = StudentDAL()
    Etudiant.delete(id)
    return redirect(url_for('liste_edudiants'))

@app.route("/", methods=["GET", "POST"])
def connexion():
    form = LoginForm()
    Utilisateur = UtilisateurDAL(bcrypt)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Utilisateur.get_user_by_username(username)
        print("user retrieved", user)

        hashed_password = user.get("password")
        if bcrypt.check_password_hash(hashed_password, password):
        # Logger l'utilisateur (avec ses données sauvegardées en session)
        # redirection vers la page principale
            print("Connexion réussie")
            session["user_id"] = user.get("id")
            return redirect(url_for('index'))

    return render_template("connexion.html", form=form)

@app.route("/inscription")
def register():
    ...
    return render_template("inscription.html")

@app.route("/process-inscription", methods=["POST"])
def process_registration():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    age = request.form.get('age')
    return render_template("remerciements.html", nom=nom, prenom=prenom)

@app.route("/register", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    Utilisateur = UtilisateurDAL(bcrypt)
    if form.validate_on_submit():
        nom_utilisateur = form.username.data
        mot_de_passe = form.password.data
        prenom = form.prenom.data
        nom = form.nom.data
        email = form.email.data
        Utilisateur.create(nom, prenom, email, mot_de_passe, nom_utilisateur)
        # Récupérées les informations soumises et inscrire l'utilisateur
        return redirect(url_for('connexion'))

    return render_template("inscription.html", form=form)

@app.route("/home")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html")

@app.errorhandler(500)
def error_500(error):
    return render_template("error_500.html")

# Exécution de l'application en utilisant le mode script
if __name__ == "__main__":
    app.run()
