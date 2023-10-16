"""
Objectif du programme : User rentre un int naturel, 
                        programme dit si l'int est premier
"""

# CONSTANTES
DEMARRAGE = "Programme de test de nombres premiers"
QUESTION = "Entre un entier ? "
PREMIER = "est premier"
NON_PREMIER = "n'est pas premier"
REPLAY = "Rejouer ? "
FIN = "Fin du programme"

# Variables
reponse = "oui"

# Affichage
print(DEMARRAGE)

# Boucle
while reponse == "oui":
    premier = True
    i = 2
    nombre = int(input(QUESTION))
    while i < nombre:
        if nombre % i == 0:
            premier = False
        i += 1
    if premier:
        print(nombre, PREMIER)
    else:
        print(nombre, NON_PREMIER)
    reponse = input(REPLAY)
print(FIN)
