import math

def present_in_row(grid, row):
    return [grid[row][i] for i in range(9) if grid[row][i] != 0]


def present_in_col(grid, col):
    return [grid[i][col] for i in range(9) if grid[i][col] != 0]


def present_in_box(grid, row, col):
    box_size = int(math.sqrt(len(grid)))
    r = (row // box_size) * box_size
    c = (col // box_size) * box_size
    present = []
    for i in range(box_size):
        for j in range(box_size):
            if grid[r + i][c + j] != 0:
                present.append(grid[r + i][c + j])
    return present


def find_possibilities(grid, row, col):
    return list(set(range(1, 10)) - set(present_in_box(grid, row, col) + present_in_col(grid, col) + present_in_row(grid, row)))


def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                possibilities = find_possibilities(grid, i, j)
                if len(possibilities) == 1:
                    grid[i][j] = possibilities[0]
                    solve_sudoku(grid)

    return grid

#find time taken for puzzle
time_sum = 0
for i in range(100):
    start = time.time()
    solve_sudoku(puzzle_medium)
    end = time.time()
    time_sum = time_sum + ((end - begin) * 0.001)

print(time_sum / 100)


