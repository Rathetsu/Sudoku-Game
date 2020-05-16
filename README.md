
# Sudoko Game
Sudoku is a logic-based, number-placement puzzle.
The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid contain all of the digits from 1 to 9. 
This program solves and allows a user to try solving a Sudoku puzzle.



## Algorithm
The code solves the Sudoku board using the **backtracking algorithm**.
The upper-bound *time complexity* is O(n(9^(n\*n))), which is the same time complexity for the naive approach to the problem. However there will be some early pruning so the time taken will be much less than the naive algorithm but the upper-bound time complexity remains the same.



