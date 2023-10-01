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

if nombre_max < a:
    nombre_max = a
    if nombre_max < b:
        nombre_max = b
        if nombre_max < c:
            nombre_max = c
    elif nombre_max < c:
        nombre_max = c


# On affiche la valeur max

print(FIN, nombre_max)
