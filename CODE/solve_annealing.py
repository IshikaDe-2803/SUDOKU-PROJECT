# import random
# import numpy as np
# import math 
# from random import choice
# import statistics 

# puzzle = """
#                     024007000
#                     600000000
#                     003680415
#                     431005000
#                     500000032
#                     790000060
#                     209710800
#                     040093000
#                     310004750
#                 """

# sudoku = np.array([[int(i) for i in line] for line in puzzle.split()])

# def print_grid(grid):
#     for num in grid:
#         print(num)

# def FixValues(sudoku):
#     for i in range (9):
#         for j in range (9):
#             if sudoku[i][j] != 0:
#                 sudoku[i][j] = 1
    
#     return(sudoku)

# FixValues(sudoku)
# #FixValues(sudoku)
# print_grid(sudoku)

"""
10-08-2021
PART 1
--1. copy sudoku function to store a copy of the sudoku--
--2. square function that returns the square coordinates--
--3. unfixed position function that stores all the unfixed values--
--4. Pick a random index from 3--
--5. list possible numbers that can fit into the random index--
--6. fill the grid using that rule--
--7. repeat this until sudoku is filled--
PART 2
8. Calculate the cost of rows and columns
PART 3
9. swapping random cells
PART 4
10. Applying simulated annealing
"""