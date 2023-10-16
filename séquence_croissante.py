"""
Objectif du programme : Lit une suite d'entiers et dit 
                        si la suite est croissante, décroissante,
                        constante ou ni croissante ni décroissante
"""

# CONSTANTES
QUESTION = "Entrez un nombre : "

# Variables

croissante = True
decroissante = True
constante = True

last_n = int(input(QUESTION))
n = int(input(QUESTION))


# Boucle
while n >= 0:
    if n > last_n:
        decroissante = False
        constante = False
    elif n < last_n:
        croissante = False
        constante = False
    else:
        croissante = False
        decroissante = False
    last_n = n
    n = int(input(QUESTION))

if croissante:
    reponse = "Croissante"
elif decroissante:
    reponse = "Décroissante"
elif constante:
    reponse = "Constante"
else:
    reponse = "Ni croissante, ni décroissante"

# Affichage
print(reponse)
