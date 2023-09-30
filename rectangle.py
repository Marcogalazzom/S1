"""
Objectif du programme : Calculer l'aire d'un rectangle
"""

# CONSTANTES

LARGEUR = "Largeur ? "
LONGUEUR = "Longueur ? "
AIRE = "L'aire du rectangle de largeur"
AIRE_NEXT = "et de longueur"

# On demande les valeurs à l'utilisateur

largeur = int(input(LARGEUR))
longueur = int(input(LONGUEUR))

# On calcule et affiche le résultat

print(AIRE, largeur, AIRE_NEXT, longueur, "vaut", largeur*longueur, end=".\n")
