# -*- coding: utf-8 -*-

# строковые префикры u и r. u- интерпретатор utf; r - буквальное печатание
# print("Привет, мир !")
# print("Привет вновь !")
# print("Мне нравится это печатать.")
# print("Ура, я пеатаю!")
# print("Это весело!")
# print("Это занятие как 'волшебство'.")
# print('Я бы "сказал", что это очень круто!')
# # 1
# print("Tu coś nowego")

# # %%
# # what does the program do
# print("Я подсчитаю свою живность")
# # number of chickens
# print("Куры", 25 + 30 / 6)
# # number of roosters
# print("Петухи", 100 - 25 * 3 % 4)
# # number of eggs
# print("А теперь подсчитаю яйца:")
# # stupid example
# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# # question 1
# print("Верно ли, что 3+2<5-7")
# # answer 1
# print(3 + 2 < 5 - 7)
# # question 2
# print("Сколько будет 3+2?", 3 + 2)
# # answer 2
# print("А сколько будет 5-7?", 5 - 7)
# # doubts
# print("Ой, я, кажется, запутался... Почему False?")
# # request
# print("Еще раз посчитаю...")
# # question 3
# print("Это больше?", 5 > -2)
# # question 4
# print("А это больше или равно?", 5 >= -2)
# # question 5
# print("А это меньше или равно?", 5 <= -2)

# # %%
# cars = 100
# space_in_a_car = 4
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers

# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("В наличии", cars, "автомобилей")
# print("И только ", drivers, "вышло на работу")
# print("Получается, что", cars_not_driven, "машин пустует")
# print("Мы можем перевести сегодня", carpool_capacity, "человек")
# print("В каждой машине будет примерно", average_passengers_per_car, "человека")

# # %%
# print("FULLBODY")

# my_name = "Artem"

# print(f"Let's say about a human by name %s.")


# # %%
# def func(a, b=5, c=10):
#     print("a =", a, "| b =", b, "| c =", c)


# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

# # %%
# num = 23
# guess = int(input("Введите число: "))
# if guess == num:
#     print("You won!")
# elif guess < num:
#     print("So close <:")
# else:
#     print("So close <:")
# print("End.")


# # %%
# def total(a=5, *num, **phonebook):
#     print(a)

#     for item in num:
#         print(num)

#     for first, second in phonebook.items():
#         print(first, second)


# print(total(10, 1, 2, 4, Jack=1223, John=2231, Max=2654))

# # %%
# age = 20
# message = f"I am {age} years old."
# print(message)

# # %%
# lng = "Python"
# wrs = "3.10"

# std = f"Learning {lng} {wrs}"
# print(std)

# # %%
# price = 199.99

# print(f"The item costs $ {price}.")
# # %%
# price = 69.99
# discount = 0.1

# cena = price - (price * discount)
# r_cena = round(cena, 2)

# print(f"The item costs {r_cena} PLN")

# # %%
# product_name = "Shoe"
# price = 49.99
# in_stock = True

# print(
#     f"""
# Product Name: {product_name}
# Price: $ {price}
# Is Available: {in_stock}
# """
# )

# # or
# product_name = "Shoe"
# price = 49.99
# in_stock = True

# print("Product Name:", product_name)
# print("Price: $", price)
# print("Is Available:", in_stock)

# # %%
# units_used = 150
# cost_per_unit = 0.15
# total_cost = units_used * cost_per_unit

# print("units used:", units_used)
# print("cost per unit: $", cost_per_unit)
# print("total cost: $", total_cost)
# # %%
# version = "1.0.1"
# separator = "-" * 40

# print(separator)
# print(f"VERSION: {version}")
# print(separator)

# # %%
# data = "01-01-2021"
# mail1 = "jannowak@poczta.com"

# autor_pr = f"author: {mail1}"
# date_pr = f"date: {data}"
# simp_sep = "=" * 40

# print(simp_sep)
# print(f"{autor_pr} \n{date_pr}")
# print(simp_sep)
# # %%
# store_name = "Shopshoe"
# item_name = "Running shoes"
# item_price = 100.00
# item_discount = 0.30
# sep = "=" * 50

# discounted_price = item_price * (1 - item_discount)

# message = (
#     f"Welcome to {store_name}!\n"
#     f"{sep}\n"
#     f"Today's special is the {item_name}, which normally costs "
#     f"${item_price:.2%}.\nBut for a limited time, you can get it "
#     f"for ${discounted_price:.2f} ({item_discount:.0%} off)!"
# )

# print(message)
# %%
# a= 2
# b= 3
# c= 4
# sum = a + b + c
# arithmetic_average= sum//3
# print(arithmetic_average)
# print(type(result))
# result = 2==2 or 1!=1 #True #False =>
# result = bool()
# print(result)

