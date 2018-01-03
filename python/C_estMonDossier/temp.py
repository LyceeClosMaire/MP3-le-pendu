import random 

easy = ["chat", "chien", "salade", "frite", "kebab", "ordinateur", "fenetre", "clavier", "souris", "voiture", "moto", "coiffeur", "champs",
        "table", "chaise", "avion", "terasse", "trousse", "cahier", ]


medium = ["garagiste", "ingenieur", "portugais", "chaussure", "pantalon", "oignon", "cellulaire", "prise", "site", "magasin", "montagne", ]


hard = ["basiquement", "stereochimie", "metaphore", "fumigene", "constitution", "turbine", "sodium", "chanvre", "mol", "gaz", "tondeuse", "piston",
        "avez", "axez", "ayez", "azur", "binz", "buzz", "chez", "czar", "dzos", "fiez", "fizz", "gaza", "gaze", "gazé", "günz", "hiez", "huez", "irez",
        "ixez", "jazz", "laze", "liez",
        "lutz", "maza", "maze", "muez", "naze", "nazi", "niez", "nuez", "onze", "osez", "ouzo", "oyez", "puez", "quiz", "ranz", "riez", "ruez", "suez", "tuez", 
        "tzar", "usez", "witz", "yuzu", "zain", "zamu", "zarb", "zecs", "zefs", "zend", "zens", "zest", "zigs", "zikr", "zinc", "zips", "zire",
        "zist", "zizi", "zobs", "zona", "zone", "zoom", "zoos", "zouk", "zozo", "zups",]
  


def motAleatoire(x): 
    if x == 1 :
        y= random.randint(0, len(easy)-1)
        return easy[y]
    if x == 2 : 
        y= random.randint(0, len(medium)-1)
        return medium[y]
    if x == 3: 
        y= random.randint(0, len(hard)-1)
        return hard[y]
