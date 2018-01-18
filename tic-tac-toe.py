### Simple Tic Tac Toe Game in Python
# Import print function
from __future__ import print_function 

# Generate a new game board

def board():
    board = []
    [board.append(i) for i in range(0,10)]
    return board

# Display game board

def print_board(board):
    print '   |   |   '
    print ' %s | %s | %s '%(board[7], board[8], board[9])
    print '   |   |   '
    print '-----------'
    print '   |   |   '
    print ' %s | %s | %s '%(board[4], board[5], board[6])
    print '   |   |   '
    print '-----------'
    print '   |   |   '
    print ' %s | %s | %s '%(board[1], board[2], board[3])
    print '   |   |   '
    print '-----------'
  
# First player choose to be X or O

def choose_token():
    prompt = "Choose your token: x, o:"
    token = ''
    while not (token == 'x' or token == 'o'):
        token = raw_input(prompt)
    if token == 'x':
        other = 'o'
    else:
        other = 'x'
    player1 = token
    player2 = other
    print "Player 1: %s\n" %token
    print "player 2: %s\n" %other
    return token

# Determine which player will begin the game    
import random

def choose_first():
    num = random.randint(1, 2)
    print 'Player %d will start the game.' %num
    return num


# Place player's token on specified square on board
def place(board, num, token):
    if num not in range(1,10):
        print 'Square does not exist.'
    elif board[num] not in range(1,10):
        print 'Already taken.'
    else:
        board[num] = token
        print '%s has been placed in position %s.' %(token, num)
# Checks if the board is full

def full(board):
    for i in board:
        if i in range(1, 10):
            return False
    return True

#  Check if a marker has won

def win_check(board, mark):
    return  ((board[7] == mark and board[8] == mark and board[9] == mark) or # Top horrizontal
    (board[4] == mark and board[5] == mark and board[6] == mark) or # middle horrizontal
    (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom horrizontal
    (board[1] == mark and board[4] == mark and board[7] == mark) or # Left vertical
    (board[2] == mark and board[5] == mark and board[8] == mark) or # Middle vertical
    (board[3] == mark and board[6] == mark and board[9] == mark) or # Right vertical
    (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) # diagonal

# Play again?

def replay():
    prompt = 'Would you like to play again?'
    answer = ''
    while not (answer == 'Y' or answer == 'N'):
        answer = raw_input(prompt).upper()
    if answer == 'N':
        return False
    return True

# Function for one turn of Tic-Tac-Toe

def play(board, marker):
    print_board(board)
    position = int(raw_input('Pick a position: 1-9\n'))
    place(board, position, marker)
    print_board(board)
    return True

# Main game function

def main():
    print 'Welcome to Tic-Tac-Toe!'
    game = board()
    start = True # Game's on!
    player1_marker = choose_token()
    if player1_marker == 'x':
        player2_marker = 'o'
    else:
        player2_marker = 'x'
    turn = choose_first()
    while start == True:
        if turn == 1: # Player 1's turn
            print 'Player 1: \n'
            play(game, player1_marker)
            if win_check(game, player1_marker):
                print_board(game)
                print 'Congratulations, you have won the game!'
                start = False
            elif full(game):
                print 'The game is a tie!'
                break
            else:
                turn = 2
        elif turn == 2: # Player 2's turn
            print 'Player 2: \n'
            play(game, player2_marker)
            if win_check(game, player2_marker):
                print_board(game)
                print 'Congratulations, you have won the game!'
                break
            elif full(game):
                print 'The game is a tie!'
                start = False
            else:
                turn = 1


while True:
    main()
    if not replay():
        break
