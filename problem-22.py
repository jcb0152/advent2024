import functools
from collections import defaultdict

filename = "input-22.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

@functools.cache
def mix(val1, val2):
    return val1 ^ val2

@functools.cache
def prune(val):
    return val % 16777216

@functools.cache
def get_next(old):
    t1 = prune(mix(old, old * 64))
    t2 = prune(mix(t1, t1 // 32))
    t3 = prune(mix(t2, t2 * 2048))
    return t3

num_runs = 2000
total = 0

seqs = defaultdict(lambda: defaultdict(int))

for i, secret in enumerate(map(int,data)):
    tmp = secret
    prev = secret % 10
    seq = tuple()
    
    for _ in range(num_runs):
        tmp = get_next(tmp)
        seq = (*seq[-3:], tmp % 10 - prev % 10)
        if len(seq) == 4:
            if i not in seqs[seq]:
                seqs[seq][i] = tmp % 10
        prev = tmp

    total += tmp

ans = 0
for vals in seqs.values():
    ans = max(ans, sum(vals.values()))


print(total)
print(ans)
