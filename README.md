# Exercice_Simplon
Créer une calculatrice faisant l'addition et la soustraction de deux nombres

02-02-2023  
- 15h - Début de l'exercice
- 20h - Première version opérationnelle avec entrée clavier

03-03-2023
- 9h - tkinter étant graphiquement dépassé, l'interface graphique sera refait sous PyQt5

# Comment j'ai programmé cette calculatrice
- J'ai appris à utiliser l'outil GitHub
- J'ai choisi de programmer la calculatrice en python. Ne sachant pas coder en objet j'ai cherché comment on code en objet sous python.
- Pour interragir avec l'utilisateur j'ai choisi d'utiliser tkinter.
- Le traitement du texte saisi dans la fenêtre tkinter et le calcul associé pouvant tenir dans une fonction, je n'ai pas vu d'intéret à créer ce programme avec des class.

# Fonctionnement du programme
- L'utilisateur saisi son calcul dans un champ dédié
- La string saisie est analysée afin de vérifier qu'elle ne contient que des chiffres, virgules, points, signe "+" ou signe "-". Dans le cas contraire, un message d'erreur est envoyé et le champ vidé.
- On vérifie si deux caractères spéciaux identiques se suivent (++; ..) ou que la string commence ou se termine par un caractère spécial. Si c'est le cas on envoie un message d'erreur et on efface le contenu du champ.
- On sépare ensuite les chiffres des signes et on les stocke séparément
- Enfin on calcule en utilisant les chiffres et signes stockés puis on met à jour le champ de saisie en y mettant le résultat trouvé.
