# Finde Zeilen, die mit 'X' beginnen, gefolgt von beliebig vielen
# (nicht-Leer-)Zeichen, gefolgt von einem ':' und einem
# Leerzeichen. Danach kann eine Zahl mit einer oder mehreren
# Ziffern und Dezimalpunkten folgen. Diese Zahl ist dann der Match.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
