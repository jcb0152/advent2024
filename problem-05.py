from collections import defaultdict

filename = "input-05.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

order = True
pages = defaultdict(set)
ans = 0
wrong = 0

for line in data:
    bad = False
    if not line:
        order = False
        continue

    if order:
        pre, post = line.split('|')
        pages[post].add(pre)
        continue
    
    vals = line.split(',')
    for i,start in enumerate(vals):
        for check in vals[i + 1:]:
            if check in pages[start]:
                bad = True
                break
        if bad:
            break
    if not bad:
        index = (len(vals) // 2) 
        ans += int(vals[index])
        continue

    remaining = set(vals)
    final = []
    while remaining:
        for val in vals:
            if len(remaining.intersection(pages[val])) == 0:
                final.append(val)
                remaining.remove(val)
                vals.remove(val)

    index = (len(final) // 2) 
    wrong += int(final[index])
print(ans)
print(wrong)
