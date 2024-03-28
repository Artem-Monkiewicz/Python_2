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
# %%
