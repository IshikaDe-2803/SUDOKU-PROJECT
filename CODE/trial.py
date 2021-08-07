import math
from random import shuffle

def print_grid(grid):
    for num in grid:
        print(num)


puzzle = [[0, 0, 0, 0, 0, 0, 1, 4, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 3],
               [0, 2, 0, 0, 1, 4, 0, 0, 5],
               [0, 0, 0, 4, 3, 5, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 0, 9],
               [0, 0, 0, 7, 6, 9, 0, 0, 0],
               [8, 0, 0, 9, 2, 0, 0, 5, 0],
               [9, 0, 0, 0, 0, 0, 7, 0, 0],
               [1, 7, 5, 0, 4, 0, 0, 0, 0]]

# def solve_sudoku(grid):  # grid
#     length = len(grid)
#     for i in range(length):
#         for j in range(length):
#             if grid[i][j] == 0:
#                 for k in range(1, length + 1):
#                     if (isValidCell(grid, i, j, k)):
#                         grid[i][j] = k
#                         if solve_sudoku(grid):
#                             return True
#                         grid[i][j] = 0
#                 return False
#     print("AA")
#     print_grid(grid)
def generate_sudoku(grid):  
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                #shuffle(num_list)
                for value in num_list:
                    if (isValidCell(grid, i, j, value)):
                        grid[i][j] = value
                        if generate_sudoku(grid):
                            return True
    grid[i][j] = 0
    return False

def isValidCell(grid, row, col, num):
    return (not (present_in_Row(grid, row, num)) and not (present_in_Col(grid, col, num)) and not (present_in_Box(grid, row, col, num)))

def present_in_Row(grid, row, num):
    for col in range(len(grid)):
        if num == grid[row][col]:
            return True
    return False

def present_in_Col(grid, col, num):
    for row in range(len(grid)):
        if num == grid[row][col]:
            return True
    return False

def present_in_Box(grid, row, col, num):
    box_size = int(math.sqrt(len(grid)))
    r = (row // box_size) * box_size
    c = (col // box_size) * box_size
    for i in range(box_size):
        for j in range(box_size):
            if num == grid[r + i][c + j]:
                return True
    return False

generate_sudoku(puzzle)

