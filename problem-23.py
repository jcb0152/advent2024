from collections import defaultdict
import itertools

filename = "input-23.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]
        
connections = defaultdict(set)
tnodes = set()

def findMaxClique(r, p, x):
    if not p and not x:
        return r
    largest = set()
    for v in list(p):
        tr = set([*r, v])
        tp = p.intersection(connections[v])
        tx = x.intersection(connections[v])

        tmp = findMaxClique(tr, tp, tx)
        if len(tmp) > len(largest):
            largest = tmp
        p.remove(v)
        x = set([*x, v])
    return largest
        
        
for line in data:
    node1, node2 = line.split('-')
    connections[node1].add(node2)
    connections[node2].add(node1)

    if node1.startswith('t'):
        tnodes.add(node1)

    if node2.startswith('t'):
        tnodes.add(node2)

threes = set()
for node in tnodes:
    connected = connections[node]
    
    for tmp in connected:
        vals = connections[tmp]
        for tmp2 in connected.intersection(vals):
            three = [node, tmp, tmp2]
            three.sort()
            threes.add(tuple(three))

print(len(threes))

allNodes = set(connections.keys())
largest = list(findMaxClique(set(), allNodes, set()))
largest.sort()
print(','.join(largest))


