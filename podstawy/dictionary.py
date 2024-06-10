# Słownik
phonebook = {}

# Dodać elementy
phonebook["Jack"] = 1111111
phonebook["Sarah"] = 222222

print(phonebook)
print(phonebook["Jack"])

# Definicja gotowego słownika
phonebook2 = {"John": 333333, "Dizee": 444444}
print(phonebook2)

# Przykład słownika
human = {}

human["name"] = "Maciej"
human["height"] = 180
human["weight"] = 90

print(human)

human_2 = {
    "name": "Maciej",
    "height": 180.5,
    "weight": 90.5,
    "Hobby": ["Vieo games", "programming", "mountain trips"],
}
print(human_2)
#
print(human_2.get("Hobby"))

# usuwanie elementu ze slownika v1
del human_2["Hobby"]
print(human_2)
# usuwanie elementu ze slownika v2
x = human_2.pop("weight")
print(human_2)
# %%
# 25/11/2023
Text = "Artem"
print(Text)
