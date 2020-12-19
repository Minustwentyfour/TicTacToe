# Defines our board as a dictionary with the numbers 1-9 on the keypad representing positions
board_now = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


# This function prints the current board
def display_board(board):
    print(board['7'] + '|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4'] + '|'+board['5']+'|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|'+board['2']+'|' + board['3'])


display_board(board_now)

# This asks the player to choose to play as either X or O
while True:
    player_symbol = (input("Please select either X or O: "))
    if player_symbol == "X" or player_symbol == "x" or player_symbol == "o" or player_symbol == "O":
        print("You have chosen: ", player_symbol)
        break
    else:
        print("Try again. You must press X or O on the keyboard to make your selection")
        continue

