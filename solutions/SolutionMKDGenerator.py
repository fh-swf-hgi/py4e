from mdutils.mdutils import MdUtils
from mdutils import Html
import os

target_file_path = "solutions.mkd"


def file_init():
    # Existierende Datei entfernen

    try:
        os.remove(target_file_path)
    except:
        0
        # Nothing to do
    f = open(target_file_path, "w", encoding="utf-8")
    f.write("Musterlösungen\n")
    f.write("==============\n")
    f.write("\n")


def py_to_md(py_path):
    py_file = open(py_path, "r", encoding="utf-8")
    target_file = open(target_file_path, "a", encoding="utf-8")

    target_file.write("Lösung\n")
    target_file.write("------\n")
    target_file.write("\n")

    target_file.write("~~~~ {.python}\n")

    for line in py_file:
        target_file.write(line)
        target_file.write("\n")

    target_file.write("~~~~\n")
    target_file.write("\n")

    target_file.close()
    py_file.close()

# Datei vorbereiten
file_init()

# Verzeichnisse und Dateien durchlaufen
for subdir, dirs, files in os.walk("files"):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if not filepath.endswith(".py"):
            continue
        py_to_md(filepath)
