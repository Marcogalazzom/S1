"""
Objectif du programme : Affiche le factorielle d'un entier n
                        saisi par l'utilisateur
"""
# CONSTANTES
QST = "Entrez un nombre : "
RST = "Le résultat de"
FST = "factorielle est de"
BST = "Voulez vous recommencer (Y/N) : "

# Variables
i = 1
factor = 1
touche = "Y"

while touche == "y" or touche == "Y":
    # Demande à l'utilisateur un entier n
    n = int(input(QST))

    # Boucle qui calcule le factorielle
    while i <= n:
        factor *= i
        i += 1

    print(RST, n, FST, factor)
    touche = input(BST)
