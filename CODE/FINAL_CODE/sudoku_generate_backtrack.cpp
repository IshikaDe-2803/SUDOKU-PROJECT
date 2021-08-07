#include <bits/stdc++.h>
using namespace std;

const int N = 9;

int empty_grid[9][9] = {{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }};

int num_list[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

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

bool generate_sudoku(int grid[N][N], int num_list[N]) {
    for (int i =0; i < N; i++) {
        for (int j =0; j < N; j++) {
            if (grid[i][j] == 0) {
                srand (time(NULL));
                random_shuffle(num_list, num_list + N);
                for (int value = 0; value < N; value++) {
                    if (isValidCell(grid, i, j, num_list[value])) {
                        grid[i][j] =  num_list[value];
                        if (generate_sudoku(grid, num_list)) {
                            return true;
                        }
                        grid[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    generate_sudoku(empty_grid, num_list);
    print_grid(empty_grid);
    return 0;
}