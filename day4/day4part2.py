file = open('lines.txt')
lines = file.readlines()

count = 0

for line in lines:
    line = line.strip()
    line = line.split(',')
    first = line[0].split('-')
    second = line[1].split('-')

    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        print(line)
        count += 1
    elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        print(line)
        count += 1
    elif int(first[0]) <= int(second[0]) <= int(first[1]):
        print(line)
        count += 1
    elif int(second[0]) <= int(first[0]) <= int(second[1]):
        print(line)
        count += 1
    else:
        continue

print(count)
