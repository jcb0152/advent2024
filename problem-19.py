from collections import deque
import functools

filename = "input-19.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

towels = data[0].split(', ')
cases = data[2:]

@functools.cache
def count(remaining):
    if len(remaining) == 0:
        return 1

    total = 0
    for towel in towels:
        if remaining.startswith(towel):
            total += count(remaining[len(towel):])
    return total

ans = 0
ans2 = 0

for i, remaining in enumerate(cases):
    tmp = count(remaining)
    ans += 1 if tmp else 0
    ans2 += count(remaining)

print(ans)
print(ans2)

