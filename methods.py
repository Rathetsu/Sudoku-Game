from math import *

"""
game = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
"""

# A function that prints out a grid in console
def print_game(game):         
    for i in range(len(game)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(len(game[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(str(game[i][j]))
            else:
                print(str(game[i][j]) + " ", end = "")


# A function that finds the next empty square and returns the position in the form of a tuple (col, row)
def next_empty(game):
    for i in range(len(game)):   
        for j in range(len(game[0])):
            if game[i][j] == 0:
                return (i, j)       # (r, c)
    return False


#A function that checks if the entered number is valid
def is_valid(game, number, position):
    #row
    for i in range(9):  
        if game[position[0]][i] == number and position[1] != i:
            return False
    #column
    for i in range(9):
        if game[i][position[1]] == number and position[0] != i:
            return False
    #box
    x = position[1] // 3
    y = position[0] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if game[i][j] == number and (i, j) != position:
                return False
    return True





        


    
