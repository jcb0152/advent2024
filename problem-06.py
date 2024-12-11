from collections import defaultdict
filename = "input-06.txt"

directions = [(-1,0), (0,1), (1,0), (0,-1)]
total = 0

def move(pos, d, grid, seen):
    global total

    while d not in seen[pos]:
        
        seen[pos].add(d)
        x,y = pos
        xmod,ymod = directions[d]

        x = x + xmod
        y = y + ymod

        if x < 0 or x >= len(grid):
            return 0

        if y < 0 or y >= len(grid[0]):
            return 0

        if grid[x][y] == '#':
            d = (d + 1) % 4
            continue

        if not grid[x][y] == 'X':
            grid[x][y] = 'X'
            total = total + 1

        pos = (x,y)

    return 1

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

start = (-1,-1)

for i,line in enumerate(data):
    for j,cell in enumerate(line):
        if cell == '^':
            start = (i,j)

data2 = []
data3 = []
for line in data:
    data2.append(list(line))

move(start, 0, data2, defaultdict(set))
total2 = 0

data2[start[0]][start[1]] = 'X'
for line in data2:
    print(''.join(line))
    total2 += line.count('X')

total3 = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '^' or data[x][y] == '#':
            continue
        tmp = []
        for line in data:
            tmp.append(list(line))

        tmp[x][y] = '#'
        total3 += move(start, 0, tmp, defaultdict(set))
    print('.')


print(total)
print(total2)
print(total3)

