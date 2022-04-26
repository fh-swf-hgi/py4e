def durchschnitt():
    anzahl = 0
    summe = 0
    durchschnitt = 0

    done = False
    while not done:
        eingabe = input("Bitte eine Zahl eingeben: ")
        try:
            z = float(eingabe)
            anzahl = anzahl + 1
            summe = summe + z
        except:
            if eingabe == "done":
                done = True
            else:
                return "Es werden nur Zahlen akzeptiert. Beenden mit 'done'"
    durchschnitt = summe / anzahl

    erg = "Anzahl: " + str(anzahl) + " Summe: " + str(summe) + " Durchschnitt: " + str(durchschnitt)
    print(erg)
    return erg


durchschnitt()
