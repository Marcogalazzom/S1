"""
Objectif du programme : Demander et afficher deux entiers de différentes manières
"""

# CONSTANTES

MESS = "Entrez deux entiers :"
CONJONCTION = " et "

# Demander à l'utilisateur les deux variables

A = int(input())
B = int(input())

# Affichage : Un par ligne

print(A,"\n" + str(B))

# Affichage : Sur la même ligne avec une virgule au milieu

print(A, B, sep=",")

# Avec un message donnant le nom et la valeur

print("A=", A, CONJONCTION, "B=", B, sep="" )

# En damier

print(A, B, A,)
print(B, A, B)
print(A, B, A)

# Sur la même ligne séparés par des tirets et avec un point d'exclamation final

print(A, B, A, B, sep="-", end="-!")
