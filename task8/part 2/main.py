#!/usr/bin/python3
""" main.py: File to hold the driver code to test hamiltonian for cycles
"""


from graph import Graph
from node import Node


def main():
    """main: Driver code to show working hamiltonian cycle finding
    """
    node0 = Node(0, [1, 3])
    node1 = Node(1, [0, 3, 4, 2])
    node2 = Node(2, [1, 4])
    node3 = Node(3, [0, 1, 4])
    node4 = Node(4, [1, 2, 3])
    graph = Graph([node0, node1, node2, node3, node4])
    for index, path in enumerate(graph.get_hamiltonian_cycles()):
        print('{0}: {1}'.format(index + 1, path))


main()
