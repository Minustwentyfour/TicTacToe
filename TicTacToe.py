import random


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# This function resets the board so all values are blank
# (removes the numbers 1-9 as they were just there as instructions)
def reset(board):
    board.update({}.fromkeys(board, ' '))


# This function asks the player where they would like to place their mark.
def player_move():
    while True:
        player_choice = int(input("Select a number between 1 and 9 to make your move: "))
        if board_now[player_choice] == ' ':
            board_now[player_choice] = player_symbol
            break
        elif 1 <= player_choice <= 9:
            return player_move
        else:
            print("Try again. You must press a number between 1-9 on the keyboard to make your selection")
            continue


# We need to define all winning states.
# This includes anywhere where there are 3 matching marks in a row, column, or diagonal
def winning():
    # Set winner to be blank until we compute who made the last move
    winner = " "
    # If player went first (and count starts at 0) and turn_count is an even number then it must be the player's turn
    if first_turn > 1 and (turn_count % 2) == 0:
        winner = "Player"
    else:
        winner = "AI"

    # If any row has equal values that are not blank, game is over
    if board_now[7] == board_now[8] == board_now[9] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    elif board_now[4] == board_now[5] == board_now[6] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    elif board_now[1] == board_now[2] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    # If any column has equal values that are not blank, game over
    elif board_now[7] == board_now[4] == board_now[1] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    elif board_now[8] == board_now[5] == board_now[2] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    elif board_now[9] == board_now[6] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    # If any diagonal line has equal values that are not blank, game over
    elif board_now[7] == board_now[5] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)

    elif board_now[9] == board_now[5] == board_now[1] != ' ':
        display_board(board_now)
        print("Game over")
        print("The winner is: ", winner)


# We also need to account for possible draws
# A draw occurs when all positions are filled but there is no winner
# We can use the turn_count to compute this
def check_draw():
    if turn_count == 9:
        print("Game Over. Ladies and gentlemen, we have a tie!")


# Defines our board as a dictionary with the numbers 1-9 on the keypad representing positions.
# We originally match the key and value so the player can see how the game works
board_now = {7: "7", 8: "8", 9: "9",
             4: "4", 5: "5", 6: "6",
             1: "1", 2: "2", 3: "3"}
# We will also print a Welcome message and some instructions here, with a diagram showing how to reference board positions with numbers
print(
    "Welcome to TicTacToe. You can reference positions on the board using the corresponding numbers on the keyboard, as shown on the board below.")
display_board(board_now)
# We then must reset the board so it contains blank values instead of numbers
reset(board_now)

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

# This chooses at random whether to let the player or AI go first
first_turn = random.randint(1, 2)
if first_turn > 1:
    print("You may have the first turn")
else:
    print("The AI will go first this time")

# Each game will have 9 moves, so we can use a for loop in the game to ensure player is reprompted for move each time (unless game is over)
# We set turn count to zero. This will be used to check winners and draws
turn_count = 0

while turn_count <= 9:
    player_move()
    # After the player or AI move, +1 to counter, board values updated, and new board is displayed
    turn_count += 1
    display_board(board_now)
    AI_move()
    turn_count += 1
    display_board(board_now)