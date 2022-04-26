import re

lines = 0
regex = str(input("Gib einen RegEx an:"))

with open("Dateien/mbox-short.txt", "r") as file:
    for line in file:
        if re.findall(regex, line):
            lines += 1
print(lines)
