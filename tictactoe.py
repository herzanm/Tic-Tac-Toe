# write your code here
user_input = list("         ")

def outputDesk(user_input):
        print("---------")
        print(f"""| {user_input[0]} {user_input[1]} {user_input[2]} |
| {user_input[3]} {user_input[4]} {user_input[5]} |
| {user_input[6]} {user_input[7]} {user_input[8]} |""")
        print("---------")

#  Exceptions:
def checkIfNumbers(user_move):
    if ''.join(user_move).isdigit() == False:
        print("You should enter numbers!")
        return False
    return True

def checkIfInScope(user_move):
    for x in user_move:
        if int(x) < 1 or int(x) > 3:
            print("Coordinates should be from 1 to 3")
            return False
    return True

def coordinatesTransfer(user_move):
    if "".join(user_move) == "11":
        return 0
    elif "".join(user_move) == "12":
        return 1
    elif "".join(user_move) == "13":
        return 2
    elif "".join(user_move) == "21":
        return 3
    elif "".join(user_move) == "22":
        return 4
    elif "".join(user_move) == "23":
        return 5
    elif "".join(user_move) == "31":
        return 6
    elif "".join(user_move) == "32":
        return 7
    elif "".join(user_move) == "33":
        return 8

def checkIfOccupied(position):
    if user_input[position] == "X" or user_input[position] == "O":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True

#  Possible outcomes
def X_winning(user_input):
        #  Horizontal win
        if user_input[0] == "X" and user_input[1] == "X" and user_input[2] == "X":
                return True
        elif user_input[3] == "X" and user_input[4] == "X" and user_input[5] == "X":
                return True
        elif user_input[6] == "X" and user_input[7] == "X" and user_input[8] == "X":
                return True
        #  Vertical win
        elif user_input[0] == "X" and user_input[3] == "X" and user_input[6] == "X":
                return True
        elif user_input[1] == "X" and user_input[4] == "X" and user_input[7] == "X":
                return True
        elif user_input[2] == "X" and user_input[5] == "X" and user_input[8] == "X":
                return True
        #  Diagonal win
        elif user_input[0] == "X" and user_input[4] == "X" and user_input[8] == "X":
                return True
        elif user_input[2] == "X" and user_input[4] == "X" and user_input[6] == "X":
                return True
        else:
                return False

def O_winning(user_input):
        #  Horizontal win
        if user_input[0] == "O" and user_input[1] == "O" and user_input[2] == "O":
                return True
        elif user_input[3] == "O" and user_input[4] == "O" and user_input[5] == "O":
                return True
        elif user_input[6] == "O" and user_input[7] == "O" and user_input[8] == "O":
                return True
        #  Vertical win
        elif user_input[0] == "O" and user_input[3] == "O" and user_input[6] == "O":
                return True
        elif user_input[1] == "O" and user_input[4] == "O" and user_input[7] == "O":
                return True
        elif user_input[2] == "O" and user_input[5] == "O" and user_input[8] == "O":
                return True
        #  Diagonal win
        elif user_input[0] == "O" and user_input[4] == "O" and user_input[8] == "O":
                return True
        elif user_input[2] == "O" and user_input[4] == "O" and user_input[6] == "O":
                return True
        else:
                return False

def draw(user_input):
    count = 0
    for x in user_input:
        if x == 'X' or x == "O":
            count += 1
    if count == 9:
            return True
    else:
            return False

def impossible(user_input, X_winning, O_winning):
    count_of_X = 0
    count_of_O = 0
    for x in user_input:
        if x == 'X':
            count_of_X += 1

        if x == 'O':
            count_of_O += 1

    difference = abs(count_of_O - count_of_X)
    if difference >= 2:
            print("Impossible")
            return bool(True)
    else:
            if X_winning(user_input) == True and O_winning(user_input) == True:
                        print("Impossible")
                        return bool(True)
            else:
                        return bool(False)

#  Going through possible outcomes
def isItOver(user_input):
    if impossible(user_input, X_winning, O_winning) == False:
        if X_winning(user_input):
            print("X wins")
            return True
        elif O_winning(user_input):
            print("O wins")
            return True
        elif draw(user_input) == True:
            print("Draw")
            return True
        else:
            return False
    else:
        return True

outputDesk(user_input)

mark = "X"

while isItOver(user_input) == False:
    user_move = input("Enter the coordinates: ").split()
    if checkIfNumbers(user_move) == False:
        continue
    else:
        if checkIfInScope(user_move) == False:
            continue
        else:
            position = coordinatesTransfer(user_move)
            if checkIfOccupied(position) == False:
                continue
            else:
                user_input[position] = mark
                outputDesk(user_input)
                if mark == "X":
                    mark = "O"
                else:
                    mark = "X"


