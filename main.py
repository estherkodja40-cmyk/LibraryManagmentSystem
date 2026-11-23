from database import connecter_db, creer_tables
from services.livre_service import ajouter_livre, afficher_livres, rechercher_livre, modifier_livre, supprimer_livre
from services.membre_service import ajouter_membre, afficher_membres, rechercher_membre, modifier_membre, supprimer_membre
from services.emprunt_service import enregistrer_emprunt, afficher_emprunts, enregistrer_retour,afficher_emprunts_en_retard
connexion = connecter_db()

creer_tables(connexion)

print("===== GESTION DE BIBLIOTHEQUE =====")

while True:
    print("\n===== GESTION DE LA BIBLIOTHÈQUE =====")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Rechercher un livre")
    print("4. Modifier un livre")
    print("5. Supprimer un livre")
    print("6. Enregistrer un membre")
    print("7. Afficher les membres")
    print("8. Rechercher un membre")
    print("9. Modifier un membre")
    print("10. Supprimer un membre")
    print("11. Enregistrer un emprunt")
    print("12. Afficher les emprunts")
    print("13. Enregistrer un retour")
    print("14. Afficher les emprunts en retard")
    print("15. Quitter")

    choix = input("\nVotre choix : ").strip()

    if choix == "1":
        titre = input("Titre du livre : ")
        auteur = input("Auteur : ")
        categorie = input("Catégorie : ")
        quantite = int(input("Quantité : "))
        ajouter_livre(connexion, titre, auteur, categorie, quantite)

    elif choix == "2":
        afficher_livres(connexion)

    elif choix == "3":
        titre = input("Titre à rechercher : ")
        rechercher_livre(connexion, titre)

    elif choix == "4":
        livre_id = int(input("ID du livre à modifier : "))
        nouveau_titre = input("Nouveau titre : ")
        nouvel_auteur = input("Nouvel auteur : ")
        nouvelle_categorie = input("Nouvelle catégorie : ")
        nouvelle_quantite = int(input("Nouvelle quantité : "))
        modifier_livre(
            connexion, livre_id, nouveau_titre,
            nouvel_auteur, nouvelle_categorie, nouvelle_quantite
        )

    elif choix == "5":
        livre_id = int(input("ID du livre à supprimer : "))
        supprimer_livre(connexion, livre_id)

    elif choix == "6":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        telephone = input("Téléphone : ")
        ajouter_membre(connexion, nom, prenom, telephone)

    elif choix == "7":
        afficher_membres(connexion)

    elif choix == "8":
        nom = input("Nom à rechercher : ")
        rechercher_membre(connexion, nom)

    elif choix == "9":
        membre_id = int(input("ID du membre à modifier : "))
        nouveau_nom = input("Nouveau nom : ")
        nouveau_prenom = input("Nouveau prénom : ")
        nouveau_telephone = input("Nouveau téléphone : ")
        modifier_membre(
            connexion, membre_id, nouveau_nom,
            nouveau_prenom, nouveau_telephone
        )

    elif choix == "10":
        membre_id = int(input("ID du membre à supprimer : "))
        supprimer_membre(connexion, membre_id)

    elif choix == "11":
        livre_id = int(input("ID du livre à emprunter : "))
        membre_id = int(input("ID du membre : "))
        enregistrer_emprunt(connexion, livre_id, membre_id)

    elif choix == "12":
        afficher_emprunts(connexion)

    elif choix == "13":
        emprunt_id = int(input("ID de l'emprunt à retourner : "))
        enregistrer_retour(connexion, emprunt_id)

    elif choix == "14":
        print("\nVérification des emprunts en retard...")
        afficher_emprunts_en_retard(connexion)

    elif choix == "15":
        print("Merci d'avoir utilisé notre application !")
        break

    else:
        print("Choix invalide. Réessayez.")

connexion.close()
