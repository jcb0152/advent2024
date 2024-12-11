import heapq
from collections import defaultdict

filename = "input-02.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

safe = 0
damp = 0
def test_vals(vals):
    prev = vals[0]
    direc = vals[1] - vals[0]
    found = False

    for i, level in enumerate(vals[1:]):
        check = level - prev

        if check * direc <= 0 or abs(check) > 3:
            return False

        prev = level
    return True

for line in data:
    if not line:
        continue

    vals = list(map(int, line.split()))

    if test_vals(vals):
        safe += 1
        damp += 1
        continue

    for i in range(len(vals)):
        corrected = [*vals[:i], *vals[i+1:]]
        if test_vals(corrected):
            damp += 1
            break
    
    


print(safe)
print(damp)
