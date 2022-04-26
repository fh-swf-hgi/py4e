def count(word, zeichen):
    count = 0
    for letter in word:
        if letter == zeichen:
            count = count + 1
    print(count)


count("Banane", "a")
