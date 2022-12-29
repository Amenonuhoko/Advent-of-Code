file = open("lines.txt", 'r')
lines = file.readlines()

# A B C
# R P S
# 1 2 3

# X Y Z
# R P S
# 1 2 3

# W L D
# 6 0 3

# A + X = 1 + 3 = 4
# A + Y = 2 + 6 = 8 CHECK
# A + Z = 3 + 0 = 3

# B + X = 1 + 0 = 1 CHECK
# B + Y = 2 + 3 = 5
# B + Z = 3 + 6 = 9

# C + X = 1 + 6 = 7
# C + Y = 2 + 0 = 2
# C + Z = 3 + 3 = 6 CHECK

count = 0
score = 0
chars = ''
for line in lines:
    count += 1
    chars = list(line)
    if chars[0] == "A":
        if chars[2] == "X":
            score += 4
            print(4)
        elif chars[2] == "Y":
            score += 8
            print(8)
        elif chars[2] == "Z":
            score += 3
            print(3)
    elif chars[0] == "B":
        if chars[2] == "X":
            score += 1
            print(1)
        elif chars[2] == "Y":
            score += 5
            print(5)
        elif chars[2] == "Z":
            score += 9
            print(9)
    elif chars[0] == "C":
        if chars[2] == "X":
            score += 7
            print(7)
        elif chars[2] == "Y":
            score += 2
            print(2)
        elif chars[2] == "Z":
            score += 6
            print(6)
    print("{} no:{} count:{}".format(line, count, score))


