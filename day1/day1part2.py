import os
directory = os.getcwd()
print(directory)
file = open("lines.txt", 'r')
Lines = file.readlines()

newlist = []
count = 0
for line in Lines:
    if line != "\n":
        count += int(line)
    else:
        newlist.append(count)
        count = 0
        print(newlist)

array = []
starter = 0
for things in newlist:
    if things > starter:
        starter = things
        array.append(starter)
        print(starter)

newlist.sort(reverse=True)

result = newlist[0] + newlist[1] + newlist[2]

print(result)