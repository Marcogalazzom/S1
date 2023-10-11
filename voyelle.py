"""
Objectif du programme : Demander lettre jusqu'à voyelle
"""

# CONSTANTES
Q = "Veuillez saisir une voyelle : "
# Variables
voyelled = False
# Boucle

while voyelled != True:
    lettre = input(Q)
    # Ou if lettre in "aeiouy"
    if lettre == "a" or lettre == "e" or lettre == "i" or lettre == "o" or lettre == "u" or lettre == "y":
        voyelled = True
