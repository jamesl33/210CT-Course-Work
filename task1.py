#!/usr/bin/python3

def factorial(n):
	""" returns factorial of input "n" alternative to using math.factorial"""
	if type(n) != int:
		raise TypeError('n: needs to be of type integer')

	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def testIfDivides(a, b):
	if type(a) != int or type(b) != int:
		raise TypeError('testIfDivides only takes integers as arguments')
		
	if factorial(a) % b:
		return False
	return True

################# Pseudo Code #################

# FACTORIAL(n)
# 	IF n = 0
# 		RETURN 1
# 	ELSE
# 		RETURN n * FACTORIAL(n - 1)

# TEST-IF-DEVIDES(a, b)
# 	IF a! MOD b = 0
# 		RETURN true
# 	ELSE
# 		RETURN false

################# Pseudo Code #################

################# Unit Test #################

import unittest

class UnitTest(unittest.TestCase):
	def test_correct(self):
		known_correct_values = [(6, 9), (20, 10000)]
		for a, b in known_correct_values:
			self.assertTrue(testIfDivides(a, b))

	def test_false(self):
		known_wrong_values = [(6,27), (20, 1000000)]
		for a, b in known_wrong_values:
			self.assertFalse(testIfDivides(a,b))

if __name__ == '__main__':
    unittest.main()

################# Unit Test #################
