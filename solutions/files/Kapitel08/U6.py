file = open('Dateien/mbox-short.txt')
from_count = 0
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    from_count += 1
print("Es gibt ", from_count, " Zeilen mit from.")
