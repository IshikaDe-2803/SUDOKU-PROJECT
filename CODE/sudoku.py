#TO GENERATE AND SOLVE SUDOKU
#STEP 1: Generate empty grid
#STEP 2: fill each square with a number using backtracking that fills up the grid
#STEP 3: remove numbers while making sure the solution is right

#TO SOLVE SUDOKU JUST FOLLOW STEP 2
import math
number_list = [1, 2, 3, 4]

#Empty grid stores a list of list --> the empty sudoku without numbers
def empty_grid(number_list):
    return [[0 for i in range(len(number_list))] for j in range(len(number_list))]

#Print grid --> Prints the sudoku puzzle
def print_grid(grid):
    for i in grid:
        print(i)    

grid = [[0, 3, 4, 0],
        [4, 0, 0, 2],
        [1, 0 ,0 ,3],
        [0, 2, 1, 0]]
        
'''
ANS:
2341
4132
1423
3214
'''

def solve_sudoku(grid): #grid
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                print(i,j)  
                for k in range(1, length + 1):
                    if (isValidCell(grid, i, j, k)):
                        grid[i][j] = k  
    return grid          

#Checks if the particular number is not present in any row/column/square
def isValidCell(grid, row, col, num):
    return (not (present_in_Row(grid, row, num)) and not (present_in_Col(grid, col, num)) and not (present_in_Box(grid, row, col, num)))

#Checks whether number is present in the specified row
def present_in_Row(grid, row, num):
    for i in range(len(grid)):
        if num == grid[row][i]:
            return True
    return False

#Checks whether number is present in the specified column
def present_in_Col(grid, col, num):
    for i in range(len(grid)):
        if num == grid[i][col]:
            return True
    return False

#Checks whether number is present in the specified block/box
def present_in_Box(grid, row, col, num):
    box_size = int(math.sqrt(len(grid)))
    r= row // box_size * box_size
    c= col // box_size * box_size
    for i in range(r):
        for j in range(c):
            if num == grid[i][j]:
                return True
    return False

print((solve_sudoku(grid)))







