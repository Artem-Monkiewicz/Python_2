# 1 czym jest zmienna, czym są typy, określanie typów w Pythonie i jak owe  określanie ma się do definicji języka silnie i słabo typowanego
from typing import Optional, List

zmienna = 10
"""
Typy podstawowe:
liczba całkowita: int
liczba zmiennoprzecinkowa: float (liczba rzeczywista)
liczby zespolone: complex
łańcuchy znaków: string
typ logiczny: boolean
typ bajtowy: bytes
typ None: None
Typy kolekcji:
    - Lista: list
    - Krotka: tuple
    - Słownik: dict
    - Zbiór: set
"""
"""
W Pythonie nie musimy określać typów zmiennych samodzielnie.
Aby sprawdzic typ zmiennej mozemy użyc funckji type()
"""
# Jak typujemy w pytanonie?
zmienna_2: int = ""  # Typowanie jest tylko sugestią dla programisty


# ___________________________________________________________________________
# 2 wykonywać podstawowe operacje matematyczne na różnych typach danych np. łączenie list, konkatenacja stringów

"""Operacje na typach liczbowych:
+ - dodawanie,
- - odejmowanie
* - mnożenie
/ - dzielenie
** - potęgowanie
// - dzielenie bez reszty czyli 5//2 = 2 (floor division)
% - reszta z dzielenia (modulo) czyli 5%3 = 2 
"""
"""Operacje arytmetyczne na napisach(działaja tez na listach):
+ - konkatynacja np. 'fajny ' + 'napis' = 'fajny napis'
* - zwielokrotnienie napisu np. 'Ala '*3='Ala Ala Ala ' (bazowo napis*liczba)
"""


# ___________________________________________________________________________
# 3 funkcja type()
"""
funkcja type zwraca nam typ wartości podanej jako argument np. type(10) = <class 'int'>
"""

print(type("10"))


# ___________________________________________________________________________
# 4 wiedzieć podstawowe informacje o wyjątkach, umieć je czytać
"""
Wyjątki to sa bledy programu występujące zazwyczaj z powodu użycia funkcji w sposób nieprzewidzany przez tworce.
np. 'napis' + 10 da nam wyjątek TypeError: can only concatenate str (not "int") to str
"""
"""
Traceback (most recent call last):
File "F:\\Python_projects\\sda\\Zadania_podstawy\\25_11_2023\\quick_recap.py", line 60, in <module>
    'napis' + 10
TypeError: can only concatenate str (not "int") to str
informacje: 
Plik z ktorego został wyrzucony wyjątek, linijka w ktorej jest wyjatek, modul
    kod z linijki gdzie jest prawdopodobnie blad
typ błedu i krótki opis przyczyny
"""

# ___________________________________________________________________________
# 5 podstawowa obsługa PyCharma
"""
Opcja Run np. klikamy ppm na plik i klikamy opcje run <filename> lub na otwartym pliku: ctrl+shift+f10
Opcja Debug np. klikamy ppm na plik i klikamy opcje debug <filename>
"""

# ___________________________________________________________________________
# 6 podstawowa obsługa debuggera
"""
Aby uruchomic debugger musimy uruchomic plik w trybie "debug"
aby zatrzymac sie w konkretnej linijce programu nalezy postawic "break point" klikając na pole obok numeru linii
Progam wykona sie bez przerw do napotkania pierwszego break pointa. nastepniemozemy przchodzic dalej linjka po linijce:
    -Step over: przechodzi do nastepnej linijki wykonuje funkcje 
    -Step into: Wchodzimy do wewnatrz funkcji jezeli jest taka mozliowsc
    -Step into My Code: Wchodzimy do wewnatrz funkcji jezeli funkcja znajduje sie w naszym projekcie
    -Step Out: Wyjsc z fukcji na poziom wyzej.
    -Run To Cursor: wykonuje program do linijki w ktorej znajduje sie nasz kursor
    -Resume Program: wykonuje program az do następnego break pointa lub końca
"""


def fib(n: int):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


fib(10)
print("Hello")


