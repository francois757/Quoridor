# Quoridor
-	Description du projet 
Ce programme permet de jouer au jeu Quoridor contre un serveur de façon manuelle ou encore de façon automatique. 
Le jeu Quoridor se joue sur un plateau de 81 cases et les joueurs commencent par placer leur pion du côté du plateau face à eux. 
Le but est d’atteindre l’autre côté du plateau en premier. 
Pour ce faire, dans son tour un joueur peut bouger son pion d’une case (on ne peut bouger en diagonal) ou encore placer un mur pour bloquer son adversaire.


-	Comment l’utiliser 
Il faut commencer par installer les modules networkx et requests. 
Par la suite, il faut faire une des commandes suivantes dans un terminal : 
1.	python main.py --help pour avoir de l'aide.
2.	python main.py idul pour jouer en mode manuel contre le serveur avec le nom idul.
3.	python main.py -a idul pour jouer en mode automatique contre le serveur avec le nom idul.
4.	python main.py -x idul pour jouer en mode manuel contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.
5.	python main.py -ax idul pour jouer en mode automatique contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.
Malheureusement, le serveur qui était utilisé pour jouer n’existe plus, donc on ne peut plus utiliser ce programme.
