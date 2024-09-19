# Eksempel 1: 'print' funktionen i sin enkelhed
print("Hello World")


# Eksempel 2: 'print' funktionen med flere "objects"
print("Hello", "World")


# Eksempel 3: 'print' funktionen med flere "objects" og "sep" keyword argumentet
print("Hello", "World", sep="-")
print("Hello", "World", sep="--ost--")


# Eksempel 4.1: 'print' funktionen med flere "objects" og "end"
print("Hello", "World", end="\n\n\n\n")


# Eksempel 4.2: 'print' funktionen med flere "objects" og "end" keyword argumentet
for i in range(5):
    print(i, end=" ")