# ___________________________________________________________________________
# 7 znajomość struktur danych takich jak lista, krotka, słownik i zbiór. W tym pojęcia mutowalności i składni list/dict/set comprehension
"""
Mutowalne(zmienialne):
    lista -> kolejność jest okreslona (jak wpisaliysmy tak bedzie)
    słownik-> kolejność jest okreslona (jak wpisaliysmy tak bedzie)
    zbior -> kolejność jest losowa(nie uporzadkowana)
Nie mutowalne(nie zmienialne):
    krotka-> kolejność jest okreslona (jak wpisaliysmy tak bedzie)
    frozen set -> kolejność jest losowa(nie uporzadkowana)
"""

# Mutowalnosc
lista = [1, 2, 3]
# mozemy dodac element do istnejacej listy
lista.append("10")
# lista sie zmienia
lista[0] = 152
print(lista)
"""
# Niemutowalne
krotka = (1, 2, 3)
krotka[0] = 152  # dostajemy blad TypeError: 'tuple' object does not support item assignment
print(krotka)
"""

# Tworzenie przez comprehension:
lista_comprehension = [element for element in range(0, 1000, 25)]
# Alternatywa z pętla:
lista_petla = []
for element in range(0, 1000, 25):
    lista_petla.append(element)
"""
składnia
[<element dodawany do listy> for <zmienna petli> in <kolekcja po ktorej iterujemy> (opcjonalnie) if <warunek dodania do nowej listy>]
"""
print(lista_comprehension)

# Słownik
slownik_comp = {
    f"d{key}": value * 2 for key, value in enumerate(lista_comprehension) if value > 500
}
print(slownik_comp)
print(type(slownik_comp))
"""
składnia
{<klucz dodawany do slownika>:<element dodawany do slownika> for <zmienna petli> in <kolekcja po ktorej iterujemy> (opcjonalnie) if <warunek dodania do nowej listy>}
"""

# zbior
set_comp = set(
    value * 2 for key, value in enumerate(lista_comprehension) if value > 500
)
set_comp = {value * 2 for key, value in enumerate(lista_comprehension) if value > 500}

print(set_comp)
print(type(set_comp))

# znajomość podstawowych metod obiektów typu list/dict/set

# list
lista.append(20)  # dodaj element do listy
lista.remove(20)  # usuwa element z listy (pierwsze jego wysta[ienei w liscie)
x = lista.pop()  # usuwa listy element o danym indexie lub ostatni i zwraca jego wartość
lista.insert(2, "")  # dodaje elemrnt do listy na konkretny numer indexu

# dict
slownik_comp.get(
    "key", ""
)  # wyciagnij wartośc dla zadanego klucza jezeli nie istnieje dostajmey None lub default
slownik_comp.update({"a": 1, "b": 2})  # rozszerza słownim o wartości z innego słownika
print(slownik_comp)

# set
set_comp.add(2)  # dodaje elemnt do zbioru
set_comp.remove(
    2
)  # usuwa elemnt ze zbioru dostaniemy wyjatek jezeli elementu nei ma w zbiorze
set_comp.discard(2)  # usuwa elemnt ze zbioru nie dosytaniemy bledu

# Set zawiera metody do opercaji an zbiorach np. union,difference,intersection

# instrukcje warunkowe, również zagnieżdżone, podstawy algebry boolowskiej

# składnia
"""
if <warunek>:
    'Wykonujemy jezeli spelniony jest <warunek> np. 5>2 = True'
    if:
        if:
            if:
                if:
    pass
elif <warunek2>:
    'wykonujemy jezeli nie spełni sie <warunek> a spełni się <warunek2>'
    pass
elif <warunek3>:
    'wykonujemy jezeli nie spełni sie <warunek>i<warunek2>  a spełni się <warunek3>'
    pass
elif <warunek4>:
    'wykonujemy jezeli nie spełni sie <warunek-3> a spełni się <warunek4>'
    pass
elif <warunek5>:
    'wykonujemy jezeli nie spełni sie <warune4> a spełni się <warunek5>'
    pass
else:
    'Wykonujemy jezeli poprzednie warunki sie nie spełnily.'
    pass
"""

"""
a and b
a\/b>| True  | False
--------------------
True | True  | False
False| False | False
"""
"""
a or b
a\/b>| True  | False
--------------------
True | True  | True
False| True  | False
"""
"""
not a
a     | not a
True  | False
False | True
"""

