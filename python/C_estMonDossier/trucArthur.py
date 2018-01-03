import random

listMot1 = ["fleur", "clavier", "gateau", "console", "cadre", "manette", "johnny", "globe"]
listMot2 = ["ordinateur", "enceinte", "clavier", "bibliothèque", "armoire", "istanbul", "artichaut"]
listMot3 = ["explorateur", "lilote", "stereochimie", "metaphore", "fumigene", "araignee", "bigorneau"]
listeB = ["abcabccab"]




def motAleatoire(a):
    """Renvoie un mot aléatoirement selon la difficulté choisie dans a"""
    if a == 1  :
        x = random.randint(0,len(listMot1)-1)
        return listMot1[x]
    if a == 2 :
        x = random.randint(0,len(listMot2)-1)
        return listMot2[x]
    if a == 3 :
        x = random.randint(0,len(listMot3)-1)
        return listMot3[x]
    if a == 4 :
        x = random.randint(0, len(listeB)-1)
        return listeB[x]




if __name__ == "__main__" :
    print(motAleatoire(1))
