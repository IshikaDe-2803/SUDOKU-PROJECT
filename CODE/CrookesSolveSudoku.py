import math
puzzle_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]


puzzle_hard = [[0, 0, 0, 0, 7, 0, 1, 4, 8],
               [0, 0, 8, 0, 0, 0, 0, 0, 3],
               [0, 2, 0, 0, 1, 4, 0, 0, 5],
               [0, 0, 0, 4, 3, 5, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 0, 9],
               [0, 0, 0, 7, 6, 9, 0, 0, 0],
               [8, 0, 0, 9, 2, 0, 0, 5, 0],
               [9, 0, 0, 0, 0, 0, 7, 0, 0],
               [1, 7, 5, 0, 4, 0, 0, 0, 0]]


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


def print_grid(grid):
    for num in grid:
        print(num)


print_grid(solve_sudoku(puzzle_medium))
print()
print_grid(solve_sudoku(puzzle_hard))
