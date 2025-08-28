import numpy as np
from constants import HUMAN, BOT, EMPTY

class Minimax:
    def __init__(self, game):
        self.game = game

def minimax(self,board, depth, is_maximizing):
    """Minimax algorithm to find the optimal move."""
    if self.game.is_winner(BOT):
        return 10 - depth
    if self.game.is_winner(board, HUMAN):
        return depth - 10
    if self.game.is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -np.inf
        for (r, c) in self.game.get_valid_actions():
            board[r, c] = BOT
            eval = minimax(board, depth + 1, False)
            board[r, c] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for (r, c) in self.game.get_valid_actions():
            board[r, c] = HUMAN
            eval = minimax(board, depth + 1, True)
            board[r, c] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(self,board):
    """Find the best move for the BOT using Minimax."""
    best_value = -np.inf
    best_move = None
    for (r, c) in self.game.get_valid_actions():
        self.game.board[r, c] = BOT
        move_value = minimax(board, 0, False)
        board[r, c] = EMPTY
        if move_value > best_value:
            best_value = move_value
            best_move = (r, c)
    return best_move