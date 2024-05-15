# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ХОРОШИЙ ПРИМЕР
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def ArgumentEqualError(Exception):
    """Выбрасывается, когда делитель равен 0"""
    pass


def ArgumentNotIntegerError(Exception):
    """Выбрасывается, когда аргумент не является целым числом"""
    pass

    # try:
    #     return a // b
    # except ZeroDivisionError:
    #     print("Error!")
    #     return 0
    # except TypeError:
    #     print("Error!")
    #     return "TypeErrr"


def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentNotIntegerError("Аргументы должны быть целыми числами")
    if b == 0:
        raise ArgumentEqualError("Делитель не может быть равен 0")
    return a // b


# ZeroDivisionError: integer division or modulo by zero
if __name__ == "__main__":
    try:
        result = divide()
    except (ArgumentEqualError, ArgumentNotIntegerError) as exc:
        print(exc)
    finally:
        print("Finish")

# %%
if __name__ == "__main__":
    a = 5
    b = 0
    try:
        if b == 0:
            raise ValueError("b nie może być zerem!")
        result = a / b
        print(f"result{result}")
    except ZeroDivisionError:
        print("Nie dzieli  się przez zero!")
    finally:
        print("Finally")
print("Koniec")


# %%
class Exception_lich(Exception):
    pass


# Włąsne wyjątki przez tworzenie klasy Exception

if __name__ == "__main__":
    a = 5
    b = 0
    try:
        if b == 0:
            raise Exception_lich("b nie może być zerem!")
        result = a / b
        print(f"result{result}")
    except ZeroDivisionError:
        print("Nie dzieli  się przez zero!")
    finally:
        print("Finally")
print("Koniec")

# %% ZADANIE trójkąt
"""
- Stwórz funkcję taingle która przyjmie arguenty a,b,c.
- Funkcja ma zwrócić obwód trójkąta a,b,c
- Funkcja powinna sprawdzić czy a,b,c są liczbami int (MyValueError)
- Funkcja powinna sprawdzić czy można zbudować trójkąt z boków a,b,c
- a + b > c, a + c > b, b + c > a, a>0, b>c , c>0
- Jeżeli nie to wywołaj swój błąd TriangleError
- Napisz w main użycie tej funkcji z obsługą błędów
- a, b, c podaje użytkownik.
"""


class TriangleError(Exception):
    pass


class MyError(Exception):
    pass


class TriangleErrorZero(Exception):
    pass


class TriangleErrorMinus(Exception):
    pass


def triagle(a, b, c):
    try:
        int_a = int(a)
        int_b = int(b)
        int_c = int(c)
    except:
        raise MyError("Wartość jest niepotężna!")

    if not (int_a + int_b > int_c or int_a + int_c > int_b or int_b + int_c > int_a):
        raise TriangleError("To nie jest trójkąt!")
    if int_a == 0 or int_b == 0 or int_c == 0:
        raise TriangleErrorZero("To nie jest trójkąt! Podałęś zero(a).")
    if int_a < 0 or int_b < 0 or int_c < 0:
        raise TriangleErrorMinus("To nie jest trójkąt! Podałęś liczbe(y) ujęmne.")
    return int_a + int_b + int_c


if __name__ == "__main__":
    a = int(input("Podaj stronę a: "))
    b = int(input("Podaj stronę b: "))
    c = int(input("Podaj stronę c: "))

    try:
        print(f"Obwód trójkąta: {triagle(a, b, c)}")
    except (ValueError, TriangleErrorMinus, TriangleError, TriangleErrorZero, MyError):
        print("Podałęś złe wartości!")
# %% Zadanie kalkulator
"""
Zrób kalkulator:
- pobierz a i b
- operacje (+, -, *, /)
- przekonwertuj a i b na int.
Jeżeli się nie uda to masz poprosić go jeszcze raz
- sprawdz czy podał poprawną operację. Wywołaj wyjątek i go obsłuż
- wykonaj operację
"""


class NotIntError(Exception):
    """When number isn't Integer"""

    pass


