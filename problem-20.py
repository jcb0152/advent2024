from collections import deque, defaultdict

filename = "input-20.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

dirs = [(-1,0), (0,-1), (1,0), (0,1)]

start = (-1,-1)
end = (-1,-1)


for r, line in enumerate(data):
    for c, val in enumerate(line):
        if val == 'S':
            start = (r,c)
        elif val == 'E':
            end = (r,c)


def count(moves, grid):
    times = {}
    while moves:
        score, pos = moves.popleft()

        if pos in times:
            continue

        times[pos] = score

        r, c = pos
        for dr, dc in dirs:
            tr, tc = r + dr, c + dc

            if grid[tr][tc] == '.' or grid[tr][tc] == 'E':
                moves.append((score + 1, (tr, tc)))
    return times


moves = deque()
moves.append((0, start))

times = count(moves, data)

rows = defaultdict(list)
cols = defaultdict(list)
tups = []

for (r, c), score in times.items():
    rows[r].append((c, score))
    cols[c].append((r, score))

    tups.append((score, (r,c)))

ans = 0
threshold = 100
cheat = 2
for tmp in [*rows.values(), *cols.values()]:
    tmp.sort()
    ppos, pscore = tmp.pop()
    while tmp:
        cpos, cscore = tmp.pop()
        if abs(cscore - pscore) - 2 >= threshold and abs(cpos - ppos) <= cheat:
            ans += 1
        ppos, pscore = cpos, cscore
            
print(ans)

ans2 = 0
threshold = 100
cheat = 20
for i, (pscore, (pr, pc)) in enumerate(tups):
    for cscore, (cr, cc) in tups[i + 1:]:
        dist = abs(cr - pr) + abs(cc - pc)
        if abs(cscore - pscore) - dist >= threshold and dist <= cheat:
            ans2 += 1
print(ans2)
