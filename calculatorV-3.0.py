# imports
import tkinter
from tkinter import *
import keyboard


# dataBase
calcul = ''
resultat = '0'


# classesEtFonctions
class Bouton:
    
    def __init__(self, x, y, name):
        
        def boutonAction():
            updateCalcul(name)
        boutonUn = Button(tk, text=name, width= 3, height= 2, command= boutonAction, bg= "#6786A0")
        boutonUn.pack()
        boutonUn.place(x= x, y=y)
                   
class Exe:
    
    def __init__(self):
        
        def boutonExe():
           afficherResultat()
        boutonUn = Button(tk, text='Exe', width= 3, height= 2, command= boutonExe, bg= "#676FA0")
        boutonUn.pack()
        boutonUn.place(x= 0, y=345)

class Suppr:
    
    def __init__(self):
        
        def boutonSuppr():
            viderLeCalcul()
        boutonUn = Button(tk, text='Sup.', width= 3, height= 2, command= boutonSuppr, bg= "#8267A0")
        boutonUn.pack()
        boutonUn.place(x= 0, y=225)

class retour:
    
    def __init__(self):

        def boutonRetour():
            supprimerLeCalcul()
        boutonUn = Button(tk, text='ret.', width= 3, height= 2, command= boutonRetour, bg= "#8267A0")
        boutonUn.pack()
        boutonUn.place(x= 0, y=180)

class repetition:

    def __init__(self):

        def boutonRep():
            global calcul
            calcul = calcul + str(resultat)
            zoneText.configure(text= calcul, fg= '#FFFFFF')
        boutonUn = Button(tk, text='rep.', width= 3, height= 2, command= boutonRep, bg= "#6786A0")
        boutonUn.pack()
        boutonUn.place(x= 35, y=0)

def updateCalcul(value):
    global zoneText
    global calcul

    zoneText.configure(fg= "#FFFFFF")
    zoneText.config(text= calcul)
    calcul = calcul + str(value)
    zoneText.config(text= calcul)

def afficherResultat():
        global calcul
        global resultat
        global zoneText
        
        try:
            resultat = eval(calcul)
        except ZeroDivisionError:
            zoneText.configure(fg= "#A70B0B")
            zoneText.configure(text= '-ERREUR-tu_ne_peux_pas_diviser_par_0')
            calcul = ''
        except SyntaxError :
            zoneText.configure(fg= "#A70B0B")
            zoneText.configure(text= '-ERREUR__SYNTAXE-')
            calcul = ''
        else:
            zoneText.configure(text= resultat)
            calcul = ''    

def supprimerLeCalcul():
    global calcul
    calcul = calcul[:-1]          
    zoneText.configure(text = calcul, fg= '#FFFFFF')

def viderLeCalcul():
    global calcul
    calcul = ''
    zoneText.configure(text= calcul)



# keyboard
def onkeyPressed(event):
    global calcul

    if event.name.isdigit():
        updateCalcul(event.name)
    elif event.name == '+':
        updateCalcul(event.name)
    elif event.name == '-':
        updateCalcul(event.name)
    elif event.name == '*':
        updateCalcul(event.name)
    elif event.name == '/':
        updateCalcul(event.name)
    elif event.name == 'decimal':
        updateCalcul('.')
    elif event.name == 'enter':
       afficherResultat()
    elif event.name == 'suppr':
        viderLeCalcul()
    elif event.name == 'backspace':
        supprimerLeCalcul()
keyboard.on_press(onkeyPressed)
     

# creationFenetre
tk = tkinter.Tk()
tk.title('calculator V.3')
tk.configure(bg= "#90CCFD")
tk.geometry('500x500')


# creationText
zoneText = Label(tk, text = calcul, bg= "#030C46", fg= '#FFFFFF', height= 2, width= 45)
zoneText.place(x= 250, y=0)
zoneText.pack()


# creationsBoutons
exe = Exe()
suppr = Suppr()
retour = retour()
repetition = repetition()    
   
zero = Bouton(220, 345, '0')
un = Bouton(185, 300, '1')
deux = Bouton(220, 300, '2')
trois = Bouton(255, 300, '3')
quatre = Bouton(185, 255, '4')
cinq = Bouton(220, 255, '5')
six = Bouton(255, 255, '6')
sept = Bouton(185, 210, '7')
huit = Bouton(220, 210, '8')
neuf = Bouton(255, 210, '9')
point = Bouton(255, 345, '.')

plus = Bouton(0, 0, '+')
moins = Bouton(0, 45, '-')
division = Bouton(0, 90, '/')
fois = Bouton(0, 135, '*')


# boucle
tk.mainloop()