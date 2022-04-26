import re

lines = 0
regex = '^New Revision: ([0-9.]+)'
val = []

with open("Dateien/mbox-short.txt", "r") as file:
    for line in file:
        found = re.findall(regex, line)
        if found:
            for f in found:
                val.append(float(f))
print(int(sum(val) / len(val)))