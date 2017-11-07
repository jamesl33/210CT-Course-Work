#!/usr/bin/python3

from diagonals import *

n = 8 # Array Size
m = 4 # Diagonal Size

if n < m:
    raise ValueError('"m" is larger than the size of the array')

array = np.random.random_integers(1, 9, size=(n, n))
diagonals = get_all_diagonals(array, m)

for i in range(len(diagonals)):
    diagonals[i] = smallest_sum_in_array(diagonals[i], m)

print(array)
print('Answer: {0}'.format(min(diagonals)))
