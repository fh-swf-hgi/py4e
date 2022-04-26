stunden = float(input("Gib die Arbeitsstunden an: "))
satz = float(input("Gib den Stundensatz an: "))
zahlung = 0

if stunden > 40:
    zahlung = 40 * satz
    zahlung = zahlung + (stunden - 40) * satz * 1.5
else:
    zahlung = zahlung * satz

print("Zahlung:", zahlung)
