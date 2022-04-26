file = open('Dateien/mbox-short.txt')
mail_count = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[1] not in mail_count:
        mail_count[words[1]] = 1
        continue
    mail_count[words[1]] = mail_count[words[1]] + 1

tuples = mail_count.items()

print(sorted(tuples, reverse=True)[0])
