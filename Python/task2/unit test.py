#!/usr/bin/python3

import unittest
from queen import queen

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
