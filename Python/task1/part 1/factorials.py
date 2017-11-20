#!/usr/bin/python3

def factorial(num):
    """factorial

    :param num: Number which you would like the factorial of
    """
    assert isinstance(num, int)

    if num == 0:
        return 1
    return num * factorial(num - 1)

def test_divides(num_a, num_b):
    """test_divides

    :param num_a: Number we calculate the factorial of and then is tested if divides by 'b' equally
    :param num_b: 'a!' is divided by this number
    """
    assert isinstance(num_a, int)
    assert isinstance(num_b, int)

    if factorial(num_a) % num_b:
        return("{0} does not divide by {1}!".format(num_b, num_a), False)
    return("{0} divides by {1}!".format(num_b, num_a), True)
