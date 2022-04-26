list = []
while True:
    zahl = 0.0
    eingabe = input('Bitte eine Zahl eingeben: ')
    if eingabe == 'done':
        break

    try:
        zahl = float(eingabe)
    except:
        print('Falsche Eingabe')
        quit()

    list.append(zahl)

if list:
    print('Maximum: ', max(list))
    print('Minimum: ', min(list))
