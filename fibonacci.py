"""
Objectif du programme : lit un entier n et renvoie fn (fibonacci)
"""

# CONSTANTES
QST = "Entrez un entier : "

# Variables
i = 2
vi = 0  # Stocke la valeur intermédiaire

# Demande un entier n
n = int(input(QST))

# Fibonacci
if n == 0 or n == 1:
    nb_fibo = 1
else:   # n >= 2
    fnm1 = 1
    fnm2 = 1
    while i <= n:
        fn = fnm1 + fnm2
        fnm2 = fnm1
        fnm1 = fn
        i += 1
    print(fn)

# Estimation nombre d'or : fn / fnm1
print(fn/fnm2)
