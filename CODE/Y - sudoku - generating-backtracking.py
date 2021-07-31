
from itertools import count
import random
import math

empty_grid = [[0 for i in range(9)] for j in range(9)]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_grid(grid):
    for row in grid:
        print(row)


# def generate_sudoku(grid):  # grid
#     length = len(grid)
#     for i in range(length):
#         for j in range(length):
#             if grid[i][j] == 0:
#                 random.shuffle(num_list)
#                 for k in num_list:
#                     if (isValidCell(grid, i, j, k)):
#                         grid[i][j] = k
#                         if generate_sudoku(grid):
#                             return True
#                         grid[i][j] = 0
#                 return False

#     print_grid(grid)

def generate_sudoku(grid):
    length = len(grid)
    for i in range(0, 81):
        row = i // length
        col = i % length
        if (grid[row][col] == 0):
            random.shuffle(num_list)
            for digit in num_list:
                if (isValidCell(grid, row, col, digit)):
                    grid[row][col] = digit
                    if (generate_sudoku(grid)):
                        return True
                    grid[row][col] = 0
            return False
    print_grid(grid)
    print()
    remove_numbers(grid)
    return True


index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def remove_numbers(grid):

    print_grid(grid)


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


print_grid(empty_grid)
print(generate_sudoku(empty_grid))
