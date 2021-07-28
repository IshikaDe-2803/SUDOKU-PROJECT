import math

#Printing the grid
def print_grid(grid):
    for num in grid:
        print(num)

puzzle_easy = [[3, 0, 4, 0],
               [0, 1, 0, 2],
               [0, 4, 0, 3],
               [2, 0, 1, 0]]

puzzle_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle_hard = []

#Solving the Sudoku
def solve_sudoku(grid):  
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                for k in range(1, length + 1):
                    if (isValidCell(grid, i, j, k)):
                        grid[i][j] = k
                        solve_sudoku(grid)
                        grid[i][j] = 0
                return
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

#Printing solved puzzles
solve_sudoku(puzzle_easy)
solve_sudoku(puzzle_medium)