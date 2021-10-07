import java.util.*;

public class solveSudokuBruteForce {

	public static String gridToString(char[][] grid) {
		String gridStr = "";
		for (int i = 0; i < 9; i++) {
			String row = new String(grid[i]);
			gridStr = gridStr.concat(row);
		}
		return gridStr;
	}

	public static boolean checkSameRow(int row, int col) {
		if ((int) (row / 9) == (int) (col / 9)) {
			return true;
		}
		return false;
	}

	public static boolean checkSameCol(int row, int col) {
		if ((row % 9) == (col % 9)) {
			return true;
		}
		return false;
	}

	public static boolean checkSameBox(int row, int col) {
		if (((int) ((row / 9) / 3) == (int) ((col / 9) / 3)) && (((int) ((row % 9) / 3)) == ((int) ((col % 9) / 3)))) {
			return true;
		}
		return false;
	}

	public static Set<Character> findAllPossibilities(int zeroPos, String gridStr) {

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

	public static void solveSudoku(String gridStr) {

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

	public static char[][] stringToGrid(String gridStr) {
		char[][] grid = new char[9][9];
		int index = 0;
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				grid[i][j] = gridStr.charAt(index);
				index++;
			}
		}
		return grid;
	}

	public static void printSudoku(char[][] grid) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				System.out.print(grid[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		char[][] grid = { { '5', '3', '0', '0', '7', '0', '0', '0', '0' },
				{ '6', '0', '0', '1', '9', '5', '0', '0', '0' }, { '0', '9', '8', '0', '0', '0', '0', '6', '0' },
				{ '8', '0', '0', '0', '6', '0', '0', '0', '3' }, { '4', '0', '0', '8', '0', '3', '0', '0', '1' },
				{ '7', '0', '0', '0', '2', '0', '0', '0', '6' }, { '0', '6', '0', '0', '0', '0', '2', '8', '0' },
				{ '0', '0', '0', '4', '1', '9', '0', '0', '5' }, { '0', '0', '0', '0', '8', '0', '0', '7', '9' } };

		solveSudoku(gridToString(grid));

	}
}
