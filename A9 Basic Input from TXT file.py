lines = []
with open("A9 plik.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(int(line.strip()))
    print(lines)