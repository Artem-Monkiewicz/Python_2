# decorator
def make_pretty(func):
    def inner():
        func()
        print("Smsh decorated")

    return inner


# funkcja do decorowania
def ordinary1():
    print("I am ordinary1")


def ordinary2():
    print("I am ordinary2")


# ordinary()
decorated_func_call_1 = make_pretty(ordinary1)
decorated_func_call_1()


decorated_func_call_2 = make_pretty(ordinary2)
decorated_func_call_2()


# z małpką
def decorate_cake(func):
    def some_cake():
        func()
        print("I am decorated your cake")

    return some_cake


@decorate_cake
def sponge_cake():
    print("I am simple sponge cake")


sponge_cake()


# decorator
def smart_divide(func):
    def inner(a, b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            print("Cannot divide")
            return
        return func(a, b)

    return inner


# funkcja do decoracji
@smart_divide
def divide(a, b):
    print(a / b)


divide(3, 4)
divide(5, 0)
# %%
# Zadanie
# Napisz program który będzie uczył mini kultury. Jeśli napisze ktoś imię z Małej litery,to nie wyświetli powitania,a jeśli z wielkiej, to napisze przewitanie


# decorator
def cult(func):
    print("Cóż, dawaj sprawdzimy twój poziom kultury...")

    def resur(*args):
        for arg in args:
            if arg[0].isupper():
                func(*args)
                print("Fajny poziom kultury masz!")
                return
            print("Coś nie poszło ci...")

    return resur


# program
@cult
def hello_say(name):
    print(f"Hi, {name}")


hello_say("piotr")


# %% Singleton - jedna instancja - jeden obiekt. BIBLIOTEKA - singleton_decorator
def singleton(instance):
    created_instances = {}

    def get_instance(*args, **kwargs):
        if instance not in created_instances:
            created_instances[instance] = instance(*args, **kwargs)
        return created_instances[instance]

    return get_instance


@singleton
class OlaDuda:
    def __init__(self):
        print("Ola D with such look and character is only one!")


# args
# "ola" - *args
# kwargs
# name = 'ola' - **kwargs

ola_duda_1 = OlaDuda()
print(ola_duda_1)

ola_duda_2 = OlaDuda()
print(ola_duda_2)

# bez singletona
# <__main__.OlaDuda object at 0x0000026BE54387D0>
# <__main__.OlaDuda object at 0x0000026BE54384D0>

# z singletonem
# <__main__.OlaDuda object at 0x000001A3E42387D0>
# <__main__.OlaDuda object at 0x000001A3E42387D0>

# Metaclasses - controluje zachowanie class


# %% Fabryka - Abstract Factory - button
class Button:
    html = ""

    def get_html(self):
        return self.html


class Submit(Button):
    html = '<button type="submit"></button>'


class Radio(Button):
    html = '<button type="radio"></button>'


class Check(Button):
    html = '<button type="multiselect"></button>'


class ButtonFactory:
    def create_button(self, type):
        target_class = type.capitalize()
        return globals()[target_class]()


button_factory = ButtonFactory()
button = input("Podaj, jakiego buttona chcesz(radio, check lub submit): ")
print(button_factory.create_button(button).get_html())

# %%
