from tictactoe import TicTacToe
from gomuku import Gomuku
from constants import HUMAN, BOT, EMPTY
import numpy as np

def display_board(board):
    """Display the Tic-Tac-Toe board."""
    print("Current board:")
    for row in board:
        print(" | ".join(['X' if cell == HUMAN else 'O' if cell == BOT else ' ' for cell in row]))
        print("-" * 33)

def get_user_input(board):
    """Get and validate user input for the next move."""
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if (row in range(3) and col in range(3)) and board[row, col] == 0:
                return (row, col)
            else:
                print("Invalid move. The cell is either occupied or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

def human_move(board):
    # Get move from user
    move = get_user_input(board)
    # Update board with user move
    board[move] = HUMAN

# this it the stupidiest algo
def bot_move_random(board):
    ### Bot's move ###
    # Update board with bot move
    # Using random algo
    valid = False
    while not valid:
        print('Bot (random) turn to move.')
        row = rd.randint(0,2)
        col = rd.randint(0,2)
        move = (row,col)
        print(move)
        if(board[move]==0):
           board[move] = BOT
           valid = True

# this is an unbeatable algo
def bot_move_minimax(game,board):
    ### Bot's move ###
    # Update board with bot move
    # Using minimax algo
    print('Bot (minimax) turn to move.')
    move = find_best_move(game,board)
    if move:
       board[move[0], move[1]] = BOT

def minimax(game,board, depth, is_maximizing):
    """Minimax algorithm to find the optimal move."""
    if game.is_winner(BOT):
        return 10 - depth
    if game.is_winner(HUMAN):
        return depth - 10
    if game.is_draw():
        return 0

    if is_maximizing:
        max_eval = -np.inf
        for (r, c) in game.get_valid_actions():
            board[r, c] = BOT
            eval = minimax(game, board, depth + 1, False)
            board[r, c] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for (r, c) in game.get_valid_actions():
            board[r, c] = HUMAN
            eval = minimax(game, board, depth + 1, True)
            board[r, c] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(game,board):
    """Find the best move for the BOT using Minimax."""
    best_value = -np.inf
    best_move = None
    for (r, c) in game.get_valid_actions():
        game.board[r, c] = BOT
        move_value = minimax(game,board, 0, False)
        board[r, c] = EMPTY
        if move_value > best_value:
            best_value = move_value
            best_move = (r, c)
    return best_move

def check_game_status(game, player):
    msg = ''
    if game.is_winner(player) and player == HUMAN:
        msg = 'Human player wins!'
    elif game.is_winner(player) and player == BOT:
        msg = 'Bot wins!'
    elif game.is_draw():
        msg = 'The game ends in a draw!'
    return msg

# Example usage
if __name__ == "__main__":
    import numpy as np0
    import random as rd
    # Initialize the game board
    game = TicTacToe()
#    game = Gomuku()
    game.reset()
    board = game.board
    #human = 1
    #bot = -1

    # Loop for user moves
    while True:
        display_board(board)
        
        human_move(board)
        msg = check_game_status(game,HUMAN)
        if msg != '':
            display_board(board)
            print (msg)
            break
        bot_move_minimax(game,board)
        msg = check_game_status(game,BOT)
        if msg != '':
            display_board(board)
            print(msg)
            break
        # Display updated board
        display_board(board)
