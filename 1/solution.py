with open('env/input', 'r') as f:
    puzzle_input = f.read()



def part1(left, right):
    length = len(left)

    diff = 0

    while length > 0:
        minl = min(left)
        minr = min(right)

        diff += abs(minl - minr)
        left.remove(minl)
        right.remove(minr)

        length = len(left)
    
    return diff


def part2(left, right):
    similarity = 0

    for num in left:
        similarity += num * right.count(num)
    
    return similarity



left = []
right = []

for line in puzzle_input.split('\n'):
    lines = line.split()
    left.append(int(lines[0]))
    right.append(int(lines[1]))

print(part2(left, right))
print(part1(left, right))