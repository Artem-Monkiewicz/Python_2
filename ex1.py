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
