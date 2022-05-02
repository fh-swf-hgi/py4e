def minmax():
    anzahl = 0
    minimum = None
    maximum = None

    done = False
    while not done:
        eingabe = input("Bitte eine Zahl eingeben: ")
        try:
            z = float(eingabe)
            if minimum is None:
                minimum = z
            else:
                if z < minimum:
                    minimum = z
            if maximum is None:
                maximum = z
            else:
                if z > maximum:
                    maximum = z
        except:
            if eingabe == "done":
                done = True
            else:
                return "Es werden nur Zahlen akzeptiert. Beenden mit 'done'"

    erg = "Minimum: " + str(minimum) + " Maximum: " + str(maximum)
    print(erg)
    return erg


minmax()
