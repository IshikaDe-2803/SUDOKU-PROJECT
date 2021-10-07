package java_sudoku_testing;
// import java.io.*;

public class SudokuBacktracking {
	int[][] grid;
	int gridSize;
	int subGridSize;
	int difficulty;

	SudokuBacktracking(int gridSize, int difficulty) {
		this.gridSize = gridSize;
		subGridSize = (int) Math.sqrt(gridSize);
		this.difficulty = difficulty;
		grid = new int[gridSize + 1][gridSize + 1];
	}

	public void generateSudoku() {
		fillDiagonalBoxes();

		fillRemainingBoxes(0, subGridSize);

		removeDigits();
	}

	void fillDiagonalBoxes() {
		for (int i = 0; i < gridSize; i = i + subGridSize)
			fillgrid(i, i);
	}

	boolean presentInBox(int rowStart, int colStart, int digit) {
		for (int i = 0; i < subGridSize; i++)
			for (int j = 0; j < subGridSize; j++)
				if (grid[rowStart + i][colStart + j] == digit)
					return true;

		return false;
	}

	void fillgrid(int row, int col) {
		int digit;
		for (int i = 0; i < subGridSize; i++) {
			for (int j = 0; j < subGridSize; j++) {
				do {
					digit = randomGenerator(gridSize);
				} while (presentInBox(row, col, digit));

				grid[row + i][col + j] = digit;
			}
		}
	}

	int randomGenerator(int digit) {
		return (int) Math.floor((Math.random() * digit + 1));
	}

	boolean isValid(int i, int j, int digit) {
		return (!presentInRow(i, digit) && !presentInCol(j, digit)
				&& !presentInBox(i - i % subGridSize, j - j % subGridSize, digit));
	}

	boolean presentInRow(int i, int digit) {
		for (int j = 0; j < gridSize; j++)
			if (grid[i][j] == digit)
				return true;
		return false;
	}

	boolean presentInCol(int j, int digit) {
		for (int i = 0; i < gridSize; i++)
			if (grid[i][j] == digit)
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

		for (int digit = 1; digit <= gridSize; digit++) {
			if (isValid(i, j, digit)) {
				grid[i][j] = digit;
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
			return 67;
		}
		return -1;

	}

	public void removeDigits() {
		int spaces = numberOfSpaces();
		while (spaces != 0) {
			int cellId = randomGenerator(gridSize * gridSize);

			int i = (cellId / gridSize);
			int j = cellId % 9;
			if (j != 0)
				j = j - 1;

			if (grid[i][j] != 0) {
				spaces--;
				grid[i][j] = 0;
			}
		}
	}

	public void printSudoku() {
		for (int i = 0; i < gridSize; i++) {
			for (int j = 0; j < gridSize; j++)
				System.out.print(grid[i][j] + ", ");
			System.out.println();
		}
		System.out.println();
	}

	public boolean solveSudoku() {
		int start = 0;
		for (int row = start; row < gridSize; row++) {
			for (int col = start; col < gridSize; col++) {
				if (grid[row][col] == 0) {
					for (int digit = start + 1; digit <= gridSize; digit++) {
						if (isValid(row, col, digit)) {
							grid[row][col] = digit;
							if (solveSudoku()) {
								return true;
							}
							grid[row][col] = 0;
						}
					}
					return false;
				}
			}
		}
		printSudoku();
		return true;
	}

	public static void main(String[] args) {
		Double time_total = 0.0;
		for (int i = 0; i < 100; i++) {
			long startTime = System.nanoTime();
			SudokuBacktracking sudoku = new SudokuBacktracking(9, 2);
			sudoku.generateSudoku();
			sudoku.printSudoku();
			sudoku.solveSudoku();
			long endTime = System.nanoTime();
			time_total += ((double) (endTime - startTime) / 1000000000);
		}
		System.out.println(time_total / 100);
	}
}