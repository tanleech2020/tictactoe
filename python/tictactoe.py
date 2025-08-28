import numpy as np
from board_game import BoardGame

class TicTacToe (BoardGame):
    def __init__(self):
        self.ROWS = 3
        self.COLS = 3
        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)

#    def reset(self):
#        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)
#        return self.board
    def is_winner(self, player):
        for i in range(self.ROWS):
            if all([self.board[i, j] == player for j in range(self.COLS)]) or all([self.board[j, i] == player for j in range(self.COLS)]):
                return True
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == player or self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == player:
            return True
        return False

    def is_draw(self):
        return not any(0 in row for row in self.board)


#    def get_valid_actions(self):
#        actions = [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]
#        return actions


'''
    def step(self, action, player):
        if self.board[action] != 0:
            raise ValueError("Invalid action")
        self.board[action] = player
        if self.is_winner(player):
            return self.board, 1, True
        elif self.is_draw():
            return self.board, 0, True
        else:
            return self.board, 0, False
'''