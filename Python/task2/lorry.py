#!/usr/bin/python3

class lorry:
	def __init__(self, maxLoad):
		"""
		class attributes:
			__maxLoad: integer representing the maximum load the lorry can hold
			__loadComposition: interger representing the price of the cargo in the lorry
			__cargo: dictionary representing the cargo held in the lorry
		"""
		if type(maxLoad) != int:
			raise TypeError('maxLoad: must be of type integer')

		self.__maxLoad = maxLoad
		self.__loadComposition = 0
		self.__cargo = {} # cargo is a dictionary {material name: amount}

	def get_cargo(self):
		return self.__cargo

	def get_loadComposition(self):
		return self.__loadComposition

	def get_maxLoad(self):
		return self.__maxLoad

	def set_cargo(self, cargo):
		self.__cargo = cargo

	def set_loadComposition(self, loadComposition):
		self.__loadComposition = loadComposition

	def current_cargo_weight(self):
		"""
		output:
			returns the current cargo weight in the lorry
		"""
		weight = 0
		for material in self.__cargo:
			weight += self.__cargo[material]
		return weight

	def most_expensive_material(self, materials):
		"""
		arguments:
			list: list of 'material' objects
		output:
			integer: index of the most expensive 'material' object in the 'materials' list
		"""
		cost = 0
		for i in range(len(materials)):
			if (materials[i].get_price() > cost) and (materials[i].get_quantity() > 0):
				cost = materials[i].get_price()
				most_expensive = i
		return most_expensive

	def pickup_deliviery(self, materials):
		"""
		arguments:
			list: list of 'material' objects
		output:
			NONE: there is no output however 'self.__cargo' is updated with the most expensive load possible using the input list
		"""
		if type(materials) != list:
			raise TypeError('materials: should be a list of materials')

		while self.current_cargo_weight() < self.get_maxLoad():
			cargo = self.get_cargo()
			loadComposition = self.get_loadComposition()
			most_expensive_index = self.most_expensive_material(materials)

			if materials[most_expensive_index].get_name() in cargo:
				cargo[(materials[most_expensive_index].get_name())] += 1
				loadComposition += materials[most_expensive_index].get_price()
			else:
				cargo[(materials[most_expensive_index].get_name())] = 1
				loadComposition += materials[most_expensive_index].get_price()

			self.set_cargo(cargo)
			self.set_loadComposition(loadComposition)
			materials[most_expensive_index].decriment()

	def __str__(self):
		"""
		output:
			returns a string containing info about current load and its value
		"""
		info = 'Load composition value = {0}\n'.format(self.get_loadComposition())
		for key in self.get_cargo():
			info = info + '{0}kg of {1} and '.format(self.get_cargo()[key], key)
		info = info[:-4]
		return info
