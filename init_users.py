import sqlite3

# Création de l'objet connection
connection = sqlite3.connect("school.db")

# Création du curseur
cursor = connection.cursor()

# Initialisation du schéma de la base de données
with open("users.sql", "r") as file:
    script = file.read()

# Création du schéma de la base de données depuis le script
cursor.executescript(script)
