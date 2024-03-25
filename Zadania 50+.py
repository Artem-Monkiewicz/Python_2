# 01,12,23 WPROWADZANIE DANYCH

print("ZAdanie 50")
imie = input("Wprowadż imie,ok?: ")
print(f"OK, masz na imie {imie}")

print("ZAdanie 51")
wiek = input("Wprowadż wiek,ok?: ")
print(f"OK, masz {wiek} lat")

# Type INT!!!
print("ZAdanie 52")
wiek_added = int(
    input("Wprowadż swój wiek, ja powiem, ile będziesz miał za 50 lat, ok?: ")
)
print(f"OK, za 50 lat będziesz miał {wiek_added + 50} lat")

print("ZAdanie 53")
days = int(input("Podaj ilość dni: "))

result = days / 365

print(f"{days} dni to {result} lat")


print("Zadanie 54")
exception = True
while exception:
    exception = False
    try:
        miles = float(input("Podaj ilość mil: "))
    except:
        exception = True
        print("Wpisz poprawna warotśc liczbowa")

result = miles * 1.6

print(f"{miles} mil to {result} km")

#iNSTRUKCJE STERUJĄCE
print("Zadanie 55")
nameBond = input("Podaj imie: ")
if nameBond == "Bond":
    print(f"Welcome on board 007!")
else:
    print(f"Cześć, {nameBond}")

# 55 v2
name = input("Podaj imie: ")
#Niezależnie od literek a spacji
x = name.lower()
x = x.strip()
if "bond" in name.lower().strip():
    print("Welcome aboard agent 007.")
else:
    print(f"Hey, {name}")



#56
number = int(input("Podaj liczbe: "))

if number % 2 == 0:
    print("Parzysta!")
else:
    print("Nieparzysta!")

#custom

number = int(input("Podaj liczbe: "))

if number%3 ==0:
    print("Liczba podzielna przez 3")
elif number%2 == 0:
    print("liczba jest podzielna przez 2")
else:
    print("Liczba nie jest podzielna ani przez 3 ani przez 2")


#Pętla

dzielnik = 50
dzielniki= []
while dzielnik >1:
    if number%dzielnik == 0:
        dzielniki.append(dzielnik)
    dzielnik -=1
if dzielniki:
    print(f"Liczba jest podzielna przez {dzielniki[0]}")
else:
    print(f"liczba nie ejst pdozielna przez liczbe mniejsza lub rowna 50")

#Pętla WHILE

n = 1
while n < 6:
    n += 1
    print(n)

#break continue

#FUNKCJA RANGE 5:00 TIme

#%%
# Zadanie 58
lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
my_message = ""

i = 0
while i < len(lst):
    if lst[i] == 100:
        my_message = f"There is a 100 at index no: {i}"
    i += 1

print(my_message)

# Zadanie 59
lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
i = 0
lst2 = []
while i < len(lst1):
    if lst1[i]:  # lst1[i] != "":
        lst2.append(lst1[i])
    i += 1
print(lst2)

# Zadanie 60
print("Zadanie 60")
lst = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]

for animal in lst:
    print(animal)

# Zadanie 61
print("Zadanie 61")
lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
    print(f"Hello!, {name}")
# Zadanie 62
print("Zadanie 62")
napis = "Civilization"
c = 0
for char in napis:
    c += 1

print(c)
print(c == len(napis))

# Zadanie 63
print("Zadanie 63")
lst1 = ["Phil", "Oz", "Seuss", "Dre"]
lst2 = []
for name in lst1:
    lst2.append(f"Dr. {name}")

print(lst2)
# Zadanie 64
print("Zadanie 64")
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []
for number in lst1:
    lst2.append(number ** 2)
print(lst2)

# Zadanie 65
print("Zadanie 65")
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for number in lst1:
    if number > 0:
        lst2.append(number)

print(lst2)
# Zadanie 66
print("Zadanie 66")
dict = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
for value in dict.values():
    if value > 1000:
        lst.append(value - 1000)
print(lst)
print(dict)

# Zadanie 67
print("Zadanie 67")
lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []
for item in lst1:
    lst2.append(type(item))

lst3 = [type(item) for item in lst1]
print(lst2)
print(lst3)

# Zadanie 68
print("Zadanie 68")
lst1 = [1, 2, 3, 4, 5]
lst2 = [number for number in lst1]
print(lst2)
# Zadanie 69
print("Zadanie 69")
rng = [number for number in range(1200, 2001, 130)]
print(rng)

# Zadanie 70
print("Zadanie 70")
lst1 = [44, 54, 64, 74, 104]
lst2 = [number + 6 for number in lst1]
print(lst2)

# Zadanie 71
print("Zadanie 71")
lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [number ** 2 for number in lst1 if number ** 2 > 50]
print(lst2)

# Zadanie 72
print("Zadanie 72")
dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}
lst = [key.upper() for key in dict if dict[key] < 5000]
lst1 = [key.upper() for key, value in dict.items() if value < 5000]
print(lst)
print(lst1)