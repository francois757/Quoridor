"""Module qui créer la classe Quoridorx qui sert à jouer en mode graphique"""

import quoridor


import turtle


class Quoridorx(quoridor.Quoridor):
    """Classe qui sert à jouer en mode graphique"""
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs)
        print(self.jeu['joueurs'][0])
        wn = turtle.Screen()
        wn.title("Quoridorx")
        wn.setup(width=500, height=500)
        wn.bgcolor("white")
        self.joueur1 = turtle.Turtle()
        self.joueur1.penup()
        self.joueur2 = turtle.Turtle()
        self.joueur2.penup()
        self.dessin = turtle.Turtle()
        self.dessin.speed(100)
        self.dessin.hideturtle()
        Quoridorx.dessin(self, (-225, -225), (-225, 225))
        Quoridorx.dessin(self, (-225, 225), (225, 225))
        Quoridorx.dessin(self, (225, 225), (225, -225))
        Quoridorx.dessin(self, (225, -225), (-225, -225))
        for x in range(1, 9):
            Quoridorx.dessin(self, (-225, 225 - x*50), (225, 225 - x*50))
        for x in range(1, 9):
            Quoridorx.dessin(self, (225 - x*50, -225), (225 - x*50, 225))
        Quoridorx.afficher(self)
        Quoridorx.afficher(self)

    def afficher(self):
        # placement joueurs
        self.joueur1.goto(Quoridorx.scalingj(self.jeu['joueurs'][0]["pos"]))
        self.joueur2.goto(Quoridorx.scalingj(self.jeu['joueurs'][1]["pos"]))
        # mur vertical
        self.dessin.pencolor("red")
        self.dessin.pensize(5)
        self.dessin.seth(90)
        for x in self.jeu["murs"]["verticaux"]:
            self.dessin.penup()
            self.dessin.goto(Quoridorx.scalingm(x))
            self.dessin.pendown()
            self.dessin.forward(100)
        # mur horizontal
        self.dessin.seth(0)
        for x in self.jeu["murs"]["horizontaux"]:
            self.dessin.penup()
            self.dessin.goto(Quoridorx.scalingm(x))
            self.dessin.pendown()
            self.dessin.forward(100)
        

    def dessin(self, depart, arrive):
        self.dessin.penup()
        self.dessin.goto(depart)
        self.dessin.pendown()
        self.dessin.goto(arrive)
    
    def scalingj(pos):
        a = ()
        for x in pos:
            a += (x * 50 - 250 ,)
        return a
    
    def scalingm(pos):
        a = ()
        for x in pos:
            a += (x * 50 - 275 ,)
        return a
    




TEST1 = Quoridorx([{'nom': 'nom1', 'murs': 10, 'pos': (5, 6)}, {'nom': 'nom2', 'murs': 8, 'pos': (5, 7)}], {'horizontaux': [[4,4]],'verticaux': [[4,4]]})

turtle.mainloop()