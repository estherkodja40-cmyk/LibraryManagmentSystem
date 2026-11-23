
def ajouter_membre(connexion, nom, prenom, telephone):

    curseur = connexion.cursor()

    requete = """
    INSERT INTO membres (nom, prenom, telephone)
    VALUES (?, ?, ?)
    """

    curseur.execute(requete, (nom, prenom, telephone))

    connexion.commit()

    print("Membre enregistré avec succès !")

def afficher_membres(connexion):

    curseur = connexion.cursor()

    requete = "SELECT * FROM membres"

    curseur.execute(requete)

    membres = curseur.fetchall()

    if not membres:
        print("Aucun membre enregistré.")
        return

    print("\n===== LISTE DES MEMBRES =====")

    for membre in membres:
        print("----------------------------")
        print("ID :", membre[0])
        print("Nom :", membre[1])
        print("Prénom :", membre[2])
        print("Téléphone :", membre[3])

def rechercher_membre(connexion, nom):

    curseur = connexion.cursor()

    requete = """
    SELECT * FROM membres
    WHERE nom LIKE ?
    """

    curseur.execute(requete, ("%" + nom + "%",))

    membres = curseur.fetchall()

    if not membres:
        print("Aucun membre trouvé.")
        return

    print("\n===== RÉSULTATS DE LA RECHERCHE =====")

    for membre in membres:
        print("----------------------------")
        print("ID :", membre[0])
        print("Nom :", membre[1])
        print("Prénom :", membre[2])
        print("Téléphone :", membre[3])

def modifier_membre(connexion, membre_id, nouveau_nom, nouveau_prenom, nouveau_telephone):

    curseur = connexion.cursor()

    requete = """
    UPDATE membres
    SET nom = ?,
        prenom = ?,
        telephone = ?
    WHERE id = ?
    """

    curseur.execute(
        requete,
        (nouveau_nom, nouveau_prenom, nouveau_telephone, membre_id)
    )

    connexion.commit()

    if curseur.rowcount == 0:
        print("Aucun membre trouvé avec cet ID.")
    else:
        print("Membre modifié avec succès !")

def supprimer_membre(connexion, membre_id):

    curseur = connexion.cursor()

    requete = """
    DELETE FROM membres
    WHERE id = ?
    """

    curseur.execute(requete, (membre_id,))

    connexion.commit()

    if curseur.rowcount == 0:
        print("Aucun membre trouvé avec cet ID.")
    else:
        print("Membre supprimé avec succès !")