# imie = ("Zorro")
# liczba = 40
# licba2 = 42.2
# napis = "abc"
# log = True
# wiek_osoby = liczba
# print(wiek_osoby)
# liczba3 = int(licba2)
# print(liczba3)
# liczba4 = float(liczba)
# print(liczba4)
# print(f'Hello,{imie}!')

# Napisz program, który wyświetli na ekranie informację o tym, czy wartość zmiennej jest podzielna przez 7

# wartosc = int(input('podaj wartosc: '))
# if wartosc % 7 == 0:
#     print('Wartosc dzieli się na 7')
# else:
#     print("Wartość nie dzieli na 7")

# Napisz program, który wyświetli na ekranie napis "Wartość zmiennej jest nieparzysta", jeżeli wartość zmiennej jest nieparzysta, w przeciwnym razie wyświetli na ekranie napis "Podana wartość jest parzysta"

# wartosc = int(input("Podaj wartosc: "))
# if wartosc % 2 == 0:
#     print('Wartosc parzysta')
# else:
#     print('Wartosc nieparzysta')

# Napisz program, który wyświetli na ekranie informację o tym, czy wartość zmiennej jest podzielna przez 7, przez 5, czy przez 3. Jeżeli wartość zmiennej nie jest podzielna przez żadną z liczb wyświetli stosowny komunikat.
# wartosc = int(input("Wpisz wartosc: "))
# if wartosc %5 == 0:
#     print('wartosc dzieli sie na 5')
# elif wartosc %3 == 0:
#     print('wartosc dzieli sie na 3')
# elif wartosc %7 == 0:
#     print('wartosc dzieli sie na 7')
# else:
#     print('wartosc dziwna')

# Napisz program, który dla podanej zmiennej wyświetli:
# różnicę pomiędzy wartością tej zmiennej, a liczbą 17, jeżeli różnica ta wynosi mniej niż 17,
# kwadrat tej różnicy, w przeciwnym wypadku.

# wartosc = int(input('Podaj wartosc: '))
# wartosc_17 = wartosc - 17
# if wartosc_17 > 17:
#     print(f'Twoja wartosc >17, to: {wartosc_17}')
# else:
#     print(f'Twoja wartosc <17, to: {wartosc}')

# Napisz program, który zwróci sumę trzech podanych liczb. Jeżeli wszystkie trzy liczby są równe zwróci potrójną wartość ich sumy.
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# c = int(input('Podaj c: '))
#
# x = a + b + c
# x3 = sum((a, b, c))**3
# if a ==b and a == c:
#     print(f'Podane wartosci rowne sobie! suma x3: {x3}')
# else:
#     print(f'Podane wartosci nie rowne sobie! suma: {x}')

# %% pętle
# x = 0
# while x < 5:
#     x = x + 1
# print(x)

# Napisz program, który wyświetli wszystkie liczby naturalne z przedziału 0, 50.
# x = 0
# while x <= 50:
#     print(x)
#     x += 1

# Napisz program, który wyświetli wszystkie liczby parzyste z przedziału 0, 100.
# x = 0
# while x<=100:
#     print(x)
#     x+=2

# Napisz program, który wyświetli na ekranie kwadraty wszystkich liczb całkowitych z przedziału 0, 10.
# x = 0
# while x<=10:
#     print(x**2)
#     x+=1

# Korzystając z pętli, wypisz liczby od -20 do 20. Następnie wypisz:
# 6 pierwszych liczb
# 6 ostatnich liczb
# wszystkie parzyste liczby
# wszystkie liczby oprócz cyfry 5
# wszystkie liczby do cyfry 7 włącznie
# wszystkie liczby podzielne przez 3
# sumę wszystkich liczb
# sumę liczb większych lub równych 4
# wszystkie liczby oraz ich potęgi
# wszystkie liczby oraz ich wartości modulo 10

# 1
# x = -20
# while x<=20:
#     print(x)
#     x+=1
# #2
# count = 0
# while count<6:
#     print(x)
#     x+=1
#     count+=1
# 3
# while count<6:
#     print(x*-1)
#     x-=1
#     count+=1
# 4
# while x<=20:
#     if x%2==0:
#         print(x)
#     x+=1
# 5
# while x<=20:
#     if x !=5:
#         print(x)
#     x+=1
# 6
# while x <= 7:
#     print(x)
#     x +=1
# 7
# while x <= 20:
#     print(x // 3)
#     x += 1
# 8
# x = -20
# count = 0
# while x <= 20:
#     print(x)
#     count += x
#     x += 1
#
# print(f'sum = {count}.')
# 9
# while x <= 20:
#     if x >= 4:
#         count += x
#     x += 1
#
# print(f'sum = {count}.')
# 10
# while x <= 20:
#     print(x, x**2, x**3, x**4, x**5, x**6)
#     x += 1

