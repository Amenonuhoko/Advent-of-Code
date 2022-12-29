file = open('lines.txt')
lines = file.readlines()

count = 0

for line in lines:
    line = line.strip()
    line = line.split(',')
    first = line[0].split('-')
    second = line[1].split('-')
    print(line)
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        print("{}               {}".format(first[0], first[1]))
        print("      {}  {}       ".format(second[0], second[1]))
        count += 1
        print('+1')
        print('\n')
        continue
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        print("      {}  {}       ".format(first[0], first[1]))
        print("{}               {}".format(second[0], second[1]))
        count += 1
        print('+1')
        print('\n')
        continue
    else:
        continue

    # if first[0] <= second[0] <= first[1]:
    #     if first[1] >= second[1] >= first[1]:
    #         print("{}               {}".format(first[0], first[1]))
    #         print("      {}  {}       ".format(second[0], second[1]))
    #         count += 1
    #         print('+1 \n')
    # elif second[0] <= first[0] <= second[1]:
    #     if second[1] >= first[1] >= second[0]:
    #         print("      {}  {}       ".format(first[0], first[1]))
    #         print("{}               {}".format(second[0], second[1]))
    #         count += 1
    #         print('+1 \n')

print(count)
