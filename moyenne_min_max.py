"""
Objectif du programme : Prend les notes de l'utilisateur
                        et renvoie la moyenne, la meilleure et la pire note
"""

# CONSTANTES
NOTE = "Entrez une note : "

# Variables
nb_notes = 0
note = 0
total_note = 0
moyenne = 0
max_note = 0
min_note = 21

# Boucle
note = float(input(NOTE))
while note <= 20 and note >= 0:
    nb_notes += 1
    total_note += note
    if note > max_note:
        max_note = note
    if note < min_note:
        min_note = note
    note = float(input(NOTE))
moyenne = total_note/nb_notes
print("Le nombre de notes est", nb_notes)
print("La moyenne est", moyenne)
print("La meilleure note est", max_note)
print("La pire note est", min_note)
