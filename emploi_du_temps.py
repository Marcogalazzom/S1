"""
Objectif du programme : Calculer le nombre d'heures 
                        de cours de l'utilisateur
"""

# CONSTANTES

HOURS = "Combien d'heures par semaine ? "
WEEKS = "Combien de semaines de cours ? "
TOTAL = "Total :"

# On demande les valeurs à l'utilisateur

hours = int(input(HOURS))
weeks = int(input(WEEKS))

# On calcule et on affiche le nombre total d'heures

print(TOTAL, hours*weeks, end=" heures\n")
