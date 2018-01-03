import random

def motAleatoire():
    listMot = ["ordinateur", "table", "clavier", "bibliothèque", "armoire", "istanbul", "artichaut"]
    x = random.randint(0,len(listMot)-1)
    return listMot[x]

print(motAleatoire())

