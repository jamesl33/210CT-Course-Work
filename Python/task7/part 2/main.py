#!/usr/bin/python3

from weighted_graph import WeightedGraph
from weighted_node import WeightedNode

# Example of node attributes
# node_0 = (Value: 0, ConnectedTo: node1, node4, Weights((node_0, node_1): 1, (node_1, node_2): 2)
def main():
    """main: Example case for finding longest and shortest path
    """
    node_0 = WeightedNode(0, [1, 4], {(0, 1): 1, (0, 4): 11})
    node_1 = WeightedNode(1, [2], {(1, 2): 2})
    node_2 = WeightedNode(2, [3], {(2, 3): 3})
    node_3 = WeightedNode(3, [], {})
    node_4 = WeightedNode(4, [5], {(4, 5): 14})
    node_5 = WeightedNode(5, [3], {(5, 3): 12})
    graph = WeightedGraph([node_0, node_1, node_2, node_3, node_4, node_5])

    print('The longest path is {0}'.format(graph.longest_path(0, 3)))
    print('The shortest path is {0}'.format(graph.shortest_path(0, 3)))

main()
