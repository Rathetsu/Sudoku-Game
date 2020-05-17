
# Sudoko Game
Sudoku is a logic-based, number-placement puzzle.
The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid contain all of the digits from 1 to 9. 

### Overview 
The executable file can be found in the dist folder.
The program allows the user to solve a Sudoku board and lets him know if he makes a wrong decision. 
The program features a simple GUI with 2 buttons.

 1. The **Solve** button prints the whole solution of the current board.
 2. The **Restart** button removes all the entries and prints a new grid on the board.



### The Solving Algorithm 
The code solves the Sudoku board using the **backtracking algorithm**.
The upper-bound *time complexity* is O(n(9^(n\*n))), which is the same time complexity for the naive approach to the problem.
However my implementation of the algorithm is efficient enough so the time taken will be much less than the naive algorithm albeit the upper-bound time complexity remaining the same.



