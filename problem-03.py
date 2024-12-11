import re

filename = "input-03.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")

pattern = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
pos = -1
ans = 0
enabled = True
for found in re.findall(pattern, ''.join(data)):
    if enabled and 'mul' in found:
        nums = re.split(r'\(|,|\)', found)
        ans += int(nums[1]) * int(nums[2])
        continue
    if 'don\'t' in found:
        enabled = False
    elif 'do' in found:
        enabled = True
print(ans)
