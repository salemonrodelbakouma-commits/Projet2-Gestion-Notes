# PROJET 2 : Gestion des Notes des Etudiants

etudiants = []

def ajouter_etudiant():
    nom = input("Nom de l'etudiant : ")
    note1 = float(input("Note 1 : "))
    note2 = float(input("Note 2 : "))
    note3 = float(input("Note 3 : "))
    moyenne = (note1 + note2 + note3) / 3
    
    if moyenne >= 16:
        mention = "Excellent"
    elif moyenne >= 14:
        mention = "Tres Bien"
    elif moyenne >= 12:
        mention = "Bien"
    elif moyenne >= 10:
        mention = "Passable"
    else:
        mention = "Echec"
    
    etudiant = {"nom": nom, "moyenne": moyenne, "mention": mention}
    etudiants.append(etudiant)
    print(f"{nom} ajoute avec moyenne {moyenne:.2f} - {mention}")

def afficher_etudiants():
    if len(etudiants) == 0:
        print("Aucun etudiant enregistre.")
    else:
        print("\n--- LISTE DES ETUDIANTS ---")
        for e in etudiants:
            print(f"{e['nom']} | Moyenne : {e['moyenne']:.2f} | Mention : {e['mention']}")

def chercher_etudiant():
    nom = input("Nom a chercher : ")
    for e in etudiants:
        if e['nom'].lower() == nom.lower():
            print(f"Trouve : {e['nom']} | Moyenne : {e['moyenne']:.2f} | {e['mention']}")
            return
    print("Etudiant non trouve.")

def meilleur_etudiant():
    if len(etudiants) == 0:
        print("Aucun etudiant.")
    else:
        meilleur = etudiants[0]
        for e in etudiants:
            if e['moyenne'] > meilleur['moyenne']:
                meilleur = e
        print(f"Meilleur : {meilleur['nom']} avec {meilleur['moyenne']:.2f}")

while True:
    print("\n===== MENU =====")
    print("1. Ajouter un etudiant")
    print("2. Afficher tous les etudiants")
    print("3. Chercher un etudiant")
    print("4. Meilleur etudiant")
    print("5. Quitter")
    
    choix = input("Ton choix : ")
    
    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        afficher_etudiants()
    elif choix == "3":
        chercher_etudiant()
    elif choix == "4":
        meilleur_etudiant()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, reessaie.")
