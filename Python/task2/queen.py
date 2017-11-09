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
		Recursively place a queen until you can longer place a queen
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
