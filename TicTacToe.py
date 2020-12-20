import random


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# This function resets the board so all values are blank
# (removes the numbers 1-9 as they were just there as instructions)
def reset_board(board):
    board.update({}.fromkeys(board, ' '))


# This function asks the player where they would like to place their mark.
def player_move():
    global turn
    while True:
        try:
            player_choice = int(input("Select a number between 1 and 9 to make your move: "))
            if player_choice not in range(0, 9):
                print("Selection must be a number between 1-9.")
            elif board_now[player_choice] == ' ':
                board_now[player_choice] = player_symbol
                break
            else:
                print("Try again. That position is taken. ")
        except ValueError:
            print("Selection must be a number between 1-9.")

    display_board(board_now)
    turn = "AI"


# This function chooses the AI' first move. We take one of the top corners
# If the AI went second then 7 may be taken, so we try two corners
def ai_first_move():
    global turn
    if board_now[7] == " ":
        board_now[7] = AI_symbol
        display_board(board_now)
        turn = "Player"
    elif board_now[9] == " ":
        board_now[9] = AI_symbol
        display_board(board_now)
        turn = "Player"


# This is the AI second move. If centre is blank take there. Otherwise, take a corner.
def ai_second_move():
    global turn
    if board_now[5] == " ":
        board_now[5] = AI_symbol
        display_board(board_now)
        turn = "Player"
    # If AI went second and it is its second move then at this stage there will be 3 marks on the board.
    # We know the centre is one, because we can't get to this step unless centre is taken
    # That means we need to offer a choice of three corners, in case the first 2 we try are taken
    elif board_now[7] == " ":
        board_now[7] = AI_symbol
        display_board(board_now)
        turn = "Player"

    elif board_now[9] == " ":
        board_now[9] = AI_symbol
        display_board(board_now)
        turn = "Player"

    elif board_now[1] == " ":
        board_now[1] = AI_symbol
        display_board(board_now)
        turn = "Player"


def game_moves():
    if turn == "Player":
        player_move()

    # AI's first move if it is AI turn first
    elif turn == "AI" and counter == 1:
        print("AI's move is:")
        ai_first_move()
    # AI first move if AI is second
    elif turn == "AI" and counter == 2:
        print("AI's move is:")
        ai_first_move()

    # AI's second move if AI is first to go
    elif turn == "AI" and counter == 3:
        print("AI's move is:")
        ai_second_move()

    # AI's second move if AI is second to go
    elif turn == "AI" and counter == 4:
        print("AI's move is:")
        ai_second_move()


# We need to define all winning states.
# This includes anywhere where there are 3 matching marks in a row, column, or diagonal
def check_winner():
    # If any row has equal values that are not blank, game is over
    if board_now[7] == board_now[8] == board_now[9] != ' ':
        print("Game over")
        return True

    elif board_now[4] == board_now[5] == board_now[6] != ' ':
        print("Game over")
        return True

    elif board_now[1] == board_now[2] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    # If any column has equal values that are not blank, game over
    elif board_now[7] == board_now[4] == board_now[1] != ' ':
        print("Game over")
        return True

    elif board_now[8] == board_now[5] == board_now[2] != ' ':
        print("Game over")
        return True

    elif board_now[9] == board_now[6] == board_now[3] != ' ':
        print("Game over")
        return True

    # If any diagonal line has equal values that are not blank, game over
    elif board_now[7] == board_now[5] == board_now[3] != ' ':
        print("Game over")
        return True

    elif board_now[9] == board_now[5] == board_now[1] != ' ':
        print("Game over")
        return True


def check_draw():
    for i in board_now:
        if i == ' ':
            return True


# Defines our board as a dictionary with the numbers 1-9 on the keypad representing positions.
# We originally match the key and value so the player can see how the game works
board_now = {7: "7", 8: "8", 9: "9",
             4: "4", 5: "5", 6: "6",
             1: "1", 2: "2", 3: "3"}

# We will also print some instructions here, with a diagram showing how to reference board positions with numbers
print("You can reference positions on the board using the corresponding numbers on the keyboard, as shown below.")
display_board(board_now)

# This asks the player to choose to play as either X or O
while True:
    player_symbol = (input("Please select either X or O? "))
    if player_symbol == "X" or player_symbol == "x":
        AI_symbol = "O"
        print("You have chosen: ", player_symbol, ",and the AI will be: ", AI_symbol)
        break
    elif player_symbol == "o" or player_symbol == "O":
        AI_symbol = "X"
        print("You have chosen: ", player_symbol, ",and the AI will be: ", AI_symbol)
        break
    else:
        print("Try again. You must press X or O on the keyboard to make your selection")
        continue

reset_board(board_now)
turn = None
counter = 0

first_turn = random.randint(1, 2)
if first_turn > 1:
    print("You may have the first turn")
    turn = "Player"
else:
    print("The AI will go first this time")
    turn = "AI"

while not check_winner() and not check_draw():
    game_moves()
    counter += 1

if check_draw():
    print("We have a draw!")

if check_winner():
    print("The winner is", )
