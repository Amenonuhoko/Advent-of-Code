from collections import defaultdict

file = open('lines.txt')
lines = file.readlines()

path = []
root = []
dir = defaultdict(int)

# All Lines
for line in lines:
    line = line.strip('\n')
    line = line.split(' ')

    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                root.pop()
            else:
                root.append(line[2])
        if line[1] == 'ls':
            continue
    elif line[0] != '$':
        if line[0] == 'dir':
            continue
        else:
            dir[tuple(root)] += int(line[0])
            path = root[:-1]
            while path:
                dir[tuple(path)] += int(line[0])
                path.pop()

answer = 0
print(dir)
print(sum([x for x in dir.values() if x <= 100_000]))

print(min([d for d in dir.values() if d + (70_000_000 - dir[('/'),]) >= 30_000_000]))

# for line in lines:
#
#     line = line.split(' ')
#
#     if line[0] == '$':
#         if 0 < total:
#             record.append([depth, total])
#         total = 0
#         if line[1] == 'cd':
#             if line[2] == '..':
#                 count -= 1
#
#             else:
#                 count += 1
#         else:
#             depth = count
#
#         directories = 0
#     else:
#         if line[0] == 'dir':
#             directories += 1
#             continue
#             # tally[1][count - 1][0] += line[1] + ' '
#         else:
#             total += int(line[0])
# maximum = 0
# for things in record:
#     print(things)
# print(maximum)