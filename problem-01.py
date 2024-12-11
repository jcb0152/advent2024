import heapq
from collections import defaultdict

filename = "input-01.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = ["1 2", "1 1", "1 1", "2 2", "3 6"]
left = []
right = []

lcount = defaultdict(int)
rcount = defaultdict(int)

for line in data:
    if not line:
        continue
    l, r = map(int, line.split())
    heapq.heappush(left, l)
    heapq.heappush(right, r)

    lcount[l] += 1
    rcount[r] += 1

total_diff = 0
sim = 0

while left or right:
    val = left[0]
    total_diff += abs(heapq.heappop(left) - heapq.heappop(right))

    sim += val * rcount[val]
    

print(total_diff)
print(sim)
