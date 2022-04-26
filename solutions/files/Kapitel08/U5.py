list = []
file = open('Dateien/romeo.txt')
for line in file:
    words = line.split()
    for word in words:
        if word in list:
            continue
        list.append(word)
print(sorted(list))
