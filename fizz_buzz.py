"""
Objectif du programme : Ecrire un Fizz buzz de 1 à 100
"""

# CONSTANTES
FB = "fizzbuzz"
F = "fizz"
B = "buzz"

# Variables
i = 1   # Compteur

# Boucle

while i <= 1000:
    if i % 3 == 0 and i % 5 == 0:
        print(FB)
        i += 1
    elif i % 3 == 0:
        print(F)
        i += 1
    elif i % 5 == 0:
        print(B)
        i += 1
    else:
        print(i)
        i += 1
