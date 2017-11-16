#!/usr/bin/python3

import graph

node1 = graph.node(1, [2, 4])
node2 = graph.node(2, [1, 3])
node3 = graph.node(3, [2])
node4 = graph.node(4, [1])
graph1 = graph.graph([node1, node2, node3, node4])

print(graph1.is_connected())