# 11
# while x <= 20:
#     print(x, x%10)
#     x += 1

# Napisz program, który wyświetli liczby będące wielokrotnością 5 i podzielne przez 7 z przedziału 1500-2700
# num = 1500
# end_num = 2700
#
# while num <= end_num:
#     if num % 5 == 0 and num % 7 == 0:
#         print(num)
#     num += 1

# Napisz program, który wypisze na ekranie liczby od 0 do 6 z pominięciem 3 i 6.
# x = 0
# x_end = 6
# while x < x_end:
#     if x != 3 and x != 6:
#         print(x)
#     x+=1

# %%
# Podsumowanie części pierwszej
# W tym miejscu kończymy omawianie podstawowych elementów składniowych języka Python. Informacje przedstawione w pierwszej części wystarczą do napisania dowolnie złożnego programu. Każdy istniejący obecnie program komputerowy, gra czy portal internetowy, mogą zostać napisane za pomocą samych typów, operatorów, instrukcji przypisania, warunków i pętli.

# Napisz program, który dla zadanej listy wyświetli kolejno wszystkie jej elementy razem z ich typami. Dla listy
# a_list = [4, True, None]
# program powinien wyświetlić wynik:

# 4 <class 'int'>
# True <class 'bool'>
# None <class 'NoneType'>
# Dana jest tablica 10 elementowa: a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]. Napisz program, który wypisze:

# wszytkie cyfry,

# 6 pierwszych cyfr,

# 6 ostatnich cyfr,

# wszystkie parzyste cyfry,

# wszystkie cyfry na nieparzystych indeksach,

# wszystkie cyfry oprócz cyfry 5,

# wszystkie cyfry do cyfry 7 włącznie,

# wszystkie cyfry podzielne przez 3,

# sumę wszystkich cyfr,

# sumę cyfr większych lub równych 4,

# najmniejszą i największą cyfrę.

# Napisz program, który dla zadanej liczby słów, np: a_list = [kot, elementarz, okno, komputer] wyświetli kolejne elementy listy razem z informacją o długości tych elementów.

# Napisz program, który dla zadanej listy słów, np:

# list_of_words = ["spam", "stół", "spam", "brązowy", "powietrze", "malware", "spam", "koniec"]
# wyświetli tylko te elementy listy, które nie mają wartości "spam". Ponadto jeżeli element listy ma wartość "malware" program powinien natychmiast przerwać działanie. Użyj instrukcji break. Informacji o działaniu instrukcji break poszukaj w internecie.


# Napisz program, który dla zadanej listy wyświetli kolejno wszystkie jej elementy razem z ich typami.
# a_list = [4, True, None]
# a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
#
# #1
# # print(a_list)
#
# #2
# # print(a_list[0:6])
# #3
# # print(a_list[4:10])
# #4
# # a_list_par = [num for num in a_list if num % 2 == 0]
# # print(a_list_par)
# #5
# # a_list_nie = [a_list[i] for i in range(0, len(a_list)) if i % 2 != 0]
# # print(a_list_nie)
#
# #or przez WHILE
#
# # niep_list = []
# # i = 1
# # while i < len(a_list):
# #     niep_list.append(a_list[i])
# #     i += 2
# # print(niep_list)
#
# #6
# # for item in a_list:
# #     print(item)
# # for item in a_list:
# #     if item %2 == 0:
# #         print(item)
# # print(a_list[5:-1])
# # for i in a_list:
# #     if i%2==0:
# #         print(i)
# # print(a_list[1::2])
# # for i in a_list:
# #     if i != 5:
# #         print(i, end=' ')
# print(a_list)

# %% class

# class Pies:
#     def __init__(self, name, is_hungry):
#         self.name = name
#         self.is_hungry = is_hungry
#     def szczekaj(self):
#         print("Hau, hau")
#     def jedz(self):
#         if self.is_hungry == True:
#             self.is_hungry = False


# pies1 = Pies("Burek", True)
# pies1.is_hungry
# pies1.jedz()
# pies1.is_hungry


# class Person:
#     def __init__(self, name, srname, gender, age, pesel):
#         self.name = name
#         self.srname = srname
#         self.gender = gender
#         self.age = age
#         self.pesel = pesel
#     def pens(self):
#         if self.gender == 'M' and self.age >= 65:
#             print('Yes, this man is retired')
#         elif self.gender == 'F' and self.age >= 60:
#             print('Yes, this woman is a pensioner')
#         else:
#             print('No, this person is not retired')
#     def age_difference(self, other_person):
#         diff = abs(self.age - other_person.age)
#         return diff

# %%
# f -строки

# header1 = "Name"
# header2 = "Age"
# name = "John"
# age = 22

