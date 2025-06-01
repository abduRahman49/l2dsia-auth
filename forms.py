from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo

# Formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField(label="Nom d'utilisateur", name="username", validators=[DataRequired()])
    password = PasswordField(label="Mot de passe", name="password", validators=[DataRequired()])


# Formulaire d'inscription
class RegistrationForm(FlaskForm):
    prenom = StringField(label="Prénom", name="prenom", validators=[DataRequired()])
    nom = StringField(label="Nom", name="nom", validators=[DataRequired()])
    email = EmailField(label="@ email", name="email")
    username = StringField(label="Nom d'utilisateur", name="username", validators=[DataRequired()])
    password = PasswordField(label="Mot de passe", name="password", validators=[DataRequired()])
    password_confirm = PasswordField(label="Confirmation du mot de passe",
                                     name="password_confirm",
                                     validators=[DataRequired(),
                                                 EqualTo("password", "Les valeurs des mots de passe sont différentes")]
                                                 )
