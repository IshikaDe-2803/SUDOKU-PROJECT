package java_sudoku_testing;

import java.util.*;

public class SudokuBrute {
    int[][] grid;
    int gridSize;
    int subGridSize;
    int difficulty;

    SudokuBrute(int gridSize, int difficulty) {
        this.gridSize = gridSize;
        subGridSize = (int) Math.sqrt(gridSize);
        this.difficulty = difficulty;
        grid = new int[gridSize + 1][gridSize + 1];
    }

    public void generateSuduko() {
        fillDiagonalBoxes();

        fillRemainingBoxes(0, subGridSize);

        removeDigits();
    }

    void fillDiagonalBoxes() {
        for (int i = 0; i < gridSize; i = i + subGridSize)
            fillgrid(i, i);
    }

    boolean presentInBox(int rowStart, int colStart, int num) {
        for (int i = 0; i < subGridSize; i++)
            for (int j = 0; j < subGridSize; j++)
                if (grid[rowStart + i][colStart + j] == num)
                    return true;

        return false;
    }

    void fillgrid(int row, int col) {
        int num;
        for (int i = 0; i < subGridSize; i++) {
            for (int j = 0; j < subGridSize; j++) {
                do {
                    num = randomGenerator(gridSize);
                } while (presentInBox(row, col, num));

                grid[row + i][col + j] = num;
            }
        }
    }

    int randomGenerator(int num) {
        return (int) Math.floor((Math.random() * num + 1));
    }

    boolean isValid(int i, int j, int num) {
        return (!presentInRow(i, num) && !presentInCol(j, num)
                && !presentInBox(i - i % subGridSize, j - j % subGridSize, num));
    }

    boolean presentInRow(int i, int num) {
        for (int j = 0; j < gridSize; j++)
            if (grid[i][j] == num)
                return true;
        return false;
    }

    boolean presentInCol(int j, int num) {
        for (int i = 0; i < gridSize; i++)
            if (grid[i][j] == num)
                return true;
        return false;
    }

    boolean fillRemainingBoxes(int i, int j) {
        if (j >= gridSize && i < gridSize - 1) {
            i = i + 1;
            j = 0;
        }
        if (i >= gridSize && j >= gridSize)
            return true;

        if (i < subGridSize) {
            if (j < subGridSize)
                j = subGridSize;
        } else if (i < gridSize - subGridSize) {
            if (j == (int) (i / subGridSize) * subGridSize)
                j = j + subGridSize;
        } else {
            if (j == gridSize - subGridSize) {
                i = i + 1;
                j = 0;
                if (i >= gridSize)
                    return true;
            }
        }

        for (int num = 1; num <= gridSize; num++) {
            if (isValid(i, j, num)) {
                grid[i][j] = num;
                if (fillRemainingBoxes(i, j + 1))
                    return true;

                grid[i][j] = 0;
            }
        }
        return false;
    }

    public int numberOfSpaces() {
        if (difficulty == 0) {
            return 36;
        }
        if (difficulty == 1) {
            return 46;
        }
        if (difficulty == 2) {
            return 52;
        }
        return -1;

    }

    public void removeDigits() {
        int spaces = numberOfSpaces();
        while (spaces != 0) {
            int cellId = randomGenerator(gridSize * gridSize);

            int i = (cellId / gridSize);
            int j = cellId % 9;
            // if (j != 0)
            // j = j - 1;

            if (grid[i][j] != 0) {
                spaces--;
                grid[i][j] = 0;
            }
        }
    }

    public String gridToString() {
        String gridStr = "";
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++)
                gridStr += (Integer.toString(grid[i][j]));
        }
        return gridStr;
    }

    public boolean checkSameRow(int row, int col) {
        if ((int) (row / 9) == (int) (col / 9)) {
            return true;
        }
        return false;
    }

    public boolean checkSameCol(int row, int col) {
        if ((row % 9) == (col % 9)) {
            return true;
        }
        return false;
    }

    public boolean checkSameBox(int row, int col) {
        if (((int) ((row / 9) / 3) == (int) ((col / 9) / 3)) && (((int) ((row % 9) / 3)) == ((int) ((col % 9) / 3)))) {
            return true;
        }
        return false;
    }

    public Set<Character> findAllPossibilities(int zeroPos, String gridStr) {

        Set<Character> presentInSudoku = new HashSet<Character>();
        for (int i = 0; i < gridStr.length(); i++) {
            if (checkSameRow(zeroPos, i) || checkSameCol(zeroPos, i) || checkSameBox(zeroPos, i)) {

                presentInSudoku.add(gridStr.charAt(i));
            }
        }

        Set<Character> allPossibilities = new HashSet<Character>();
        allPossibilities.addAll(Arrays.asList(new Character[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }));
        allPossibilities.removeAll(presentInSudoku);
        return allPossibilities;
    }

    public void solveSudoku(String gridStr) {

        int zeroPos = gridStr.indexOf('0');

        Set<Character> possibilities = findAllPossibilities(zeroPos, gridStr);
        for (Character val : possibilities) {
            if (zeroPos != -1) {
                gridStr = gridStr.substring(0, zeroPos) + val + gridStr.substring(zeroPos + 1, gridStr.length());
                solveSudoku(gridStr);
            } else {
                printSudoku(stringToGrid(gridStr));
            }
        }

    }

    public static int[][] stringToGrid(String gridStr) {
        int[][] gridsolved = new int[9][9];
        int index = 0;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                gridsolved[i][j] = Integer.parseInt(String.valueOf(gridStr.charAt(index)));
                index++;
            }
        }
        return gridsolved;
    }

    public void printSudoku(int[][] puzzle) {
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++)
                System.out.print(puzzle[i][j] + ", ");
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Double time_total = 0.0;
        for (int i = 0; i < 100; i++) {
            System.out.println(i);
            long startTime = System.nanoTime();
            SudokuBrute sudoku = new SudokuBrute(9, 0);
            sudoku.generateSuduko();
            sudoku.printSudoku(sudoku.grid);
            sudoku.solveSudoku(sudoku.gridToString());
            long endTime = System.nanoTime();
            time_total += ((double) (endTime - startTime) / 1000000000);
        }
        System.out.println(time_total / 100);
    }
}