# sprawne używanie cięcia list
"""
Składnia:
lista[start:stop:step]
"""
lista = [1, 23, 4, 5, 6, 6, 7, 8, 9, 0, 4]
# piwszych 3 elementy
print(lista[:3])
# lista od 3 do 6 elementu
print(lista[2:6])
# lsita z korkiem co 2
print(lista[::2])
# jak odwrocic liste?
print(lista[::-1])


# znajomość argsów i kwargsów oraz wartości domyślnych
# Wartości domyślne
def f_1(a: int = 0, b: int = 0):
    return a + b


f_1()


# args
def sumuj(*args):
    # args to krotka z wartościami podanymi jako pozycyjny parametr funkcji
    suam = 0
    print("Argsy")
    print(args)
    for arg in args:
        suam += arg
    return suam


print(sumuj(1, 1, 1, 1, 1))
print(sumuj(1, 1))


# kwargs
def suma_skladnikow(**kwargs):
    # kwargs jest to słownik gdzie kluczem jest nazwa parametru a wartosvia jego wartość
    suma = 0
    print("Kwargsy")
    print(kwargs)
    for value in kwargs.values():
        suma += value
    return suma


print(suma_skladnikow(eggs=1, bread=2, carrot=1))

# umiejętność korzystania z importów np. funkcji random, pokazane słówko "as"
import random  # importujemy caly modul random do uzywania piszemy random.funkcja()

x = random.randint(0, 10)

from math import sqrt  # importuje wybrana funkcje z modułu

y = sqrt(10)

from datetime import *  # importujemy wszystkie funkcje z modulu datetime

c = time(10, 0, 0)
print(c)

import time as t  # importujemy caly modul time i zmieniamy jego nazwenictwo w naszym pliku

print("Im going to sleep")
# t.sleep(5)
print("I wakeup")

# iterowanie po kolekcjach (for, while)

"""składnia
while <warunek>:
    <instrukcje>
"""
i = 0
while i < 10:
    print(f"Iteracja {i}")
    i += 1

# for
"""skaldnia
for <zmienna> in <kolekcja>:
    <instrukcje>
"""
print("Petla for:")
for i in range(100):
    print(f"Iteracja for {i}")

# tak nie robimy:
lst = [1, 2, 3]
for i in lst:
    print(f"Element listy = {i}")
    # lst.remove(2)  # zmienianie kolekcji na ktorej pracujemy to nie najlepszy pomysl

# umiejętność zapisu i odczytu z pliku (w tym podstawowe tryby pracy z plikami)

"""tryby:
r - do odczytu
w - do zapisu (usuwa cala zawartosc pliku przed zapisem)
a - append do dopisywania do pliku
+ - otwarcie pliku zarowno do odczytu jaki do zapisu(np.r+)
b - tryb binarny
t - tryb teksowy (domyslny)
x - tryb tworzenia pliku
"""

# otwieranie plikow:

f = open("test_2.txt", "a")
f.write("\nSuper tekst")
f.close()  # close zapisuje dane do pliku na dysku.

with open("test_2.txt", "a") as f:
    f.write("\nContext manager wita")
    # Close wykonuje sie z automatu po zakonczenu bloku wcieca


# Tworzenie klas
class SuperPartia:
    def __init__(self, nazwa, ilosc_czlonkow):  # nazywana konstruktorem
        self.nazwa = nazwa
        self.ilosc_czlonkow = ilosc_czlonkow

    def przydziel_stanowisko(self, **kwargs):
        for stanowisko, osoba in kwargs.items():
            print(f"{osoba} dostaje stanowisko {stanowisko}")

    def wyraz_zdanie(self, partner_1, partner_2):
        if type(partner_1) == type(partner_2) and self.nazwa in [
            "Prawo i Sprawiedliwość",
            "Konfederacja",
        ]:
            print("To tzreba leczyc.")
        else:
            print("Spoko związek.")

    def __str__(
        self,
    ):  # reprezentacja napisowa naszej klasy gdy zostanie wywolana funkcja str() na obiekcie
        return f"Partia: {self.nazwa} ilosc czlonkow: {self.ilosc_czlonkow}"


