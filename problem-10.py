from collections import deque

filename = "input-10.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

dirs = [(-1,0), (0,-1), (1,0), (0,1)]

def check(r,c,grid, found):
    score = 0
    current = int(grid[r][c])

    if current == 9:
        found.add((r,c))
        return 1
    
    up = str(current + 1)
    for dr,dc in dirs:
        tr = r + dr
        tc = c + dc
        
        if tr < 0 or tr >= len(grid):
            continue

        if tc < 0 or tc >= len(grid[0]):
            continue

        if int(grid[tr][tc]) == int(up):
            score += check(tr,tc,grid, found)

    return score
            
            
total = 0
for r, line in enumerate(data):
    for c, val in enumerate(line):
        if int(val) == 0:
            total += check(r,c,data, set())

print(total)
