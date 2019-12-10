'''Module api'''
import requests


URL_BASE = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    """Fonction qui va retourner les 20 dernières parties jouées associées à l'idul indiqué"""
    rep = requests.get(URL_BASE+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        dic = rep.json()
    if 'message' in dic:
        raise RuntimeError(dic['message'])
    return dic['parties']

def débuter_partie(idul):
    """Fonction qui va débuter une partie associée à l'idul indiqué"""
    rep = requests.post(URL_BASE+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        dic = rep.json()
    if 'message' in dic:
        raise RuntimeError(dic['message'])
    return (dic['id'], dic['état'])

def jouer_coup(id_partie, type_coup, position):
    """Fonction qui permet de jouer des coups, les types de coups sont D pour déplacer le joueur,
     MH pour placer un mur horizontal et MV pour placer un mur vertical"""
    rep = requests.post(URL_BASE+'jouer/',
                        data={'id': id_partie, 'type': type_coup, 'pos': position})
    if rep.status_code == 200:
        try:
            dic = rep.json()
            if 'message' in dic:
                raise RuntimeError(dic['message'])
            if 'gagnant' in dic:
                raise StopIteration(dic['gagnant'])
            return dic['état']
        except RuntimeError:
            return dic['message']
    return None
