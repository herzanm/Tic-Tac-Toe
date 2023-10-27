def print_grid(grid):
    print("---------")
    print(f"| {grid[0][0]} {grid[0][1]} {grid[0][2]} |")
    print(f"| {grid[1][0]} {grid[1][1]} {grid[1][2]} |")
    print(f"| {grid[2][0]} {grid[2][1]} {grid[2][2]} |")
    print(f"---------")


def move(grid, player):
    while True:
        user_input = input().split()
        try:
            if playground[int(user_input[0]) - 1][int(user_input[1]) - 1] != '_':
                print("This cell is occupied! Choose another one!")
            else:
                playground[int(user_input[0]) - 1][int(user_input[1]) - 1] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                break
        except ValueError:
            print("You should enter numbers!")
        except TypeError:
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
            continue


def more_than_possible(grid):
    count_of_X = 0
    count_of_O = 0
    for i in grid:
        if i == 'X':
            count_of_X += 1
        elif i == 'O':
            count_of_O += 1
    if abs(count_of_O - count_of_X) > 1:
        return True
    else:
        return False


def winner_x(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] == 'X':
        return True
    elif grid[1][0] == grid[1][1] == grid[1][2] == 'X':
        return True
    elif grid[2][0] == grid[2][1] == grid[2][2] == 'X':
        return True
    elif grid[0][0] == grid[1][0] == grid[2][0] == 'X':
        return True
    elif grid[0][1] == grid[1][1] == grid[2][1] == 'X':
        return True
    elif grid[0][2] == grid[1][2] == grid[2][2] == 'X':
        return True
    elif grid[0][0] == grid[1][1] == grid[2][2] == 'X':
        return True
    elif grid[2][0] == grid[1][1] == grid[0][2] == 'X':
        return True
    else:
        return False


def winner_o(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] == 'O':
        return True
    elif grid[1][0] == grid[1][1] == grid[1][2] == 'O':
        return True
    elif grid[2][0] == grid[2][1] == grid[2][2] == 'O':
        return True
    elif grid[0][0] == grid[1][0] == grid[2][0] == 'O':
        return True
    elif grid[0][1] == grid[1][1] == grid[2][1] == 'O':
        return True
    elif grid[0][2] == grid[1][2] == grid[2][2] == 'O':
        return True
    elif grid[0][0] == grid[1][1] == grid[2][2] == 'O':
        return True
    elif grid[2][0] == grid[1][1] == grid[0][2] == 'O':
        return True
    else:
        return False


def draw(grid):
    if any([y == '_' for x in grid for y in x]):
        return False
    return True


def check_for_end(grid):
    if more_than_possible(grid):
        print("Impossible")
        exit(1)
    elif winner_x(grid) and winner_o(grid):
        print("Impossible")
        exit(1)
    elif winner_x(grid):
        print("X wins")
        exit(1)
    elif winner_o(grid):
        print("O wins")
        exit(1)
    elif draw(grid):
        print("Draw")
        exit(1)


playground = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
turn = 'X'
# main
while True:
    print_grid(playground)
    check_for_end(playground)
    move(playground, turn)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
