"""
Objectif du programme : Échanger des valeurs de trois variables
"""

# CONSTANTES
MESS_DEMANDE = "Entrez trois réels : "
MESS_AFFICHAGE = "Vous avez saisi"
MESS_FINAL = "Après échange des variables"
CONJONCTION = "et"

# On demande à l'utilisateur trois réels

print(MESS_DEMANDE)

x = float(input())
y = float(input())
z = float(input())

print(MESS_AFFICHAGE, x, CONJONCTION, y, CONJONCTION, z)

# On échange les valeurs

x_bis = x  # On crée une variable intermédiaire pour stocker x
x = y
y = z
z = x_bis

# On affiche le résultat

print(MESS_FINAL, x, CONJONCTION, y, CONJONCTION, z)
