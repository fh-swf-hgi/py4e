# Dateiort: Dateien/mbox-short_modified.txt
filename = input("Gib eine Datei an: ")
if filename == "blafabel":
    print("Du laberst mich an?")
    exit()

file = open(filename, "r")

count = 0
summe = 0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        zahl = float(line[line.find(":") + 1:])
        summe = summe + zahl
        count = count + 1
print("Summe:", summe)
print("Anzahl:", count)

file.close()
