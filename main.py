apprenants = []
def afficher_menu():
    print("\n--- MENU POINTAGE ---")
    print("1. Ajouter un apprenant")
    print("2. Enregistrer la présence")
    print("3. Afficher les apprenants présents")
    print("4. Calculer le taux de présence")
    print("5. Quitter")

def ajouter_apprenant():
    identifiant = input("Identifiant : ")

    for a in apprenants:
        if a["id"] == identifiant:
            print("Identifiant déjà utilisé.")
            return

    nom = input("Nom : ")
    prenom = input("Prénom : ")
    promo = input("Promo : ")

    apprenant = {
        "id": identifiant,
        "nom": nom,
        "prenom": prenom,
        "promo": promo,
        "presence": None
    }
    apprenants.append(apprenant)
    print("Apprenant ajouté")

def enregistrer_presence():
    if len(apprenants) == 0:
        print("Aucun apprenant.")
        return

    for a in apprenants:
        if a["presence"] is not None:
            continue

        while a["presence"] is None:
            choix = input(f"{a['prenom']} {a['nom']} (p = présent / a = absent) : ").lower()
            if choix == "p":
                a["presence"] = "présent"
            elif choix == "a":
                a["presence"] = "absent"
            else:
                print("Erreur : saisir p ou a.")

def afficher_presents():
    print("\nApprenants présents :")
    for a in apprenants:
        if a["presence"] == "présent":
            print(f"- {a['prenom']} {a['nom']}")

def calculer_taux_presence():
    presents = 0
    for a in apprenants:
        if a["presence"] == "présent":
            presents += 1

    if len(apprenants) > 0:
        taux = (presents / len(apprenants)) * 100
        print("Taux de présence :", taux, "%")
    else:
        print("Aucun apprenant.")

def main():

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            ajouter_apprenant()
        elif choix == "2":
            enregistrer_presence()
        elif choix == "3":
            afficher_presents()
        elif choix == "4":
            calculer_taux_presence()
        elif choix == "5":
            print("Fin du programme")
            break
        else:
            print("Choix invalide")
main()
