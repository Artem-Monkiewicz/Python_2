print("Zadanie 28")
empty_list_a = []
empty_dictionary = {}
empty_krotka = ()
print(empty_list_a, type(empty_list_a))
print(empty_dictionary, type(empty_dictionary))
print(empty_krotka, type(empty_krotka))

print("ZAdanie 29")
list1 = ["Notebook", "Monitor", "Mouse", "Qwerty", 1]
print(list1)

dictionaty_1 = {
    "Notebook": "Hp Pavilion",
    "Monitor": "HP LE1851w",
    "Mouse": "Microsoft Windows Mouse",
    "Qwerty": "Microsoft Sculpture Qwerty",
    "Ilość": "1",
}
print(dictionaty_1)

krotka1 = ("Notebook", "Monitor", "Mouse", "Qwerty")
print(krotka1)

# LISTY
print("ZAdanie 30")
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)

print("ZAdanie 31")
print(lst[1])

print("ZAdanie 32")
lst1 = [11, 100, 101, 999, 1001]
answer_2_1 = lst1[-1]
print("Ostatni element v1")
print(answer_2_1)
answer_2_2 = lst1[4]
print("Ostatni element v2")
print(answer_2_2)
answer_2_3 = lst1[len(lst1) - 1]
print("Ostatni element v3")
print(answer_2_3)

print("ZAdanie 33")
gift_list = ["socks", "4K drone", "vine", "jam"]
print(gift_list)
gift_list.append("pajamas")
print(gift_list)

print("ZAdanie 34")
gift_list.pop(4)
print(gift_list)

# Dodawanie- append
print(gift_list)
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)
gift_list.pop(4)
print(gift_list)

print("ZAdanie 35")
print(gift_list)
gift_list.insert(2, "slippers")
print(gift_list)

print("ZAdanie 36")
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_3 = lst.index(8679)
print(answer_3)

print("ZAdanie 37")
lst2 = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
# v1
# lst2.remove(99)
# v2 -ZADZIAŁA ZAWSZE
# lst2.pop()
# v3 - ZADZIAŁA JEŻELI ELEMENTY SĄ UNIKALNE
lst2.remove(lst[-1])
print(lst2)

print("ZAdanie 38")
lst3 = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst3.reverse()
print(lst3)
# v2
lst4 = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
lst_reversed = list(reversed(lst4))
print(lst_reversed)

print("ZAdanie 39")
lst4 = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_4 = lst4.count(6)
print(answer_4)

print("ZAdanie 40")
print("SUMA")
lst5 = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_5 = sum(lst5)
print(answer_5)

print("ZAdanie 41")
lst6 = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
answer_6a = min(lst6)
print(answer_6a, "Najmniejszy")
answer_6b = max(lst6)
print(answer_6b, "Największy")
# v2
lst6.sort()
ans_a_v2 = lst6[0]
ans_b_v2 = lst6[-1]
print(f"Minimum: {ans_a_v2}")
print(f"Maximum: {ans_b_v2}")

# Słowniki

print("ZAdanie 43")

dict = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}
ans_a = dict["born"]
print(f"Palto urodził sie w roku: {ans_a}")
dict["born"] = -428
print(f'Palto urodził sie w roku: {dict["born"]}')

print("ZAdanie 44")
dict1 = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}
dict1["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict1)

print("ZAdanie 45")
dict = {
    "son’s name": "Lucas",
    "son’s eyes": "green",
    "son’s height": 32,
    "son’s weight": 25,
}
dict["son’s height"] += 2
print(dict)
print(dict["son’s height"])

print("ZAdanie 46")
dict = {
    "son’s name": "Lucas",
    "son’s eyes": "green",
    "son’s height": 32,
    "son’s weight": 25,
}
answ1 = list(dict.items())
print(answ1, type(answ1))


print("ZAdanie 47")
dict = {
    "son’s name": "Lucas",
    "son’s eyes": "green",
    "son’s height": 32,
    "son’s weight": 25,
}
answer_7 = dict.get("son’s eyes")
print(answer_7)
answer_8 = print(dict.get("son's age", "2"))

print("ZAdanie 48")

dict = {
    "son’s name": "Lucas",
    "son’s eyes": "green",
    "son’s height": 32,
    "son’s weight": 25,
}

dict.clear()
print(dict)

print("ZAdanie 49")
dict = {
    "son’s name": "Lucas",
    "son’s eyes": "green",
    "son’s height": 32,
    "son’s weight": 25,
}
anw = len(dict)
print(anw)
