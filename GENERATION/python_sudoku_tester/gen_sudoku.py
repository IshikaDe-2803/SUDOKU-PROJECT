import random


class Generate_Sudoku:
    grid = [[0 for i in range(9)] for j in range(9)]
    grid_size = len(grid)
    sub_grid_size = 3
    difficulty = 0

    def __init__(self, difficulty) -> None:
        self.difficulty = difficulty

    def generate_sudoku(self):
        self.fill_diagonal_boxes()
        self.fill_remaining_boxes(0, self.sub_grid_size)
        self.removes_digit()

    def fill_diagonal_boxes(self):
        for i in range(0, self.grid_size, self.sub_grid_size):
            self.fill_grid(i, i)

    def grid_unfilled(self, rowStart: int, colStart: int, num: int) -> bool:
        for i in range(0, self.sub_grid_size):
            for j in range(0, self.sub_grid_size):
                if self.grid[rowStart + i][colStart + j] == num:
                    return False
        return True

    def fill_grid(self, row: int, col: int):
        num = self.random_generator(self.grid_size)
        for i in range(0, self.sub_grid_size):
            for j in range(0, self.sub_grid_size):
                while not self.grid_unfilled(row, col, num):
                    num = self.random_generator(self.grid_size)
                self.grid[row + i][col + j] = num

    def random_generator(self, num) -> int:
        return random.randint(1, num)

    def is_valid_box(self, i: int, j: int, num: int) -> bool:
        return (self.row_unfilled(i, num) and self.col_unfilled(j, num) and self.grid_unfilled(i - i % self.sub_grid_size, j - j % self.sub_grid_size, num))

    def row_unfilled(self, i: int, num: int) -> bool:
        for j in range(0, self.grid_size):
            if self.grid[i][j] == num:
                return False
        return True

    def col_unfilled(self, j: int, num: int) -> bool:
        for i in range(0, self.grid_size):
            if self.grid[i][j] == num:
                return False
        return True

    def fill_remaining_boxes(self, i: int, j: int) -> bool:
        if (j >= self.grid_size and i < self.grid_size - 1):
            i = i + 1
            j = 0

        if (i >= self.grid_size and j >= self.grid_size):
            return True

        if (i < self.sub_grid_size):
            if (j < self.sub_grid_size):
                j = self.sub_grid_size

        elif (i < self.grid_size - self.sub_grid_size):
            if (j == (int)(i / self.sub_grid_size) * self.sub_grid_size):
                j = j + self.sub_grid_size

        else:
            if (j == self.grid_size - self.sub_grid_size):
                i = i + 1
                j = 0
                if (i >= self.grid_size):
                    return True

        for num in range(1, self.grid_size + 1):
            if self.is_valid_box(i, j, num):
                self.grid[i][j] = num
                if self.fill_remaining_boxes(i, j + 1):
                    return True
                self.grid[i][j] = 0
        return False

    def get_empty_space(self):
        if (self.difficulty == 0):
            return 36
        if (self.difficulty == 1):
            return 46
        if (self.difficulty == 2):
            return 67

    def removes_digit(self):
        empty_places = self.get_empty_space()
        while (empty_places != 0):
            cellId = self.random_generator(self.grid_size * self.grid_size) - 1
            i = (cellId // self.grid_size)
            j = cellId % 9
            if (self.grid[i][j] != 0):
                empty_places = empty_places - 1
                self.grid[i][j] = 0


sudoku = Generate_Sudoku(2)
sudoku.generate_sudoku()
print(sudoku.grid)
