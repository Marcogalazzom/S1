"""
Objectif du programme : Demander n entiers et 
                        afficher le max et le min
"""

# CONSTANTES

Q_INT = "Entrez un entier : "
Q_REP = "Voulez-vous continuer ? (y/n) "
MAX = "Le maximum est"
MIN = "et le minimum est"

# Variable

rep = "y"

# On initialise le max et le min avec a

a = int(input(Q_INT))
maximum = a
minimum = a

# Boucle
while rep == "y":
    a = int(input(Q_INT))
    if a > maximum:
        maximum = a
    elif a < minimum:
        minimum = a
    rep = input(Q_REP)

# On affiche le résultat

print(MAX, maximum, MIN, minimum, end=".\n")
