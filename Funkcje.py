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
