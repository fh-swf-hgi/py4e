def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


repeat_lyrics()


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# Der folgende Fehler erscheint:
# NameError: name 'repeat_lyrics' is not defined
