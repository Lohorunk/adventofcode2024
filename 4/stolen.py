WORD = 'XMAS'

directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
def process_correct(matrix):
    solutions = 0
    for y, line in enumerate(matrix):
        for x, _ in enumerate(line):
            if matrix[y][x] == "X":
                for dir in directions:
                    for index in range(1, 4):
                        try:
                            if matrix[y+index*dir[1]][x+index*dir[0]] != WORD[index] or y + index * dir[1] < 0 or x + index * dir[0] < 0:
                                break
                            if index == 3:
                                solutions += 1
                        except:
                            break
    return solutions
puzzle_input = """"""
matrix = puzzle_input.strip().splitlines()
print(process_correct(matrix))