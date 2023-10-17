"""
Objectif du programme : Deux joueurs lance un dé chacun leur tour,
                        le second joueur à un dé pipé (3 dés)
"""
import random

# CONSTANTES
P1_WIN = "Joueur 1 gagne"
P2_WIN = "Joueur 2 gagne"
QST = "Nombre de parties : "
WIN = "Le joueur legit a gagné au total :"

# Variables
de_p1 = random.randint(1,6)
lance_pipe = 3
maximum_de2 = 0
i = 0
parties = 0
compteur_p1 = 0

# Demande à l'utilisateur le nombre de parties

nb_parties = int(input(QST))

# Calcul le nombre de parties
while parties < nb_parties:
    i = 0
    maximum_de2 = 0
    while i < lance_pipe:
        de_p2 = random.randint(1,6)
        if de_p2 > maximum_de2:
            maximum_de2 = de_p2
        i += 1
    de_p2 = maximum_de2
    if de_p1 > de_p2:
        compteur_p1 += 1
    parties += 1
print(WIN,compteur_p1,"parties")
