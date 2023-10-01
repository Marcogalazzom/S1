"""
Objectif du programme : Demande trois int et affiche le plus grand
"""

# CONSTANTES

QUESTION = "Entrez un entier "
FIN = "La valeur maximum est"

# On crée la variable max

nombre_max = 0

# On demande les trois entiers

a = int(input(QUESTION + "a : "))
b = int(input(QUESTION + "b : "))
c = int(input(QUESTION + "c : "))

# On compare les trois valeurs

if a > c:
    if b < c or b < a:
        nombre_max = a
    else:
        nombre_max = b
else:   # Si c > a
    if b < c:
        nombre_max = c
    else:
        nombre_max = b

# On affiche la valeur max

print(FIN, nombre_max)
