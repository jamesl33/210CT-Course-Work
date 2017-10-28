#!/usr/bin/python3

def factorial(n):
	"""
	alternative to using math.factorial()
	arguments:
		integer 'n': number which you want the factorial of
	output:
		integer 'n!': returns the factorial of 'n'
	"""
	if type(n) != int:
		raise TypeError('n: needs to be of type integer')

	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def testIfDivides(a, b):
	"""
	arguments:
		integer 'a': number we calculate the factorial of and then is tested if divides by 'b' equally
			integer 'b: 'a!' is divided by this number
	output:
		tuple[0]:
			string: string which is will be printed e.g '9 divides by 6!'
		tuple[1]:
			bool: boolean representing if 'a! / b' is equal to 0

	"""
	if type(a) != int or type(b) != int:
		raise TypeError('testIfDivides only takes integers as arguments')

	if factorial(a) % b:
		return("{0} does not divide by {1}!".format(b, a), False)
	return("{0} divides by {1}!".format(b, a), True)

################# Pseudo Code #################

# FACTORIAL(n)
#     IF n = 0
#         RETURN 1
#     ELSE
#         RETURN n * FACTORIAL(n - 1)

# TEST-IF-DEVIDES(a, b)
#     IF a! MOD b = 0
#         RETURN true
#     ELSE
#         RETURN false

################# Pseudo Code #################

################# Labsheet Main ################# Comment out code inside of 'Labsheet Main' when running unit test

testValues = [(6, 9), (20, 10000), (6, 27), (20, 1000000)]
for a, b in testValues:
	print(testIfDivides(a, b)[0])

################# Labsheet Main #################

################# Unit Test ################# Uncomment code inside of 'Unit Test' when unit testing

# import unittest
#
# class UnitTest(unittest.TestCase):
#     def test_correct(self):
#         known_correct_values = [(6, 9), (20, 10000)]
#         for a, b in known_correct_values:
#             self.assertTrue(testIfDivides(a, b)[1])
#
#     def test_false(self):
#         known_wrong_values = [(6, 27), (20, 1000000)]
#         for a, b in known_wrong_values:
#             self.assertFalse(testIfDivides(a,b)[1])
#
# if __name__ == '__main__':
#     unittest.main()

################# Unit Test #################
