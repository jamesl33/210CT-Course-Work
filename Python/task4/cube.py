#!/usr/bin/python3

class cube:
	def __init__(self, color, edgeLength):
		self.__color = color
		self.__edgeLength = edgeLength

	def get_edge_length(self):
		return self.__edgeLength

	def get_color(self):
		return self.__color
