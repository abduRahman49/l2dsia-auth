CREATE TABLE utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom INTEGER NOT NULL,
    nom_utilisateur TEXT NOT NULL,
    email TEXT,
    mot_de_passe TEXT NOT NULL
);
