"""
Objectif du programme : Faire un dé pipé
"""

import random

# CONSTANTES
J = "Quel est ton prénom ? "
F = "fait"
W = "gagne"
# Variables

# Demander les prénoms des 2 joueurs
P1 = input(J)
P2 = input(J)

# Tirer un vrai dé de 6 et l'afficher
de = random.randint(1, 6)
print(P1, F, de)

# Tirer un dé pipé de 1 à 3 et l'afficher
de_pipe = random.randint(1, 3)
print(P2, F, de_pipe)

# Déterminer le vainqueur et afficher le prénom
if de >= de_pipe:
    print(P1, W)
else:
    print(P2, W)


# Dé impair 6
de_impair = random.randint(1, 5)
if de_impair % 2 == 0:
    de_impair += 1
print(de_impair)

# Dé proba

de_proba = random.random()
if de_proba < 0.3:
    de_proba = 1
elif de_proba < 0.5:
    de_proba = 2
elif de_proba < 0.65:
    de_proba = 3
elif de_proba < 0.8:
    de_proba = 4
elif de_proba < 0.9:
    de_proba = 5
else:
    de_proba = 6

print(de_proba)
