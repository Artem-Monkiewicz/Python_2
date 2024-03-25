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
