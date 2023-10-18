"""
Objectif du programme : Calculer un polynôme du second degré
"""

import math

# CONSTANTES
REEL = "Entrez un réel : "
DELTA = "Delta vaut :"
X0 = "La racine unique est :"
X1 = "La première racine est :"
X2 = "La seconde racine est :"
NOTX = "Pas de racine dans R"

# Demande a, b, c à l'utilisateur
a = float(input(REEL))
b = float(input(REEL))
c = float(input(REEL))

# Calcul du polynôme
delta = b**2 - 4 * a * c

print(DELTA, delta)

if delta > 0:
    # Deux racines
    print(X1, (-b - math.sqrt(delta))/(2 * a))
    print(X2, (-b + math.sqrt(delta))/(2 * a))
elif delta == 0:
    print(X0, (-b)/(2 * a))
else:
    print(NOTX)