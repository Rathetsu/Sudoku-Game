import generate_problem
import solve


# Here we assign the list 'game' with the random grid from the grids.py file
game = generate_problem.pass_grid()


# The main driver and the backtracking function
def backtracking(game):
    empty = solve.next_empty(game)
    if not(empty):                  # Base case: We're done once there're no empty squares left.
        return True
    else:
        r, c = empty
    for i in range(1, 10):
        if solve.is_valid(game, i, (r, c)):
            game[r][c] = i

            if backtracking(game):
                return True
            else:
                game[r][c] = 0

    return False


solve.print_game(game)
print("\n___________________________\n")
backtracking(game)
solve.print_game(game)
