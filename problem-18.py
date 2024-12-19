import heapq

filename = "input-18.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

dirs = [(-1,0), (0,-1), (1,0), (0,1)]

size = 70
limit = 1024

#size = 6
#limit = 12


board = [['.' for i in range(size + 1)] for i in range(size + 1)]

start = (0,0)
end = (size,size)

def valid(r, c):
    return r >= 0 and r <= size and c >= 0 and c <= size

def search(nodes, visited, grid):
    while nodes:
        score, pos, path = heapq.heappop(nodes)
        if pos in visited:
            continue

        visited.add(pos)
        r, c = pos
        for dr, dc in dirs:
            tr = r + dr
            tc = c + dc

            if (tr, tc) == end:
                return score + 1, path
            
            if valid(tr, tc) and grid[tr][tc] != '#':
                heapq.heappush(moves, (score + 1, (tr, tc), [*path, (tc, tr)]))
    return -1, path

prev = []
for i, line in enumerate(data):
    x, y = map(int, line.split(','))
    board[y][x] = '#'

    if i == limit:
        prev.append((x,y))

    if i >= limit and (x, y) in prev:
        moves = []
        heapq.heappush(moves, (0, start, []))
        num, prev = search(moves, set(), board)
        if num == -1:
            print(x,y)
            break
    
    

