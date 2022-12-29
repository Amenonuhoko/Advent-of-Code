file = open('lines.txt', 'r')
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

starter = 0
for things in newlist:
    if things > starter:
        starter = things
        print(things)

