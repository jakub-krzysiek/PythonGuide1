name = "Wojtek"
#name = name.lower()
#name = name.upper()
print(name)
print(name[0])
print(len(name))
name = name.replace("jte", "kij")
print(name)

for letter in name:
    print(letter)

if 'w' in name:
    print("jest taka literka")

test_string = "ala ma kota i jd"
#test_string = test_string.replace(" ", ", ")
#test_string = test_string.split(" ")
if test_string.startswith("ala"):
    print("ala")
if test_string.endswith("jd"):
    print("jd")

new_string = test_string+" "+name
new_string = f"{name} jest kozak, a {test_string}"
print(new_string)
print(new_string[-2])
print(new_string[3:-3])