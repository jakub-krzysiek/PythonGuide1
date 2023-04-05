ocena_1 = 5
ocena_2 = 3
oceny = [4, 5, 3, 2, 1, 6, 4]

print(oceny[3])
oceny[3] = 5
print(oceny[3])

for i in range(len(oceny)):
    print(oceny[i], end=" ")

for ocena in oceny:
    print(ocena, end=" ")

for i, ocena in enumerate(oceny):
    oceny[i] += 1

for i, ocena in enumerate(oceny):
    if i % 2 == 0 and ocena > 3:
        print(i, ocena)

oceny.append(5)
oceny.extend([3, 1, 2])
oceny.insert(4, 4)
#oceny.remove([2,2])
oceny.pop()
#oceny.sort()
oceny = sorted(oceny, reverse=True)

for ocena in oceny:
    if ocena == 4:
        print("jest taka ocena")
        break

if 4 in oceny:
    print("jest taka ocena")

print(oceny)
print(oceny.index(2))