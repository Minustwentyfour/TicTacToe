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


# We need to define all winning states.
# This includes anywhere where there are 3 matching marks in a row, column, or diagonal
def check_winner():
    # If any row has equal values that are not blank, game is over
    if board_now[7] == board_now[8] == board_now[9] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    elif board_now[4] == board_now[5] == board_now[6] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    elif board_now[1] == board_now[2] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    # If any column has equal values that are not blank, game over
    elif board_now[7] == board_now[4] == board_now[1] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    elif board_now[8] == board_now[5] == board_now[2] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    elif board_now[9] == board_now[6] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    # If any diagonal line has equal values that are not blank, game over
    elif board_now[7] == board_now[5] == board_now[3] != ' ':
        display_board(board_now)
        print("Game over")
        return True

    elif board_now[9] == board_now[5] == board_now[1] != ' ':
        display_board(board_now)
        print("Game over")
        return True


# Each game will have 9 moves,
# so we can use a for loop in the game to ensure player is prompted for move each time (unless game is over)
# We set turn count to zero. This will be used to check winners and draws
def game_play():
    # We must reset the board so it contains blank values instead of numbers and set turn count back to one
    reset_board(board_now)
    turn_count = 1

    while turn_count < 9:
        if not check_winner():
            if turn == "Player":
                player_move()
                # check_winner()
                display_board(board_now)
                turn_count += 1

            elif turn == "AI":
                # AI_move()
                # check_winner()
                turn_count += 1
                display_board(board_now)
        else:
            print("The winner is", turn)
            break
    if turn_count == 9:
        print("We have a draw!")


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

# This chooses at random whether to let the player or AI go first
first_turn = random.randint(1, 2)
if first_turn > 1:
    turn = "Player"
    print("You may have the first turn")
else:
    turn = "AI"
    print("The AI will go first this time")

game_play()
