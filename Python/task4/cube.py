#!/usr/bin/python3

class cube:
    def __init__(self, edgeLength, color):
        self.__edgeLength = edgeLength
        self.__color = color

    def get_edge_length(self):
        return self.__edgeLength

    def get_color(self):
        return self.__color

