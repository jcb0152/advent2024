import re
filename = "input-17.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

data = data[:-1]

combo = [0,1,2,3,'A','B','C','_']

regs = {
    'A': 0,
    'B': 0,
    'C': 0,
    }

def get_combo(num):
    operand = combo[num]
    if operand in ['A', 'B', 'C']:
        operand = regs[operand]
    return operand

output = []
def operate(code, num, ptr):
    global output
    global regs
    ptr += 2
    if code == 0:
        operand = get_combo(num)
        regs['A'] = regs['A'] // (2 ** operand)
        
    elif code == 1:
        regs['B'] = regs['B'] ^ num

    elif code == 2:
        operand = get_combo(num)
        regs['B'] = operand % 8

    elif code == 3:
        if regs['A'] != 0:
            ptr = num

    elif code == 4:
        regs['B'] = regs['B'] ^ regs['C']

    elif code == 5:
        operand = get_combo(num)
        output.append(str(operand % 8))

    elif code == 6:
        operand = get_combo(num)
        regs['B'] = regs['A'] // (2 ** operand)

    elif code == 7:
        operand = get_combo(num)
        regs['C'] = regs['A'] // (2 ** operand)

    return ptr

def run_prog(prog, a):
    global output
    output = []
    regs['A'] = a
    regs['B'] = 0
    regs['C'] = 0
    ptr = 0
    while ptr < len(prog) - 1:
        op1 = prog[ptr]
        op2 = prog[ptr + 1]

        op1 = int(op1)
        op2 = int(op2)
            
        ptr = operate(op1, op2, ptr)
    return output

def recursive(prog, a, idx):
    for i in range(8):
        cur = a + i
        output = run_prog(prog, cur)
        print(cur, output)
        print(prog[idx:])
        if prog == output:
            return cur
        if prog[idx:] == output:
            tmp = recursive(prog, cur * 8, idx - 1)
            if tmp != 0:
                return tmp
    return 0
        
    
pattern = "Register ([A-Za-z]): (\\d+)"
prog = []

for line in data:
    if 'Register' in line:
        vals = re.search(pattern, line)
        regs[vals.group(1)] = int(vals.group(2))
        continue

    if not line:
        continue

    if 'Program' in line:
        _, nums = line.split(": ")
        prog = nums.split(',')

ans = 0

ans = recursive(prog, 0, len(prog) - 1)
print(ans)
