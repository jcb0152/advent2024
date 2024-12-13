from collections import deque
filename = "input-09.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

def calc(a,b):
    return 0.5 * (b - a + 1) * (a + b)

data = data[0]

disk = True
free = deque()
files = deque()
final = deque()
idx = 0
num = 0

for block in list(data):
    if disk:
        files.append((idx, num, int(block)))
        idx += int(block)
        num += 1
    else:
        free.append((idx, int(block)))
        idx += int(block)

    disk = not disk

total = 0
idx = 0

drive = {}
tmpfiles = deque()
remain = deque()

free.append((-1,-1))
while files:
    curfile = files.pop()
            
    while free:
        curspace = free.popleft()

        if curspace == (-1,-1):
            remain.appendleft(curfile)
            drive[curfile[0]] = curfile
            free.append(curspace)
            break

        elif curspace[1] >= curfile[2] and curspace[0] < curfile[0]:
            drive[curspace[0]] = (curspace[0], curfile[1], curfile[2])
            tmpfiles.append((curspace[0], curfile[1], curfile[2]))
            tmp = curspace[0] + curfile[2]
            tmp2 = curspace[1] - curfile[2]
            if tmp2 != 0:
                free.append((tmp, tmp2))
            break

        free.append(curspace)

    while curspace != (-1,-1):
        curspace = free.popleft()
        free.append(curspace)
    
idx = 0
tmp = list(drive.keys())
tmp.sort()

total1 = 0
for val in tmp:
    idx, num, size = drive[val]
    total1 += num * calc(idx, idx + size - 1)
    
print(total1)
while files:
    print(final)
    file = files.popleft()
    idx = file[0]
    total += file[1] * calc(idx, idx + file[2] - 1)
    for _ in range(file[2]):
        final.append(file[1])
    idx += file[2]

    if free:
        space = free.popleft()[0]
    else:
        continue
    
    tmp = deque()
    print('filling')
    print('free', free)
    while space > 0:
        if files:
            file = files.pop()
        else:
            idx += space
            for _ in range(file[2]):
                final.append('.')
            break
        if file[2] > space:
            tmp.append(file)
            continue
            frag = file[2] - space
            total += file[1] * calc(idx, idx + space - 1)
            idx += space
            files.append((file[0], file[1], frag))
            space = 0
        else:
            total += file[1] * calc(idx, idx + file[2] - 1)
            idx += file[2]
            space = space - file[2]
            for _ in range(file[2]):
                final.append(file[1])

        print(final)
    while tmp:
        file = tmp.pop()
        files.append(file)

print(total)
print(final)            
