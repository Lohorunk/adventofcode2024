import copy

with open('env/input', 'r') as f:
    puzzle_input = f.read()



def check_safety(report):
    last_increase = None

    for i, j in zip(report, report[1:]):
        if not(1 <= abs(i - j) <= 3):
            safe = False
            break

        increase = i < j

        if last_increase != None:
            if increase != last_increase:
                safe = False
                break
        else:
            last_increase = increase
            
        safe = True

    return safe

def part1(reports):
    safe_ammount = 0

    for report in reports:
        safe_ammount += int(check_safety(report))

    return safe_ammount

def part2(reports):
    safe_ammount = 0

    for report in reports:
        if check_safety(report):
            safe_ammount += 1
            continue

        for i in range(len(report)):
            tmp = copy.copy(report)
            tmp.pop(i)
            if check_safety(tmp):
                safe_ammount += 1
                break
        
    return safe_ammount



reports = []

for line in puzzle_input.split('\n'):
    reports.append(
        [int(i) for i in line.split()]
    )

print(part1(reports))
print(part2(reports))