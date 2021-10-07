#include<bits/stdc++.h>
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

void print_grid(vector<vector<char>> arr) {
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++) 
            cout << arr[i][j] << " ";
        cout << endl;
    }
}

void solveSudoku(string gridStr){
    int zeroPos = gridStr.find('0');
    set<char> possibilities = findAllPossibilities(zeroPos, gridStr);
    for (char val: possibilities){
            if(zeroPos == string::npos) {
                print_grid(stringToGrid(gridStr));
            }     
            gridStr = gridStr.substr(0, zeroPos) + val + gridStr.substr(zeroPos + 1, gridStr.length() - zeroPos - 1);
            solveSudoku(gridStr);		
    }
}

int main(){
    vector<vector<int>> grid = {{5, 3, 0, 0, 7, 0, 0, 0, 0},
                {6, 0, 0, 1, 9, 5, 0, 0, 0},
                {0, 9, 8, 0, 0, 0, 0, 6, 0},
                {8, 0, 0, 0, 6, 0, 0, 0, 3},
                {4, 0, 0, 8, 0, 3, 0, 0, 1},
                {7, 0, 0, 0, 2, 0, 0, 0, 6},
                {0, 6, 0, 0, 0, 0, 2, 8, 0},
                {0, 0, 0, 4, 1, 9, 0, 0, 5},
                {0, 0, 0, 0, 8, 0, 0, 7, 9}};
    solveSudoku(gridToString(grid));
    return 0;
}

