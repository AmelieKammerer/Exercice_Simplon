# Exercice_Simplon
Créer une calculatrice faisant l'addition et la soustraction de deux nombres

02-02-2023  
- 15h - Début de l'exercice
- 20h - Première version opérationnelle avec entrée clavier

03-03-2023
- 9h  - tkinter étant graphiquement dépassé, l'interface graphique sera refait sous PyQt5
- 14h - la calculatrice est fonctionnelle aussi bien avec une entrée clavier qu'en utilisant ses boutons. Recherche du potentiels bugs puis création d'un fichier executable
- 15h - bugs fix. L'executable pesant 35Mo, github ne veut pas le récupérer, upload sur google drive.
- 16h - explication de trois principes de la POO
- 18h - Léger bug fix et optimisation

# Comment j'ai programmé cette calculatrice
- J'ai appris à utiliser l'outil GitHub
- J'ai choisi de programmer la calculatrice en python. Ne sachant pas coder en objet j'ai cherché comment fonctionne la POO sous python.
- Pour interragir avec l'utilisateur j'ai choisi d'utiliser PyQt5.
- La calculatrice est gérée dans une class.

# Fonctionnement du programme
- L'utilisateur saisi son calcul dans un champ dédié ou à l'aide des boutons de la calculatrice.
- Le bouton "=" valide la saisie et lance l'analyse de cette dernière. Le bouton "C" permet de réinitialiser le champ la saisie et vide le champ.
- La string saisie est analysée afin de vérifier qu'elle ne contient que des chiffres, virgules, points, signe "+" ou signe "-". Dans le cas contraire, un message d'erreur est envoyé et le champ vidé.
- On vérifie si deux caractères spéciaux identiques se suivent (++; ..) ou que la string commence ou se termine par un caractère spécial. En fonction on ajustera la string pour éviter toute erreur de syntaxe.
- On sépare ensuite les chiffres des signes et on les stocke séparément
- Enfin on calcule en utilisant les chiffres et signes stockés puis on met à jour le champ de saisie en y mettant le résultat trouvé.

# Execution du programme:
- Ouvrir le fichier python dans un IDE et executer le programme.

OU

- Télécharger l'exécutable avec ce lien et le lancer sur votre machine: https://drive.google.com/file/d/1KNN9e_oEQGeU3ugmbdsH2Vk-wlsDRY-S/view?usp=share_link

# Explication de trois principes de la POO (Programation Orientée Objet):
- L'encapsulation: C'est le niveau d'accès donné aux variables et fonctions d'un objet. En public, les variables et fonction peuvent être lues et modifiées librement. En private elles sont accessibles uniquement dans le fichier où elles ont été crées. En protected, elles sont accessibles uniquement par l'objet et ses enfants.
- L'héritage: On peu définir un objet enfant en se basant sur un objet existant. L'héritage est la capacité de l'objet enfant d'accéder aux variables et fonction de son parent.
- Le Polymorphisme: C'est la possibilité pour des objets enfants de posséder des variables et fonctions qui leur sont propres en plus de celles de leur parent.
