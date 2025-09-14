# lesFonctions
def remplirLaList():
    
    # dataBase
    listUtilisateur = []
    tailleListe = '0'
    tailleListeInt = int(tailleListe)
    entreeUtilisateur = None
    
    
    #leCode
    while True:
        tailleListe = input('Combien de nombre -->  ')
        
        try:
            int(tailleListe)
        except:
            print('-ERREUR-vous devez entrer un nombre.')
        else:
            
            if int(tailleListe) <= 20:
                break
            else:
                print('-ERREUR-votre liste ne doit pas contenir plus de 20 nombres.')
    tailleListeInt = int(tailleListe)
    
    for i in range(tailleListeInt):
        
        while True:
            entreeUtilisateur = input('veillez entrer un nombre -->  ')
            
            try:
                int(entreeUtilisateur)
            except:
                print('-ERREUR-vous devez entrer un nombre.')
            else:
                break
            
        listUtilisateur.append(int(entreeUtilisateur))
    
    return listUtilisateur ,tailleListeInt


def compterLesNombresPairesEtFinaliser(un, deux):
    # dataBase
    repetition = 0
    nombrePaire = 0
    dataNombrePaire = [0, 2, 4, 6, 8]
    repetitionDeux = 0
    Nombre = None 
    
    # leCode
    for i in range(deux): 
        Nombre = str(un[repetition])
        
        for i in range(5):
            
            if int(Nombre[-1]) == dataNombrePaire[repetitionDeux]:
                nombrePaire += 1
            repetitionDeux += 1
        repetitionDeux = 0
        repetition += 1

    if nombrePaire <= 0:
        print('Il y a de pas nombre paire.')
    elif nombrePaire == 1:
        print('Il y a un seul nombre paire.')
    else:
        print('il y a %s nombres paires.' %nombrePaire)


#leCode
while True:
    listNombre ,tailleList = remplirLaList()
    compterLesNombresPairesEtFinaliser(listNombre ,tailleList)
    
    while True:
        recommencer = input('Recommencer ? oui/non -->  ')
        
        if recommencer == 'oui':
            break
        elif recommencer == 'non':
            break
        else:
            print('-ERREUR- Vous devez rentrer "oui" ou "non".')
    
    if recommencer == 'non':
        break