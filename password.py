"""
Objectif du programme : Demander à l'utilisateur le mot de passe
                        définit à l'avance 
"""

# CONSTANTES
QST = "Mot de passe : "
REFUS = "Accès refusé"
ACCES = "Accès autorisé"

# Variables
mdp = "turlututu"
user_mdp = ""
essai = 1
# Boucle

while mdp != user_mdp and essai <= 5:
    user_mdp = input(QST)
    if mdp != user_mdp:
        print(REFUS)
        essai += 1
    else:   # Si le mot de passe est le bon
        print(ACCES)

