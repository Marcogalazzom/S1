"""
Objectif du programme : afficher la suite de Syracuse
"""

# CONSTANTES
QST = "Entrez un entier strictement positif : "
DVOL = "Durée de vol :"
MAXI = "Maximum atteint en :"
PLD = "Plus longue descente :"

# Variables
i = 0   # Durée de vol
d = 0   # Descente
pld = 0 # Plus longue descente


# Demande à l'utilisateur un entier
n = int(input(QST))
nmax = n    # Maximum atteint par la suite
# Syracuse
while n != 1:
    if n % 2 == 0:
        n /= 2
        d += 1
    else:   # Si n n'est pas un multiple de 2
        n = 3 * n + 1
        d = 0
    i += 1
    if nmax < n:
        nmax = n
    if d > pld:
        pld = d
    print(n)

# Affichage des résultats
print(DVOL, i)
print(MAXI, int(nmax))
print(PLD, pld)