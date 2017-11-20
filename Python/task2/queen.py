#!/usr/bin/python3

class Queen():
    def __init__(self, bs):
        """__init__

        :param bs: int representing the size of the board

        board State [1, 3, 0, 2] = [ - Q - - ]
                                   [ - - - Q ]
                                   [ Q - - - ]
                                   [ - - Q - ]
        """
        assert bs <= 8
        self.board_size = bs
        self.board_state = []

    def is_safe(self, pos_x, pos_y):
        """is_safe: Checks if its safe to place a queen at position 'x, y'

        :param pos_x: int representing column
        :param pos_y: int representing row
        """
        for col in range(len(self.board_state)):
            row = self.board_state[col]
            if pos_x == col or pos_y == row:
                return False
            if pos_x + pos_y == col + row or pos_x - pos_y == col - row:
                return False
        return True

    def place_queen(self, pos=0):
        """place_queen: Recursively place a queen until you can longer place a queen backtrack
        until you can place another queen

        :param pos: Int representing position on the board
        """
        """
        input:
                int pos: value used when called  recursively to stop queens being placed in the
                same place causing infinite loop
        output:
                list boardState: list representing chess board with 8 queens placed on it
        """
        if len(self.board_state) == self.board_size:
            return self.board_state
        for col in range(pos, self.board_size):
            if self.is_safe(len(self.board_state), col):
                self.board_state.append(col)
                return self.place_queen()
        last_queen_row = self.board_state.pop()
        return self.place_queen(last_queen_row + 1)
