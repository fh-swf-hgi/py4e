punktzahl = input("Geben Sie ihre Punktzahl an: ")

try:
    punkte = float(punktzahl)
except:
    print("Bitte eine Zahl eingeben")
    quit()

if punkte >= 0.9 and punkte <= 1:
    print(1)
elif punkte >= 0.8 and punkte <= 1:
    print(2)
elif punkte >= 0.7 and punkte <= 1:
    print(3)
elif punkte >= 0.6 and punkte <= 1:
    print(4)
elif 0 <= punkte < 0.6:
    print(5)
else:
    print("Falsche Punktanzahl, bitte geben Sie die Punkte von 0.0 bis 1.0 ein")