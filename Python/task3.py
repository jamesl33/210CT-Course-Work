#!/usr/bin/python3

class queen():
	def __init__(self, bs):
		"""
		class attributes:
			int boardSize: integer representing the size of the board
			list boardState: list representing the chess board state (index represents column, boardstate[index] represents row)

			e.g [1, 3, 0, 2] = [ - Q - - ]
						   	   [ - - - Q ]
						       [ Q - - - ]
						       [ - - Q - ]
		"""
		if bs > 8:
			raise ValueError('boardSize: must be no larger than 8')
		self.boardSize = bs
		self.boardState = []

	def is_safe(self, x, y):
		"""
		Checks if its safe to place a queen at position 'x, y'
		input:
			int x: integer representing column
			int y: integer representing row
		"""
		for col in range(len(self.boardState)):
			row = self.boardState[col]
			if x == col or y == row: # Check horizontally and vertically
				return False
			if x + y == col + row or x - y == col - row: # Check diagonals
				return False
		return True

	def place_queen(self, pos=0):
		""" 
		Recursivly place a queen until you can longer place a queen
		backtrack until you can place another queen
		input:
			int pos: value used when called  recursively to stop queens being placed in the same place causing infinite loop
		output:
			list boardState: list representing chess board with 8 queens placed on it
		"""
		if len(self.boardState) == self.boardSize:
			return self.boardState # N Queens have been placed: Solution Found
		for col in range(pos, self.boardSize):
			if self.is_safe(len(self.boardState), col):
				self.boardState.append(col)
				return self.place_queen()
		else:
			lastQueenRow = self.boardState.pop()
			return self.place_queen(lastQueenRow + 1)

################# Pseudo Code #################

# solve(pos=0)
# 	boardState = []
# 	IF LEN(boardState)
# 		FOR i = pos; pos < 8
# 			IF safe_placement(LEN(boardState))
# 				boardState APPEND i
# 				RETURN solve()
# 		lastQueenRow = boardState.pop()
# 		return solve(lastQueenRow + 1)

################# Pseudo Code #################

################# Labsheet Test #################

solver = queen(8)
print(solver.place_queen())

################# Labsheet Test #################

################# Unit Test #################

import unittest

class UnitTest(unittest.TestCase):
	def test_correct(self):
		""" Run place_queen() function with every value from 0 to 8 and check if the result is in the known correct values """
		known_correct_values = [[0, 4, 7, 5, 2, 6, 1, 3],
								[1, 3, 5, 7, 2, 0, 6, 4],
								[2, 0, 6, 4, 7, 1, 3, 5],
								[3, 0, 4, 7, 1, 6, 2, 5],
								[4, 0, 3, 5, 7, 1, 6, 2],
								[5, 0, 4, 1, 7, 2, 6, 3],
								[6, 0, 2, 7, 5, 3, 1, 4],
								[7, 1, 3, 0, 6, 4, 2, 5]]

		for i in range(8):
			solver = queen(8)
			self.assertTrue(solver.place_queen(i) in known_correct_values)

	def test_is_safe(self):
		""" Tests if is_safe function is working as is should be """
		solver = queen(8)
		solver.boardState = [0]
		self.assertFalse(solver.is_safe(0, 1))
		self.assertFalse(solver.is_safe(1, 0))
		self.assertFalse(solver.is_safe(1, 1))
		self.assertTrue(solver.is_safe(2, 1))
		self.assertTrue(solver.is_safe(1, 2))

if __name__ == '__main__':
    unittest.main()

################# Unit Test #################
