"a"

l = 0   # Nombre de lignes
i = 0   # Nombre de caractères par ligne
caractere = "*"

while l < 5:
    i = 0
    while i < 4:
        print(caractere,end='')
        i+=1
    l += 1
    print()

l = 0
i = 0

"b"
n = 0

while l < 5:
    i = 0
    n += 1
    while i < n:
        print(caractere, end='')
        i += 1
    l += 1
    print()

i = 0
n = 0
l = 0

"c"
n = 5
blanc = 5
while l < 5:
    i = 0
    blanc -= 1
    while i < n:
        if i < blanc:
            print(' ', end="")
        else:
            print(caractere, end='')
        i += 1
    l += 1
    print()

"d"

l = 0
i = 0
n = 6

while l < 5:
    i = 0
    n -= 1
    while i < n:
        print(caractere, end='')
        i += 1
    l += 1
    print()

"e"

i = 0
l = 0
blanc = -1
n = 5

while l < 5:
    blanc += 1
    i = 0
    while i < n:
        if i < blanc:
            print(' ', end='')
        else:
            print(caractere, end='')
        i += 1
    l += 1
    print()


"f"

i = 0
l = 0
partie_blanc = 2
blanc = 5
blanc2 = 9
n = 9

while l < 5:
    blanc -= 1
    i = 0
