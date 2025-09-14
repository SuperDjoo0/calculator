
def recupererLeSensDeLaConversion():
    breakwhile = 1
    sensDeConversion = None
    while(breakwhile == 1):
        sensDeConversion = input('Sens de converion(pouce en cm, cm en pouce) -->  ')
        

        if sensDeConversion == 'pouce en cm' or sensDeConversion == 'cm en pouce':
            breakwhile = 0
        else:
            print("ERREUR-le sens de la conversion n'as pas été reconnue-")
    return sensDeConversion

def recupererLaValeur():
    true = True
    while(true):
        valeurUtilsateur = input('Valeur à convertir -->  ')
        try:
            breakWhile = float(valeurUtilsateur)
        except:
            print('ERREUR-La valeur doit êtres écrit en nombre-')
        else:
            true = False
    return valeurUtilsateur

def afficherResultat(conversion, valeur):
    if conversion == 'pouce en cm':
        resultat = float(valeur) * 2.54
        print('%s pouces vaut %s cm.' %(valeur, resultat))

    elif conversion == 'cm en pouce':
        resultat = float(valeur) * 0.394
        print('%s cm vaut %s pouces.' %(valeur, resultat))
    

conversion = recupererLeSensDeLaConversion()
valeur = recupererLaValeur()
afficherResultat(conversion, valeur)