empty_grid = [[0] * 9] * 9


def grid_to_string(grid):
    return ''.join(map(str, [''.join(map(str, i)) for i in grid]))


def find_all_possibilities(zero_pos: int, grid_str: str):

    present_in_sudoku = {grid_str[col] for col in range(len(grid_str)) if (check_same_row(
        zero_pos, col) or check_same_col(zero_pos, col) or check_same_block(zero_pos, col))}

    return {str(i) for i in range(10)} - present_in_sudoku


def generate_sudoku(grid_str: str) -> str:
    zero_pos = grid_str.find('0')

    for value in find_all_possibilities(zero_pos, grid_str):
        grid_str = grid_str[0: zero_pos] + value + grid_str[zero_pos + 1:]
        generate_sudoku(grid_str)
        if (grid_str.find('0') == -1):
            print(grid_str)


def check_same_row(row, col):
    if (row // 9) == (col // 9):
        return True
    return False


def check_same_col(row, col):
    if (row % 9) == (col % 9):
        return True
    return False


def check_same_block(row, col):
    if ((row // 9) // 3 == (col // 9) // 3) and ((row % 9) // 3 == (col % 9) // 3):
        return True
    return False


def string_to_grid(str_solved_sudoku):
    solved_sudoku = []
    row = []
    for i in range(len(str_solved_sudoku) + 1):
        if i % 9 == 0 and i != 0:
            solved_sudoku.append(row)
            if len(solved_sudoku) == 9:
                return solved_sudoku
            row = []
        row.append(int(str_solved_sudoku[i]))


def print_sudoku(grid):
    for row in grid:
        print(row)


print(generate_sudoku(grid_to_string(empty_grid)))
