#include <bits/stdc++.h>

using namespace std;

class SudokuGenerator {
    public :
    int boardSize = 9;
    int boxSize = 3;
    int board[9][9] = {
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

    SudokuGenerator(int no_of_missing) {
        missingVals = no_of_missing;
    }

    void fillValues() {
        fillDiagonal();
        fillRemaining(0, boxSize);
        removeDigits();
    }

    void fillDiagonal() {
        for (int i = 0; i < boardSize; i = i + boxSize)
            fillBoard(i, i);
    }

    bool boardUnfilled(int rowStart, int colStart, int num) {
        for (int i = 0; i < boxSize; i++)
            for (int j = 0; j < boxSize; j++)
                if (board[rowStart + i][colStart + j] == num)
                    return false;
        return true;
    }

    void fillBoard(int row, int col) {
        int num;
        for (int i = 0; i < boxSize; i++) {
            for (int j = 0; j < boxSize; j++) {
                do {
                    num = randomGenerator(boardSize);
                } while (!boardUnfilled(row, col, num));

                board[row + i][col + j] = num;
            }
        }
    }

    int randomGenerator(int num) {
        srand(time(0));
        return rand() % num + 1;
    }

    bool isValid(int i, int j, int num) {
        return (rowUnfilled(i, num) && colUnfilled(j, num)
                && boardUnfilled(i - i % boxSize, j - j % boxSize, num));
    }

    bool rowUnfilled(int i, int num) {
        for (int j = 0; j < boardSize; j++)
            if (board[i][j] == num)
                return false;
        return true;
    }

    bool colUnfilled(int j, int num) {
        for (int i = 0; i < boardSize; i++)
            if (board[i][j] == num)
                return false;
        return true;
    }

    bool fillRemaining(int i, int j) {
        if (j >= boardSize && i < boardSize - 1) {
            i = i + 1;
            j = 0;
        }
        if (i >= boardSize && j >= boardSize) {
            return true;
        }
        if (i < boxSize) {
            if (j < boxSize) {
                j = boxSize;
            }
        } 
        else if (i < boardSize - boxSize) {
            if (j == (int) (i / boxSize) * boxSize)
                j = j + boxSize;
        } 
        else {
            if (j == boardSize - boxSize) {
                i = i + 1;
                j = 0;
                if (i >= boardSize) {
                    return true;
                }
            }
        }

        for (int num = 1; num <= boardSize; num++) {
            if (isValid(i, j, num)) {
                board[i][j] = num;
                if (fillRemaining(i, j + 1))
                    return true;
                board[i][j] = 0;
            }
        }
        return false;
    }

    void removeDigits() {
        int empty_places = missingVals;
        while (empty_places != 0) {
            int cellId = randomGenerator(boardSize * boardSize);
            int i = (cellId / boardSize);
            int j = cellId % 9;
            if (board[i][j] != 0) {
                empty_places--;
                board[i][j] = 0;
            }
        }
    }

    vector<vector<int>> getSudokuQuestion() {
        vector<vector<int>> questionBoard;
        for (int i = 0; i < boardSize; i++) {
            vector<int> row;
            for (int j = 0; j < boardSize; j++) {
                row.push_back(board[i][j]);
            }
            questionBoard.push_back(row);
        }
        return questionBoard;
    }
};