# print(f"| {header1:10} | {header2:10} |")
# print("-" * 27)
# print(f"| {name:10} | {age:10} |")


# # Zmiana sposobu wyswietlania zmiennej
# n = 109.2345654324
# print(f"{n:.3f}")  # wyswietli 109.234

# procent = 0.71
# print(f"{procent:.1%}")  # wyswietli 71.0%

# %%
# def print_hello(text: str) -> None:
#     print(f"Hello {text}")


# print_hello("world")


# def add(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result


# # print(add(1, 2, 3, 4, 5))


# def print_name_and_something(name, *strings):
#     print(f"Imię: {name}")
#     for string in strings:
#         print(string)


# print_name_and_something("Jack", "a", "b", "c", "d")

# %%
# from math import pi

# hippizape_radius = 28
# hippizape_price = 22

# swiatpizzy_radius = 28
# swiatpizzy_price = 29

# nocnapizz_radius = 33
# nocnapizz_price = 29


# def area(radius, price):
#     area = pi * radius * radius
#     return area / price


# area1 = area(hippizape_radius, hippizape_price)
# area2 = area(swiatpizzy_radius, swiatpizzy_price)
# area3 = area(nocnapizz_radius, nocnapizz_price)

# print(area1)
# print(area2)
# print(area3)


# %%
class Parent:
    def say_hello(self):
        print("Привет от родительского класса!")


class Child(Parent):
    def say_hello(self):
        super().say_hello()
        print("Привет от дочернего класса!")


c = Child()
c.say_hello()


# %%
class BankAccount:

    def __init__(self, number, sum):
        self.account_number = number
        self.balance = sum
        print(f"Создан счет. Начальный баланс: {sum} единиц")

    def add(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} единиц")

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum} единиц")
        else:
            print("Недостаточно средств на счете")


acc1 = BankAccount("123456577", 1000)
acc1.add(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)

# %%
# from dataclasses import dataclass
#
# @dataclass
# class Prostokat():
#     a: int
#     b: int
#
#     def obwod(self):
#         return 2 * (self.a + self.b)
#
#     def pole(self):
#         return self.a * self.b
#
# p1 = Prostokat(3,4)
# p2 = Prostokat(5,6)
# print(p1)
# print(p1 == p2)


class Prostokat:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"Prostokat(a={self.a}, b={self.b})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Prostokat) and self.a == other.a and self.b == other.b

    def obwod(self) -> float:
        return 2 * (self.a + self.b)

    def pole(self) -> float:
        return self.a * self.b


P1 = Prostokat(2, 3)
P2 = Prostokat(2, 4)
print(P1.obwod)
print(P1.pole())

# %%
import time


def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.2f} секунд")

    return wrapper


@timing_decorator
def some_long_running_function():
    time.sleep(5)
    print("Функция завершила работу")


some_long_running_function()


# %%
def upper(string):
    return string.upper()


i = ["one", "two", "three"]

newlist = list(map(upper, i))
newlist2 = list(str.upper() for str in i)

print(newlist)
print(newlist2)

# %%
items = [
    1,
    2,
    3,
    4,
    5,
]

# odds = list(filter(lambda x: x % 3, items))

# print(odds)

from functools import reduce

items_sum = reduce(lambda x: x % 3, items)
print(items_sum)

# %%
# from dataclasses import dataclass
#
# @dataclass
# class Prostokat():
#     a: int
#     b: int
#
#     def obwod(self):
#         return 2 * (self.a + self.b)
#
#     def pole(self):
#         return self.a * self.b
#
# p1 = Prostokat(3,4)
# p2 = Prostokat(5,6)
# print(p1)
# print(p1 == p2)


class Prostokat:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"Prostokat(a={self.a}, b={self.b})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Prostokat) and self.a == other.a and self.b == other.b

    def obwod(self) -> float:
        return 2 * (self.a + self.b)

    def pole(self) -> float:
        return self.a * self.b


P1 = Prostokat(2, 3)
P2 = Prostokat(2, 4)
print(P1.obwod)
print(P1.pole())

# %%
string = "1 0 0 1 0 1"
str2 = int(string[::2], 2)
print(f"The found number is: {str2}")

# %%
input_text = "Python Course"
result = input_text[::-1]
print(f'The reversed text of "Python Course" is: {result}')


# %%
# Original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# First three elements: [0, 1, 2]
# Last three elements: [7, 8, 9]

all_num = list(range(0, 10))
three_first_num = list(all_num[0:3])
three_last_num = list(all_num[-3:])

print(f"Original list: {all_num}")
print(f"First three elements: {three_first_num}")
print(f"Last three elements: {three_last_num}")

# %%
personnel = [
    "John Smith, Private First Class",
    "Jane Doe, Captain",
    "Bob Johnson, Sergeant",
]

