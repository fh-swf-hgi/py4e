import re

file = open('Dateien/mbox-short.txt')
chars = dict()
for line in file:
    for char in line:
        char = char.lower()
        if re.search("[a-z]", char):
            if char not in chars:
                chars[char] = 1
                continue
            chars[char] = chars[char] + 1
sorted_dict = sorted(chars)

for char in sorted_dict:
    print(char, ":", chars[char])