class ZnakError(Exception):
    """When an operator function is specified incorrectly"""

    pass


def get_number(name):
    while True:
        try:
            value = int(input(f"Podaj {name}: "))
            break
        except NotIntError:
            print("Wartość jest zła!")
    return value


def get_op(op_list):
    while True:
        try:
            value = input(f"Podaj operacje: ")
            if value not in op_list:
                raise ZnakError("Błędny znak operacji! Może być tylko: +, -, *, /")
            break
        except ZnakError:
            print("Wartość jest zła! Błędny znak operacji! Może być tylko: +, -, *, /")
    return value


if __name__ == "__main_-":
    a = get_number("a")
    b = get_number("b")
    op = get_op(["+", "-", "*", "/"])

    if op == "+":
        print(f"Wynik to: {a + b}")
    elif op == "-":
        print(f"Wynik to: {a - b}")
    elif op == "*":
        print(f"Wynik to: {a * b}")
    elif op == "/":
        print(f"Wynik to: {a / b}")
# %% classes ABC

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_beep(self):
        pass


class BMW(Car):
    def __init__(self, name):
        self.name = name

    def get_beep(self):
        print("beep")


# %%


class BMW(Car):
    def __init__(self, name):
        self.__name = name

    def get_beep(self):
        print("beeep")

    def get_name(self):
        return "+++" + self.__name + "+++"

    def set_name(self, new_name):
        if new_name == "Beti" or new_name == "Auto":
            self.__name = new_name


# %%
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_beep(self):
        pass


class BMW(Car):
    def __init__(self, name):
        self.name = name

    def get_beep(self):
        print("beeep")

    def get_name(self):
        return "+++" + self.name + "+++"

    def set_name(self, new_name):
        if new_name == "Beti" or new_name == "Auto":
            self.name = new_name


class Audi(Car):
    def __init__(self, name):
        self.__name = name

    def get_beep(self):
        print("aaaaa")


class Mercedes(Car):
    def __init__(self, name):
        self.__name = name

    def get_beep(self):
        print("brrrr")


if __name__ == "__main__":
    my_cars = [BMW("car1"), Audi("car2"), Mercedes("car3"), BMW("car4")]
    for car in my_cars:
        car.get_beep()


# %% Zadanie employee
# plik employee
class Employee:
    def __init__(self, name, age, salary, title):
        self.name = name
        self.age = age
        self.salary = salary
        self.title = title
        pass

    def introduce_yourself(self):
        print(f"Hi, I am {self.name}")

    def salary_increase(self, value):
        self.salary += value


class Boss(Employee):
    def __init__(self, name, age, salary, title):
        super(Boss, self).__init__(name, age, salary, title)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def employees_salary_increase(self, value):
        for employee in self.employees:
            employee.salary_increase(value)


# plik main

from employee import Employee, Boss


if __name__ == ("__main__"):
    emp1 = Employee("emp1", 30, 5000, "eng.")
    emp2 = Employee("emp2", 23, 8000, "eng.")
    emp3 = Employee("emp3", 25, 7000, "eng.")
    boss = Boss("boss1", 50, 10000, "boss")
    boss.add_employee(emp1)
    boss.add_employee(emp2)
    boss.add_employee(emp3)

    for emp in boss.employees:
        emp.introduce_yourself()

    boss.employees_salary_increase(500)
    print(emp1.salary)


# %% _init_ and new(cls) #1
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initializing Singleton instance")


# Создаем два объекта класса Singleton
obj1 = Singleton()
obj2 = Singleton()

# obj1 и obj2 будут одним и тем же объектом
print(obj1 is obj2)  # True


# %% _init_
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)
print(person.name)  # Alice
print(person.age)  # 30

# %% __init__ дополнительная инииализация объяекта


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = None

    def set_year(self, year):
        self.year = year


car = Car("Toyota", "Corolla")
car.set_year(2020)
print(car.year)  # 2020

# %% new(cls)


