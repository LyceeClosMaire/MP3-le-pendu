import pickle
import temp
import jeu
import csv
import os
import time


def score (mot, nom, score):
    """Fonction qui en enregistre les score, la fonction demande le mot qui a été trouvé, le nom ou pseudo du vainqueur
        ainsi que le score qu'il vient de réaliser. Cette fonction va permettre d'neregistrer tous ces éléments mais
        en ajoutant aussi la date de l'enregistrement, dans un fichier scv nommé Scores  """
    now = time.ctime()                                              # On demande la date de l'enregistrement du score
    date = time.strftime("%Y, %m, %d, %H", time.strptime(now))      # On ne sélectionne que l'année, le mois, le jour et l'heure à enregistrer

    donneesRecentes = [mot, nom, score, date]                       # Données que l'on veut rajouter à notre fichier csv

    fichierCSV = open("scores.csv", mode='r', newline='')           # On ouvre le fichier des scores en mode lecture
    entreeSCV = csv.reader(fichierCSV, dialect='excel')
    donnees = []
    for ligne in entreeSCV:                                         # On y lit ligne par ligne le contenu et on l'enregistre dans une variable
        donnees.append(ligne)
    fichierCSV.close()                                              # On ferme le fichier


    fichierCSV = open("scores.csv", mode="w", newline='')           # On ouvre le fichier en mode écriture
    sortieCSV = csv.writer(fichierCSV, dialect='excel')
    for ligne in donnees :
        sortieCSV.writerow(ligne)                                   # On reécrit le fichier avec les anciennes valeurs et on rajoute le nouveau score
    sortieCSV.writerow(donneesRecentes)
    fichierCSV.close()                                              # On ferme le fichier

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
    """ Fonction qui demande le nombre d'erreur du joueur actuel (error), la lettre que le joueur recherche (x) dans le mot qu'il doit deviner (mot). La Variable
        cache (cache) étant les lettres cachés où déjà trouvé du joueur. Il faut aussi donner le niveau du mot (lvl)"""

    gagne = True
    lettre = lettre.lower()
    mot = mot.lower()
    cacheD = list(cache)
    cache = list(cache)
    y = 0

    for let in mot :
        if let == lettre :      # Si une des lettres que le joueur demande se trouve dans le mot
            cache[y] = lettre   # Alors on remplace la lettre cachée par la lettre trouvée
        y += 1

    if cache == cacheD :        # Si le joueur a choisi une lettre ne se trouvant pas dans le mot ..
        error = error + 1       # ... Rajouter une erreur

    if error == 7 :             # Si le joueur commet 7 erreurs alors il a perdu
        gameOver = True
        return gameOver

    for tiret in cache :
        if tiret == "-":        # Si il reste une seule lettre cachée dans le mot alors le joueur n'a pas encore gagné
            gagne = False

    if gagne == True :
        pts = lvl * 1000 + lvl *2 * 100 - error**2 * 10         # Si aucune lettre cachée reste à trouver alors on calcule le score
        return gagne, pts
    print('vous avez fait', error, "erreurs, votre derniere lettre choisie était le", lettre.upper() , "il vous reste à trouver", cache)

    return error, lettre, cache     # On retourne le nombre d'erreur, la lettre que le joueur vient de choisir et toutes les lettres encore cachées
