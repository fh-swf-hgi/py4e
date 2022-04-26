unique_words = dict()
file = open('Dateien/words.txt')
for line in file:
    words = line.split()
    for word in words:
        if word in unique_words:
            continue
        unique_words[word] = 1
print(unique_words)
