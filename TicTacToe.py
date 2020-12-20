import random


def display_board(board):
    """

    :param board: represents each position on the board
    :return: The values for the current board are printed
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def reset_board(board):
    """

    :param board: Each board position
    :return: board_now is reset so all values are blank
    """
    board.update({}.fromkeys(board, ' '))


def player_move():
    """
    This function asks the player for their move until they enter a valid choice
    :return: Updated board is printed and turn is changed to AI
    """
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


def ai_first_move():
    """
    This function chooses the AI first move (7, if taken then 9)
    :return: Updated board is printed and turn is changed
    """
    global turn
    if board_now[7] == " ":
        board_now[7] = AI_symbol
        display_board(board_now)
        turn = "Player"
    elif board_now[9] == " ":
        board_now[9] = AI_symbol
        display_board(board_now)
        turn = "Player"


def ai_second_move():
    """
    This function chooses the AI second move
    First the second and third row are checked to see if there are 2 player marks.
    If found, the third empty square is taken.
    Otherwise an empty square is found (either 5, 7, 9, or 1, in that order)

    :return:Updated board is printed and turn changed to player
    """
    global turn
    row2 = (board_now[4], board_now[5], board_now[6])
    row3 = (board_now[1], board_now[2], board_now[3])
    # Check row 2 for 2 played symbols
    if row2.count(player_symbol) == 2 and row2.count(' ') == 1:
        if board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[6] == " ":
            board_now[6] = AI_symbol
            display_board(board_now)
            turn = "Player"
    # Check row 3 for 2 player symbols
    elif row3.count(player_symbol) == 2 and row3.count(' ') == 1:
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
    # If centre if free, go there
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
    """
    This function chooses every AI move except the first and second.
    Every row, column and diagonal line are first defined.
    Each are checked for 2 matching marks (AI or player).
    If found, the third empty square is chosen.
    Otherwise, the first empty square found is chosen.
    :return: Updated board is printed and turn changed to player.
    """
    global turn
    # Defining the lines
    row1 = (board_now[7], board_now[8], board_now[9])
    row2 = (board_now[4], board_now[5], board_now[6])
    row3 = (board_now[1], board_now[2], board_now[3])
    col1 = (board_now[1], board_now[4], board_now[7])
    col2 = (board_now[2], board_now[5], board_now[8])
    col3 = (board_now[3], board_now[6], board_now[9])
    diag1 = (board_now[1], board_now[5], board_now[9])
    diag2 = (board_now[7], board_now[5], board_now[3])

    # Checking row 1 for 2 matching symbols.
    # We count the player and ai marks in each of the above lines. If any line has 2 marks that are the same, go there
    if (row1.count(AI_symbol) == 2 and row1.count(' ') == 1) or (
            row1.count(player_symbol) == 2 and row1.count(' ') == 1):
        # If we are on the third move we know 7 is taken (from our 1st or 2nd move),
        # so we only need to check if 8 and 9 are available
        if board_now[8] == " ":
            board_now[8] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[9] == " ":
            board_now[9] = AI_symbol
            display_board(board_now)
            turn = "Player"
    # Checking row 2 for 2 matching symbols
    elif (row2.count(AI_symbol) == 2 and row2.count(' ') == 1) or (
            row2.count(player_symbol) == 2 and row2.count(' ') == 1):
        if board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[6] == " ":
            board_now[6] = AI_symbol
            display_board(board_now)
            turn = "Player"
    # Checking row 3 for 2 matching symbols
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
    # Checking column 1 for 2 matching symbols
    elif (col1.count(AI_symbol) == 2 and col1.count(' ') == 1) or (
            col1.count(player_symbol) == 2 and col1.count(' ') == 1):
        if board_now[4] == " ":
            board_now[4] = AI_symbol
            display_board(board_now)
            turn = "Player"
        elif board_now[1] == " ":
            board_now[1] = AI_symbol
            display_board(board_now)
            turn = "Player"
    # Checking column 2 for 2 matching symbols
    elif (col2.count(AI_symbol) == 2 and col2.count(' ') == 1) or (
            col2.count(player_symbol) == 2 and col2.count(' ') == 1):
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
    # Checking column 3 for 2 matching symbols
    elif (col3.count(AI_symbol) == 2 and col3.count(' ') == 1) or (
            col3.count(player_symbol) == 2 and col3.count(' ') == 1):
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
    # Checking diagonal 1 for 2 matching symbols
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
    # Checking diagonal 2 for 2 matching symbols
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
    # If no line has 2 matching symbols, choose the first available empty square
    # We know that 7 is taken, as that was our first choice, so check every other square
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
        elif board_now[5] == " ":
            board_now[5] = AI_symbol
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
    """
    This function calls either player or AI to make their move, depending on who's turn it is
    :return:
    """
    if turn == "Player":
        player_move()

    # AI's first move if AI is first to go
    elif turn == "AI" and counter == 1:
        print("AI's first move is:")
        ai_first_move()
    # AI first move if AI is second to go
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
    # If it is not the first or second move
    else:
        print("AI next move is:")
        ai_next_move()


def check_winner():
    """
    Winning states are defined and checked
    :return: Return true if winning state is found
    """
    # If any row has 3 AI or 3 player symbols
    if board_now[7] == board_now[8] == board_now[9] == AI_symbol \
            or board_now[7] == board_now[8] == board_now[9] == player_symbol:
        return True

    elif board_now[4] == board_now[5] == board_now[6] == AI_symbol \
            or board_now[4] == board_now[5] == board_now[6] == player_symbol:
        return True

    elif board_now[1] == board_now[2] == board_now[3] == AI_symbol \
            or board_now[1] == board_now[2] == board_now[3] == player_symbol:
        return True

    # If any column has 3 AI or 3 player symbols
    elif board_now[7] == board_now[4] == board_now[1] == AI_symbol or\
            board_now[7] == board_now[4] == board_now[1] == player_symbol:
        return True

    elif board_now[8] == board_now[5] == board_now[2] == AI_symbol or\
            board_now[8] == board_now[5] == board_now[2] == player_symbol:
        return True

    elif board_now[9] == board_now[6] == board_now[3] == AI_symbol or\
            board_now[9] == board_now[6] == board_now[3] == player_symbol:
        return True

    # If any diagonal line has 3 AI or 3 player symbols
    elif board_now[7] == board_now[5] == board_now[3] == AI_symbol \
            or board_now[7] == board_now[5] == board_now[3] == player_symbol:
        return True

    elif board_now[9] == board_now[5] == board_now[1] == AI_symbol or\
            board_now[9] == board_now[5] == board_now[1] == player_symbol:
        return True

    else:
        return False


# Define our board as a dictionary with the numbers 1-9 on the keypad representing positions.
# We originally match the key and value so the player can see how the game works.
board_now = {7: "7", 8: "8", 9: "9",
             4: "4", 5: "5", 6: "6",
             1: "1", 2: "2", 3: "3"}

# We will also print some instructions here, with a diagram showing how to reference board positions with numbers.
print("You can reference positions on the board using the corresponding numbers on the keyboard, as shown below.")
display_board(board_now)

# This asks the player to choose to play as either X or O. Keeps asking until valid input found.
while True:
    player_symbol = (input("Please select either X or O? "))
    if player_symbol == "X" or player_symbol == "x":
        AI_symbol = "O"
        print("You have chosen ", player_symbol, "and the AI will be ", AI_symbol)
        break
    elif player_symbol == "o" or player_symbol == "O":
        AI_symbol = "X"
        print("You have chosen ", player_symbol, "and the AI will be ", AI_symbol)
        break
    else:
        print("Try again. You must press X or O on the keyboard to make your selection")
        continue

# The board is reset at the start of the game.
reset_board(board_now)
turn = None
counter = 1

# Random number decides whether first turn is player or AI
first_turn = random.randint(1, 2)
if first_turn > 1:
    print("You may have the first turn")
    turn = "Player"
else:
    print("The AI will go first this time")
    turn = "AI"

# While loop controls main gameplay
while True:
    game_moves()
    counter += 1
    if check_winner() and turn == "Player":
        print("Game over! The winner is AI")
        break
    if check_winner() and turn == "AI":
        print("Game over! The winner is Player")
        break
    if counter == 10:
        print("We have a draw!")
        break
