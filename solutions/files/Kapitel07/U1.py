file = open("Dateien/mbox-short.txt", "r")

for line in file:
    print(line.upper())

file.close()