class CustomList(list):
    def __new__(cls, *args, **kwargs):
        args = [2 * x for x in args]  # Умножаем все элементы на 2 при создании списка
        return super().__new__(cls, *args, **kwargs)


custom_list = CustomList([1, 2, 3])
print(custom_list)  # [2, 4, 6]


# %% new(cls) #2
class ImmutableTuple(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, sorted(args))  # Возвращаем отсортированный кортеж


immutable_tuple = ImmutableTuple(3, 1, 2)
print(immutable_tuple)  # (1, 2, 3)

# %% @staticmethod

"""
1. @staticmethod: Этот декоратор используется для определения статического метода в классе. 
Статические методы не требуют доступа к экземпляру объекта (self) или классу (cls) и могут быть вызваны как методы класса. 
Они могут быть полезны, когда операция не зависит от конкретного экземпляра класса.
"""


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


result = MathUtils.add(3, 5)
print(result)  # 8

# %% @classmethod

"""
2. @classmethod: Этот декоратор используется для определения метода класса, 
который принимает первым аргументом ссылку на класс (обычно обозначается как cls). 
Методы класса могут использоваться для создания новых экземпляров класса или для доступа к атрибутам класса.
"""


class Person:
    total_count = 0

    def __init__(self, name):
        self.name = name
        Person.total_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count


person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_total_count())  # 2


# %%
class Person:
    total_count = 0

    def __init__(self, name):
        self.name = name
        Person.total_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count


person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_total_count())  # 2

# %% .copy

my_dict = {"a": [1, 2, 2, 3], "b": [1, 3, 4, 5]}

my_copy = my_dict.copy()

my_dict["a"].append(4)

my_copy["b"].append(5)


print(my_dict)
print(my_copy)

# %% pickle  -> dump
from employee import Employee
import pickle

if __name__ == "__main__":
    name = input("podaj nazwe:")
    age = input("podaj wiek:")
    salary = input("podaj place")
    title = input("podaj tytul")

    emp1 = Employee(name, age, salary, title)
    print(emp1)

    with open("emp1.txt", "w") as f:
        pickle.dumps(emp1, f)

# %%

from employee import Employee
import pickle


