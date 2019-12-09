"""Module qui créer la classe Quoridorx qui sert à jouer en mode graphique"""

import quoridor


import turtle


class Quoridorx(quoridor.Quoridor):
    """Classe qui sert à jouer en mode graphique"""
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs)
        wn = turtle.Screen()
        wn.title(f"Quoridorx - Rouge: {self.nom[0]}   Noir: {self.nom[1]}")
        wn.setup(width=500, height=500)
        self.joueur1 = turtle.Turtle()
        self.joueur1.shape("circle")
        self.joueur1.color("")
        self.joueur1.penup()
        self.joueur2 = turtle.Turtle()
        self.joueur2.shape("circle")
        self.joueur2.color("yellow")
        self.joueur2.penup()
        self.dessins = turtle.Turtle()
        self.dessins.speed(100)
        self.dessins.hideturtle()
        Quoridorx.dessin(self, (-225, -225), (-225, 225))
        Quoridorx.dessin(self, (-225, 225), (225, 225))
        Quoridorx.dessin(self, (225, 225), (225, -225))
        Quoridorx.dessin(self, (225, -225), (-225, -225))
        for x in range(1, 9):
            Quoridorx.dessin(self, (-225, 225 - x*50), (225, 225 - x*50))
        for x in range(1, 9):
            Quoridorx.dessin(self, (225 - x*50, -225), (225 - x*50, 225))
    def afficher(self):
        # placement joueurs
        self.joueur1.goto(Quoridorx.scalingj(self, self.jeu['joueurs'][0]["pos"]))
        self.joueur2.goto(Quoridorx.scalingj(self, self.jeu['joueurs'][1]["pos"]))
        # mur vertical
        self.dessin.pensize(6)
        self.dessin.seth(90)
        for x in self.jeu["murs"]["verticaux"]:
            self.dessins.penup()
            self.dessins.goto(Quoridorx.scalingm(self, x))
            self.dessins.pendown()
            self.dessins.forward(100)
        # mur horizontal
        self.dessins.seth(0)
        for x in self.jeu["murs"]["horizontaux"]:
            self.dessins.penup()
            self.dessins.goto(Quoridorx.scalingm(self, x))
            self.dessins.pendown()
            self.dessins.forward(100)
    def dessin(self, depart, arrive):
        self.dessins.penup()
        self.dessins.goto(depart)
        self.dessins.pendown()
        self.dessins.goto(arrive)    
    def scalingj(self, pos):
        a = ()
        for x in pos:
            a += (x * 50 - 250 ,)
        return a   
    def scalingm(self, pos):
        a = ()
        for x in pos:
            a += (x * 50 - 275 ,)
        return a
