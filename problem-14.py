import re
import os
import time
filename = "input-14.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

width = 101
height = 103

#width = 11
#height = 7

end = 100

small = (-1,101 * 103)
for end in range(0,10001):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    overlapping = 0
    for line in data:
        p,v = line.split()
        _,nums = p.split('=')
        px,py = map(int,nums.split(','))

        _, nums = v.split('=')
        vx,vy = map(int,nums.split(','))

        xend = (px + vx * end) % width
        yend = (py + vy * end) % height

        if grid[yend][xend] != 0:
            overlapping += 1
        
        grid[yend][xend] += 1

    if overlapping < small[1]:
        small = (end, overlapping)
print(small)
for line in grid:
    print(line)
tl = 0
tr = 0
bl = 0
br = 0

for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if i < height // 2 and j < width // 2:
            tl += cell
        if i < height // 2 and j > width // 2:
            tr += cell

        if i > height // 2 and j < width // 2:
            bl += cell

        if i > height // 2 and j > width // 2:
            br += cell
        
print(tl * tr * bl * br)

