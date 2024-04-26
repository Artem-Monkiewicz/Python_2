# -*- coding: utf-8 -*-

# строковые префикры u и r. u- интерпретатор utf; r - буквальное печатание
print("Привет, мир !")
print("Привет вновь !")
print("Мне нравится это печатать.")
print("Ура, я пеатаю!")
print("Это весело!")
print("Это занятие как 'волшебство'.")
print('Я бы "сказал", что это очень круто!')
# 1
print("Tu coś nowego")

# %%
# what does the program do
print("Я подсчитаю свою живность")
# number of chickens
print("Куры", 25 + 30 / 6)
# number of roosters
print("Петухи", 100 - 25 * 3 % 4)
# number of eggs
print("А теперь подсчитаю яйца:")
# stupid example
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# question 1
print("Верно ли, что 3+2<5-7")
# answer 1
print(3 + 2 < 5 - 7)
# question 2
print("Сколько будет 3+2?", 3 + 2)
# answer 2
print("А сколько будет 5-7?", 5 - 7)
# doubts
print("Ой, я, кажется, запутался... Почему False?")
# request
print("Еще раз посчитаю...")
# question 3
print("Это больше?", 5 > -2)
# question 4
print("А это больше или равно?", 5 >= -2)
# question 5
print("А это меньше или равно?", 5 <= -2)

# %%
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("В наличии", cars, "автомобилей")
print("И только ", drivers, "вышло на работу")
print("Получается, что", cars_not_driven, "машин пустует")
print("Мы можем перевести сегодня", carpool_capacity, "человек")
print("В каждой машине будет примерно", average_passengers_per_car, "человека")

# %%
print("FULLBODY")

my_name = "Artem"

print(f"Let's say about a human by name %s.")


# %%
def func(a, b=5, c=10):
    print("a =", a, "| b =", b, "| c =", c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)

# %%
num = 23
guess = int(input("Введите число: "))
if guess == num:
    print("You won!")
elif guess < num:
    print("So close <:")
else:
    print("So close <:")
print("End.")


# %%
def total(a=5, *num, **phonebook):
    print(a)

    for item in num:
        print(num)

    for first, second in phonebook.items():
        print(first, second)


print(total(10, 1, 2, 4, Jack=1223, John=2231, Max=2654))

# %%
age = 20
message = f"I am {age} years old."
print(message)

# %%
lng = "Python"
wrs = "3.10"

std = f"Learning {lng} {wrs}"
print(std)

# %%
price = 199.99

print(f"The item costs $ {price}.")
# %%
price = 69.99
discount = 0.1

cena = price - (price * discount)
r_cena = round(cena, 2)

print(f"The item costs {r_cena} PLN")

# %%
product_name = "Shoe"
price = 49.99
in_stock = True

print(
    f"""
Product Name: {product_name}
Price: $ {price}
Is Available: {in_stock}
"""
)

# or
product_name = "Shoe"
price = 49.99
in_stock = True

print("Product Name:", product_name)
print("Price: $", price)
print("Is Available:", in_stock)

# %%
units_used = 150
cost_per_unit = 0.15
total_cost = units_used * cost_per_unit

print("units used:", units_used)
print("cost per unit: $", cost_per_unit)
print("total cost: $", total_cost)
# %%
version = "1.0.1"
separator = "-" * 40

print(separator)
print(f"VERSION: {version}")
print(separator)

# %%
data = "01-01-2021"
mail1 = "jannowak@poczta.com"

autor_pr = f"author: {mail1}"
date_pr = f"date: {data}"
simp_sep = "=" * 40

print(simp_sep)
print(f"{autor_pr} \n{date_pr}")
print(simp_sep)
# %%
store_name = "Shopshoe"
item_name = "Running shoes"
item_price = 100.00
item_discount = 0.30
sep = "=" * 50

discounted_price = item_price * (1 - item_discount)

message = (
    f"Welcome to {store_name}!\n"
    f"{sep}\n"
    f"Today's special is the {item_name}, which normally costs "
    f"${item_price:.2%}.\nBut for a limited time, you can get it "
    f"for ${discounted_price:.2f} ({item_discount:.0%} off)!"
)

print(message)
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
#%%
5. **Функции:**
- Объявление функции с помощью def.
    - Функции могут принимать аргументы и возвращать значения.

7. **Методы строк:**
- upper(), lower(), split(), join(), replace() и другие.

8. **Обработка исключений:**
try:
# код, который может вызвать исключение
except ТипИсключения as e:
# обработка исключения


9. **Модули:**
- Импортирование модулей с помощью import.
- Установка сторонних модулей через pip.

### Полезные ссылки:
- Официальная документация Python: https://docs.python.org/3/
- Курс "Learn Python" на Codecademy: https://www.codecademy.com/learn/learn-python

#%%
Podsumowanie części pierwszej
W tym miejscu kończymy omawianie podstawowych elementów składniowych języka Python. Informacje przedstawione w pierwszej części wystarczą do napisania dowolnie złożnego programu. Każdy istniejący obecnie program komputerowy, gra czy portal internetowy, mogą zostać napisane za pomocą samych typów, operatorów, instrukcji przypisania, warunków i pętli.

Napisz program, który dla zadanej listy wyświetli kolejno wszystkie jej elementy razem z ich typami. Dla listy
a_list = [4, True, None]
program powinien wyświetlić wynik:

4 <class 'int'>
True <class 'bool'>
None <class 'NoneType'>
Dana jest tablica 10 elementowa: a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]. Napisz program, który wypisze:

wszytkie cyfry,

6 pierwszych cyfr,

6 ostatnich cyfr,

wszystkie parzyste cyfry,

wszystkie cyfry na nieparzystych indeksach,

wszystkie cyfry oprócz cyfry 5,

wszystkie cyfry do cyfry 7 włącznie,

wszystkie cyfry podzielne przez 3,

sumę wszystkich cyfr,

sumę cyfr większych lub równych 4,

najmniejszą i największą cyfrę.

Napisz program, który dla zadanej liczby słów, np: a_list = [kot, elementarz, okno, komputer] wyświetli kolejne elementy listy razem z informacją o długości tych elementów.

Napisz program, który dla zadanej listy słów, np:

list_of_words = ["spam", "stół", "spam", "brązowy", "powietrze", "malware", "spam", "koniec"]
wyświetli tylko te elementy listy, które nie mają wartości "spam". Ponadto jeżeli element listy ma wartość "malware" program powinien natychmiast przerwać działanie. Użyj instrukcji break. Informacji o działaniu instrukcji break poszukaj w internecie.


#Napisz program, który dla zadanej listy wyświetli kolejno wszystkie jej elementy razem z ich typami.
a_list = [4, True, None]
