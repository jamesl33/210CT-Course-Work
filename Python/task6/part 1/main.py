#!/usr/bin/python3

from diagonals import *

def main(n, m):
    if n < m:
        raise ValueError('"m" is larger than the size of the array')

    array = np.random.random_integers(1, 9, size=(n, n))
    diagonals = get_all_but_middle(array, m)

    for i in range(len(diagonals)):
        diagonals[i] = sum(diagonals[i])

    diagonals.append(smallest_sum_in_middle(array, m))

    print(array)
    print('The smallest sum of diagonals parallel to the main one is {0}'.format(min(diagonals)))

main(4, 2)
