import grids
from random import randint
from math import *


def pass_grid():
    return grids.grid[randint(1, grids.num_of_grids - 1)]



"""
backtracking.backtracking(game)
solve.print_game(game)
"""


"""
game = [[randint(1, 9) for i in range(9)] for j in range(9)]
"""


"""
def unique_list(lst):
    new_lst = [new_lst.append(item) if item not in new_lst  else 0 for item in lst]
    return new_lst
"""

"""
def valid_game(game):
    for i in range(9):
        for j in range(9):
            row = game[i]
            col = [[game[x][j] for x in range(9)]]
            w = i - (i % 3)
            z = j - (j % 3)
            box = [game[w + k][z : z + 3] for k in range(3)]
            box = [x for r in box for x in r]
            while game[i][j] in row or game[i][j] in col or game[i][j] in box:
                value = game[i][j]
                while game[i][j] == value:
                    game[i][j] = randint(1, 9)
                solve.print_game(game)    
                print("\n____________________________\n")
    return game
"""
#backtracking(game)
#print_game(game)


#print(valid_game(game))
#solve.print_game(game)
