"""
Objectif du programme : Demander à l'utilisateur son prénom
                        et afficher un message de bienvenue
"""

# CONSTANTES

QUESTION = "Comment t'appelles-tu ? "
MESSAGE = "Bonjour"

# On demande à l'utilisateur son prénom

name = input(QUESTION)

# On affiche le message de bienvenue

print(MESSAGE, name, end=" !\n")
