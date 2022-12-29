file = open('lines.txt')
lines = file.readlines()

columns = list()
count = 0
box = ''
boxes = []
temp = []

# All Lines
for line in lines:
    line = line.strip('\n')

    if line != '' and line[0] != 'm' and line[1] != '1':
        # Lines that don't contain move and numbers
        chars = list(line)

        # Find the letters inside boxes
        box = ''
        for i in range(1, len(chars), 4):
            box += chars[i]
        boxes.append(box)

while count <= len(boxes):
    temp = []
    for things in boxes:
        for i, items in enumerate(things):
            if i == count:
                temp.append(items)
    columns.append(temp)
    count += 1

# for things in columns:
#     for stuff in things:
#         stuff.strip(" ")


for boxes in columns:
    while " " in boxes:
        boxes.remove(" ")


    # for i, letters in enumerate(boxes):
    #     if letters == ' ':
    #         del boxes[i]
    #     print("{} {}".format(i, letters))

for line in lines:
    if line[0] == 'm':
        line = line.split(' ')

        destination = int(line[5]) - 1
        selected = int(line[3]) - 1
        numberToAdd = int(line[1])

        # Select X
        tempList = columns[selected][0:numberToAdd]

        # Move X from X
        columns[selected].reverse()
        columns[selected] = columns[selected][:len(columns[selected]) - numberToAdd]
        columns[selected].reverse()
        print(numberToAdd)
        print(columns[selected])


        # To X
        tempList.reverse()
        for things in tempList:
            columns[destination].insert(0, things)


answer = ''

for things in columns:
    answer += things[0]

print(answer)