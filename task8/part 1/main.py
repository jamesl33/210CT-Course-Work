#!/usr/bin/python3
"""
"""


from string_converter import levenshtein


print('Distance between "abc" and "abcd": {0}'.format(levenshtein('abc', 'abcd')))
print('Distance between "abd" and "ab": {0}'.format(levenshtein('abd', 'ab')))
print('Distance between "abd" and "abc": {0}'.format(levenshtein('abd', 'abc')))
print('Distance between "kitten" and "sitting": {0}'.format(levenshtein('kitten', 'sitting')))

print('Distance between "abc" and "abcd": {0}'.format(levenshtein('abc', 'abcd', 3, 4, 5)))
print('Distance between "abd" and "ab": {0}'.format(levenshtein('abd', 'ab', 3, 4, 5)))
print('Distance between "abd" and "abc": {0}'.format(levenshtein('abd', 'abc', 3, 5, 6)))
print('Distance between "kitten" and "sitting": {0}'.format(levenshtein('kitten',
                                                                        'sitting', 3, 4, 5)))
