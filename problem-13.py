import re
filename = "input-13.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

cases = []
current = []
for line in data:
    if not line:
        cases.append(current)
        current = []
        continue
    nums = re.findall(r'\d+', line)
    current.append(tuple(map(int, nums)))

total = 0
for (ax,ay),(bx,by),(px,py) in cases:

    px += 10000000000000
    py += 10000000000000
    
    det = (ax * by) - (ay * bx)
    inv = det ** -1

    ta = inv * (by * px - bx * py)
    tb = inv * (-1 * ay * px + ax * py)

    a = round(ta)
    b = round(tb)
    
    tx = a * ax + b * bx
    ty = a * ay + b * by

    if tx != px or ty != py:
        continue
    
    if a >= 0 and b >= 0:
        total += 3 * a + b
        
print(total)
