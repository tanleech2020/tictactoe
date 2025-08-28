import numpy as np
from board_game import BoardGame

class Gomuku (BoardGame):
    player = None
    def __init__(self):
        self.ROWS = 9
        self.COLS = 9
        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)

    def reset(self):
        self.board = np.zeros((9, 9), dtype=int)
        return self.board

    def is_winner(self, player):
        self.player = player
        for row in range(self.board_size[0]):
            for col in range(self.board_size[1]):
                status = self.checkWin(row,col,5)
                if(status is True):
                    return status
        return False

    def is_draw(self):
        return not any(0 in row for row in self.board)

    def get_valid_actions(self):
        actions = [(i, j) for i in range(self.board_size[0]) for j in range(self.board_size[1]) if self.board[i, j] == 0]
        return actions
    
    # check for winner implementation
    def checkWin(self, row, col, count=5):
        if (row >= 8 and col >= 8) or (row <= 0 and col <= 0):
            # only check backward diagonal, horizontal and vertical
            return (self.check_horizontal_win(row, col, count) or self.check_vertical_win(row, col, count)
                    or self.check_diagonal_b_win(row, col-1, count))
        elif (row <= 0 and col >= 8) or (row >= 8 and col <= 0):
            # only check forward diagonal, horizontal and vertical
            return (self.check_horizontal_win(row, col, count) or self.check_vertical_win(row, col, count)
                    or self.check_diagonal_f_win(row,
                                                 col, count))
        else:
            return (self.check_horizontal_win(row, col, count) or self.check_vertical_win(row, col, count)
                    or self.check_diagonal_f_win(row,
                                                 col, count) or self.check_diagonal_b_win(row, col, count))

    # checking \ diagonal backward moves
    def check_diagonal_b_win(self, r, c, count):
        totalcnt = 1
        isTopLeftCorner = False
        isBottomRightCorner = False
        start_r = r
        start_c = c
#        print('start_c: ',start_c)
        if r >= 8 and c >= 8:
            # bottom right corner
            start_r = r - 1
            start_c = c - 1
            isBottomRightCorner = True
        elif r <= 0 and c <= 0:
            # top left corner
            start_r = r + 1
            start_c = c + 1
            isTopLeftCorner = True
        # count left up
        if not isTopLeftCorner:
            left_count = self.countDF_Piece(start_r - 1, -1, start_c - 1, -1)
        #        print('left_count: ', left_count)
        else:
            left_count = 0
        # count right down
        if not isBottomRightCorner:
            right_count = self.countDF_Piece(start_r, self.board_size[0], start_c, self.board_size[1])
        #        print('right_count: ', right_count)
        else:
            right_count = 0
        totalcnt = totalcnt + left_count + right_count
        #    print('total cnt: ', totalcnt)
        if totalcnt == count:
            return True

        return False

    # checking / diagonal forward moves
    def check_diagonal_f_win(self, r, c, count):
        total_count = 1
        isTopRightCorner = False
        isBottomLeftCorner = False
        start_r = r
        start_c = c
        if r >= 8 and c <= 0:
            # bottom left corner
            start_r = r - 1
            start_c = c + 1
            isBottomLeftCorner = True
        elif r <= 0 and c >= 8:
            # top right corner
            start_r = r + 1
            start_c = c - 1
            isTopRightCorner = True
        # count left down
        if not isBottomLeftCorner:
            #print('bottom left corner')
            left_count = self.countDF_Piece(start_r + 1, self.board_size[0], start_c - 1, -1)
        else:
            left_count = 0
        # count right up
        if not isTopRightCorner and start_c <8:
            #print('top right corner with start_c: ',start_c)
            right_count = self.countDF_Piece(start_r - 1, -1, start_c + 1, self.board_size[1])
        else:
            right_count = 0
        total_count = total_count + left_count + right_count
        if total_count == count:
            return True

        return False

    # check for win vertically
    def check_vertical_win(self, r, c, count):
        total_count = 1
        start = 0
        if r > 0:
            start = r - 1
        elif r <= 0:
            # top row of the board
            start = max(0, r)
        # count up
        up_count = self.count_piece_straight(None, c, start, -1)  # countV_Piece(c, start, -1, piece)
        if r < self.board_size[0] - 1:
            down_count = self.count_piece_straight(None, c, r + 1,
                                                   self.board_size[0])  # countV_Piece(c, r + 1, board.rows, piece)
        else:
            # bottom column of the board
            down_count = 0
        total_count = total_count + up_count + down_count
        if total_count == count:
            return True

        return False

    # check for win horizontally
    def check_horizontal_win(self, r, c, count):
        total_count = 1
        start = 0
        if c > 0:
            start = c - 1
        elif c <= 0:
            # first column of the board
            start = max(0, c)
        # count left
        left_count = self.count_piece_straight(r, None, start, -1)
        if c < self.board_size[1] - 1:
            right_count = self.count_piece_straight(r, None, c + 1, self.board_size[1])
        else:
            # last column of the board
            right_count = 0
        total_count = total_count + left_count + right_count
        if total_count == count:
            return True
        return False

    def countDF_Piece(self, start_r, end_r, start_c, end_c):
        cnt = 0
        if end_r > start_r and end_c < start_c:
            r_incr = 1
            c_incr = -1
        elif end_r < start_r and end_c < start_c:
            r_incr = -1
            c_incr = -1
        elif end_r > start_r and end_c > start_c:
            r_incr = 1
            c_incr = 1
        else:
            r_incr = -1
            c_incr = 1

        for r in range(start_r, end_r, r_incr):
            #if self.board.getPiece(r, start_c) == self.piece:
#            print('row: ',r)
#            print('col: ',start_c)
            if start_c<self.board_size[1] and self.board[r, start_c] == self.player:
                cnt = cnt + 1
            else:
                break
            start_c = start_c + c_incr
        return cnt

    def count_piece_straight(self, r, c, start, end):
        cnt = 0
        increment = 1
        if start > end:
            increment = -1

        if r is None and c is not None:
            # count vertical
            for r in range(start, end, increment):
                # if self.board.getPiece(r, c) == self.piece:
                if self.board[r, c] == self.player:                
                    cnt = cnt + 1
                else:
                    break
        elif r is not None and c is None:
            # count horizontal
            for c in range(start, end, increment):
                #if self.board.getPiece(r, c) == self.piece:
                if self.board[r, c] == self.player:                
                    cnt = cnt + 1
                else:
                    break
        return cnt