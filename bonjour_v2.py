"""
Objectif du programme : Afficher le prénom de l'utilisateur
                        et un message dans la langue de son choix
"""

# CONSTANTES

Q_PRENOM = "Quelle est votre prénom ? "
Q_LANGUE = "Quelle est votre langue ? (English or Français) "
MESS_ENG = "Hello"
MESS_FR = "Bonjour"

# On demande à l'utilisateur son prénom et sa langue

prenom = input(Q_PRENOM)
langue = input(Q_LANGUE)

# On vérifie la langue rentrée

if langue == "1" or langue == "English" or langue == "english":
    print(MESS_ENG, prenom)
else: # Si la langue sélectionnée n'est pas anglais c'est forcément français
    print(MESS_FR, prenom)
