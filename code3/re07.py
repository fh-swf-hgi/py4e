# Finde Zeilen, mit einem at-Zeichen zwischen zwei Zeichen. Die
# Zeichenfolge vor dem at muss mit einem Buchstaben oder einer
# Ziffer beginnen; die Zeichenfolge nach dem at muss mit einem
# Buchstaben enden.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
