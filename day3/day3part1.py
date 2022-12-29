import numpy as np

file = open('lines.txt')
lines = file.readlines()

chars = []
count = 0
answers = []
duplicates = ''

for line in lines:
    chars = list(line)
    partOne = chars[:len(chars)//2]
    partTwo = chars[len(chars)//2:]
    for things in partOne:
        for stuff in partTwo:
            if things == stuff:
                duplicates = things
    answers.append(duplicates)

last = 0
for yeet in answers:
    if yeet.islower():
        number = ord(yeet) - 96
        last += number
    else:
        number = ord(yeet) - 38
        last += number
print(last)



