'''Module principal'''
import argparse


import api


import quoridorx


def analyser_commande():
    """Fonction qui va analyser les commandes entrées dans le terminal"""
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help= 'IDUL du joueur.')
    parser.add_argument('-l', '--lister', action='store_true',
                        help='Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('-a', action='store_true',
                        help='Jouer en mode automatique contre le serveur.')
    parser.add_argument('-x', action='store_true',
                        help='Jouer en mode manuel contre le serveur avec affichage graphique.')
    parser.add_argument('-ax', action='store_true',
                        help='Jouer en mode automatique contre le serveur avec affichage graphique.')
    return parser.parse_args()



def afficher_damier_ascii(jeu):
    """Fonction qui va affichier le damier de jeu"""
    nom = [jeu['joueurs'][0]['nom'], jeu['joueurs'][1]['nom']]
    table = []
    let = [['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |'],
           ['  |', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '   |']]
    while len(table) < 9:
        table.append([[' ', '.', ' ', ' '], [' ', '.', ' ', ' '],
                      [' ', '.', ' ', ' '], [' ', '.', ' ', ' '],
                      [' ', '.', ' ', ' '], [' ', '.', ' ', ' '],
                      [' ', '.', ' ', ' '], [' ', '.', ' ', ' '], [' ', '.', ' ']])
    nj = 1
    for joueur in jeu['joueurs']:
        table[joueur['pos'][1] - 1][joueur['pos'][0] - 1][1] = str(nj)
        nj += 1
    for mur in jeu['murs']['horizontaux']:
        let[mur[1] - 1][mur[0]] = '----'
        let[mur[1] - 1][mur[0] + 1] = '--- '
        if mur[0] == 8:
            let[mur[1] - 1][mur[0]] = '----'
            let[mur[1] - 1][mur[0] + 1] = '---|'
    for m in jeu['murs']['verticaux']:
        table[m[1] - 1][m[0] - 2][3] = '|'
        table[m[1]][m[0] - 2][3] = '|'
        if let[m[1]][m[0] - 1] == '--- ':
            let[m[1]][m[0] - 1] = '---|'
        else:
            let[m[1]][m[0] - 1] = '   |'
    nl = 9
    for index, line in enumerate(table):
        for index2, variable in enumerate(line):
            table[index][index2] = ''.join(variable)
    damier = f'Légende: 1={nom[0]}, 2={nom[1]}' + '\n' + '   -----------------------------------'
    for li in reversed(table):
        if nl == 1:
            damier += '\n' + f'{nl} |' + ''.join((li)) + '|'
        else:
            damier += '\n' + f'{nl} |' + ''.join((li)) + '|' + '\n' + ''.join(let[nl - 1])
        nl -= 1
    damier += '\n' + '--|-----------------------------------'
    damier += '\n' + '  | 1   2   3   4   5   6   7   8   9'
    print(damier)


if __name__ == "__main__":
    DIC = (vars(analyser_commande()))
    print(DIC)
    k = DIC['idul']
    IDUL = (k[0])
if DIC['lister'] is True:
    print(api.lister_parties(IDUL))
else:
    PARTIE = api.débuter_partie(IDUL)
    JEU = PARTIE[1]
    while 1:
        afficher_damier_ascii(JEU)
        TYPE_COUP = input('Type coup')
        POS = input('position')
        NETAT = api.jouer_coup(PARTIE[0], TYPE_COUP, POS)
        if 'joueurs' in NETAT:
            JEU = NETAT
        else:
            print(NETAT)
