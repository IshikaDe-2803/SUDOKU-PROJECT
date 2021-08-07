import java.util.*;

public class generateSudokuBacktracking{
	
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

	public static boolean generateSudoku(int[][] grid, ArrayList<Integer> numbers){
		int gridSize = grid.length;
		int start = 0;

		for (int row = start; row < gridSize; row++){
			for (int col = start; col < gridSize; col++){
				if (grid[row][col] == 0){
					Collections.shuffle(numbers);
					for (int k = start; k < numbers.size(); k++){
						int digit = numbers.get(k);
						if (isValidCell(grid, row, col, digit)){
							grid[row][col] =  digit;
							if (generateSudoku(grid, numbers)){
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
		int[][] emptyGrid = {{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
						 	 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
							 { 0, 0, 0, 0, 0, 0, 0, 0, 0 }};
		ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
		generateSudoku(emptyGrid, numbers);
	}
}

