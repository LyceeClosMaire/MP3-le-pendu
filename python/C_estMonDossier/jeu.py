﻿import pickle
import temp
import jeu
import csv
import os
import time


def score (mot, nom, essaie):
    """Fonction des scores """
    now = time.ctime()
    date = time.strftime("%Y, %m, %d, %H", time.strptime(now))

    donneesRecentes = [mot, nom, essaie, date]          # Données que l'on veut rajouter à notre fichier csv

    fichierCSV = open("scores.csv", mode='r', newline='')
    entreeSCV = csv.reader(fichierCSV, dialect='excel')
    donnees = []
    for ligne in entreeSCV:
        donnees.append(ligne)
    fichierCSV.close()


    fichierCSV = open("scores.csv", mode="w", newline='')
    sortieCSV = csv.writer(fichierCSV, dialect='excel')
    for ligne in donnees :
        sortieCSV.writerow(ligne)
    sortieCSV.writerow(donneesRecentes)
    fichierCSV.close()

def motChoisi (a) :
    """Fonction qui renvoie une liste avec le mot caché + le mot à trouver
        selon le choix du lvl (a) de difficulté de 1 à 3 """
    leMotChoisi = temp.motAleatoire(a)    # Grace au module d'Arthur, on obtient un mot aléatoir avec un niveau de difficulté appelé a
    lettreCache = ''                            # Initialisation des lettres cachées
    for lettre in leMotChoisi :                 # Pour chaque lettre du mot aléatoire ...
        lettreCache = lettreCache + "-"         # ... On rajoute "-" dans la liste des lettres Cachées
    print(leMotChoisi, lettreCache)
    return lettreCache, leMotChoisi             # On renvoie le tout


def jeu (error, lettre, mot, cache, lvl) :
    """ Fonction qui demande le nombre d'erreur du joueur actuel (error), la lettre que le joeur recherche (x) dans le mot qu'il doit deviner (mot). La Variable
        cache (cache) étant les lettres cachés où déjà trouvé du joueur. Il faut aussi donner le niveau du mot (lvl)"""
    gagne = True
    lettre = lettre.lower()
    mot = mot.lower()
    cacheD = list(cache)
    cache = list(cache)
    y = 0
    for let in mot :
        if let == lettre :
            cache[y] = lettre
        y += 1
    if cache == cacheD :        # Si le joueur a choisi une lettre ne se trouvant pas dans le mot ..
        error = error + 1       # ... Rajouter une erreur
    if error == 7 :             # Si le joueur commet 7 erreurs alors il a perdu
        gameOver = True
        return gameOver
    for tiret in cache :
        if tiret == "-":
            gagne = False
    if gagne == True :
        pts = lvl * 1000 + lvl *2 * 100 - error**2 * 10
        return gagne, pts
    print('vous avez fait', error, "erreurs, votre derniere lettre choisie était le", lettre.upper() , "il vous reste à trouver", cache)
    return error, lettre, cache



if __name__ == "__main__" :
    score("exemple", "Baptiste", "3")