import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QGridLayout, QLineEdit, QStyleFactory, QMessageBox
#from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPalette

## Création d'une classe créant l'interface graphique
class Calculatrice(QDialog):
    # Initialisation de la classe: on indique que l'onveut deux zones dans la fenêtre. # Repere
    def __init__(self, parent = None):
        super(Calculatrice, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTextGroupBox()
        self.createButtonsGroupBox()

        main_layout = QGridLayout()
        main_layout.addWidget(self.createTextGroupBox, 0, 0)
        main_layout.addWidget(self.createButtonsGroupBox, 1, 0)

        self.setWindowTitle("Calculatrice")
        self.changeStyle('Windows')

        self.setLayout(main_layout)

        self.user_entry = ""

    # Change le style de la fenêtre
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(self.originalPalette)

        
    # Création de la zone où le texte sera saisi au clavier par l'utilisateur
    def createTextGroupBox(self):
        self.createTextGroupBox = QGroupBox()

        self.calcul_entry = QLineEdit("")

        calcul_layout = QGridLayout()
        calcul_layout.addWidget(self.calcul_entry, 0, 0)

        self.createTextGroupBox.setLayout(calcul_layout)

    # Création du clavier numérique en boutons
    def createButtonsGroupBox(self):
        self.createButtonsGroupBox = QGroupBox()

        button_0 = QPushButton("0")
        button_0.setDefault(True)
        button_0.clicked.connect(self.button0_clicked)
        button_1 = QPushButton("1")
        button_1.setDefault(True)
        button_1.clicked.connect(self.button1_clicked)
        button_2 = QPushButton("2")
        button_2.setDefault(True)
        button_2.clicked.connect(self.button2_clicked)
        button_3 = QPushButton("3")
        button_3.setDefault(True)
        button_3.clicked.connect(self.button3_clicked)
        button_4 = QPushButton("4")
        button_4.setDefault(True)
        button_4.clicked.connect(self.button4_clicked)
        button_5 = QPushButton("5")
        button_5.setDefault(True)
        button_5.clicked.connect(self.button5_clicked)
        button_6 = QPushButton("6")
        button_6.setDefault(True)
        button_6.clicked.connect(self.button6_clicked)
        button_7 = QPushButton("7")
        button_7.setDefault(True)
        button_7.clicked.connect(self.button7_clicked)
        button_8 = QPushButton("8")
        button_8.setDefault(True)
        button_8.clicked.connect(self.button8_clicked)
        button_9 = QPushButton("9")
        button_9.setDefault(True)
        button_9.clicked.connect(self.button9_clicked)
        button_add = QPushButton("+")
        button_add.setDefault(True)
        button_add.clicked.connect(self.buttonadd_clicked)
        button_minus = QPushButton("-")
        button_minus.setDefault(True)
        button_minus.clicked.connect(self.buttonminus_clicked)
        button_equal = QPushButton("=")
        button_equal.setDefault(True)
        button_equal.clicked.connect(self.buttonequal_clicked)
        button_dot = QPushButton(".")
        button_dot.setDefault(True)
        button_dot.clicked.connect(self.buttondot_clicked)
        button_correct = QPushButton("C")
        button_correct.setDefault(True)
        button_correct.clicked.connect(self.buttoncorrect_clicked)

        button_layout = QGridLayout()
        button_layout.addWidget(button_7, 0, 0)
        button_layout.addWidget(button_8, 0, 1)
        button_layout.addWidget(button_9, 0, 2)
        button_layout.addWidget(button_correct, 0, 3)
        button_layout.addWidget(button_4, 1, 0)
        button_layout.addWidget(button_5, 1, 1)
        button_layout.addWidget(button_6, 1, 2)
        button_layout.addWidget(button_add, 1, 3)
        button_layout.addWidget(button_1, 2, 0)
        button_layout.addWidget(button_2, 2, 1)
        button_layout.addWidget(button_3, 2, 2)
        button_layout.addWidget(button_minus, 2, 3)
        button_layout.addWidget(button_0, 3, 1)
        button_layout.addWidget(button_dot, 3, 0)
        button_layout.addWidget(button_equal, 3, 2)

        self.createButtonsGroupBox.setLayout(button_layout)

    # Initialise les actions que les boutons doivent réaliser quand on clique dessus    
    def button0_clicked(self):
        self.user_entry = self.user_entry + "0"
        self.calcul_entry.setText(self.user_entry)

    def button1_clicked(self):
        self.user_entry = self.user_entry + "1"
        self.calcul_entry.setText(self.user_entry)

    def button2_clicked(self):
        self.user_entry = self.user_entry + "2"
        self.calcul_entry.setText(self.user_entry)

    def button3_clicked(self):
        self.user_entry = self.user_entry + "3"
        self.calcul_entry.setText(self.user_entry)

    def button4_clicked(self):
        self.user_entry = self.user_entry + "4"
        self.calcul_entry.setText(self.user_entry)

    def button5_clicked(self):
        self.user_entry = self.user_entry + "5"
        self.calcul_entry.setText(self.user_entry)

    def button6_clicked(self):
        self.user_entry = self.user_entry + "6"
        self.calcul_entry.setText(self.user_entry)

    def button7_clicked(self):
        self.user_entry = self.user_entry + "7"
        self.calcul_entry.setText(self.user_entry)

    def button8_clicked(self):
        self.user_entry = self.user_entry + "8"
        self.calcul_entry.setText(self.user_entry)

    def button9_clicked(self):
        self.user_entry = self.user_entry + "9"
        self.calcul_entry.setText(self.user_entry)

    def buttonadd_clicked(self):
        if self.user_entry == "":
            self.user_entry = "0" + "+"

        if self.user_entry[len(self.user_entry)-1] == "+" or self.user_entry[len(self.user_entry)-1] == "-" or self.user_entry[len(self.user_entry)-1] == "," or self.user_entry[len(self.user_entry)-1] == ".":
            pass

        if self.user_entry[len(self.user_entry)-1] in ["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]:
            self.user_entry = self.user_entry + "+"

        self.calcul_entry.setText(self.user_entry)

    def buttonminus_clicked(self):
        did_signe_changed = False

        if self.user_entry == "":
            self.user_entry = "0" + "-"
            did_signe_changed = True

        if  self.user_entry[len(self.user_entry)-1] == "-" and did_signe_changed == False:
            self.user_entry = self.user_entry[:-1]
            self.user_entry = self.user_entry + "+"
            did_signe_changed = True

        if self.user_entry[len(self.user_entry)-1] == "+" and did_signe_changed == False:
            self.user_entry = self.user_entry[:-1]
            self.user_entry = self.user_entry + "-"
            did_signe_changed = True
        
        if self.user_entry[len(self.user_entry)-1] == "," or self.user_entry[len(self.user_entry)-1] == ".":
            pass

        if self.user_entry[len(self.user_entry)-1] in ["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]:
            self.user_entry = self.user_entry + "-"

        self.calcul_entry.setText(self.user_entry)

    def buttondot_clicked(self):
        if self.user_entry[len(self.user_entry)-1] == "," or self.user_entry[len(self.user_entry)-1] == "." or self.user_entry[len(self.user_entry)-1] == "+" or self.user_entry[len(self.user_entry)-1] == "-":
            pass
        else:
            self.user_entry = self.user_entry + "."

        self.calcul_entry.setText(self.user_entry)

    def buttonequal_clicked(self):
        self.user_entry = self.calcul_entry.text()
        if self.user_entry[len(self.user_entry)-1] == "," or self.user_entry[len(self.user_entry)-1] == "." or self.user_entry[len(self.user_entry)-1] == "+" or self.user_entry[len(self.user_entry)-1] == "+":
            self.user_entry = self.user_entry + "0"
            self.calcul_entry.setText(self.user_entry)
        self.calculate()

    def buttoncorrect_clicked(self):
        self.user_entry = ""
        self.calcul_entry.setText(self.user_entry)

    ## Traite la string entry et calcule #Repere
    def calculate(self):
        pass
        entry = self.calcul_entry.text()
        authorised_caracters = ["0", "1", "2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9", ",", ".", "+", "-"]
        signes = []
        syntax_error = False

        # Vérifie que calcul ne contient que des chiffres, ou les caractères suivants: ",", ".", "+", "-"
        for i in range(len(entry)):

            if entry[i] not in authorised_caracters:
                QMessageBox.about(self, "Attention !", "Le champ de saisie ne doit contenir que des chiffres, points, virgules ou les signes + ou - ")
                self.calcul_entry.setText("")
                return
            else:
                # Sauvegarde les signes du calcul
                if entry[i] == "+" or entry[i] == "-":
                    signes.append(entry[i])

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
        if calcul/int(calcul) == 1:
            calcul = int(calcul)

        # Met à jour le champ avec le résultat
        self.calcul_entry.setText(str(calcul))
        self.user_entry = str(calcul)
       

        
## Crée la fenêtre     
calcul_app = QApplication.instance() 
if not calcul_app:
    calcul_app = QApplication(sys.argv)  

fenetre_calcul = Calculatrice()
fenetre_calcul.show()
calcul_app.exec_()      





''' 

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
'''

















