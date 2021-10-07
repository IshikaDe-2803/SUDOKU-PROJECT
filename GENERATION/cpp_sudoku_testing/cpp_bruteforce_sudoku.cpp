#include<bits/stdc++.h>
#include<chrono>
#include "Cpp_sudoku_generator.h"
using namespace std;

const int N = 9;
	
string gridToString(vector<vector<int>> grid){
    string grid_string = "";
    for (int i = 0; i < 9; i++){
        string row = "";
        for (int j = 0; j < 9; j++) {
            row += to_string(grid[i][j]);
        }
        grid_string += row;
        row = "";
    }
    return grid_string;    
}

bool checkSameRow(int row, int col){
    if ((int)(row / 9) == (int)(col / 9)){
        return true;
    }
    return false;
}

bool checkSameCol(int row, int col){
    if ((row % 9) == (col % 9)){
        return true;
    }
    return false;
}

bool checkSameBox(int row, int col){
    if (((int)((row / 9)/ 3) == (int)((col / 9) / 3)) && (((int)((row % 9) / 3)) == ((int)((col % 9) / 3)))){
        return true;
    }
    return false;
}

set<char> findAllPossibilities(int zeroPos, string gridStr) {
    set<char> presentInSudoku;
    for (int i = 0; i < gridStr.length(); i++){
        if (checkSameRow(zeroPos, i) || checkSameCol(zeroPos, i) || checkSameBox(zeroPos, i)){
            presentInSudoku.insert(gridStr[i]);
        }
    }
    set<char> allPossibilities;
    set<char> possibilities;
    allPossibilities.insert({'0','1','2','3','4','5','6','7','8','9'});
    set_difference(allPossibilities.begin(), allPossibilities.end(), presentInSudoku.begin(), presentInSudoku.end(), inserter(possibilities, possibilities.end()));   
    return possibilities;
}

vector<vector<char>> stringToGrid(string gridStr) {
    vector<vector<char>> grid;
    int index = 0;
    for (int i = 0; i < 9; i++){
        vector<char> row;
        for (int j = 0; j < 9;j++){
            row.push_back(gridStr[index]);
            index++;
        }
        grid.push_back(row);
    }
    return grid;
}

void solveSudoku(string gridStr){
    int zeroPos = gridStr.find('0');
    set<char> possibilities = findAllPossibilities(zeroPos, gridStr);
    for (char val: possibilities){
            if(zeroPos == string::npos) {
                break;
                //print_grid(stringToGrid(gridStr));
            }     
            gridStr = gridStr.substr(0, zeroPos) + val + gridStr.substr(zeroPos + 1, gridStr.length() - zeroPos - 1);
            solveSudoku(gridStr);		
    }
}

int main(){
    int empty_cells = 36;
    auto time_sum = 0;
    for (int i = 0; i < 20; i++) {
        SudokuGenerator sudoku(empty_cells);
        sudoku.fillValues();
        vector<vector<int>> grid = sudoku.getSudokuQuestion();
        auto begin = chrono::high_resolution_clock::now();
        solveSudoku(gridToString(grid));
        auto end = chrono::high_resolution_clock::now();
        auto elapsed = chrono::duration_cast<chrono::nanoseconds>(end - begin);
        time_sum += elapsed.count();
    }
    cout << time_sum / 20;
    return 0;
}

