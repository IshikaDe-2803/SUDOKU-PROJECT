import java.util.*;

public class generatingSudokuBacktracking{
	public static void printSudoku(int[][] grid){
		for (int row = 0; row < grid.length; row++){
			for (int col = 0; col < grid.length; col++){
				System.out.print(grid[row][col] + " ");
			}
			System.out.println();
		}
	}


	public static boolean presentInRow(int[][] grid, int row, int digit){
		for (int col = 0; col < grid.length; col++)	{
			if (digit == grid[row][col]){
				return true;
			}
		}
		return false;
	}

	
	public static boolean presentInCol(int[][] grid, int col, int digit){
		for (int row = 0; row < grid.length; row++){
			if (digit == grid[row][col]){
				return true;
			}
		}
		return false;
	}

	public static boolean presentInBox(int[][] grid, int row, int col, int digit){
		int boxSize = 3;
		int subRow = (row / boxSize) * boxSize;
		int subCol = (col / boxSize) * boxSize;
		for (int i = 0; i < boxSize; i++){
			for (int j = 0; j < boxSize; j++){
				if (digit == grid[subRow + i][subCol + j]){
					return true;
				}
			}
		}
		return false;
	}


	public static boolean isValidCell(int[][] grid, int row, int col, int digit){
		return ((!presentInRow(grid, row, digit)) && (!presentInCol(grid, col, digit)) && (!presentInBox(grid, row, col, digit)));
	}

	public static boolean solveSudoku(int[][] grid){
		int gridSize = grid.length;
		int start = 0;
		for (int row = start; row < gridSize; row++){
			for (int col = start; col < gridSize; col++){
				if (grid[row][col] == 0){
					for (int digit = start + 1; digit <= gridSize; digit++){
						if (isValidCell(grid, row, col, digit)){
							grid[row][col] =  digit;
							if (solveSudoku(grid)){
								return true;
							}
							grid[row][col] = 0;
						}
					}
					return false;
				}
			}
		}
		printSudoku(grid);
		return true;	
	}


	public static void main(String[] args){
		int[][] grid = {{ 8, 0, 0, 0, 0, 0, 0, 0, 0 },
						{ 0, 0, 3, 6, 0, 0, 0, 0, 0 },
						{ 0, 7, 0, 0, 9, 0, 2, 0, 0 },
						{ 0, 5, 0, 0, 0, 7, 0, 0, 0 },
						{ 0, 0, 0, 0, 4, 5, 7, 0, 0 },
						{ 0, 0, 0, 1, 0, 0, 0, 3, 0 },
						{ 0, 0, 1, 0, 0, 0, 0, 6, 8 },
						{ 0, 0, 8, 5, 0, 0, 0, 1, 0 },
						{ 0, 9, 0, 0, 0, 0, 4, 0, 0 }};

		solveSudoku(grid);
	}
}
