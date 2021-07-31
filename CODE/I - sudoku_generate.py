
import random
import math

empty_grid = [[0 for i in range(9)] for j in range(9)]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_grid(grid):
    for row in grid:
        print(row)

def generate_sudoku(grid):  # grid
    #length is the length of each row/column
    length = len(grid)
    #traversing through rows
    for i in range(0, length):
        #traversing through columns
        for j in range(0, length):
            #Checking for an empty cell
            if grid[i][j] == 0:
                #Traversing through nos. 1-9 to check which number is the possible assignment to a cell
                for k in range(1, length + 1):
                    #Checking validity of the cell
                    if (isValidCell(grid, i, j, k)):
                        #initial assignment
                        grid[i][j] = k
                        #if correct solution
                        if generate_sudoku(grid):
                            return True
                        #backtracks here
                        grid[i][j] = 0
                return False
    print_grid(grid)
    #The last true ensures that only one solution is displayed and the recursion stops when the solution is found.
    return True

    ##NOTE: Am still confused as to when we get the correct solution how does the functions stop the recursion!
    
    
def remove_numbers(grid):
    pass


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

puzzle_hard = [[0, 0, 0, 0, 7, 0, 1, 4, 8],
               [0, 0, 8, 0, 0, 0, 0, 0, 3],
               [0, 2, 0, 0, 1, 4, 0, 0, 5],
               [0, 0, 0, 4, 3, 5, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 0, 9],
               [0, 0, 0, 7, 6, 9, 0, 0, 0],
               [8, 0, 0, 9, 2, 0, 0, 5, 0],
               [9, 0, 0, 0, 0, 0, 7, 0, 0],
               [1, 7, 5, 0, 4, 0, 0, 0, 0]]
# print_grid(empty_grid)
# print("\n")
# (generate_sudoku(puzzle_hard))
(generate_sudoku(empty_grid))


