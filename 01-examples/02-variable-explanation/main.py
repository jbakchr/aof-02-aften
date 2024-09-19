""" Om variable som 'containere' for data/værdier """

# Eksempel 1.1: "name" variabel som 'container' for det svar brugeren giver på 'input' funktionen
name = input("Hvad er dit navn? ")
print(name)


# Eksempel 1.2: Brug af flere variabler til at gemme input fra brugeren
name = input("Hvad er dit navn? ")
age = input("Hvor gammel er du? ")
money = input("Hvor mange penge har du i banken? ")
print(name)
print(int(age))
print(float(money))


# Eksempel 1.3: Brug af variabler til fx at printe en talrække
start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

for i in range(start, stop, step):
    print(i)


""" Erklæring og initialisering sker på samme tid (i Python) """
# Eksempel 2.1: Først 'erklærer' man at man vil bruge en variabel kaldet "number"
# og dernæst 'initialiserer' vi den her til tallet 10 (a.k.a. sætter variablen lig med 10)
number = 10


""" Variables datatype kan ændres, når man vil """
# Eksempel 3.1: Her ændres datatype af variablen "number" fra int til str
number = 10
number = "10"


""" Variables er case-sensitive """
# Eksempel 4.1: Her er variablen "name" ikke lig med variablen "Name"
name = "John"
Name = "Doe"


""" Variabler kan ændres undervejs - både til samme datatype og andre datatyper """
# Eksempel 5.1: Her ændres variablen "number" først fra 10 til 20, og derefter fra int til str
number = 10
number = 20
number = "20"
