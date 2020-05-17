import solver
import methods
import generate_problem
from time import *
from tkinter import *

MARGIN = 20  # Pixels around the board.
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the board.


class Board(Frame):
    
    game = generate_problem.pass_grid()
    empty_cells = 0
    for i in range(9):
        for j in range(9):
            if game[i][j] == 0:
                empty_cells += 1

    def __init__(self, parent):
        self.parent = parent
        self.row = 0
        self.col = 0
        Frame.__init__(self, parent)
        self.__initUI()
    
    # A function that draws the main grid split into 9 boxes each split into 9 cells.
    def draw_board(self):
        for i in range(10):

            color = "black" if i % 3 == 0 else "slate gray"

            x1 = MARGIN + i * SIDE
            y1 = MARGIN
            x2 = MARGIN + i * SIDE
            y2 = HEIGHT - MARGIN
            self.canvas.create_line(x1, y1, x2, y2, fill = color)

            x1 = MARGIN
            y1 = MARGIN + i * SIDE
            x2 = WIDTH - MARGIN
            y2 = MARGIN + i * SIDE
            self.canvas.create_line(x1, y1, x2, y2, fill = color)

    # A function that fills the board with the game for the user to solve.
    def pass_game(self):
        self.canvas.delete("numbers")
        self.canvas.delete("wrong_number")
        for i in range(9):
            for j in range(9):
                number = self.game[i][j]
                if number != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas.create_text(x, y, text = number, tags = "numbers", fill = "black")

    # A function that highlights the selected cell with the left mouse button.
    def highlighted(self):
        self.canvas.delete("highlighted")
        self.canvas.delete("wrong_highlight")
        self.canvas.delete("wrong_number")
        if self.row >= 0 and self.col >= 0:
            x1 = MARGIN + self.col * SIDE + 1
            y1 = MARGIN + self.row * SIDE + 1
            x2 = MARGIN + (self.col + 1) * SIDE - 1
            y2 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(x1, y1, x2, y2, outline = "blue", tags = "highlighted")

    # A function that highlights the cell and fills it red. Used when user enters a wrong answer.
    def wrong_highlighted(self):
        self.canvas.delete("highlighted")
        self.canvas.delete("wrong_highlight")
        if self.row >= 0 and self.col >= 0:
            x1 = MARGIN + self.col * SIDE + 1
            y1 = MARGIN + self.row * SIDE + 1
            x2 = MARGIN + (self.col + 1) * SIDE - 1
            y2 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(x1, y1, x2, y2, outline = "red", tags = "wrong_highlight")

    # A function that displays a "Victory!" message.
    def victory():
        x1 = y1 = MARGIN + SIDE * 2
        x2 = y2 = MARGIN + SIDE * 7
        self.canvas.create_oval(x1, y1, x2, y2, tags = "victory", fill = "green", outline = "green")
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y, text = "VICTORY!", tags = "victory", fill = "white", font = ("Times", 32))

    # A function that takes the number inputed by the user.
    def num_input(self, event):
        if self.row >= 0 and self.col >= 0 and event.char in "123456789":
            x = MARGIN + self.col * SIDE + SIDE / 2
            y = MARGIN + self.row * SIDE + SIDE / 2
            if methods.is_valid(self.game, int(event.char), (self.row, self.col)):
                self.canvas.delete("wrong_highlight")
                self.canvas.delete("wrong_number")
                self.canvas.create_text(x, y, text = int(event.char), tags = "numbers", fill = "blue")
                self.highlighted()
                empty_cells -= 1
            else:
                self.wrong_highlighted()
                self.canvas.create_text(x, y, text = int(event.char), tags = "wrong_number", fill = "red")
            self.col = -1   
            self.row = -1
            if empty_cells <= 0:
                self.victory()

    # A function that removes the user's answers and returns the board to the original state.
    def clear_answers(self):
        game = generate_problem.pass_grid()
        self.canvas.delete("numbers")
        self.canvas.delete("wrong_number")
        self.canvas.delete("wrong_highlight")
        self.canvas.delete("highlighted")
        self.canvas.delete("victory")
        self.game = generate_problem.pass_grid()
        self.pass_game()

    # A function that will give us the X & Y coordinates of the cell which the user clicked.
    def is_clicked(self, event):
        x, y = event.x, event .y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            # Get row and col numbers from x,y coordinates
            row = (y - MARGIN) // SIDE           
            col = (x - MARGIN) // SIDE
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game[row][col] == 0:
                self.row, self.col = row, col
            self.highlighted()
     
    def print_solution(self):
        solver.backtracking(self.game)
        self.pass_game()

    # The logic for the actual UI
    def __initUI(self):
        self.parent.title("Sudoku Game")
        self.pack(fill = BOTH, expand = 1)
        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
        self.canvas.pack(fill = BOTH, side = TOP)
        clear_button = Button(self, text = "Restart", command = self.clear_answers)
        clear_button.pack(fill = BOTH, side = BOTTOM)
        solve_button = Button(self, text = "Solve", command = self.print_solution)
        solve_button.pack(fill = BOTH, side = BOTTOM)
        self.draw_board()
        self.pass_game()
        self.canvas.bind("<Button-1>", self.is_clicked)
        self.canvas.bind("<Key>", self.num_input)


root = Tk()
Board(root)
root.geometry("%dx%d" % (WIDTH, HEIGHT + 60))
root.mainloop()