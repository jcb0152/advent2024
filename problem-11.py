from collections import defaultdict
import functools
import itertools
filename = "input-11.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

@functools.lru_cache(maxsize=2048)
def change(num):
    if num == str(0):
        return [str(1)]

    if len(num) % 2 == 0:
        l = str(int(num[:len(num) // 2]))
        r = str(int(num[len(num) // 2:]))
        return [l,r]

    return [str(int(num) * 2024)]

@functools.lru_cache(maxsize=2048)
def count(num, remaining):
    total = 0

    vals = change(num)
    remaining -= 1
    if remaining == 0:
        return len(vals)
    
    for val in vals:
        total += count(val, remaining)

    return total
        

rocks = data[0].split()
num_times = 75

total = 0
for rock in rocks:
    total += count(rock, num_times)

print(total)
def slow():
    for i in range(1,num_times + 1):
        rocks = [trock for trocks in list(map(change, rocks)) for trock in trocks]
