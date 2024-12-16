import heapq
from collections import defaultdict, deque

filename = "input-16.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

start = (-1,-1)
end = (-1,-1)

dirs = [(-1,0), (0,-1), (1,0), (0,1)]

for r, line in enumerate(data):
    for c, val in enumerate(line):
        if val == 'S':
            start = (r,c)
        elif val == 'E':
            end = (r,c)

def left(dr,dc):
    return (-1 * dc, dr)

def right(dr, dc):
    return (dc, -1 * dr)

temp = defaultdict(lambda: defaultdict(list))
def search(grid, moves, seen, best):
    global temp
    final = -1
    while moves:
        score, pos, curdir, path = heapq.heappop(moves)
        temp[(pos, curdir)][score].extend(path)
        if final != -1 and score > final:
            return final
        
        while (pos, curdir) in seen:
            score, pos, curdir, path = heapq.heappop(moves)
            temp[(pos, curdir)][score].extend(path)

        seen.add((pos, curdir))
        
        r, c = pos
        dr, dc = curdir

        dr2, dc2 = left(dr,dc)
        dr3, dc3 = right(dr,dc)

        tr = r + dr
        tc = c + dc

        if (tr, tc) == end: # and curdir == (0, -1):
            best.update(path)
            if final == -1:
                final = score + 1

        val = grid[tr][tc]
        if val == '.':
            heapq.heappush(moves, (score + 1, (tr,tc), (dr,dc), [*path, ((tr, tc), (dr, dc), score + 1)]))

        heapq.heappush(moves, (score + 1000, (r,c), (dr2,dc2), [*path, ((r, c), (dr2, dc2), score + 1000)]))
        heapq.heappush(moves, (score + 1000, (r,c), (dr3,dc3), [*path, ((r, c), (dr3, dc3), score + 1000)]))


moves = []
heapq.heappush(moves, (0, start, (0,1), [(start, (0,1), 0)]))
best = set()
print(search(data, moves, set(), best))

final_best = set()
vals = deque(best)
while vals:
    pos, cdir, score = vals.popleft()
    for tpos, tdir, tscore in temp[(pos, cdir)][score]:
        if tpos not in final_best:
            vals.append((tpos, tdir, tscore))
        final_best.add(pos)

print(len(final_best) + 1)
            

