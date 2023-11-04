# Finde Zeilen, die mit 'Details:' beginnen und auf 'rev=' enden
# gefolgt von einer Zahl. Diese Zahl ist dann der Match.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)
