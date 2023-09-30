"""
Objectif du programme : Demander à l'utilisateur son année de naissance
                        et calculer et afficher son âge
"""

# CONSTANTES

QUESTION = "Quelle est ton année de naissance ? "
MESSAGE = "En 2023, tu as"

# Demande à l'utilisateur son année de naissance

adn = int(input(QUESTION))

# Calcule et affiche son âge

print(MESSAGE, 2023-adn, "ans.")
