import jeu

img0 = ''
img1 = "_"
img2 = "_-"
img3 = "_-_"
img4 = "_-_-"
img5 = "_-_-_"
img6 = "_-_-_-"
img7 = "_-_-_-_"
jouer = True
erreur = 0
lettreD = []

x = jeu.commencement()
listemot = jeu.motChoisi(x)
mot = listemot[1]
motC = listemot[0]
print (motC)

while jouer == True :
    z = input("Choisir une lettre")
    jet = jeu.rechecheL(erreur, z, mot)
    # si une lettre est trouvé alors
        lettreD.append(jet[0])