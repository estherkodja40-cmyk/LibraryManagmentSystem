
from datetime import date, timedelta

def enregistrer_emprunt(connexion, livre_id, membre_id):

    curseur = connexion.cursor()

    # Vérifier si le livre existe et s'il est disponible
    curseur.execute(
        "SELECT quantite_disponible FROM livres WHERE id = ?",
        (livre_id,)
    )

    livre = curseur.fetchone()

    if livre is None:
        print("Ce livre n'existe pas.")
        return

    if livre[0] <= 0:
        print("Ce livre n'est pas disponible.")
        return

    # Vérifier si le membre existe
    curseur.execute(
        "SELECT id FROM membres WHERE id = ?",
        (membre_id,)
    )

    membre = curseur.fetchone()

    if membre is None:
        print("Ce membre n'existe pas.")
        return

    # Définir les dates
    date_emprunt = date.today()
    date_retour_prevue = date_emprunt + timedelta(days=14)

    # Enregistrer l'emprunt
    requete = """
    INSERT INTO emprunts
    (livre_id, membre_id, date_emprunt, date_retour_prevue)
    VALUES (?, ?, ?, ?)
    """

    curseur.execute(
        requete,
        (
            livre_id,
            membre_id,
            date_emprunt.isoformat(),
            date_retour_prevue.isoformat()
        )
    )

    # Diminuer la quantité disponible
    curseur.execute(
        """
        UPDATE livres
        SET quantite_disponible = quantite_disponible - 1
        WHERE id = ?
        """,
        (livre_id,)
    )

    connexion.commit()

    print("Emprunt enregistré avec succès !")
    print("Date d'emprunt :", date_emprunt)
    print("Date de retour prévue :", date_retour_prevue)

def afficher_emprunts(connexion):

    curseur = connexion.cursor()

    requete = """
    SELECT
        emprunts.id,
        livres.titre,
        membres.nom,
        membres.prenom,
        emprunts.date_emprunt,
        emprunts.date_retour_prevue,
        emprunts.date_retour_effective

    FROM emprunts

    JOIN livres
    ON emprunts.livre_id = livres.id

    JOIN membres
    ON emprunts.membre_id = membres.id

    ORDER BY emprunts.id
    """

    curseur.execute(requete)

    emprunts = curseur.fetchall()

    if not emprunts:
        print("Aucun emprunt enregistré.")
        return

    print("\n===== LISTE DES EMPRUNTS =====")

    for emprunt in emprunts:

        print("----------------------------")
        print("ID emprunt :", emprunt[0])
        print("Livre :", emprunt[1])
        print("Membre :", emprunt[2], emprunt[3])
        print("Date d'emprunt :", emprunt[4])
        print("Retour prévu :", emprunt[5])

        if emprunt[6] is None:
            print("Statut : En cours")
        else:
            print("Date de retour effective :", emprunt[6])
            print("Statut : Retourné")

def enregistrer_retour(connexion, emprunt_id):

    curseur = connexion.cursor()

    # Vérifier si l'emprunt existe
    curseur.execute(
        """
        SELECT livre_id, date_retour_effective
        FROM emprunts
        WHERE id = ?
        """,
        (emprunt_id,)
    )

    emprunt = curseur.fetchone()

    if emprunt is None:
        print("Cet emprunt n'existe pas.")
        return

    # Vérifier si le livre a déjà été retourné
    if emprunt[1] is not None:
        print("Ce livre a déjà été retourné.")
        return

    livre_id = emprunt[0]

    # Enregistrer la date du retour
    date_retour = date.today()

    curseur.execute(
        """
        UPDATE emprunts
        SET date_retour_effective = ?
        WHERE id = ?
        """,
        (date_retour.isoformat(), emprunt_id)
    )

    # Augmenter la quantité disponible
    curseur.execute(
        """
        UPDATE livres
        SET quantite_disponible = quantite_disponible + 1
        WHERE id = ?
        """,
        (livre_id,)
    )

    connexion.commit()

    print("Retour enregistré avec succès !")
    print("Date du retour :", date_retour)

def afficher_emprunts_en_retard(connexion):

    curseur = connexion.cursor()

    requete = """
    SELECT
        emprunts.id,
        livres.titre,
        membres.nom,
        membres.prenom,
        emprunts.date_retour_prevue

    FROM emprunts

    JOIN livres
    ON emprunts.livre_id = livres.id

    JOIN membres
    ON emprunts.membre_id = membres.id

    WHERE emprunts.date_retour_effective IS NULL
    """

    curseur.execute(requete)
    emprunts = curseur.fetchall()

    aujourd_hui = date.today()
    retards = []

    for emprunt in emprunts:

        date_prevue = date.fromisoformat(emprunt[4])

        if date_prevue < aujourd_hui:
            retards.append((emprunt, date_prevue))

    if not retards:
        print("Aucun emprunt en retard.")
        return

    print("\n===== EMPRUNTS EN RETARD =====")

    for emprunt, date_prevue in retards:

        jours_retard = (aujourd_hui - date_prevue).days

        print("----------------------------")
        print("ID emprunt :", emprunt[0])
        print("Livre :", emprunt[1])
        print("Membre :", emprunt[2], emprunt[3])
        print("Date de retour prévue :", date_prevue)
        print("Nombre de jours de retard :", jours_retard)
