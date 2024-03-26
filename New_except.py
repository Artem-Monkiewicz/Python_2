"""
Zrób kalkulator:
- pobierz a i b
- operacje (+, -, *, /)
- przekonwertuj a i b na int.
Jeżeli się nie uda to masz poprosić go jeszcze raz
- sprawdz czy podał poprawną operację. Wywołaj wyjątek i go obsłuż
- wykonaj operację
"""


# %%
class NotInt(Exception):
    pass


class ZnakError(Exception):
    pass


def get_number(name):
    while True:
        try:
            value = int(input(f"Podaj {name}: "))
            break
        except:
            print("Wartość jest zła!")


def get_op(op_list):
    while True:
        try:
            value = input(f"Podaj operacje: ")
            if value not in op_list:
                raise ZnakError("Błędny znak operacji! Może być tylko: +, -, *, /")
                break
        except:
            print("Wartość jest zła! Błędny znak operacji! Może być tylko: +, -, *, /")
    return value


# if __name__ == "__main_-":
a = get_number("a")
b = get_number("b")
op = get_op(["+", "-", "*", "/"])


# if not a or b = type(int)
#     raise('Nie podałeś poprawnej liczby!')

#     znak = input('Podaj typ operacji (+, -, *, /): ')

# if not znak = "+" or "-" or "*" or "/":
#     print(znak)
#     raise ZnakError("")

# if znak = "+":
#     print (a+b)
# if znak = "-":
#     print (a-b)
# if znak = "*":
#     print (a*b)
# if znak = "/":
#     print (a/b)

# #%%

# def get_number(name):
#     while True:
#         try:
#             value = int(input(f'podaj {name}:'))
#             break
#         except:
#             print('Podana wartosc jest zla!')
#     return value


# def get_op(op_list):
#     while True:
#         try:
#             value = input(f'podaj operacje:')
#             if value not in op_list:
#                 raise ValueError()
#             break
#         except:
#             print('Podana wartosc jest zla!')
#     return value


# if __name__ == '__main__':
#     a = get_number('a')
#     b = get_number('b')
#     op = get_op(['+', '-', '*', '/'])

#     if op == '+':
#         print(f'Wynik to: {a + b}')
#     elif op == '-':
#         print(f'Wynik to: {a - b}')
#     elif op == '*':
#         print(f'Wynik to: {a * b}')
#     elif op == '/':
#         print(f'Wynik to: {a / b}'

# %%
