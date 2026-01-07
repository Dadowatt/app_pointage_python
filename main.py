apprenants = []
def afficher_menu():
    print("\n--- MENU POINTAGE ---")
    print("1. Ajouter un apprenant")
    print("2. Enregistrer la présence")
    print("3. Afficher les apprenants présents")
    print("4. Calculer le taux de présence")
    print("5. Quitter")

def ajouter_apprenant():
    while True:
        try:
            identifiant = int(input("Identifiant : "))
            if identifiant < 1:
                print("L'identifiant doit être supérieur ou égale à 1")
                continue
            for a in apprenants:
                if a["id"] == identifiant:
                    print("Identifiant déjà utilisé.")
                    break
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue

    while True:    
        nom = input("Nom : ")
        if nom.isalpha():
            break
        print('Nom invalide')
    while True:
        prenom = input("Prénom : ")
        if prenom.replace(" ", "").isalpha():
            break
        print('Prénom invalide')

    while True:
        promo = input("Promo : ").upper().strip()
        if len(promo) == 2 and promo[0] == 'P' and promo[1].isdigit():
            break
        print('promo invalide')

    apprenant = {
        "id": identifiant,
        "nom": nom,
        "prenom": prenom,
        "promo": promo,
        "presence": None
    }
    apprenants.append(apprenant)
    print("Apprenant ajouté avec succès!")

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
    found = False
    print("\n==== Apprenants présents ==== :")
    for a in apprenants:
        if a["presence"] == "présent":
            print(f"- {a['prenom']} {a['nom']}")
            found = True
    if not found:
        print("\nAucun apprenant présent")

def calculer_taux_presence():
    presents = 0
    for a in apprenants:
        if a["presence"] == "présent":
            presents += 1

    if len(apprenants) > 0:
        taux = int((presents / len(apprenants)) * 100)
        print(f"Taux de présence : {taux} %")
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
