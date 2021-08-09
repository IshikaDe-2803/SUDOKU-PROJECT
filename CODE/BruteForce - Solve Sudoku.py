puzzle_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def grid_to_string(grid):
    return ''.join(map(str, [''.join(map(str, i)) for i in grid]))


def string_to_grid(str_solved_sudoku):
    solved_sudoku = []
    row = []
    for i in range(len(str_solved_sudoku)):
        if i % 9 == 0 and i != 0:
            solved_sudoku.append(row)
            row = []
        row.append(int(str_solved_sudoku[i]))
    return solved_sudoku


def print_sudoku(grid):
    for row in grid:
        print(row)


print_sudoku(string_to_grid(grid_to_string(puzzle_medium)))
