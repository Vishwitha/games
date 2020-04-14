import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ""
    while not( marker == 'X' or marker == 'O'):
        marker = input("Please enter the marker to pick 'X' or 'O'").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first(players):
    player1_marker = players[0]
    player2_marker = players[1]
    random_choice = random.choice(input_received)
    if player1_marker == random_choice:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1, len(board) - 1):
        if space_check(board, i):
            return False
    else:
        return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = int(input("Please enter the position of the marker:"))
    if space_check(board, position):
        return position


def replay():
    play_again = input("Please enter Yes if you want to play again:")
    if play_again.lower() == 'yes':
        return True


print("Welcome to Tic Tac Toe Game")
while True:
    #clear the board
    theboard = [' ']*10
    print(theboard)
    input_received = player_input()
    player1_marker = input_received[0]
    player2_marker = input_received[1]
    turn = choose_first(input_received)

    play_game = input('do you want to play the game :yes or no: ')
    if play_game.lower() == 'yes':
        start_game = True
    else:
        start_game = False

    while start_game:
        if turn == 'player1':
            print("player1 is playing")
            display_board(theboard)
            player_position = player_choice(theboard)
            place_marker(theboard,player1_marker,player_position)
            if win_check(theboard,player1_marker):
                print("congratulation Yo won the game")
                start_game = False
            elif full_board_check(theboard):
                display_board(theboard)
                print("Match is draw")
                break
            else:
                turn = 'player2'
        else:
            print("player2 is playing")
            display_board(theboard)
            player_position = player_choice(theboard)
            place_marker(theboard, player2_marker, player_position)
            if win_check(theboard, player2_marker):
                print("congratulation Yo won the game")
                start_game = False
            elif full_board_check(theboard):
                display_board(theboard)
                print("Match is draw")

            else:
                turn = 'player1'

    if not replay():
        break
