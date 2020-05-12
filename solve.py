from math import *


# A test case that will be replaced by the output of the generating function once the algorithm is tested
game = [
    [4,"_",7,"_",8,6,1,9,"_"],
    ["_",1,5,3,"_","_","_",6,"_"],
    [6,"_",3,"_","_","_",5,2,"_"],
    ["_","_","_","_",6,2,4,3,"_"],
    ["_",4,"_",8,"_",5,"_","_","_"],
    [2,"_",6,"_",3,"_",9,"_",1],
    [1,"_","_","_",5,8,"_",4,9],
    [5,"_","_",7,4,"_",6,"_","_"],
    ["_",6,"_","_",9,"_","_",5,"_"]
]

# A function that prints out the test case above in console
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

# print_game(game)

# A function that finds the next empty square and returns the location in the form of a tuple (col, row)
def next_empty(game):
    for i in range len(game):
        for j in range len(game[0]:
            if game[i][j] == "_":
                return (j, i)       # (col, row)


    
