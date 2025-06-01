from flask_login import LoginManager

# Instanciation du gestionnaire de connexion
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
