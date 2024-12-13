from collections import defaultdict
import heapq
import itertools
import functools

filename = "input-12.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

dirs = [(-1,0), (0,-1), (1,0), (0,1)]
visited = set()
cells = defaultdict(list)

num = 0

def find_neighbors(r,c, grid):
    vals = [(r,c)]
    visited.add((r,c))
    val = grid[r][c]
    
    for dr, dc in dirs:
        tr = r + dr
        tc = c + dc

        if tr < 0 or tr >= len(grid):
            continue

        if tc < 0 or tc >= len(grid[0]):
            continue

        if (tr,tc) in visited:
            continue

        if grid[tr][tc] != val:
            continue
        
        vals.extend(find_neighbors(tr, tc, grid))

    
    return vals

def count(r,c, grid):
    borders = []
    neighbors = []
    sides = [0,0]
    
    for dr, dc in dirs:
        tr = r + dr
        tc = c + dc

        if tr < 0 or tr >= len(grid):
            borders.append(((tr,tc), (dr,dc)))
            sides[0] += dr
            sides[1] += dc
            continue
        
        if tc < 0 or tc >= len(grid[0]):
            borders.append(((tr,tc), (dr,dc)))
            sides[0] += dr
            sides[1] += dc
            continue
        
        if grid[tr][tc] != grid[r][c]:
            borders.append(((tr,tc), (dr,dc)))
            sides[0] += dr
            sides[1] += dc
            continue

        neighbors.append((tr,tc))
    return borders, neighbors, sides

ordered = defaultdict(lambda: defaultdict(list))
def combine(borders):
    for (r,c), (dr,dc) in borders:
        if dr != 0:
            heapq.heappush(ordered[(dr,dc)][r], c)
        elif dc != 0:
            heapq.heappush(ordered[(dr,dc)][c], r)

    buckets = 0
    for ori in dirs:
        vals = ordered[ori]
        for i, indices in vals.items():
            prev = -3
            while indices:
                current = heapq.heappop(indices)
                if prev != current - 1:
                    buckets += 1
                prev = current
    return buckets
            
for r, line in enumerate(data):
    for c, val in enumerate(line):
        if (r,c) not in visited:
            cells[num] = find_neighbors(r,c,data)
            num += 1

total = 0
total2 = 0

for plot in cells.values():
    area = len(plot)

    corners = []
    uturns = []
    
    perim = 0
    perim2 = 0

    outside = set()

    first = (len(data) + 1, len(data[0]) + 1)

    for r,c in plot:
        if r < first[0] or r == first[0] and c < first[1]:
            first = (r,c)
        borders, neighbors, sides = count(r,c,data)
        perim += len(borders)
        outside.update(borders)

    perim2 = combine(outside)
    #print(data[r][c], ': ', area * perim, ', ', area * perim2)
    total += area * perim
    total2 += area * perim2
print(total)
print(total2)


