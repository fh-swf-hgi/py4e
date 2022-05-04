def remove_all(liste, wert):
    for element in liste:
        if element == wert:
            liste.remove(element)


liste = ["Banane", "Erbeere", "Apfel",
         "Banane", "Gurke"]
print("Start Liste:", liste)

remove_all(liste, "Banane")

print("Geleerte Liste:", liste)
