import numpy as np

file = open('lines.txt')
lines = file.readlines()

working = np.array_split(lines, 100)

check = []
duplicates = ''

for things in working:
    print(things)
    for stuff in things[0]:
        for moreStuff in things[1]:
            if stuff == moreStuff and stuff != '\n':
                for moremoreStuff in things[2]:
                    if moremoreStuff == stuff:
                        print(stuff)
                        duplicates = stuff
    check.append(duplicates)
print(check)


last = 0
for yeet in check:
    if yeet.islower():
        number = ord(yeet) - 96
        last += number
    else:
        number = ord(yeet) - 38
        last += number
print(last)



