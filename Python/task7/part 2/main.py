#!/usr/bin/python3

from weighted_graph import weighted_graph
from weighted_node import weighted_node

n0 = weighted_node(0, [1, 4], {(0, 1): 1, (0, 4): 11})
n1 = weighted_node(1, [2], {(1, 2): 2})
n2 = weighted_node(2, [3], {(2, 3): 3})
n3 = weighted_node(3, [], {})
n4 = weighted_node(4, [5], {(4, 5): 14})
n5 = weighted_node(5, [3], {(5, 3): 12})
g = weighted_graph([n0, n1, n2, n3, n4, n5])

print('The longest path is {0}'.format(g.longest_path(0, 3)))
print('The shortest path is {0}'.format(g.shortest_path(0, 3)))