super_partia_pis = SuperPartia("Prawo i Sprawiedliwość", 45000)
# print(super_partia_pis)
# super_partia_pis.przydziel_stanowisko(Formułowanie_Programu_Politycznego = "Jan Kowalski",Uczestnictwo_w_Wyborach="Jarek" )


# Dziedziczenie
class Human:
    def __init__(self, wzrost, waga):
        self.waga = waga
        self.wzorst = wzrost
        self.partner = None

    def komunikuj_sie(self):
        print("Człowiek sie komunikuje.")


class Woman(Human):
    def __init__(self, waga, wzrost, dlugie_wlosy: bool):
        super().__init__(wzrost, waga)
        self.dlugie_wlosy = dlugie_wlosy
        self.partner: Optional[Human] = None

    def change_partner(self, new_partner: Optional[Human] = None):
        if self.partner:
            self.partner.partner = None
        self.partner = new_partner
        self.partner.partner = self

    def __str__(self):
        dlugie_wlosy = "Długie włosy" if self.dlugie_wlosy else "Krótke włosy"
        return f"Kobieta waga: {self.waga} wzrost :{self.wzorst} {dlugie_wlosy}"


class Man(Human):
    def __init__(self, wzrost, waga, zarost: bool):
        super().__init__(wzrost, waga)
        self.zarost = zarost
        self.partner: Optional[Human] = None

    def change_partner(self, new_partner: Optional[Human] = None):
        if self.partner:
            self.partner.partner = None
        self.partner = new_partner
        self.partner.partner = self

    def __str__(self):
        zarost = "ma zarost" if self.zarost else "nie ma zarostu"
        return f"Męszczyzna waga: {self.waga} wzrost :{self.wzorst} {zarost}"


mezczyzne = Man(180, 80, True)
mezczyzna2 = Man(200, 100, False)
kobieta = Woman(55, 165, True)
mezczyzne.change_partner(mezczyzna2)

super_partia_pis.wyraz_zdanie(mezczyzne, mezczyzna2)
print(mezczyzne.waga)
print(mezczyzne.partner)
print(kobieta.partner)

# Modyfikowalne (mutable) i niemodyfikowalne (immutable) typy
# Oto krókie podsumowanie dzielące zmienne na modyfikowalne i niemodyfikowalne:

# Mutable
# Zawartość raz utworzonych zmiennych takiego typu, można modyfikować bez konieczności tworzenia nowej zmiennej - oszczędność pamięci, kolekcje te mogą być naprawdę duże, zwracanie za każdym razem nowej sekwencji mogłoby doprowadzić do problemów z pamięcią.

# ------- lista,
# ------- zbiór,
# ------- słownik.


# Immutable
# Zmiennych tego typu nie można modyfikować po utworzeniu, za każdym razem zostanie utworzony nowy byt.

# ------- int,
# ------- float,
# ------- bool,
# ------- str,
# ------- tuple,
# ------- frozenset.

"""Operacje na zbiorach: Python oferuje różne operacje na zbiorach, takie jak:

add(element): Dodaje element do zbioru.

remove(element): Usuwa element z zbioru. Generuje wyjątek, jeśli element nie istnieje.

discard(element): Usuwa element z zbioru, jeśli istnieje, a w przeciwnym razie nie powoduje błędu.

pop(): Usuwa i zwraca losowy element ze zbioru. Może być przydatny, gdy nie istnieje określony porządek w zbiorze.

clear(): Usuwa wszystkie elementy ze zbioru.

union(other_set): Zwraca nowy zbiór zawierający elementy z obecnego zbioru i innego zbioru.

intersection(other_set): Zwraca nowy zbiór zawierający elementy wspólne obecnego zbioru i innego zbioru.

difference(other_set): Zwraca nowy zbiór zawierający elementy, które występują w obecnym zbiorze, ale nie występują w innym zbiorze.

symmetric_difference(other_set): Zwraca nowy zbiór zawierający elementy, które występują w jednym z dwóch zbiorów, ale nie w obu.

issubset(other_set): Sprawdza, czy obecny zbiór jest podzbiorem innego zbioru.

issuperset(other_set): Sprawdza, czy obecny zbiór jest nadzbiorem innego zbioru.
"""
"""
"""
