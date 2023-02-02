import tkinter
from tkinter import *
from tkinter import messagebox


## Initialise une fenêtre tkinter pour récupérer des entrées clavier
calcul_window = Tk()
calcul_window.title("Calculatrice")
calcul_window.config(bg = "#202020")

# Récupère la taille d'écran de l'utilisateur
screen_width = calcul_window.winfo_screenwidth()
screen_height = calcul_window.winfo_screenheight()

# Initialise la taille par défaut de la fenêtre
calcul_window_w = int(screen_width/2)
calcul_window_h = int(screen_height/2)
calcul_window.geometry(f'{calcul_window_w}x{calcul_window_h}')

# Crée le champ de saisie pour l'utilisateur
user_entry = StringVar()
calcul_entry = Entry(calcul_window, background = "#3b3b3b",foreground = "#ffffff",insertbackground = "#ffffff", justify = 'center',textvariable = user_entry ,width = 30)
calcul_entry.pack()

# Crée la fonction qui calcule
def calculate():
    entry = user_entry.get()
    authorised_caracters = ["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9", ",", ".", "+", "-"]
    signes = []
    syntax_error = False

    # Vérifie que calcul ne contient que des chiffres, ",", ".", "+", "-"
    for i in range(len(entry)):

        if entry[i] not in authorised_caracters:
            messagebox.showinfo("Attention !", "Le champ de saisie ne doit contenir que des chiffres, points, virgules ou les signes + ou - ")
            user_entry.set("")
            return
        else:

            # On vérifie que le premier ou dernier caractère soit un caractère spécial ou si deux caracères spéciaux se suivent
            if i == 0:
                if authorised_caracters.index(entry[i]) > 9:
                    syntax_error = True
            if i < len(entry):
                if authorised_caracters.index(entry[i]) > 9 and authorised_caracters.index(entry[i+1]) > 9:
                    syntax_error = True
            if i == len(entry):
                if authorised_caracters.index(entry[i]) > 9 :
                    syntax_error = True

            # Sauvegarde les signes du calcul
            if entry[i] == "+" or entry[i] == "-":
                signes.append(entry[i])
    
    # Renvoie une erreur si il y a eu une erreur de syntaxe
    if syntax_error == True:
        messagebox.showinfo("Attention !", "Le champ de saisie ne doit ni commencer ni se terminer par un caractère spécial. Il ne faut pas non plus que deux caractères spéciaux se suivent.")
        user_entry.set("")
        return

    # Modifie entry pour avoir la liste des nombres du calcul
    entry = entry.replace('+', '|')    
    entry = entry.replace('-', '|')          
    entry = entry.replace(',', '.') 
    entry = entry.split("|")

    # Calcul
    calcul = float(entry[0])
    for i in range(len(signes)):
        if signes[i] == "+":
            calcul = calcul + float(entry[i+1])
        if signes[i] == "-":
            calcul = calcul - float(entry[i+1])

    # Met à jour le champ avec le résultat et bouge le curseur à la fin du champ
    user_entry.set(calcul)
    calcul_entry.icursor(len(str(calcul)))
    print(len(str(calcul)))

# Crée le bouton "="
calcul_button = Button(calcul_window, text = "=", command = calculate)
calcul_button.pack()


## Crée la fenêtre

calcul_window.mainloop()

















