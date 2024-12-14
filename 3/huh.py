import re

with open('env/input', 'r') as f:
    puzzle_input = f.read()


def part1():
    num = 0

    for i in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle_input):
        num += int(i[0]) * int(i[1])
    
    return num

def part2():
    num = 0

    matches = []
    dodonts = []

    for i in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle_input):
        matches.append(i)

    for i in re.finditer(r"do\(\)|don't\(\)", puzzle_input):
        dodonts.append(
            [i.span()[0], False if "'" in i.group() else True]
        )

    mask = {}
    last = None
    i = 0
    
    while i < len(dodonts):
        if i == 0:
            mask[(0, dodonts[i][0])] = True
            i += 1
            continue

        mask[(dodonts[i - 1][0], dodonts[i][0])] = dodonts[i - 1][1]

        if i == len(dodonts) - 1:
            mask[(dodonts[i][0]), 99999999999] = dodonts[i][1]

        i += 1

    for i in matches:
        pos = i.span()[0]
        nums = i.group().replace('mul(', '').replace(')', '').strip().split(',')
        for j in mask:
            if j[0] < pos < j[1]:
                if mask[j]:
                    num += int(nums[0]) * int(nums[1])
                    break
            
    return num

print(part1())
print(part2())