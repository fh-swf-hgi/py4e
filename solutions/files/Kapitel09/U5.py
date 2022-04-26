file = open('Dateien/mbox-short.txt')
mail_count = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    domain = words[1].split("@")[1]
    if domain not in mail_count:
        mail_count[domain] = 1
        continue
    mail_count[domain] = mail_count[domain] + 1

print(mail_count)
