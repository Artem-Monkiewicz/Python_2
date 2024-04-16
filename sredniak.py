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

# %%
