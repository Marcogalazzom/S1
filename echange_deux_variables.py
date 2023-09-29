"""
Objectif du programme : Échanger des valeurs de deux variables
"""

# CONSTANTES

MESS_DEMANDE = "Entrez deux réels : "
MESS_AFFICHAGE = "Vous avez saisi"
MESS_FINAL = "Après échange des variables :"
CONJONCTION = "et"

# On demande à l'utilisateur deux réels

print(MESS_DEMANDE)
x = float(input())
y = float(input())
print(MESS_AFFICHAGE, x, CONJONCTION, y)

# On échange les valeurs des variables

x_bis = x  # On crée une variable intermédiaire pour stocker x
x = y
y = x_bis

# On affiche le résultat

print(MESS_FINAL, x, CONJONCTION, y)
