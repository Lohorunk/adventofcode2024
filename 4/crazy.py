#
# no worko
#
#
import re

with open('env/input', 'r') as f:
    puzzle_input = f.read()
puzzle_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

WORD = 'XMAS'

def find_startpoints(matrix):
    y = 0

    start_positions = []

    while y < len(matrix):
        xpos = [j.start() for j in re.finditer(WORD[0], matrix[y])]
        for x in xpos:
            start_positions.append([x, y])
        y += 1

    return start_positions

def find_directions(start_positions, matrix, xmax, ymax, wordleft):
    directions = []

    directionl = [-wordleft, 0, wordleft]

    for pos in start_positions:
        posdirs = []
        for x in directionl:
            for y in directionl:
                if ((0 <= (pos[0] + x) <= xmax) and
                    (0 <= (pos[1] + y) <= ymax) and
                    ([x, y] != [0, 0])):
                    posdirs.append([x, y])
                    
        directions.append(posdirs)

    return directions

def search_direction(matrix, direction, startpoint):
    x = startpoint[0]
    y = startpoint[1]
    huuox = x + direction[0] - 1
    huuoy = y + direction[1] - 1

    bruhx = 1 if x < x + direction[0] else -1
    bruhy = 1 if y < y + direction[1] else -1
    xtrace = list(range(x, huuox, bruhx))
    ytrace = list(range(y, huuoy, bruhy))
    if direction[0] == 0:
        xtrace = [x, x, x, x]
    if direction[1] == 0:
        ytrace = [y, y, y, y]

    print(bruhx, bruhy, '|', x, y, '|', huuox, huuoy, '|', range(y, huuoy, bruhy))
    print(xtrace, ytrace)

    curr_word = ''
    
    for xt, yt in zip(xtrace, ytrace):
        curr_word += matrix[yt][xt]

    return curr_word == WORD

def process(matrix):
    xmax = len(matrix[0])
    ymax = len(matrix) - 1

    wordleft = len(WORD) - 1

    startpoints = find_startpoints(matrix)
    directions = find_directions(startpoints, matrix, xmax, ymax, wordleft)

    count = 0

    for point, directions in zip(startpoints, directions):
        for direction in directions:
            count += int(search_direction(matrix, direction, point))
            

    return count

matrix = []
for i in puzzle_input.strip().splitlines():
    matrix.append(i)

print(process(matrix))