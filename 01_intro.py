# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:21:04 2023

@author: Lich Rave
"""
# First comment

# %%

print("training from scratch, day 25 (25.03.24)")
print(2 + 2)
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 // 3

# %%
2**5

# %%
a = 10
b = 20

c = a * b

# %%
print(c)

# %%
print("love python")

# %%
import os

os.getcwd()

# %%
print(
    """
Instrukcja uruchamiania pliku przyklad.py

   --file [nazwa pliku]
        zapisuje output do pliku
        
   --quiet
        wycisza logi w konsoli
Koniec."""
)


# %%
text = "I love Python. "
print(text)
print(text * 3)
print("hau..." * 8)
print("*" * 30)

# %%
"Python"
"Py" "thon"
print("Py" "thon")

# %%

# %%
print("statement to be printed", end="white space or any character or string ")


# %%
if __name__ == "__main__":
    a = 5
    b = 0
    try:
        result = a / b
        print(f"result{result}")
    except:
        print("nie dziel na zero!")
    finally:
        print("Koniec")

# %%
