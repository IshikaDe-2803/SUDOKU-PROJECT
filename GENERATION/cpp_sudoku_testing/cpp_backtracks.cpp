#include <bits/stdc++.h>
using namespace std;

class sudoku_backtrack {
    public:
    int gridSize = 9;
    int boxSize = 3;
    int grid[9][9] = {
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0, 0, 0},
		}; 
    int missingVals;

    sudoku_backtrack(int no_of_missing) {
        missingVals = no_of_missing;
    }

    void fillValues() {
        fillDiagonal();
        fillRemaining(0, boxSize);
        removeDigits();
    }

    void fillDiagonal() {
        for (int i = 0; i < gridSize; i = i + boxSize)
            fillgrid(i, i);
    }

    bool present_in_Row(int row, int num) {
    for (int col = 0; col < gridSize; col++) {
        if (num == grid[row][col]) {
            return true;
        }
    }
    return false;
}

    bool present_in_Col(int col, int num) {
        for (int row = 0; row < gridSize; row++) {
            if (num == grid[row][col]) {
                return true;
            }
        }
        return false;
    }

    bool present_in_Box(int rowStart, int colStart, int digit) {
            for (int i = 0; i < boxSize; i++)
                for (int j = 0; j < boxSize; j++)
                    if (grid[rowStart + i][colStart + j] == digit)
                        return true;

            return false;
        }

    bool isValidCell(int row, int col, int num) {
        return (!(present_in_Row(row, num)) && !(present_in_Col(col, num)) && !(present_in_Box(row - row % boxSize, col - col % boxSize, num)));
    }
    void fillgrid(int row, int col) {
        int num;
        for (int i = 0; i < boxSize; i++) {
            for (int j = 0; j < boxSize; j++) {
                do {
                    num = randomGenerator(gridSize);
                } while (present_in_Box(row, col, num));
                grid[row + i][col + j] = num;
            }
        }
    }

    int randomGenerator(int num) {
        srand(time(0));
        return rand() % num + 1;
    }

    bool fillRemaining(int i, int j) {
        if (j >= gridSize && i < gridSize - 1) {
            i = i + 1;
            j = 0;
        }
        if (i >= gridSize && j >= gridSize) {
            return true;
        }
        if (i < boxSize) {
            if (j < boxSize) {
                j = boxSize;
            }
        } 
        else if (i < gridSize - boxSize) {
            if (j == (int) (i / boxSize) * boxSize)
                j = j + boxSize;
        } 
        else {
            if (j == gridSize - boxSize) {
                i = i + 1;
                j = 0;
                if (i >= gridSize) {
                    return true;
                }
            }
        }

        for (int num = 1; num <= gridSize; num++) {
            if (isValidCell(i, j, num)) {
                grid[i][j] = num;
                if (fillRemaining(i, j + 1))
                    return true;
                grid[i][j] = 0;
            }
        }
        return false;
    }

    void removeDigits() {
        int empty_places = missingVals;
        while (empty_places != 0) {
            int cellId = randomGenerator(gridSize * gridSize);
            int i = (cellId / gridSize);
            int j = cellId % 9;
            if (grid[i][j] != 0) {
                empty_places--;
                grid[i][j] = 0;
            }
        }
    }
    bool solve_sudoku() {
        for (int i = 0; i < gridSize; i++) {
            for (int j =0; j < gridSize; j++) {
                if (grid[i][j] == 0) {
                    for (int k = 1; k < gridSize + 1; k++) {
                        if (isValidCell(i, j, k)) {
                            grid[i][j] = k;
                            if (solve_sudoku()) {
                                return true;
                            }
                            grid[i][j]=0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
};

int main(){
    int empty_cells = 46;
    for (int i = 1; i < 11; i ++) {
        sudoku_backtrack sudoku(empty_cells);
        sudoku.fillValues();  
        auto begin = chrono::high_resolution_clock::now();
        sudoku.solve_sudoku();
        auto end = chrono::high_resolution_clock::now();
        auto elapsed = chrono::duration_cast<chrono::nanoseconds>(end - begin);
        cout << elapsed.count() << endl;
    }
    return 0;
}
