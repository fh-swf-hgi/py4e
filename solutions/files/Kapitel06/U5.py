str = 'X-DSPAM-Confidence:0.8475'

zahl = float(str[str.find(":") + 1:])
print(zahl)
