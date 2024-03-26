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
