#!/usr/bin/python3

def factorial(n):
	""" returns factorial of input "n" alternative to using math.factorial"""
	if type(n) != int:
		raise TypeError('n: needs to be of type integer')

	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def testIfDivides(a, b):
	if type(a) != int or type(b) != int:
		raise TypeError('testIfDivides only takes integers as arguments')
		
	if factorial(a) % b:
		return False
	return True

# Test input cases
test_cases = [(6, 9), (6,27), (20, 10000), (20, 1000000)]
# Testing loop using inputs from worksheet
for i in test_cases:
	print(testIfDivides(i[0], i[1]))
