def lohnberechnung(arbeitsstunden, stundenlohn):
    zahlung = 0

    if arbeitsstunden > 40:
        zahlung = 40 * stundenlohn
        zahlung = zahlung + (arbeitsstunden - 40) * satz * 1.5
    else:
        zahlung = arbeitsstunden * stundenlohn

    print("Monatsgehalt:", zahlung)


try:
    stunden = float(input("Anzahl Arbeitsstunden: "))
    satz = float(input("Stundenlohn:"))
except:
    print("Fehler, bitte gib eine Zahl ein")
