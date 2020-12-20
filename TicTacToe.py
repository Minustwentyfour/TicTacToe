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
            if player_choice not in range(1, 10):
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
    row3 = (board_now[1], board_now[2], board_now[3])
    if (row3.count(AI_symbol) == 2 and row3.count(' ') == 1) or (
            row3.count(player_symbol) == 2 and row3.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[2] == " ":
            board_now[2] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[3] == " ":
            board_now[3] = AI_symbol
            display_board(board_now)
            turn = "Player"
    elif board_now[5] == " ":
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


def ai_next_move():
    global turn

    row1 = (board_now[7], board_now[8], board_now[9])
    row2 = (board_now[4], board_now[5], board_now[6])
    row3 = (board_now[1], board_now[2], board_now[3])
    col1 = (board_now[1], board_now[4], board_now[7])
    col2 = (board_now[2], board_now[5], board_now[8])
    col3 = (board_now[3], board_now[6], board_now[9])
    diag1 = (board_now[1], board_now[5], board_now[9])
    diag2 = (board_now[7], board_now[5], board_now[3])

    # We count the marks in each of these. If any line has 2 marks that are the same, go there
    if (row1.count(AI_symbol) == 2 and row1.count(' ') == 1) or (
            row1.count(player_symbol) == 2 and row1.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[8] == " ":
            board_now[8] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[9] == " ":
            board_now[9] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (row2.count(AI_symbol) == 2 and row2.count(' ') == 1) or (
            row2.count(player_symbol) == 2 and row2.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[6] == " ":
            board_now[6] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (row3.count(AI_symbol) == 2 and row3.count(' ') == 1) or (
            row3.count(player_symbol) == 2 and row3.count(' ') == 1):
        if board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[2] == " ":
            board_now[2] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[3] == " ":
            board_now[3] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (col1.count(AI_symbol) == 2 and col1.count(' ') == 1) or (
            col1.count(player_symbol) == 2 and col1.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (col2.count(AI_symbol) == 2 and col2.count(' ') == 1) or (
            col2.count(player_symbol) == 2 and col2.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[8] == " ":
            board_now[8] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[5] == " ":
            board_now[5] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[2] == " ":
            board_now[2] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (col3.count(AI_symbol) == 2 and col3.count(' ') == 1) or (
            col3.count(player_symbol) == 2 and col3.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move), so 8 or 9 could be free
        if board_now[9] == " ":
            board_now[9] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[6] == " ":
            board_now[6] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[3] == " ":
            board_now[3] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (diag1.count(AI_symbol) == 2 and diag1.count(' ') == 1) or (
            diag1.count(player_symbol) == 2 and diag1.count(' ') == 1):
        if board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[5] == " ":
            board_now[5] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[9] == " ":
            board_now[9] = AI_symbol
            display_board(board_now)
            turn = "Player"

    elif (diag2.count(AI_symbol) == 2 and diag2.count(' ') == 1) or (
            diag2.count(player_symbol) == 2 and diag2.count(' ') == 1):
        if board_now[7] == " ":
            board_now[7] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[5] == " ":
            board_now[5] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[3] == " ":
            board_now[3] = AI_symbol
            display_board(board_now)
            turn = "Player"
            # We know that 7 and 5 are taken now as those were our first and second choice moves
    else:
        if board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[2] == " ":
            board_now[2] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[3] == " ":
            board_now[3] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[6] == " ":
            board_now[6] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[8] == " ":
            board_now[8] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[9] == " ":
            board_now[9] = AI_symbol
            display_board(board_now)
            turn = "Player"


def game_moves():
    if turn == "Player":
        player_move()

    # AI's first move if it is AI turn first
    elif turn == "AI" and counter == 1:
        print("AI's first move is:")
        ai_first_move()
    # AI first move if AI is second
    elif turn == "AI" and counter == 2:
        print("AI's first move is:")
        ai_first_move()

    # AI's second move if AI is first to go
    elif turn == "AI" and counter == 3:
        print("AI's second move is:")
        ai_second_move()

    # AI's second move if AI is second to go
    elif turn == "AI" and counter == 4:
        print("AI's second move is:")
        ai_second_move()

    else:
        print("AI next move is:")
        ai_next_move()


# We need to define all winning states.
# This includes anywhere where there are 3 matching marks in a row, column, or diagonal
def check_winner():
    # If any row has equal values that are not blank, game is over
    if board_now[7] == board_now[8] == board_now[9] == AI_symbol \
            or board_now[7] == board_now[8] == board_now[9] == player_symbol:
        return True

    elif board_now[4] == board_now[5] == board_now[6] == AI_symbol \
            or board_now[4] == board_now[5] == board_now[6] == player_symbol:
        return True

    elif board_now[1] == board_now[2] == board_now[3] == AI_symbol \
            or board_now[1] == board_now[2] == board_now[3] == player_symbol:
        return True

    # If any column has equal values that are not blank, game over
    elif board_now[7] == board_now[4] == board_now[1] == AI_symbol or\
            board_now[7] == board_now[4] == board_now[1] == player_symbol:
        return True

    elif board_now[8] == board_now[5] == board_now[2] == AI_symbol or\
            board_now[8] == board_now[5] == board_now[2] == player_symbol:
        return True

    elif board_now[9] == board_now[6] == board_now[3] == AI_symbol or\
            board_now[9] == board_now[6] == board_now[3] == player_symbol:
        return True

    # If any diagonal line has equal values that are not blank, game over
    elif board_now[7] == board_now[5] == board_now[3] == AI_symbol \
            or board_now[7] == board_now[5] == board_now[3] == player_symbol:
        return True

    elif board_now[9] == board_now[5] == board_now[1] == AI_symbol or\
            board_now[9] == board_now[5] == board_now[1] == player_symbol:
        return True

    else:
        return False


# def check_draw():


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
counter = 1

first_turn = random.randint(1, 2)
if first_turn > 1:
    print("You may have the first turn")
    turn = "Player"
else:
    print("The AI will go first this time")
    turn = "AI"

while True:
    game_moves()
    counter += 1
    if counter == 10:
        print("We have a draw!")
        break
    if check_winner() and turn == "Player":
        print("Game over! The winner is AI")
        break
    if check_winner() and turn == "AI":
        print("Game over! The winner is Player")
        break
