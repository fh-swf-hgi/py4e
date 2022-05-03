import os

target_file_path = "./solutions.mkd"

# Bereitet die Zieldatei vor
def file_init():
    # Existierende Datei entfernen
    try:
        os.remove(target_file_path)
    except:
        0
        # Nothing to do


"""Python Quellcode Datei an mkd Datei enhängen.
py_path definiert die Pythondatei, welche eingefügt werden soll. """


def py_to_mkd(py_path):
    py_file = open(py_path, "r", encoding="utf-8")

    # Überschrift einfügen
    target_file.write("Lösung\n")
    target_file.write("------\n")
    target_file.write("\n")

    target_file.write("~~~~ {.python}\n")

    # Quellcodedateien einfügen
    for line in py_file:
        target_file.write(line)

    target_file.write("\n~~~~\n")
    target_file.write("\n")
    py_file.close()


# Programmablauf startet
# Datei vorbereiten
file_init()
target_file = open(target_file_path, "a", encoding="utf-8")

# Aktuell besuchtes Verzeichnisss
curr_dir = ""

# Verzeichnisse und Dateien im Ordner files zum Hinzufügen durchlaufen
for subdir, dirs, files in os.walk("files"):
    for file in files:
        filepath = subdir + os.sep + file

        # Prüfen ob Kapitel bereits vorhanden, vergleich mit Zwischengespeichertem Ordner
        if subdir.split("/")[-1] != "Dateien" and curr_dir is not subdir:
            curr_dir = subdir
            target_file.write("Musterlösungen\n")
            target_file.write("==============\n")

        # Prüfen ob Python Datei, ansonsten Überspringen
        if not filepath.endswith(".py"):
            continue
        # Python datei hinzufügen
        py_to_mkd(filepath)

target_file.close()
