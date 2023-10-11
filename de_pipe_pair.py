"""
Objectif du programme : Faire un de pipe qui tire jusqu'à nombre pair
"""

import random

# CONSTANTES
DE = "Résultat du dé :"
TIRAGE = "Nombre de tirages :"

# Variables
i = 0
flagged_pair = False

# Boucle jusqu'à pair
while flagged_pair != True:
    de = random.randint(1, 6)
    if de % 2 == 0:
        i += 1
        flagged_pair = True
    else:
        i+= 1

print(DE, de, TIRAGE, i)