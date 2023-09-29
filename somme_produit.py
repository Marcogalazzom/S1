"""
Objectif du programme : Affiche la somme et le produit 
                        de deux réels rentrés par l'utilisateur
"""

# CONSTANTES

X = "x=? "
Y = "y=? "

# Demande à l'utilisateur les deux réels

x_str = input(X)
y_str = input(Y)

# On vérifie si x et y sont des réels ou des int

if "." in x_str:
    x = float(x_str)
else:
    x = int(x_str)

if "." in y_str:
    y = float(y_str)
else:
    y = int(y_str)

# Affiche la somme et le produit

print(x, "+", y, "=", round(x+y, 3))
print(x, "*", y, "=", round(x*y, 3))
