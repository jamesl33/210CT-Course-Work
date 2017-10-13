#!/usr/bin/python3

class Queens():
	def __init__(self, board_size=8):
		if board_size >= 13:
			raise ValueError('board_size: must be a value less than 13') # Values over 13 exceeds pythons recursion limit

		self.board_size = board_size
		self.chess_board_state = [] # index = col, self.chess_board_state[index] = row

	def under_attack(self, x, y): # x = row, y = column
		""" Method to find out if a queen a place 'x' 'y' would be under attack """
		for column in self.chess_board_state:
			row = self.chess_board_state.index(column)
			if x == row or y == column or x + y == row + column or x - y == row - column:
				return True
		return False

	def place_queen(self, startPos=0):
		""" Backtracking queen placement which returns a solution when found """
		if len(self.chess_board_state) == self.board_size: # If there is a queen in every column of the board the solution has been found
			return self.chess_board_state
		else:
			for row in range(startPos, self.board_size):
				if not self.under_attack(len(self.chess_board_state), row):
					self.chess_board_state.append(row)
					return self.place_queen()
			else:
				lastRow = self.chess_board_state.pop()
				return self.place_queen(lastRow + 1)

################# Unit Test #################

import unittest

class UnitTest(unittest.TestCase):
	def test_correct(self):
		known_correct_values = [1, 3, 0, 2]
		solver = Queens(4)
		self.assertEqual(known_correct_values, solver.place_queen())

	def test_correct(self):
		known_correct_values = [0, 4, 7, 5, 2, 6, 1, 3]
		solver = Queens()
		self.assertEqual(known_correct_values, solver.place_queen())

	def test_false(self):
		solver = Queens(4)
		known_wrong_values = [1, 2, 2, 1]
		self.assertNotEqual(known_wrong_values, solver.place_queen())

	def test_false(self):
		solver = Queens()
		known_wrong_values = [2, 4, 5, 6, 2, 5, 5, 5]
		self.assertNotEqual(known_wrong_values, solver.place_queen())

if __name__ == '__main__':
    unittest.main()

################# Unit Test #################
