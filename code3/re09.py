# Finde Zeilen, die mit 'X' beginnen, gefolgt von beliebig vielen
# (nicht-Leer-)Zeichen, gefolgt von einem ':' und einem Leerzeichen.
# Der gesuchte Match ist die Zeichenfolge (ohne Leerzeichen) die auf
# das Leerzeichen in ": " folgt.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)
