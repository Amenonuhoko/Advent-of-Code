file = open('lines.txt')
data = file.read().splitlines()

for y, width in enumerate(data[1:-1], 1):
    for x, height in enumerate(width[1:-1], 1):
        up = ([data[y - i][x] for i in range(1, y + 1)])
        down = ([data[y + i][x] for i in range(1, len(data) - y)])
        left = ([data[x][x - i] for i in range(1, x + 1)])
        right = ([data[x][x + i] for i in range(1, len(data) - x)])
        print(up, down, left, right)

