oceny = [4, 5, 3, 2, 1, 6, 4, 3, 6, 5, 2, 1, 4, 5, 1]
#oceny = set(oceny)
#print(oceny)
oceny = list(set(oceny))
print(oceny)


oceny_marka = [1, 2, 3, 2, 3, 1, 1, 2, 1]
oceny_kozaka = [6, 5, 6, 4, 6, 3, 4, 6, 5, 5]

marek_set = set(oceny_marka)
kozak_set = set(oceny_kozaka)
print(marek_set.intersection(kozak_set))
print(marek_set.difference(kozak_set))
print(kozak_set.difference(marek_set))