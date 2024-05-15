# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:21:04 2023

@author: Lich Rave
"""
# First comment
"""
training from scratch, day 46.1 (15.05.24)
"""

# %%
b3
print("2")
print(2 + 2)
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 // 3

# %%
2**5

# %%
a = 10
b = 20

c = a * b

# %%
print(c)

# %%
print("love python")

# %%
import os

os.getcwd()

# %%
print(
    """
Instrukcja uruchamiania pliku przyklad.py

   --file [nazwa pliku]
        zapisuje output do pliku
        
   --quiet
        wycisza logi w konsoli
Koniec."""
)


# %%
text = "I love Python. "
print(text)
print(text * 3)
print("hau..." * 8)
print("*" * 30)

# %%
"Python"
"Py" "thon"
print("Py" "thon")

# %%

# %%
print("statement to be printed", end="white space or any character or string ")


# %%
if __name__ == "__main__":
    a = 5
    b = 0
    try:
        result = a / b
        print(f"result{result}")
    except:
        print("nie dziel na zero!")
    finally:
        print("Koniec")

# %%
# Słownik
phonebook = {}

# Dodać elementy
phonebook["Jack"] = 1111111
phonebook["Sarah"] = 222222

print(phonebook)
print(phonebook["Jack"])

# Definicja gotowego słownika
phonebook2 = {"John": 333333, "Dizee": 444444}
print(phonebook2)

# Przykład słownika
human = {}

human["name"] = "Maciej"
human["height"] = 180
human["weight"] = 90

print(human)

human_2 = {
    "name": "Maciej",
    "height": 180.5,
    "weight": 90.5,
    "Hobby": ["Vieo games", "programming", "mountain trips"],
}
print(human_2)
#
print(human_2.get("Hobby"))

# usuwanie elementu ze slownika v1
del human_2["Hobby"]
print(human_2)
# usuwanie elementu ze slownika v2
x = human_2.pop("weight")
print(human_2)


# %%
# %%
# def nazwa_funkcji_1():
#     <instrukcje> *ciało funkcji
# %% Przykład
def print_hello_world():
    print("Witaj, świecie!")


print("Przed funkcją")
print_hello_world()
print("Po funkcji")


# %%
def print_fullname(name, surname, title=None):
    if title is None:
        print(f"{name} {surname}")
    else:
        print(f"{title} {name} {surname}")


print_fullname("John", "Snow")
print_fullname(surname="John", name="Snow", title="Syr.")
print_fullname("John", surname="Snow")
print_fullname("John", "Snow", "Mr.")


# %%
def ge_hello(text: str) -> str:
    return f"Hello {text}"


print(ge_hello("World"))

# %% Z dowolną liczbą ilość (*args)


def add(*args):
    print(args)
    result = sum(args)
    return result


print(add(40, 10, 10, 20))


def add1(a, b, *numbers):
    print(numbers)
    result = a + b + sum(numbers)
    return result


print(add1(1, 2, 3, 4, 5))


# %% **kwargs
def add_ingrid(**kwargs):
    print(kwargs)


add_ingrid(banan=10, marchewka=20, melon=10)


# %%
def add_cos(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)  # może być pusta krotka
    print(kwargs)  # może być pusty słownik


add_cos(
    1,
    2,
    3,
    2,
    1,
    2,
    1,
    1,
    1,
    2,
    1,
    2,
    21,
    21,
    2,
    21,
    65,
    2,
    13,
    2,
    pope="Janek",
    mome="Jacek",
)


# %% Czwiczenia

# Zadanie 76
print("Zadanie 76:")


def f_1():
    print("Hello World")


f_1()

# Zadanie 77
print("Zadanie 77:")


def f_2():
    print("Hello World")


ans_1 = f_2()
print(ans_1)  # None


# Zadanie 78
print("Zadanie 78:")


def f_3():
    return "Hello, World!"


ans_2 = f_3()
print(ans_2)


# Zadanie 79
print("Zadanie 79:")


def f_4():
    print("Hello, world!")
    return "Hello, World!"


ans_3 = f_4()
print(ans_3)

# Zadanie 80
print("Zadanie 80:")


def zawsze_100(*args):
    return 100


print(zawsze_100(50))
print(zawsze_100(99999999999999999999999999999999999999999999999999))

# Zadanie 81
print("Zadanie 81:")


def d_1(number: int):
    return number


print(d_1(44))
print(d_1("Maciej"))

# Zadanie 83
# print("Zadanie 83:")


# def f_name():
#     name = input("Podaj swoje imie: ")
#     print(f"Hello, {name}!")


# f_name()

# Zadanie 84
print("Zadanie 84:")


def f_8(number: int):
    return number + 5


def f_9(number: int):
    return f_8(number) * 2


print(f_9(6))

# %%

Krotka_1 = ()
Krotka_2 = 1, 2, 3, 4

print(Krotka_1)
print(Krotka_2)


Krotka_2 = 10, 2, 6, 5

print(Krotka_2)

# %%
import time

st = time.time()
numbers = []
for i in range(int(1e8)):
    numbers.append(i)
et = time.time()
loop_time = et - st

print(len(numbers))
st = time.time()
numbers_comp = [i for i in range(int(1e6))]
print(len(numbers_comp))
et = time.time()
comp_time = et - st

print(f"loop time = {loop_time}")
print(f"comprehension time = {comp_time}")

# %%


# Class representing an ugly woman (adaptee)
class UglyWoman:
    def look_ugly(self):
        return "Ugly woman"


# Adapter class (makeup)
class MakeupAdapter:
    def __init__(self, ugly_woman, beautiful_women):
        self._ugly_woman = ugly_woman
        self._beautiful_women = beautiful_women

    def look_beautiful(self):
        # Using the adaptee method with added makeup
        return f"{self._ugly_woman.look_ugly()} ===> {self._beautiful_women.look_beautiful()}"


# Target class representing a beautiful woman
class BeautifulWoman:
    def look_beautiful(self):
        return "Beautiful woman"


# Helper function to check the appearance
def check_appearance(woman):
    print(woman.look_beautiful())


# Create an instance of an ugly woman
ugly_woman = UglyWoman()
beautiful_women = BeautifulWoman()

# Create an adapter with the ugly woman as adaptee
makeup_adapter = MakeupAdapter(ugly_woman, beautiful_women)

# # Create an instance of a beautiful woman as the target
# beautiful_woman = BeautifulWoman()

# Call the check_appearance function using the adapter
check_appearance(makeup_adapter)

# %%

# F INPUT
print("Witam serdecznie.")
user_name = input("Podaj swoje imię: ")
print(f"Cześć, {user_name}!")

# lista polecen

# F IF elif ELSE
x = 50
y = 50
if x > y:
    print(f"x:{x} jest większe od y:{y}")
elif x == y:
    print(f"x:{x} równa się y:{y}")

else:
    print(f"x:{x} jest mniejsze od y:{y}")


# Wódka
x = 3
y = 3
procenty = int(input("Podaj procenty: "))
if procenty >= 90:
    print("Masz mocny bimber")
elif procenty >= 80:
    print("Dobra wodka")
elif procenty >= 70:
    print("Srednia wodka")
else:
    print("Oranżada")

# Pętla
# nieskończone iter. - WHILE
# zdefiniowan. iteracj - określ. liczba iteracji


# WHILE


# %%

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

# %%
