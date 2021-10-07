import time
import math
import random

grid_size = 9
sub_grid_size = 3


def generate_sudoku(grid, difficulty):
    fill_diagonal_boxes(grid)
    fill_remaining_boxes(grid, 0, sub_grid_size)
    removes_digit(grid, difficulty)
    return grid


def fill_diagonal_boxes(grid):
    for i in range(0, grid_size, sub_grid_size):
        fill_grid(grid, i, i)


def fill_grid(grid, row: int, col: int):
    num = random_generator(grid_size)
    for i in range(0, sub_grid_size):
        for j in range(0, sub_grid_size):
            while present_in_Box(grid, row, col, num):
                num = random_generator(grid_size)
            grid[row + i][col + j] = num


def random_generator(num) -> int:
    return random.randint(1, num)


def present_in_Box(grid, row, col, num):
    box_size = int(math.sqrt(len(grid)))
    r = (row // box_size) * box_size
    c = (col // box_size) * box_size
    for i in range(box_size):
        for j in range(box_size):
            if num == grid[r + i][c + j]:
                return True
    return False


def fill_remaining_boxes(grid, i: int, j: int) -> bool:
    if (j >= grid_size and i < grid_size - 1):
        i = i + 1
        j = 0

    if (i >= grid_size and j >= grid_size):
        return True

    if (i < sub_grid_size):
        if (j < sub_grid_size):
            j = sub_grid_size

    elif (i < grid_size - sub_grid_size):
        if (j == (int)(i / sub_grid_size) * sub_grid_size):
            j = j + sub_grid_size

    else:
        if (j == grid_size - sub_grid_size):
            i = i + 1
            j = 0
            if (i >= grid_size):
                return True

    for num in range(1, grid_size + 1):
        if is_valid_cell(grid, i, j, num):
            grid[i][j] = num
            if fill_remaining_boxes(grid, i, j + 1):
                return True
            grid[i][j] = 0
    return False


def is_valid_cell(grid, row, col, num):
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


def removes_digit(grid, difficulty):
    empty_places = get_empty_space(difficulty)
    while (empty_places != 0):
        cellId = random_generator(grid_size * grid_size) - 1
        i = (cellId // grid_size)
        j = cellId % 9
        if (grid[i][j] != 0):
            empty_places = empty_places - 1
            grid[i][j] = 0


def get_empty_space(difficulty):
    if (difficulty == 0):
        return 36
    if (difficulty == 1):
        return 46
    if (difficulty == 2):
        return 52


def grid_to_string(grid) -> str:
    return ''.join(map(str, [''.join(map(str, i)) for i in grid]))


def solve_sudoku(grid_str: str) -> None:
    zero_pos = grid_str.find('0')

    for value in find_all_possibilities(zero_pos, grid_str):
        grid_str = grid_str[0: zero_pos] + value + grid_str[zero_pos + 1:]
        solve_sudoku(grid_str)
        if (grid_str.find('0') == -1):
            string_to_grid(grid_str)


def find_all_possibilities(zero_pos: int, grid_str: str) -> set:
    present_in_sudoku = {grid_str[col] for col in range(len(grid_str)) if (check_same_row(
        zero_pos, col) or check_same_col(zero_pos, col) or check_same_block(zero_pos, col))}

    return {str(i) for i in range(10)} - present_in_sudoku


def check_same_row(row: int, col: int) -> bool:
    if (row // 9) == (col // 9):
        return True
    return False


def check_same_col(row: int, col: int) -> bool:
    if (row % 9) == (col % 9):
        return True
    return False


def check_same_block(row: int, col: int) -> bool:
    if ((row // 9) // 3 == (col // 9) // 3) and ((row % 9) // 3 == (col % 9) // 3):
        return True
    return False


def string_to_grid(str_solved_sudoku: str) -> None:
    solved_sudoku = []
    row = []
    for i in range(len(str_solved_sudoku) + 1):
        if i % 9 == 0 and i != 0:
            solved_sudoku.append(row)
            if len(solved_sudoku) == 9:
                return solved_sudoku
            row = []
        row.append(int(str_solved_sudoku[i]))


def main():
    total_time = 0
    for i in range(100):
        print(i)
        start = time.time()
        grid = [[0 for i in range(9)] for j in range(9)]
        difficulty = 2
        solve_sudoku(grid_to_string(generate_sudoku(grid, difficulty)))
        end = time.time()
        total_time += ((end - start) * 0.001)
    print(total_time / 100)


main()
