
filename = "input-15.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

dirs = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
    }

def transform(line):
    new = []
    for val in line:
        if val in ['#', '.']:
            new.append(val)
            new.append(val)
        elif val == '@':
            new.append(val)
            new.append('.')
        elif val == 'O':
            new.append('[')
            new.append(']')
    return new

def make_move(pos, move, grid):
    r,c = pos
    dr,dc = dirs[move]

    tr = r + dr
    tc = c + dc

    if grid[tr][tc] == '#':
        return pos

    if grid[tr][tc] == '.':
        return (tr,tc)

    if grid[tr][tc] in ['[', ']']:
        affected = []
        affected.append((tr,tc))
        
        if grid[tr][tc] == '[':
            affected.append((tr, tc + 1))
        else:
            affected.append((tr, tc - 1))

        blocked = False
        for cr,cc in affected:
            r1 = cr + dr
            c1 = cc + dc
            if (r1,c1) in affected:
                continue
            
            if grid[r1][c1] in ['[', ']']:
                affected.append((r1,c1))
                if grid[r1][c1] == '[':
                    to_add = (r1, c1 + 1)
                else:
                    to_add = (r1, c1 - 1)

                if to_add not in affected:
                    affected.append(to_add)

            if grid[r1][c1] == '#':
                blocked = True
                break

        if blocked:
            return pos

        for cr,cc in reversed(affected):
            r1 = cr + dr
            c1 = cc + dc
            grid[r1][c1] = grid[cr][cc]
            grid[cr][cc] = '.'
            
        return (tr,tc)
        
warehouse = []
movements = []

start = (-1,-1)
finding = True

for r, line in enumerate(data):
    if not line:
        finding = False
        continue
    
    if finding:
        line = transform(list(line))
        warehouse.append(line)
        if '@' in line:
            start = (r, line.index('@'))

    else:
        movements.append(line)

r,c = start
warehouse[r][c] = '.'

movements = ''.join(movements)
current = start

for move in movements:
    current = make_move(current, move, warehouse)

score = 0
for r, line in enumerate(warehouse):
    for c, val in enumerate(line):
        if val == '[':
            score += 100 * r + c

print(score)
    
