#!/usr/bin/python3

class queen():
    def __init__(self, bs):
        """__init__

        :param bs: int representing the size of the board

        board State [1, 3, 0, 2] = [ - Q - - ]
                                   [ - - - Q ]
                                   [ Q - - - ]
                                   [ - - Q - ]
        """
        assert(bs <= 8)
        self.boardSize = bs
        self.boardState = []

    def is_safe(self, x, y):
        """is_safe: Checks if its safe to place a queen at position 'x, y'

        :param x: int representing column
        :param y: int representing row
        """
        for col in range(len(self.boardState)):
            row = self.boardState[col]
            if x == col or y == row:
                return False
            if x + y == col + row or x - y == col - row:
                return False
        return True

    def place_queen(self, pos=0):
        """place_queen: Recursively place a queen until you can longer place a queen backtrack until you can place another queen

        :param pos: Int representing position on the board
        """
        """
        input:
                int pos: value used when called  recursively to stop queens being placed in the same place causing infinite loop
        output:
                list boardState: list representing chess board with 8 queens placed on it
        """
        if len(self.boardState) == self.boardSize:
            return self.boardState
        for col in range(pos, self.boardSize):
            if self.is_safe(len(self.boardState), col):
                self.boardState.append(col)
                return self.place_queen()
        else:
            lastQueenRow = self.boardState.pop()
            return self.place_queen(lastQueenRow + 1)
