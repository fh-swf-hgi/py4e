import urllib.request

url = input("Geben Sie eine URL an: ")
content = urllib.request.urlopen(url).read()
content = content.decode()

print(content[:3000])
print(len(content))