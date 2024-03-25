# Zbiór

# Stworz set
animals = {"pies", "kot", "słoń"}
animals2 = {"koń", "słon", "kot", "tygrys"}
print(animals, type(animals))

# dodawanie elementów
animals.add("mysz")
print(animals, type(animals))
# elementy w zbiorze unikalne, nie powatarzają się
animals.add("mysz")
print(animals, type(animals))

# usuwanie - Nie da się usunąć tego, czegonie ma
print("Usuwanie_ DISCARD/REMOVE")
animals.discard("lew")
print(animals, type(animals))

animals.discard("mysz")
print(animals, type(animals))

# Sprawdzanie części wspólnej
print("Intersection - sprawdzanie cząści wspólnej")
print(animals.intersection(animals2))
# Sprawdzenie różnicy zbiórów
print("Difference - sprawdzanie cząści różnej")
print(animals.difference(animals2))

# sprawdzanie czy danny zbiór jest nadzbiórem(znajduje sie w innym)
print("Issuperset - Nadzbióry")
print(animals.issuperset(animals2))

# polączenie zbiórów
print("Union - polączenie zbiórów")
print(animals.union(animals2))
