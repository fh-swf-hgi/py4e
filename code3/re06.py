# Finde Zeilen, die ein at-Zeichen zwischen zwei Zeichen haben:
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
