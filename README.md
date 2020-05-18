
  

# Sudoko Game

Sudoku is a logic-based, number-placement puzzle.

The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid contain all of the digits from 1 to 9.

  

### Overview


The program allows the user to solve a Sudoku board and lets him know if he makes a wrong decision.

The program features a simple GUI with 2 buttons.

  

1. The **Solve** button prints the whole solution of the current board.

2. The **Restart** button removes all the entries and prints a new grid on the board.

  

> Note: The GUI is currently buggy and needs future improvement.


### Running The Program

Run the [GAME.py](https://github.com/Rathetsu/Sudoku-Game/blob/master/GAME.py) file for the GUI version of the app.
use `python3 GAME.py`
here is a screenshot of the program at run-time:

![Screenshot of the program at run-time](https://i.imgur.com/FEGqubt.png)
  

### The Solving Algorithm

The code solves the Sudoku board using the **backtracking algorithm**.

The upper-bound time complexity is O(n(9^(n\*n))), which is the same time complexity for the naive approach to the problem.

However my implementation of the algorithm is efficient enough so the time taken will be much less than the naive algorithm albeit the upper-bound time complexity remaining the same.

### Future Development 
In the not so distant future, I will be:
 1. Adding a feature to solve a Sudoku board that a user inputs.
 2. Fixing a couple of visual bugs in the UI.
 3. Replacing the current [generate_problem.py](https://github.com/Rathetsu/Sudoku-Game/blob/master/generate_problem.py) with an actual Sudoku Generator that implements the same backtracking algorithm as it just arbitrarily picks a puzzle from a list of already-made puzzles in [grids.py](https://github.com/Rathetsu/Sudoku-Game/blob/master/grids.py).
