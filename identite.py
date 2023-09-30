"""
Objectif du programme : Demander à l'utilisateur
                        son nom et prénom et l'afficher
"""

# CONSTANTES

Q_PNOM = "Quel est ton prénom ? "
Q_NOM = "Quel est ton nom ? "
IDENTITE = "Identité : "

# On demande le prénom et le nom de l'user

fname = input(Q_PNOM) 
lname = input(Q_NOM)

# On affiche l'identité de l'user

print(IDENTITE, fname, lname)
