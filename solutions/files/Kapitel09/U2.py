file = open('Dateien/mbox-short.txt')
weekdays = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[2] not in weekdays:
        weekdays[words[2]] = 1
        continue
    weekdays[words[2]] = weekdays[words[2]] + 1

print(weekdays)