# Enter your solution here
pers1 = personnel[2]
pers2 = pers1[0:11]
print(str(pers2))
# or

personnel = [
    "John Smith, Private First Class",
    "Jane Doe, Captain",
    "Bob Johnson, Sergeant",
]

# Enter your solution here
pers1 = personnel[2][:11]
print(str(pers1))

# %%
stock_prices = [
    102.3,
    103.4,
    105.6,
    108.2,
    109.7,
    112.4,
    113.6,
    115.2,
    116.8,
    119.1,
    121.3,
    122.5,
    124.7,
    126.1,
    127.4,
    129.2,
    130.4,
    132.6,
    133.8,
    135.1,
    136.3,
]

# Enter your solution here
x = stock_prices[:5]
y = stock_prices[-5:]
first_p = sum(x) / 5
sec_p = sum(y) / 5

# first_p =
# sec_p =


print(f"Average stock price for the first week: ${first_p:.2f}")
print(f"Average stock price for the last week: ${sec_p:.2f}")


# %%
parts = [
    ["50x20x1.5", "25x10x1.0"],
    ["55x22x1.8", "30x15x1.2"],
    ["60x24x2.0", "35x20x1.5"],
]

# # Enter your solution here
# l - długośc
# w - szerokość
# t - grubość

# float

part_that_i_need = str(parts[1][:1])

corrected_arg = str(part_that_i_need.replace("x", ""))
print(corrected_arg)

l = float(corrected_arg[2:4])
w = float(corrected_arg[4:6])
t = float(corrected_arg[6:9])

print(f"length = {l}")
print(f"width = {w}")
print(f"height = {t}")


# %%
# %% 1

import random

random_numbers = [random.randint(-999, 999) for number in range(100)]
print(len(random_numbers))

print_numbers = [f"{number} -> {number**2}\n" for number in random_numbers]

with open("liczby_kwadratowe.txt", "w") as file:
    file.writelines(print_numbers)
    # for number in random_numbers:
    # file.write(f"{number} -> {number**2}\n")
    # print(f"{number} -> {number**2}", file=file)

file.close()
print("Koniec")


# %% 2
with open("Liczby_kwadratowe.txt", "a+") as f:
    f.write("Cos dopisane\n")
    f.seek(0)
    content = f.read()


print(content)

# %% 3 najdłuższe słowo w pliku

with open("slowa.txt") as f:
    content = f.read()  # Cały tekst jako napis
    slowa = content.split()  # pojedyncze słowa
    najdluzsze = max(slowa, key=len)
    print(najdluzsze)

# %%

import threading


def iterate_print(iter):
    for item in iter:
        print(item)


if __name__ == "__main__":
    # tworzenie wątków
    t1 = threading.Thread(
        target=iterate_print, args=(range(5),)
    )  # wypisywanie kolejnych liczb naturalnych
    t2 = threading.Thread(
        target=iterate_print, args=("Python",)
    )  # wypisywanie kolejnych znaków napisu

    # uruchomienie wątków
    t1.start()
    t2.start()

    # czekanie z wykonaniem dalszego kodu, aż oba wątki się zakończą
    t1.join()
    t2.join()

    print("Done!")


# %%
class Employee:
    def __init__(self, name, age, salary, title):
        self.name = name
        self.age = age
        self.salary = salary
        self.title = title

    def introduce_yourself(self):
        return f"Hello, I'm Employee! My name {self.name}, I'm {self.age} years old, and my title is {self.title} and my salary is $ {self.salary}"

    def salary_incrise(self, increase):
        self.salary += increase
        return f"Now my salary is $ {self.salary}"


class Boss(Employee):
    def __init__(self, name, age, salary, title):
        super().__init__(name, age, salary, title)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def increase_salaries(self, increase):
        for employee in self.employees:
            employee.salary_increase(increase)

    def introduce_yourself(self):
        return super().introduce_yourself() + "And I am a boss!"


# main

from employee import Employee, Boss

employee1 = Employee("John", 20, 5000, "Programmer")
employee2 = Employee("Jane", 30, 10000, "Manager")
employee3 = Employee("Puma", 50, 2500, "Engineer")
employee4 = Employee("Nike", 42, 3558, "Elektroman")
employee5 = Employee("Sam", 25, 5000, "Engineer")

boss = Boss("Rebook", 19, 550000, "Boss")

boss.add_employee(employee1)
boss.add_employee(employee2)
boss.add_employee(employee3)
boss.add_employee(employee4)
boss.add_employee(employee5)

print(employee1.introduce_yourself())
print(employee2.introduce_yourself())
print(employee3.introduce_yourself())
print(employee4.introduce_yourself())
print(employee5.introduce_yourself())
print(boss.introduce_yourself())

