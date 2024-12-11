import itertools
filename = "input-07.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]

ops = ['+', '*', '||']
total = 0
for line in data:
    if not line:
        continue

    test, nums = line.split(': ')

    test = int(test)
    nums = list(map(int, nums.split()))

    choices = itertools.product(ops, repeat= (len(nums) - 1))
    for seq in choices:
        tmp = nums[0]
        i = 1
        for op in seq:
            if op == '+':
                tmp += nums[i]
                i += 1
            elif op == '*':
                tmp *= nums[i]
                i += 1
            elif op == '||':
                tmp = int(str(tmp) + str(nums[i]))
                i += 1
        if tmp == test:
            total += tmp
            break
print(total)

    
