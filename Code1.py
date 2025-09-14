def demandAge():
    ageUtilisateurPlusTard = 0
    while ageUtilisateurPlusTard == 0:
        ageUtilisateur = input('Age -->  ')
        try:
            ageUtilisateurPlusTard = int(ageUtilisateur)
        except:
            print("ERREUR, veuillez rentrer un age inscrit en nombre")
    
    return ageUtilisateurPlusTard

def demandPrenom():
    prenomUtilisateur = input("Prénom -->  ")
    while prenomUtilisateur == (""):
        print("ERREUR, veuillez renter un prenom.")
        prenomUtilisateur = input('Prénom -->  ')
    return prenomUtilisateur

def afficherResultat(prenom, age):
    print('Bonjour, ' + prenom + ' vous avez, ' + str(age) + ' ans.')
    print("L'an prochain, vous aurez "+ str(age + 1) + ' ans')
    
    if age == 17:
        print("vous êtes presque majeur.")
    
    elif  12 <= age >= 16:
        print("Vous êtes adolecent.")

    elif age == 1 or age == 2:
        print("Vous êtes un bébé.")
    
    elif age == 18:
        print("Tout juste majeur, Félicitation!")

    elif age >= 60:
        print("Vous êtes seniors.")

    elif age >= 18:
        print("Vous êtes majeur.")


    elif age < 10:
        print("Vous êtes un enfant")

    else:
        print("vous êtes mineur.")


prenom = demandPrenom()
age = demandAge()
afficherResultat(prenom, age)   