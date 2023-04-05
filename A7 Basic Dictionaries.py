from copy import deepcopy
oceny_all = [[1, 2, 3, 5, 2, 3], [6, 6, 6], [3, 3, 4]]

oceny_slownik = {}
oceny_slownik["Marek"] = [1, 2, 3, 5, 2, 3]
oceny_slownik["Kozak"] = [6, 6, 6]
print(oceny_slownik["Marek"])
print(oceny_slownik["Kozak"])

for imie, oceny in oceny_slownik.items():
    print(imie, oceny)

for oceny in oceny_slownik.values():
    print(oceny)

for student in oceny_all:
    for ocena in student:
        print(ocena, end=' ')
    print()

oceny_2 = deepcopy(oceny_all)
oceny_2[0][0] = 123
print(oceny_all)
print(oceny_2)
# print(oceny_all[0][4])