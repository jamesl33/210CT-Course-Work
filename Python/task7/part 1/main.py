#!/usr/bin/python3

from graph import Graph
from node import Node

# Example of node attributes
# node1 = (Value: 1, ConnectedTo: node2, node4)

def main():
    """main: Example to show testing if a graph is connected or not
    """
    node1 = Node(1, [2, 4])
    node2 = Node(2, [1, 3])
    node3 = Node(3, [2])
    node4 = Node(4, [1])
    graph1 = Graph([node1, node2, node3, node4])

    if graph1.is_connected():
        print("The graph is connected")
    else:
        print("The graph is not connected")

main()
