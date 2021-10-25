import math
import time
# Printing the grid
from generating_grid import sudoku_puzzle

def print_grid(grid):
    for num in grid:
        print(num)

def solve_sudoku(grid):  # grid
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                for k in range(1, length + 1):
                    if (isValidCell(grid, i, j, k)):
                        grid[i][j] = k
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    print_grid(grid)

# Checks if the particular number is not present in any row/column/square i.e. checking
# whether number in cell is valid for sudoku


def isValidCell(grid, row, col, num):
    return (not (present_in_Row(grid, row, num)) and not (present_in_Col(grid, col, num)) and not (present_in_Box(grid, row, col, num)))

# Checks whether number is present in the specified row


def present_in_Row(grid, row, num):
    for col in range(len(grid)):
        if num == grid[row][col]:
            return True
    return False

# Checks whether number is present in the specified column


def present_in_Col(grid, col, num):
    for row in range(len(grid)):
        if num == grid[row][col]:
            return True
    return False

# Checks whether number is present in the specified block/box


def present_in_Box(grid, row, col, num):
    box_size = int(math.sqrt(len(grid)))
    r = (row // box_size) * box_size
    c = (col // box_size) * box_size
    for i in range(box_size):
        for j in range(box_size):
            if num == grid[r + i][c + j]:
                return True
    return False


# Printing solved puzzles

def main():
    print("Image has been read.")
    print("Sudoku puzzle:")
    print_grid(sudoku_puzzle)
    t1 = time.time()
    print()
    print("Solved sudoku:")
    solve_sudoku(sudoku_puzzle)
    print()
    t2 = time.time()
    print()
    print("Time taken: ", t2 - t1, "seconds")
main()
