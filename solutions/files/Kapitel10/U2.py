file = open('Dateien/mbox-short.txt')
hour_count = dict()
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    hour = words[5].split(":")[0]
    if hour not in hour_count:
        hour_count[hour] = 1
        continue
    hour_count[hour] = hour_count[hour] + 1

for hour in sorted(hour_count):
    print(hour, hour_count[hour])
