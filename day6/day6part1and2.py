file = open('lines.txt')
lines = file.readlines()

count = 0
search = ''
found = False
checking = []

for line in lines:
    chars = list(line)

    while not found:
        checking = chars[count:count + 14]
        for i in chars:
            if checking.count(i) > 1:
                print(checking)
                count += 1
                break
            else:
                continue
        if checking.count(i) > 1:
            continue
        else:
            print(checking)
            print(count + 14)
            found = True

