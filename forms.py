from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired

# Formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField(label="Nom d'utilisateur", name="username", validators=[DataRequired()])
    password = PasswordField(label="Mot de passe", name="password", validators=[DataRequired()])


# Formulaire d'inscription
class RegistrationForm(FlaskForm):
    prenom = StringField(label="Prénom", validators=[DataRequired()])
    nom = StringField(label="Nom", validators=[DataRequired()])
    email = EmailField(label="@ email")
    username = StringField(label="Nom d'utilisateur", validators=[DataRequired()])
    password = PasswordField(label="Mot de passe", validators=[DataRequired()])
    password_confirm = PasswordField(label="Confirmation du mot de passe", validators=[DataRequired()])
