import pickle
import trucArthur

def score ():
    fichierScore = open("score.txt", "w")
    fichierScore.write("Ne supprimez pas ce fichier")
    fichierScore.close()

def motChoisi () :
    leMotChoisi = trucArthur.motAleatoire()
    return leMotChoisi

def rechecheL (x, mot) :
    y = 0
    place = []
    x = x.lower()
    for lettre in mot :
        if x == lettre :
            place.append(y)
        y += 1
    print(place)


rechecheL("a", "antouane")