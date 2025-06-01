DATABASE_NAME = "school.db"


class StudentDAL:

    def __init__(self):
        import sqlite3

        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def create(self, nom: str, age: int):
        """
        Insérer un nouvel étudiant
        """
        arguments = (nom, age)
        requete = "INSERT INTO etudiants(nom, age) VALUES(?, ?)"
        self.cursor.execute(requete, arguments)
        self.connection.commit()

    def update(self, name: str, age: int, id: int):
        """
        Modifie un étudiant avec la possibilité de modifier le nom et/ou age
        """
        arguments = {
            "id": id
        }
        if name:
            arguments["name"] = name
        if age:
            arguments["age"] = age

        requete = "UPDATE etudiants SET :nom, :age WHERE :id"
        self.cursor.execute(requete, arguments)
        self.connection.commit()

    def delete(self, id: int):
        """
        supprime un étudiant à partir de son id
        """
        arguments = (id,)
        requete = "DELETE FROM etudiants WHERE id = ?"
        self.cursor.execute(requete, arguments)
        self.connection.commit()

    def get_one(self, id: int):
        """
        Retourne un seul étudiant à partir de son id
        """
        arguments = (id,)
        requete = "SELECT * FROM etudiants WHERE id = ?"
        self.cursor.execute(requete, arguments)
        return self.cursor.fetchone()
  
    def get_all(self):
        """
        Retourne l'ensemble des étudiants
        """
        requete = "SELECT * FROM etudiants"
        self.cursor.execute(requete)

        return [
            {
                "id": item[0],
                "nom": item[1],
                "age": item[2]
            } for item in self.cursor.fetchall()
        ]

class UtilisateurDAL:

    def __init__(self, bcrypt):
        import sqlite3
        self.bcrypt = bcrypt
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def create(self, nom, prenom, email, mot_de_passe, nom_utilisateur):
        """
        Méthode permettant l'inscription d'un nouvel utilisateur
        """
        requete = "INSERT INTO utilisateurs(nom, prenom, email, mot_de_passe, nom_utilisateur) VALUES(?, ?, ?, ?, ?)"
        password_hash = self.bcrypt.generate_password_hash(mot_de_passe)
        arguments = (nom, prenom, email, password_hash, nom_utilisateur)
        self.cursor.execute(requete, arguments)
        self.connection.commit()

    def get_user_by_username(self, username):
        """
        Récupération de l'utilisateur en fonction du nom d'utilisateur
        """
        requete = "SELECT * FROM utilisateurs WHERE nom_utilisateur = ?"
        arguments = (username,)
        self.cursor.execute(requete, arguments)
        result = self.cursor.fetchone()
        return {
            "id": result[0],
            "username": result[3],
            "password": result[-1]
        }
