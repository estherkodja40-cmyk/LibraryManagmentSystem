
def ajouter_livre(connexion, titre, auteur, categorie, quantite):

    curseur = connexion.cursor()

    requete = """
    INSERT INTO livres
    (titre, auteur, categorie, quantite_totale, quantite_disponible)
    VALUES (?, ?, ?, ?, ?)
    """

    curseur.execute(
        requete,
        (titre, auteur, categorie, quantite, quantite)
    )

    connexion.commit()

    print("Livre ajouté avec succès !")


def afficher_livres(connexion):

    curseur = connexion.cursor()

    requete = "SELECT * FROM livres"

    curseur.execute(requete)

    livres = curseur.fetchall()

    if not livres:
        print("Aucun livre enregistré.")
        return

    print("\n===== LISTE DES LIVRES =====")

    for livre in livres:
        print("----------------------------")
        print("ID :", livre[0])
        print("Titre :", livre[1])
        print("Auteur :", livre[2])
        print("Catégorie :", livre[3])
        print("Quantité totale :", livre[4])
        print("Quantité disponible :", livre[5])


def rechercher_livre(connexion, titre):

    curseur = connexion.cursor()

    requete = """
    SELECT * FROM livres
    WHERE titre LIKE ?
    """

    curseur.execute(requete, ("%" + titre + "%",))

    livres = curseur.fetchall()

    if not livres:
        print("Aucun livre trouvé.")
        return

    print("\n===== RÉSULTATS DE LA RECHERCHE =====")

    for livre in livres:
        print("----------------------------")
        print("ID :", livre[0])
        print("Titre :", livre[1])
        print("Auteur :", livre[2])
        print("Catégorie :", livre[3])
        print("Quantité totale :", livre[4])
        print("Quantité disponible :", livre[5])
def modifier_livre(connexion, livre_id, nouveau_titre, nouvel_auteur, nouvelle_categorie, nouvelle_quantite):

    curseur = connexion.cursor()

    requete = """
    UPDATE livres
    SET titre = ?,
        auteur = ?,
        categorie = ?,
        quantite_totale = ?,
        quantite_disponible = ?
    WHERE id = ?
    """

    curseur.execute(
        requete,
        (nouveau_titre, nouvel_auteur, nouvelle_categorie,
         nouvelle_quantite, nouvelle_quantite, livre_id)
    )

    connexion.commit()

    if curseur.rowcount == 0:
        print("Aucun livre trouvé avec cet ID.")
    else:
        print("Livre modifié avec succès !")

def supprimer_livre(connexion, livre_id):

    curseur = connexion.cursor()

    requete = """
    DELETE FROM livres
    WHERE id = ?
    """

    curseur.execute(requete, (livre_id,))

    connexion.commit()

    if curseur.rowcount == 0:
        print("Aucun livre trouvé avec cet ID.")
    else:
        print("Livre supprimé avec succès !")
