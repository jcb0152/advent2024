import itertools
from collections import defaultdict
filename = "input-08.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

nodes = defaultdict(list)

maxr = len(data)
maxc = len(data[0]) 

for (r, row) in enumerate(data):
    for (c, col) in enumerate(row):
        if not col == '.':
            nodes[col].append((r,c))

anti = set()
for name,node in nodes.items():
    for left,right in itertools.permutations(node, 2):
        dr = right[0] - left[0]
        dc = right[1] - left[1]

        lowr = left[0] - dr
        lowc = left[1] - dc

        while lowr >= 0 and lowr < maxr and lowc >= 0 and lowc < maxc:
            anti.add((lowr,lowc))
            lowr = lowr - dr
            lowc = lowc - dc

        highr = lowr + dr
        highc = lowc + dc
            
        while highr >= 0 and highr < maxr and highc >= 0 and highc < maxc:
            anti.add((highr,highc))
            highr = highr + dr
            highc = highc + dc

print(len(anti))
