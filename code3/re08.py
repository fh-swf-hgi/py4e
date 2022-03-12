# Wie in re07.py aber etwas praeziser für E-Mail Adressen,
# da Sonderzeichen in Mailadressen erlaubt sind.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
