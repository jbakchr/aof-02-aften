# Simpel brug af en variabel til at gemme input fra brugeren i en variabel
name = input("Hvad er dit navn? ")
print(name)


# Brug af flere variabler til at gemme input fra brugeren
name = input("Hvad er dit navn? ")
age = input("Hvor gammel er du? ")
money = input("Hvor mange penge har du i banken? ")
print(name)
print(int(age))
print(float(money))


# Brug af variabler til at printe en talrække
start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

for i in range(start, stop, step):
    print(i)
