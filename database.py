import sqlite3

def connecter_db():
    connexion = sqlite3.connect("bibliotheque.db")
    connexion.execute("PRAGMA foreign_keys = ON")
    return connexion

def creer_tables(connexion):

    curseur = connexion.cursor()

    curseur.executescript("""
    
    CREATE TABLE IF NOT EXISTS livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        auteur TEXT NOT NULL,
        categorie TEXT,
        quantite_totale INTEGER NOT NULL,
        quantite_disponible INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS membres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        telephone TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS emprunts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livre_id INTEGER NOT NULL,
        membre_id INTEGER NOT NULL,
        date_emprunt TEXT NOT NULL,
        date_retour_prevue TEXT NOT NULL,
        date_retour_effective TEXT,

        FOREIGN KEY (livre_id) REFERENCES livres(id),
        FOREIGN KEY (membre_id) REFERENCES membres(id)
    );

    """)

    connexion.commit()
    print("Les tables ont été créées avec succès !")
