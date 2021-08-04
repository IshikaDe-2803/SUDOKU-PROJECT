#include <bits/stdc++.h>
using namespace std;

const int N = 9;
int puzzle[9][9] = {{ 8, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 3, 6, 0, 0, 0, 0, 0 },
						{ 0, 7, 0, 0, 9, 0, 2, 0, 0 },
						{ 0, 5, 0, 0, 0, 7, 0, 0, 0 },
						{ 0, 0, 0, 0, 4, 5, 7, 0, 0 },
						{ 0, 0, 0, 1, 0, 0, 0, 3, 0 },
						{ 0, 0, 1, 0, 0, 0, 0, 6, 8 },
						{ 0, 0, 8, 5, 0, 0, 0, 1, 0 },
						{ 0, 9, 0, 0, 0, 0, 4, 0, 0 }};

void print_grid(int arr[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
}



bool present_in_Row(int grid[N][N], int row, int num) {
    for (int col = 0; col < N; col++) {
        if (num == grid[row][col]) {
            return true;
        }
    }
    return false;
}

bool present_in_Col(int grid[N][N], int col, int num) {
    for (int row = 0; row < N; row++) {
        if (num == grid[row][col]) {
            return true;
        }
    }
    return false;
}

bool present_in_Box(int grid[N][N], int row, int col, int num) {
    int box_size = int(sqrt(N));
    int r = (row/box_size) * box_size;
    int c = (col/box_size) * box_size;
    for (int i = 0; i < box_size; i++) {
        for (int j = 0; j < box_size; j++) {
            if (num == grid[r + i][c + j]) {
                return true;
            }
        }
    }
    return false;
}

bool isValidCell(int grid[N][N], int row, int col, int num) {
    return (!(present_in_Row(grid, row, num)) && !(present_in_Col(grid, col, num)) && !(present_in_Box(grid, row, col, num)));
}

bool solve_sudoku(int grid[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j =0; j < N; j++) {
            if (grid[i][j] == 0) {
                for (int k = 1; k < N + 1; k++) {
                    if (isValidCell(grid, i,j, k)) {
                        grid[i][j] = k;
                        if (solve_sudoku(grid)){
                            return true;
                        }
                        grid[i][j]=0;
                    }
                }
                return false;
            }
        }
    }
    print_grid(grid);
    return true;
}


int main() {
    
    solve_sudoku(puzzle);
    return 0;
}