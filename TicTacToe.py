import random

# Defines our board as a dictionary with the numbers 1-9 on the keypad representing positions.
# We originally match the kay and value so the player can see how the game works
board_now = {7: "7", 8: "8", 9: "9",
             4: "4", 5: "5", 6: "6",
             1: "1", 2: "2", 3: "3"}
print("Welcome to TicTacToe. You can reference positions on the board using the corresponding numbers on the keyboard.")


def display_board(board):
    print(board[7] + '|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4] + '|'+board[5]+'|' + board[6])
    print('-+-+-')
    print(board[1] + '|'+board[2]+'|' + board[3])


display_board(board_now)


# This function resets the board so all values are blank
# (removes the numbers 1-9 as they were just there as instructions)
def reset(board):
    board.update({}.fromkeys(board, ' '))


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
# We don't know whose turn it is yet, so assign 0
turn = 0
first_turn = random.randint(1, 2)
if first_turn > 1:
    print("You may have the first turn")
else:
    print("The AI will go first this time")


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


count = 1
player_move()
count += 2
display_board(board_now)


# We need to define all winning states. This includes anywhere where there are 3 matching marks in a rox, column,
# or diagonal
def who_wins():
    # If player went first and count is even then it must be the player's turn
    if first_turn > 1 and (count % 2) != 0:
        winner = "Player"
    else:
        winner = "AI"
    return winner
