file = open("lines.txt", 'r')
lines = file.readlines()



# AX BY CZ
# Rock Lose Paper Draw Scissor Win
# AY BZ CX
# Rock Draw Paper Win Scissor Lose
# AZ BX CY
# Rock Win Paper Lose Scissor Draw

# 3 5 7
# 4 9 2
# 8 1 6



count = 0
score = 0
chars = ''
for line in lines:
    count += 1
    chars = list(line)
    if chars[0] == "A":
        if chars[2] == "X":
            score += 3
        elif chars[2] == "Y":
            score += 4
        elif chars[2] == "Z":
            score += 8
    elif chars[0] == "B":
        if chars[2] == "X":
            score += 1
        elif chars[2] == "Y":
            score += 5
        elif chars[2] == "Z":
            score += 9
    elif chars[0] == "C":
        if chars[2] == "X":
            score += 2
        elif chars[2] == "Y":
            score += 6
        elif chars[2] == "Z":
            score += 7
    print("{} no:{} count:{}".format(line, count, score))

    # B Paper + X Lose = Rock 1 + 0 = 1 CHECK
    # B Paper + Y Draw = Paper 2 + 3 = 5
    # B Paper + Z Win = Scissor 3 + 6 = 9

    # C Scissor + X Lose = Paper 2 + 0 = 2
    # C Scissor + Y Draw = Scissor 2 + 3 = 5
    # C Scissor + Z Win = Rock 1 + 6 = 7 CHECK

    # A Rock + X Lose = Scissor 3 + 0 = 3
    # A Rock + Y Draw = Rock 1 + 3 = 4 CHECK
    # A Rock + Z Win = Paper 2 + 6 = 8

    # B Paper + X Lose = Rock 1 + 0 = 1 CHECK
    # B Paper + Y Draw = Paper 2 + 3 = 5
    # B Paper + Z Win = Scissor 3 + 6 = 9

    # C Scissor + X Lose = Paper 2 + 0 = 2
    # C Scissor + Y Draw = Scissor 2 + 3 = 5
    # C Scissor + Z Win = Rock 1 + 6 = 7 CHECK

    # A B C
    # R P S
    # 1 2 3

    # X Y Z
    # 0 3 6

    # A Rock + X Lose = Scissor 3 + 0 = 3
    # A Rock + Y Draw = Rock 1 + 3 = 4 CHECK
    # A Rock + Z Win = Paper 2 + 6 = 8

    # Scissor Paper Rock
    # Rock Scissor Paper
    # Paper Rock Scissor

    # 3 2 1
    # 1 3 2
    # 2 1 3

    # 0 3 6
    # 3 6 0
    # 6 0 3