def load_emp(file_name: str) -> Employee:
    with open(file_name, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    new_emp1 = load_emp("emp1.dat")
    print(new_emp1)

# %% class


class Person:
    pass


p1 = Person()
p1.name = "Elon"
p1.surname = "Smith"
p1.place_of_birth = "USA"

p2 = Person()
p2.name = "Sergei"
p2.surname = "Korolev"
p2.place_of_birth = "Belarus"

print(p1.name)

print(f"Name: {p1.name}, Nazwisko: {p1.surname}, Miasto: {p1.place_of_birth}.")

print(f"Name: {p2.name}, Nazwisko: {p2.surname}, Miasto: {p2.place_of_birth}.")


# %% self
class Person:
    def print_info(self, n):
        for i in range(n):
            print(
                f"Name: {self.name}, Surname: {self.surname}, Place of Birth: {self.place_of_birth}."
            )

    def get_age(self):
        actually_year = int(input("Please enter your actually year: "))
        age = actually_year - self.year_of_birth
        print(f"Your age is {age} years old.")


p1 = Person()
p1.name = "Elon"
p1.surname = "Smith"
p1.place_of_birth = "USA"
p1.year_of_birth = 1980

p2 = Person()
p2.name = "Sergei"
p2.surname = "Korolev"
p2.place_of_birth = "Belarus"
p2.year_of_birth = 1995

# 1
# p1.print_info(3)
# p2.print_info(5)

# 2
Person.print_info(p1, 3)
Person.print_info(p2, 5)

# get_age
p1.get_age()
p2.get_age()


# %% __init__
class Person:
    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth

    def print_info(self, n):
        for i in range(n):
            print(
                f"Name: {self.name}, Surname: {self.surname}, Place of Birth: {self.place_of_birth}."
            )

    def get_age(self):
        actually_year = int(input("Please enter your actually year: "))
        age = actually_year - self.year_of_birth
        print(f"Your age is {age} years old.")


p1 = Person("Elon", "Musk", "USA", 1994)
p2 = Person("Sergei", "Korolev", "Belarus", 1995)
p3 = Person("Albert", "Einstein", "Germany", 1979)

p1.print_info(1)
p2.print_info(1)
p3.print_info(1)


# %% Атрибут класса
class Circle:
    PI = 3.14  # Атрибут класса

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return self.radius * 2 * Circle.PI

    def get_area(self):
        return Circle.PI * self.radius**2


c1 = Circle(3)
print(c1.get_perimeter())
print(c1.get_area())

c2 = Circle(7)
print(c2.get_perimeter())
print(c2.get_area())


# %%
class Person:
    people_count = 0

    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth

        Person.people_count += 1

    def print_info(self, n):
        for i in range(n):
            print(
                f"Name: {self.name}, Surname: {self.surname}, Place of Birth: {self.place_of_birth}."
            )

    def get_age(self):
        actually_year = int(input("Please enter your actually year: "))
        age = actually_year - self.year_of_birth
        print(f"Your age is {age} years old.")


p1 = Person("Elon", "Musk", "USA", 1994)
p2 = Person("Sergei", "Korolev", "Belarus", 1995)
p3 = Person("Albert", "Einstein", "Germany", 1979)

p1.print_info(1)
p2.print_info(1)
p3.print_info(1)

print(Person.people_count)

# %% operations on files
import csv
import json


def print_menu(menu: dict):
    print("==================================")
    for option in menu.values():
        print(option)
    while True:
        result = input("Input option: ")
        for key in menu.keys():
            if result == str(key):
                print(f"Chosed option {key}")
                print("==================================")
                return key
        else:
            print("Invalid option. Please try again.")


def save_to_file():
    file_name = input("Enter file name: ")
    print(
        "You can write at this file. If you dont want to overwrite it, just write q!."
    )
    with open(file_name, "w") as f:
        while True:
            line = input()
            if line == "q!":
                break
            else:
                f.write(line + "\n")


def read_from_file():
    file_name = input("Enter file name: ")
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")


def save_to_file_csv():
    file_name = input("Enter file name: ")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("1; Michal; 45\n")
        f.write("1; Ala; 20\n")


if __name__ == "__main__":
    menu = {
        1: "1. Save file",
        2: "2. Load file",
        3: "3. Save file as .CSV",
        5: "5. Exit file",
    }

    with open("menu.txt", "w") as f:
        json.dump(menu, f, indent=4)
    # with open('menu.txt', 'r') as f:
    #     json.load(f)

    while True:
        menu_result = print_menu(menu)
        if menu_result == "1":
            save_to_file()
        elif menu_result == "2":
            read_from_file()
        elif menu_result == "3":
            save_to_file_csv()
        elif menu_result == "5":
            print("End of program")
            break

# funkc wewnętrzn


def select_gender(gender):
    def gender_male(name):
        print(f"Hello, I am {name}! I am a male person.")

    def gender_female(name):
        print(f"Hi, and I am {name}! I am a female person.")

    if gender == "male":
        return gender_male
    elif gender == "female":
        return gender_female


# program
if __name__ == "__main__":
    my_func = select_gender("male")
    my_func("Michał")


# %% Decoratory
def my_dec(func):
    def wrapper(*args, **kwargs):
        return "+++++" + func(*args, **kwargs) + "+++++"

    return wrapper


def my_name():
    return "Jestem Artem"


def say_hello(name):
    return f"Hello {name}"


# bez
print(my_name())
# z
print(my_dec(my_name)())
# arg
print(my_dec(say_hello)("Ola"))

# %% Stały decorator


def my_dec(func):
    def wrapper(*args, **kwargs):
        return "+++++" + func(*args, **kwargs) + "+++++"

    return wrapper


@my_dec
def my_name():
    return "Jestem Artem"


def say_hello(name):
    return f"Hello {name}"


# @ stały
print(my_name())
# z
# print(my_dec(my_name)())
# #arg
# print(my_dec(say_hello)("Ola"))

# %% Dekoratoe z argumentami

from datetime import datetime


def run_only_between(from_=10, to_=11):
    # Udekoruje tylko w określonych godzinach
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()

        return wrapper

    return dec


@run_only_between(10, 11)
def say_something():
    print("Hello World")


print(say_something())

# %% Manager kontekstu


class SecretData:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print("ENTER")
        return list(reversed(self.data))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")
        print(f" TYPE: {exc_type}, VAL: {exc_val}, TB: {exc_tb}")
        for i in range(len(self.data)):
            self.data[i] = 0
        return True


with SecretData([34, 12, 22, 24]) as data:
    print(data)
    a = 3 / 0
print("PO SECRETDATA")

# Menager kontekstu #2
import contextlib


@contextlib.contextmanager
def my_func():
    print("part1")
    print("part2")
    print("part3")
    yield 1


with my_func() as result:
    print(result)

# Menager kontekstu #3
from contextlib import contextmanager


@contextmanager
def my_func(value):
    print(f"part{value}")
    yield value


with my_func(1) as result:
    print(result)
with my_func(2) as result:
    print(result)
with my_func(3) as result:
    print(result)

#%% Dziedziczenie
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        super().__init__(imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


os1 = Osoba("Henryk", 54)
os2 = Pracownik("Jacek", 36, 20, 160)
os3 = Student("Agata", 22, 1000)
print(os1)
print(os2)
print(os3)

#%%
class A:
    pass


class B(A):
    pass


class C:
    pass


class D(C):
    pass


class E(B, C, D):
    pass


print(E.mro())


#%%
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

#%%
from abc import ABC, abstractmethod
    from math import pi


    class Figura(ABC):
        @abstractmethod
        def obwod(self):
            pass

        @abstractmethod
        def pole(self):
            pass

    class Prostokat(Figura):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def obwod(self):
            return 2 * (self.a + self.b)

        def pole(self):
            return self.a * self.b


    class Kolo(Figura):
        def __init__(self, r):
            self.r = r

        def obwod(self):
            return 2 * self.r * pi

        def pole(self):
            return pi * self.r ** 2
        
    prostokat = Prostokat(3, 5)
    kolo = Kolo(12)
    print(prostokat.obwod())
    print(kolo.obwod())

store_name = "Shopshoe"
item_name = "Running shoes"
item_price = 100.00
item_discount = 0.30

discounted_price = item_price * (1 - item_discount)

message = (
    f"Welcome to {store_name}!\n"
    f'{"-" * 50}\n'
    f"Today's special is the {item_name}, which normally costs "
    f"${item_price:.2f}.\nBut for a limited time, you can get it "
    f"for ${discounted_price:.2f} ({item_discount:.0%} off)!"
)

print(message)


brand = "Ford"
model = "Mustang"
year = "2021"
color = "Red"
mileage = "5000"

print('CAR DETAILS')
print(f'Make: {brand}')
print(f'Model: {model}')
print(f'Year: {year}')
print(f'Color: {color}')
print(f'Mileage: {mileage} miles')

experiment_name = 'The Effects of Temperature on Enzyme Activity'
treatment_group = 'Group A'
enzyme_activity = 12.3456

print(f'Welcome to {experiment_name}!')
print(f'The {treatment_group} enzyme activity level is {enzyme_activity:.2f} units.')

item1 = 'Apples'
quantity1 = 5
price1 = 1.50

item2 = 'Bananas'
quantity2 = 7
price2 = 0.99

item3 = 'Oranges'
quantity3 = 4
price3 = 2.25

empty_pipe = "|" + "-" *15
print(empty_pipe*3, end="|\n")

print(f'| {item1}        | {quantity1}             | ${price1:.2f}         |')
print(f'| {item2}       | {quantity2}             | ${price2:.2f}         |')
print(f'| {item3}       | {quantity3}             | ${price3:.2f}         |')

item1 = 'Apple'
quantity1 = 10
price1 = 1.50

item2 = 'Banana'
quantity2 = 5
price2 = 0.75

item3 = 'Cherry'
quantity3 = 20
price3 = 0.25

line = "+" + "-" * 9 + "+" + "-" * 13 + "+" + "-" * 11 + "+"

dane1 = "Item"
dane2 = "Quantity"
dane3 = "Price"

print(line)
print(f"| {dane1:<7} | {dane2:<11} | {dane3:<9} |")
print(line)
print(f"| {item1:<7} | {quantity1:<11} | ${price1:<8.2f} |")
print(f"| {item2:<7} | {quantity2:<11} | ${price2:<8.2f} |")
print(f"| {item3:<7} | {quantity3:<11} | ${price3:<8.2f} |")
print(line)


line = "=" * 50
menu = "> Main Menu"
line1 = "1. View all products"
line2 = "2. Search for a product"
line3 = "3. Add a new product"
line4 = "5. Delete a product"
line5 = "7. Checkout"
line6 = "8. Exit"


print(line)
print(menu)
print(line)
print(f'\t{line1}\n\t{line2}\n\t{line3}\n\t{line4}\n\t{line5}\n\t{line6}')

ring = 5
PI = 3.14
print(f'The area of the circle is: {PI*ring**2} cm2')

prc = 0.03
kwota = 1000
okres = 5

inwest = kwota * (1+prc) ** okres

print(f'The final value of the investment is: {inwest:.2f} PLN')


num_of_cars = 100
num_of_parts = 1000
cost_per_part = 10

# Enter your solution here
total_cost = num_of_cars*num_of_parts*cost_per_part
avg_cost_per_car = total_cost/num_of_cars

print('Total cost of manufacturing all the cars: ', total_cost)
print('Average cost per car:', avg_cost_per_car)

num_of_cars = 100
num_of_parts = 1000
cost_per_part = 10

# Enter your solution here
total_cost = num_of_cars*num_of_parts*cost_per_part
avg_cost_per_car = total_cost/num_of_cars

print('Total cost of manufacturing all the cars: ', total_cost, sep='')
print('Average cost per car: ', avg_cost_per_car, sep= "")


num_of_users = 9045
num_of_posts = 54822
num_of_likes = 251561

avg_posts_per_user = num_of_posts / num_of_users
avg_likes_per_post = num_of_likes / num_of_posts

print(f'Average number of posts per user: {avg_posts_per_user:.2f}')
print(f'Average number of likes per post: {avg_likes_per_post:.2f}')

employee_id = 123451612
username_number = employee_id % 10001
username_suffix = str(username_number)
username = 'user_' + username_suffix
print(username)

total_num_posts = 47
posts_per_page = 10

pg = total_num_posts / posts_per_page

print(f'The total number of pages required to display all the posts is: {round(pg)}')

file_name = 'view.jpg'
# Enter your solution here

print(f'The file extension of the file "{file_name}" is: {file_name[5:8]}')

#%%
import urllib.request
import ssl
import codecs
import json


def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method="GET")
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read().decode()
        else:
            return False
    return content


def get_data_from_url(url, file_name):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method="GET")
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read()
        else:
            return False

    with open(file_name, "wb") as f2:
        f2.write(content)
    return True


def get_text_from_url(url, file_name):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method="GET")
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read().decode("unicode")
            print(content)
        else:
            return False

    with open(file_name, "w") as f2:
        f2.write(content)
    return True


if __name__ == "__main__":
    # get_data_from_url('https://bilingual-kid.com/wp-content/uploads/2019/07/Bolek-i-Lolek.png', 'bolek.png')
    # get_data_from_url('https://onet.pl', 'onet.html')

    json_data = json.loads(
        get_from_url("https://api.nbp.pl/api/exchangerates/rates/a/chf?format=json")
    )

    zloty = float(input("Podaj wartość[PLN]"))
    kurs = float(json_data["rates"][0]["mid"])
    print(f"{zloty}[PLN] = {zloty/kurs}[CHF] po kursie {kurs}")

#%%



