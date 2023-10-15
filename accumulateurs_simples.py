"""
Objectif du programme : Utiliser l'accumulation
"""

# CONSTANTES
N = "Entrez un nombre : "
SPE = "Somme des entiers jusqu'à"
SPEI = "Sommes des entiers impairs jusqu'à"
TOUCHE = "Voulez vous continuer (Y/N) : "

# Variables
i = 1
somme = 0
touche = ""

# Demander n à l'utilisateur

n = int(input(N))

while i <= n:
    somme += i
    i += 1


print(SPE, n, ":", somme)

i = 0
somme = 0

while i <= n:
    if i%2 == 1:
        somme += i
    i += 1
print(SPEI, n, ":", somme)

somme = 0

while touche != "N" and touche !="n":
    nombre = int(input(N))
    somme += nombre
    touche = input(TOUCHE)
print("Somme des nombres entiers lus au clavier :", somme)

touche = ""
produit = 1

while touche != "N" and touche !="n":
    nombre = int(input(N))
    produit *= nombre
    touche = input(TOUCHE)
print("Produit des nombres entiers lus au clavier :", produit)


i = 1
paires = int(input("Nombres de paires : "))
n1 = 0
n2 = 0
drapeau = True

while i <= paires:
    n1 = int(input(N))
    n2 = int(input(N))
    if n1 > n2:
        drapeau = False
    i += 1

if drapeau == True:
    print("Toutes les paires sont en ordre croissant")
else:
    print("Toutes les paires ne sont pas en ordre croisant")
