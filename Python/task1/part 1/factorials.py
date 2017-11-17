def factorial(n):
    """factorial

    :param n: Number which you would like the factorial of
    """
    if type(n) != int:
        raise TypeError('n: needs to be of type integer')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def testIfDivides(a, b):
    """testIfDivides

    :param a: Number we calculate the factorial of and then is tested if divides by 'b' equally
    :param b: 'a!' is divided by this number
    """
    assert(isinstance(a, int))
    assert(isinstance(b, int))
    if factorial(a) % b:
        return("{0} does not divide by {1}!".format(b, a), False)
    return("{0} divides by {1}!".format(b, a), True)
