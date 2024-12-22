import functools
import itertools
from collections import defaultdict

filename = "input-21.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

numpad = (
    ('7','8','9'),
    ('4','5','6'),
    ('1','2','3'),
    ('-','0','A'),
    )

keypad = (
    ('-', '^', 'A'),
    ('<', 'v', '>'),
    )

dirs = {
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
    'A': (0,0),
    }


shortest_paths = {}

total = 0
layers = 26

@functools.cache
def find(val, buttons):
    for r, line in enumerate(buttons):
        for c, num in enumerate(line):
            if num == val:
                return (r,c)
    
@functools.cache
def find_paths(current, target, buttons, layers):
    if current == target:
        return ['A']
    
    cr, cc = find(current, buttons)
    nr, nc = find(target, buttons)

    seq = []
    dr = nr - cr
    dc = nc - cc

    if dc < 0:
        seq.extend(list('<' * abs(dc)))
    if dr < 0:
        seq.extend(list('^' * abs(dr)))
    if dr > 0:
        seq.extend(list('v' * abs(dr)))
    if dc > 0:
        seq.extend(list('>' * abs(dc)))

    paths = itertools.permutations(seq, len(seq))
    best = []

    for path in map(lambda x: (*x, 'A'), paths):
        total = []

        tr = cr
        tc = cc

        bad = False
        
        for dr, dc in map(lambda x: dirs[x], path):
            tr += dr
            tc += dc
            if buttons[tr][tc] == '-':
                bad = True
                break
        if bad:
            continue

        if layers == 1:
            total = path
        else:
            for prev,cur in itertools.pairwise(['A', *path]):
                tmp = find_paths(prev, cur, keypad, layers - 1)
                total.extend(tmp)

        if best == [] or len(total) < len(best):
            best = total
    return best

def walk(path, buttons = keypad):
    r,c = find('A', buttons)
    ans = []

    for val in path:
        dr, dc = dirs[val]
        r += dr
        c += dc

        if val == 'A':
            ans.append(buttons[r][c])
    return ans

@functools.cache
def count_tups(path, iterations):
    tups = {}
    if iterations == 0:
        for prev, cur in itertools.pairwise(['A', *path]):
            tups[(prev, cur)] = 1
    else:
        for prev, cur in itertools.pairwise(['A', *path]):
            new_tups = count_tups(shortest_paths[(prev, cur)], iterations - 1)
            for k, v in new_tups.items():
                if k in tups:
                    tups[k] += v
                else:
                    tups[k] = v
    return tups


for start, end in itertools.product('^>v<A', repeat=2):
    shortest_paths[(start, end)] = ''.join(walk(find_paths(start, end, keypad, 2)))

for code in data:
    tlayers = layers - 1
    path = ()
    for prev, cur in itertools.pairwise(['A', *code]):
        path = (*path, *walk(walk(find_paths(prev, cur, numpad, 3))))
    path_len = sum(count_tups(tuple(path), tlayers).values())
    
    print(code, '=', path_len)
    num = int(code[:-1])
    total += num * path_len

print(total)