boss.increase_salaries(5000)

print(employee1.introduce_yourself())
print(employee2.introduce_yourself())
print(employee3.introduce_yourself())
print(employee4.introduce_yourself())
print(employee5.introduce_yourself())
print(boss.introduce_yourself())


# %%
from dataclasses import dataclass, field


@dataclass
class Employee:
    name: str
    age: int
    salary: int
    title: str

    def introduce_yourself(self):
        return (
            f"Hello, I'm {self.name}, I have {self.age} y.o., my salary: ${self.salary}"
        )

    def salary_increase(self, increase):
        self.salary += increase
        return f"My new salary is: ${self.salary}"


@dataclass
class Boss(Employee):
    employees: list = field(default_factory=list)

    def add_employee(self, employee):
        self.employees.append(employee)

    def increase_salary(self, increase):
        for employee in self.employees:
            employee.salary_increase(increase)

    def introduce_yourself(self):
        return super().introduce_yourself() + " And I am a boss!"


# main.py
from employee import Employee, Boss

# Создаем сотрудников
employee1 = Employee("Иван", 30, 50000, "инженер")
employee2 = Employee("Анна", 28, 55000, "дизайнер")
employee3 = Employee("Сергей", 35, 60000, "разработчик")

# Создаем босса
boss = Boss("Алексей", 45, 100000, "директор")

# Босс добавляет сотрудников
boss.add_employee(employee1)
boss.add_employee(employee2)
boss.add_employee(employee3)

# Все представляются
# print(employee1.introduce_yourself())
# print(employee2.introduce_yourself())
# print(employee3.introduce_yourself())
# print(boss.introduce_yourself())

# Босс повышает зарплату всем сотрудникам
boss.increase_salary(15000000)

# Все снова представляются
print(employee1.introduce_yourself())
print(employee2.introduce_yourself())
print(employee3.introduce_yourself())


