import math
from random import shuffle, randint

empty_grid = [[0 for i in range(9)] for j in range(9)]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_grid(grid):
    for row in grid:
        print(row)

def generate_sudoku(grid):  
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                shuffle(num_list)
                for value in num_list:
                    if (isValidCell(grid, i, j, value)):
                        grid[i][j] = value
                        if generate_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False

    return True    

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

#INTERNET CODE:
# def remove(grid):
#     #Start Removing Numbers one by one

#     #A higher number of attempts will end up removing more numbers from the grid
#     #Potentially resulting in more difficiult grids to solve!
#     attempts = 5 
#     counter=1
#     while attempts>0:
#     #Select a random cell that is not already empty
#         row = randint(0,8)
#         col = randint(0,8)
#     while grid[row][col]==0:
#         row = randint(0,8)
#         col = randint(0,8)
#     #Remember its cell value in case we need to put it back  
#     backup = grid[row][col]
#     grid[row][col]=0
    
#     #Take a full copy of the grid
#     copyGrid = []
#     for r in range(0,9):
#         copyGrid.append([])
#         for c in range(0,9):
#             copyGrid[r].append(grid[r][c])
    
#     #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
#     counter=0      
#     solve_sudoku(copyGrid)   
#     #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
#     if counter!=1:
#         grid[row][col]=backup
#         #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
#         attempts -= 1
#     print(grid)
    
   
(generate_sudoku(empty_grid))

print_grid(empty_grid)