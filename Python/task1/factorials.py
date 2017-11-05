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
