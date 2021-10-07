puzzle_medium = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle_hard = [[0, 0, 0, 0, 7, 0, 1, 4, 8],
               [0, 0, 8, 0, 0, 0, 0, 0, 3],
               [0, 2, 0, 0, 1, 4, 0, 0, 5],
               [0, 0, 0, 4, 3, 5, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 0, 9],
               [0, 0, 0, 7, 6, 9, 0, 0, 0],
               [8, 0, 0, 9, 2, 0, 0, 5, 0],
               [9, 0, 0, 0, 0, 0, 7, 0, 0],
               [1, 7, 5, 0, 4, 0, 0, 0, 0]]


def grid_to_string(grid) -> str:
    return ''.join(map(str, [''.join(map(str, i)) for i in grid]))


def find_all_possibilities(zero_pos: int, grid_str: str) -> set:
    present_in_sudoku = {grid_str[col] for col in range(len(grid_str)) if (check_same_row(
        zero_pos, col) or check_same_col(zero_pos, col) or check_same_block(zero_pos, col))}

    return {str(i) for i in range(10)} - present_in_sudoku


def solve_sudoku(grid_str: str) -> None:
    zero_pos = grid_str.find('0')

    for value in find_all_possibilities(zero_pos, grid_str):
        grid_str = grid_str[0: zero_pos] + value + grid_str[zero_pos + 1:]
        solve_sudoku(grid_str)
        if (grid_str.find('0') == -1):
            print_sudoku(string_to_grid(grid_str))


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


def print_sudoku(grid) -> None:
    for row in grid:
        print(row)


solve_sudoku(grid_to_string(puzzle_medium))
print()
solve_sudoku(grid_to_string(puzzle_hard))
