

import random
from random import randint, shuffle
import math

empty_grid = [[0 for i in range(9)] for j in range(9)]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_grid(grid):
    for row in grid:
        print(row)

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
    
    return True

def generate_sudoku(grid):  # grid
    # length is the length of each row/column
    length = len(grid)
    # traversing through rows
    for i in range(0, length):
        # traversing through columns
        for j in range(0, length):
            # Checking for an empty cell
            if grid[i][j] == 0:
                # Traversing through nos. 1-9 to check which number is the possible assignment to a cell
                random.shuffle(num_list)
                for k in num_list:
                    # Checking validity of the cell
                    if (isValidCell(grid, i, j, k)):
                        # initial assignment
                        grid[i][j] = k
                        # if correct solution
                        if generate_sudoku(grid):
                            return True
                        # backtracks here
                        grid[i][j] = 0
                return False

    remove_numbers(grid, 64)
    print_grid(grid)
    #remove_num(grid)
    # The last true ensures that only one solution is displayed and the recursion stops when the solution is found.
    return True

    # NOTE: Am still confused as to when we get the correct solution how does the functions stop the recursion!

# def unique_soln(grid):
#     c = 0

#     if c == 1:
#         return True
#     else:
#         return False

##########################################
def remove_numbers(grid, count):
    while (count != 0):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        value = grid[i][j]
        if (grid[i][j] != 0):
            count -= 1
            grid[i][j] = 0
        #if(not unique_soln(grid)):
            grid[i][j] = value
            remove_numbers(grid, count + 1)
########################################
'''
Mere hisaab se yeh code chalna chahiye, but i dont know how to code a function to count number of solutions
'''
#     #1. entire row/column or box should have atleast one element
#     #2. the sudoku should give us one unique solution (minimum: 17 numbers i.e. 64 spaces)
#     #If the above two conditions are not satisfied, then what??
    
#     return grid
# def remove_num(grid):
#     attempts = 5 
#     counter=1
#     while attempts>0:
#     #Select a random cell that is not already empty
#         row = randint(0,8)
#         col = randint(0,8)
#         while grid[row][col]==0:
#             row = randint(0,8)
#             col = randint(0,8)
#     #Remember its cell value in case we need to put it back  
#         backup = grid[row][col]
#         grid[row][col]=0
    
#     #Take a full copy of the grid
#         copyGrid = []
#         for r in range(0,9):
#             copyGrid.append([])
#             for c in range(0,9):
#                 copyGrid[r].append(grid[r][c])
    
#     #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
#         counter=0      
#         solve_sudoku(copyGrid)   
#     #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
#         if counter!=1:
#             grid[row][col]=backup
#         #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
#             attempts -= 1
#             print_grid(grid)

def isValidCell(grid, row, col, num):
    return (not (present_in_Row(grid, row, num)) and not (present_in_Col(grid, col, num)) and not (present_in_Box(grid, row, col, num)))

# Checks whether number is present in the specified row
#


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
