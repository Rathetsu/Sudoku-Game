from solve import *


# The main driver and the backtracking function
def backtracking(game):
    empty = next_empty(game)
    if not(empty):                  # Base case: We're done once there're no empty squares left.
        return True
    else:
        r, c = empty
    for i in range(1, 10):
        if is_valid(game, i, (r, c)):
            game[r][c] = i

            if backtracking(game):
                return True
            else:
                game[r][c] = 0

    return False

"""
print_game(game)
print("\n___________________________\n")
backtracking(game)
print_game(game)
"""