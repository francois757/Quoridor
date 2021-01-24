"""Module principal"""
import argparse
import api
import time
import quoridorx


def analyser_commande():
    """Fonction qui va analyser les commandes entrées dans le terminal"""
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', action='store_true',
                        help='Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('-a', action='store_true',
                        help='Jouer en mode automatique.')
    parser.add_argument('-x', action='store_true',
                        help='Jouer en mode manuel avec affichage graphique.')
    parser.add_argument('-ax', action='store_true',
                        help='Jouer en mode automatique avec affichage graphique.')
    return parser.parse_args()


if __name__ == "__main__":
    DIC = (vars(analyser_commande()))
    IDUL = DIC['idul']

    if DIC['lister']:
        print(api.lister_parties(IDUL))
    elif DIC['a']:
        PARTIE = api.débuter_partie(IDUL)
        JEU = PARTIE[1]
        JEUQUORIDOR = quoridorx.quoridor.Quoridor(JEU['joueurs'], JEU['murs'])
        print(JEUQUORIDOR)
        COUP = JEUQUORIDOR.jouer_coup(1)
        while 1:
            TYPE_COUP = COUP[0]
            POS = COUP[1]
            NETAT = api.jouer_coup(PARTIE[0], TYPE_COUP, POS)
            JEU = NETAT
            JEUQUORIDOR = quoridorx.quoridor.Quoridor(JEU['joueurs'], JEU['murs'])
            print(JEUQUORIDOR)
            COUP = JEUQUORIDOR.jouer_coup(1)
    elif DIC['x']:
        PARTIE = api.débuter_partie(IDUL)
        JEU = PARTIE[1]
        JEUQUORIDOR = quoridorx.Quoridorx(JEU['joueurs'], JEU['murs'])
        JEUQUORIDOR.afficher()
        while 1:
            try:
                TYPE_COUP = input('Type coup')
                POS = (int(input('position en x')), int(input('position en y')))
                NETAT = api.jouer_coup(PARTIE[0], TYPE_COUP, POS)
                if 'joueurs' in NETAT:
                    if TYPE_COUP == 'MH':
                        JEUQUORIDOR.placer_mur(1, POS, 'horizontaux')
                    elif TYPE_COUP == 'MV':
                        JEUQUORIDOR.placer_mur(1, POS, 'verticaux')
                    elif TYPE_COUP == 'D':
                        JEUQUORIDOR.déplacer_jeton(1, POS)
                    ÉTAT = JEUQUORIDOR.état_partie()
                    if len(ÉTAT['murs']['horizontaux']) != len(NETAT['murs']['horizontaux']):
                        JEUQUORIDOR.placer_mur(2, NETAT['murs']['horizontaux'][-1], 'horizontaux')
                    elif len(ÉTAT['murs']['verticaux']) != len(NETAT['murs']['verticaux']):
                        JEUQUORIDOR.placer_mur(2, NETAT['murs']['verticaux'][-1], 'verticaux')
                    elif ÉTAT['joueurs'][1]['pos'] != NETAT['joueurs'][1]['pos']:
                        JEUQUORIDOR.déplacer_jeton(2, tuple(NETAT['joueurs'][1]['pos']))
                    JEUQUORIDOR.afficher()
                else:
                    print(NETAT)
            except StopIteration:
                if not JEUQUORIDOR.partie_terminée():
                    print(JEU['joueurs'][1]['nom'])
                else:
                    print(JEUQUORIDOR.partie_terminée())
                time.sleep(10)
                break
    elif DIC['ax']:
        PARTIE = api.débuter_partie(IDUL)
        JEU = PARTIE[1]
        JEUQUORIDOR = quoridorx.Quoridorx(JEU['joueurs'], JEU['murs'])
        JEUQUORIDOR.afficher()
        COUP = JEUQUORIDOR.jouer_coup(1)
        while 1:
            try:
                TYPE_COUP = COUP[0]
                POS = COUP[1]
                NETAT = api.jouer_coup(PARTIE[0], TYPE_COUP, POS)
                ÉTAT = JEUQUORIDOR.état_partie()
                if len(ÉTAT['murs']['horizontaux']) != len(NETAT['murs']['horizontaux']):
                    JEUQUORIDOR.placer_mur(2, NETAT['murs']['horizontaux'][-1], 'horizontaux')
                elif len(ÉTAT['murs']['verticaux']) != len(NETAT['murs']['verticaux']):
                    JEUQUORIDOR.placer_mur(2, NETAT['murs']['verticaux'][-1], 'verticaux')
                elif ÉTAT['joueurs'][1]['pos'] != NETAT['joueurs'][1]['pos']:
                    JEUQUORIDOR.déplacer_jeton(2, tuple(NETAT['joueurs'][1]['pos']))
                JEUQUORIDOR.afficher()
                COUP = JEUQUORIDOR.jouer_coup(1)
            except StopIteration:
                if not JEUQUORIDOR.partie_terminée():
                    print(JEU['joueurs'][1]['nom'])
                else:
                    print(JEUQUORIDOR.partie_terminée())
                time.sleep(5)
                break
    else:
        PARTIE = api.débuter_partie(IDUL)
        JEU = PARTIE[1]
        JEUQUORIDOR = quoridorx.quoridor.Quoridor(JEU['joueurs'], JEU['murs'])
        print(JEUQUORIDOR)
        while 1:
            TYPE_COUP = input('Type coup')
            POS = input('Position')
            NETAT = api.jouer_coup(PARTIE[0], TYPE_COUP, POS)
            if 'joueurs' in NETAT:
                JEU = NETAT
                JEUQUORIDOR = quoridorx.quoridor.Quoridor(JEU['joueurs'], JEU['murs'])
                print(JEUQUORIDOR)
            else:
                print(NETAT)