# %%
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(self, imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        super().__init__(self, imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


class PracujacyStudent(Pracownik, Student):
    def __init__(self, imie, wiek, stawka, liczba_godzin, stypendium):
        Pracownik.__init__(self, imie, wiek, stawka, liczba_godzin)
        Student.__init__(self, imie, wiek, stypendium)

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin + self.stypendium


os1 = Osoba("Henryk", 54)
os2 = Pracownik("Jacek", 36, 20, 160)
os3 = Student("Agata", 22, 1000)
os4 = PracujacyStudent("Monika", 24, 9.5, 70, 550)
print(os1)
print(os2)
print(os3)
print(os4)

# %%
none_var = None
bool_var1 = False
bool_var2 = True

# Enter your solution here

print(f"The type of none_var is: {type(none_var)}")
print(f"The type of bool_var1 variable is: {type(bool_var1)}")
print(f"The type of bool_var2 variable is: {type(bool_var2)}")

# %%
my_flag = False

if type(my_flag) is bool:
    print("The variable is of boolean type: True")

# %%
followers = ["john", "jane", "jacob", "jessica", "jenny"]
profile_picture = "https://example.com/profile.jpg"
post_ids = [1, 2, 3, 4, 5]
bio = "Travel enthusiast | Photographer | Nature lover"
timestamp = 1649499360

print(type(followers))
print(type(profile_picture))
print(type(post_ids))
print(type(bio))
print(type(timestamp))

# <class 'list'>
# <class 'str'>
# <class 'list'>
# <class 'str'>
# <class 'int'>
# %%
followers = ["john", "jane", "jacob", "jessica", "jenny"]
profile_picture = "https://example.com/profile.jpg"
post_ids = [1, 2, 3, 4, 5]
bio = "Travel enthusiast | Photographer | Nature lover"
timestamp = 1649499360

# Enter your solution here

cond_a = tuple
cond_b = str
cond_c = list
cond_d = set
cond_e = float


if type(followers) is cond_a:
    print(True)
else:
    print(False)

if type(profile_picture) is cond_b:
    print(True)
else:
    print(False)

if type(post_ids) is cond_c:
    print(True)
else:
    print(False)

if type(bio) is cond_d:
    print(True)
else:
    print(False)

if type(timestamp) is cond_e:
    print(True)
else:
    print(False)

# %%
followers = ["john", "jane", "jacob", "jessica", "jenny"]
profile_picture = "https://example.com/profile.jpg"
post_ids = [1, 2, 3, 4, 5]
bio = "Travel enthusiast | Photographer | Nature lover"
timestamp = 1649499360

print(isinstance(followers, tuple))
print(isinstance(profile_picture, str))
print(isinstance(post_ids, list))
print(isinstance(bio, set))
print(isinstance(timestamp, float))

# %%
my_text = "python is a popular programming language."

my_text2 = my_text.capitalize()

print(my_text2)
# %%
my_text = "python is a popular programming language."

p_in_text = my_text.count("p")

print(f"The character 'p' occurs {p_in_text} times in the text.")
# %%
code1 = "FVNISJND-XX-2024"
code2 = "FVNISJND-XY-2023"
x = code1[12:16]
y = code2[12:16]

text1 = "Does code1 end with '2024'? "
text2 = "Does code2 end with '2024'? "

xy = x == "2024"
yx = y == "2024"

print(f"{text1}{xy}")
print(f"{text2}{yx}")
# %%
path1 = "youtube.com/watch?v=5EhRztVxums"
path2 = "google.com/search?q=car"

g = path1.startswith("youtube")
d = path2.startswith("youtube")

print(f"path1: {g}")
print(f"path2: {d}")
# %%
base = "https://e-smartdata.teachable.com/p/"
path1 = base + "sciezka-data-scientist-machine-learning-engineer"
path2 = base + "sciezka-data-scientist-deep-learning-engineer"
path3 = base + "sciezka-bi-analyst-data-analyst"

print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")
# %%
code1 = "FVNISJND-20"
code2 = "FVNISJND20"

x = code1.isalnum()
y = code2.isalnum()

print(f"Is code1 alphanumeric? {x}")
print(f"Is code2 alphanumeric? {y}")
# %%
text = "Google Colab"
print(text.lower())
# %%
text = "Google Colab"
print(text.upper())
# %%
text = "  Google Colab   "
print(text.strip())
# %%
text = "340-23-245-235"
print(text.replace("-", ""))
# %%
text = "Open,High,Low,Close"
print(text.split(","))
# %%
text = """Python is a general purpose language.
Python is popular."""
print(text.splitlines())
# %%
num = 34
padded_num = str(num).zfill(6)
print(padded_num)
# %%
url = (
    "https://e-smartdata.teachable.com/p/sciezka-data-scientist"
    "-machine-learning-engineer"
)
n = url[36:85]
h = n.replace("-", " ")
print(h)
# %%
url = (
    "https://e-smartdata.teachable.com/p/sciezka-data-scientist"
    "-machine-learning-engineer"
)
n = url[36:85]
h = n.replace("-", " ")
print(h)
# %%
seat_assignment = " 24a "
gate_announcement = "Boarding for flight UA 123 has begun."
gate_number = "B12"
cities = ["New York", "Los Angeles", "Chicago"]

clean_seat_assignment = seat_assignment.strip()
updated_announcement = gate_announcement.replace("Boarding", "Departing")
uppercase_seat = clean_seat_assignment.upper()
terminal = gate_number.replace("12", "")
gate = gate_number.replace("B", "")
cities_string = ", ".join(cities)


print(clean_seat_assignment)
print(updated_announcement)
print(uppercase_seat)
print(terminal)
print(gate)
print(cities_string)
# %%
seat_map_header = "SEAT MAP"
row1 = ["A1", "B1", "C1", "D1", "E1", "F1"]
row2 = ["A2", "B2", "C2", "D2", "E2", "F2"]

row_slash = "-" * 10
row_slash2 = "-" * 9
header = row_slash + seat_map_header + row_slash2
seat_row1 = f"{row1[0]} - {row1[1]} - {row1[2]} | {row1[3]} - {row1[4]} - {row1[5]}"
seat_row2 = f"{row2[0]} - {row2[1]} - {row2[2]} | {row2[3]} - {row2[4]} - {row2[5]}"
print(header)
print(seat_row1)
print(seat_row2)
# %%
seat_map_header = "SEAT MAP"
row1 = ["A1", "B1", "C1", "D1", "E1", "F1"]
row2 = ["A2", "B2", "C2", "D2", "E2", "F2"]

row1_string = " - ".join(row1[:3]) + " | " + " - ".join(row1[3:])
row2_string = " - ".join(row2[:3]) + " | " + " - ".join(row2[3:])

centered_header = seat_map_header.center(27, "-")

print(centered_header)
print(row1_string)
print(row2_string)
# %%
seat_assignment = "Seat 24A"
boarding_group = "Group C"
delay_time = "30 mins"
baggage_weight = "23 kg"

clean_seat_assignment = seat_assignment[5:8]
clean_boarding_group = boarding_group[-1]
clean_delay_time = delay_time[:2]
clean_baggage_weight = baggage_weight[:2]

print(clean_seat_assignment)
print(clean_boarding_group)
print(clean_delay_time)
print(clean_baggage_weight)
# %%
seat_assignment = "Seat 24A"
boarding_group = "Group C"
delay_time = "30 mins"
baggage_weight = "23 kg"

clean_seat_assignment = seat_assignment.removeprefix("Seat ")
clean_boarding_group = boarding_group.removeprefix("Group ")
clean_delay_time = delay_time.removesuffix(" mins")
clean_baggage_weight = baggage_weight.removesuffix(" kg")

print(clean_seat_assignment)
print(clean_boarding_group)
print(clean_delay_time)
print(clean_baggage_weight)
# %%
gate_number = "B12"
flight_number = "123"
seat_assignment = "24A"

padded_num1 = str(gate_number).zfill(4)
padded_num2 = str(flight_number).zfill(6)
padded_num3 = str(seat_assignment).zfill(4)
print(padded_num1)
print(padded_num2)
print(padded_num3)
# %%
subjects = {"mathematics", "polish"}

subjects.add("english")

print(subjects)
# %%
text = "Programming in python."
vowels = {"a", "e", "i", "o", "u"}

tex_low = text.lower()
tex_space = tex_low.replace(" ", "").replace(".", "")
tex_set = set(tex_space)
nw_set = tex_set.difference(vowels)
print(len(nw_set))
# %%
text = "Programming in python."
vowels = {"a", "e", "i", "o", "u"}

tex_low = text.lower()
tex_space = tex_low.replace(" ", "").replace(".", "")
tex_set = set(tex_space)
nw_set = tex_set.difference(vowels)
print(f"Number of consonants: {len(nw_set)}")
# %%
set_A = {2, 4, 6, 8}
set_B = {4, 10}

print(f"Symmetric difference: {set_A.symmetric_difference(set_B)}")
# %%
ad1_ids = {"001", "002", "003"}
ad2_ids = {"002", "003", "007"}

sim_dif = ad1_ids.symmetric_difference(ad2_ids)
print(f"Selected IDs: {sim_dif}")
# %%
clicked_ids = {"9001", "9002", "9005"}
bought_ids = {"9002", "9004", "9005"}

id = clicked_ids.intersection(bought_ids)
print(f"Customer IDs: {id}")
# %%
flights = {"AA100", "UA200", "DL300", "WN400"}
booked_flights = {"AA100", "WN400"}
available_flights = flights - booked_flights
# %%
daily_menu = {
    "burger",
    "fries",
    "hot dog",
    "chicken sandwich",
    "pasta with seafood",
}
fixed_vegetarian_options = {
    "fries",
    "onion rings",
    "pasta with seafood",
    "feta salad",
}
vegetarian_menu = daily_menu.intersection(fixed_vegetarian_options)
# %%
wig20 = ("CDR", "PKO", "PEO")
mwig40 = ("PLW", "AMC", "BFT")

# Enter your solution here
w = (wig20, mwig40)
# %%
members = (("Kasia", 23), ("Tomek", 19))
new_members = (members[0], ("Adam", 26), members[1])
print(new_members)
# %%
default_settings = ("YES", "NO", "NO", "YES", "NO")
x = default_settings.count("YES")
print(f'Number of occurrences of "YES": {x}')
# %%
names = ("Monika", "Tomek", "Adam", "Olaf")
x = sorted(names)
print(tuple(x))
# %%
info = (("Monika", 19), ("Tomek", 21), ("Adam", 18), ("Jarek", 30))

asc_info = tuple(sorted(info, key=lambda item: item[1]))
desc_info = tuple(sorted(info, key=lambda item: item[1], reverse=True))

print(f"Ascending: {asc_info}")
print(f"Descending: {desc_info}")
# %%
stocks = [("Playway", ("PLW", 310)), ("CD Projekt", ("CDR", 300))]

print(stocks[0][1][0])
# %%
objectives1 = ("Secure the perimeter", "Neutralize enemy targets")
objectives2 = ("Provide medical assistance", "Evacuate civilians")

coordinates1 = ((35.6895, 139.6917), (34.0537, -118.2424))
coordinates2 = ((40.7128, -74.0060), (51.5074, -0.1278))

p1 = objectives1 + coordinates1
p2 = objectives2 + coordinates2

print(f"First mission: {p1}")
print(f"Second mission: {p2}")
# %%
ranks = (
    "Private",
    "Corporal",
    "Sergeant",
    "Lieutenant",
    "Captain",
    "Major",
    "Colonel",
)
num_ranks = len(ranks)
major_index = ranks.index("Major")
colonel_present = "Colonel" in ranks

print(num_ranks)
print(major_index)
print(colonel_present)
# %%
cities = ["Warszawa", "Łódź", "Kraków"]
cities.append("Gdańsk")

print(cities)
# %%
idx = ["001", "002", "001", "003", "001"]
print(f'Occurrences count: {idx.count("001")}')
# %%
text = "Programowanie w języku Python"
text = text.lower()
text = text.replace("ę", "e")
text1 = list(set(text))
text1.remove(" ")
text1.sort()

print(text1[:10])
# %%

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
