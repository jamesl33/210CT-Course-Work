#!/usr/bin/python3

class material:
	def __init__(self, name, quantity, price_per_kilo):
		""" instantiate settings base values """
		if type(quantity) != int:
			raise TypeError('quantity: must be of type int')

		if type(name) != str:
			raise TypeError ('name: must be of type string')

		if type(price_per_kilo) != int:
			raise TypeError ('price_per_kilo: must be of type integer')

		self.__name = name
		self.__price_per_kilo = price_per_kilo
		self.__quantity = quantity

	def get_price(self):
		return self.__price_per_kilo

	def get_quantity(self):
		return self.__quantity

	def get_name(self):
		return self.__name

	def decriment(self):
		self.__quantity -= 1

	def __str__(self):
		""" displays 'name', 'price per kilogram' and 'quantity' followed by a new line """
		info = ''
		info = info + 'Name: {0}\nPPK: {1}\nQuantity: {2}\n'.format(self.__name, self.__price_per_kilo, self.__quantity)
		return info

class lorry:
	def __init__(self, max_load):
		""" instantiate settings base values """
		if type(max_load) != int:
			raise TypeError('max_load: must be of type integer')

		self.__max_load = max_load
		self.__load_composition = 0
		self.__cargo = {} # cargo is a dictionary {material name: amount}

	def current_cargo_weight(self):
		""" return current weight of cargo in lorry; uses 'self.__cargo' and adds up amounts of each material into a total value """
		weight = 0
		for material in self.__cargo:
			weight += self.__cargo[material]
		return weight

	def most_expensive_material(self, materials):
		""" finds the most expensive item in list of "material" objects """
		cost = 0
		for i in range(len(materials)):
			if (materials[i].get_price() > cost) and (materials[i].get_quantity() > 0):
				cost = materials[i].get_price()
				most_expensive = i
		return most_expensive

	def pickup_deliviery(self, materials):
		""" 'pickup' delivery; choose the most expensive load that the lorry can load """
		if type(materials) != list:
			raise TypeError('materials: should be a list of materials')

		while self.current_cargo_weight() < self.__max_load:
			most_expensive_index = self.most_expensive_material(materials)
			if materials[most_expensive_index].get_name() in self.__cargo:
				self.__cargo[(materials[most_expensive_index].get_name())] += 1
				self.__load_composition += materials[most_expensive_index].get_price()
			else:
				self.__cargo[(materials[most_expensive_index].get_name())] = 1
				self.__load_composition += materials[most_expensive_index].get_price()

			materials[most_expensive_index].decriment()

	def __str__(self):
		""" dislays load composition and cargo when printing lorry object """
		info = 'Load composition value = {0}\n'.format(self.__load_composition)
		for key in self.__cargo:
			info = info + '{0}kg of {1} and '.format(self.__cargo[key], key)
		info = info[:-4]
		info = info +'\n'
		return info

################# Start of Testing #################

# Testing material objects
gold = material('Gold', 4, 100)
copper = material('Copper', 7, 65)
plastic = material('Plastic', 15, 50)
diamond = material('diamond', 1, 1000)
ruby = material('Ruby', 2, 500)

# Testing materials to be passed to pickup_delivery method
materials = [gold, plastic, copper]
additionalMaterials = [gold, plastic, copper, diamond, ruby]

# Testing lorry object
labsheetLorry = lorry(10) # create a lorry whose max_load capacity is 10kg
labsheetLorry.pickup_deliviery(materials) # load the lorry to the max level
print(labsheetLorry) # display the lorrys load composition and cargo

# Another testing object
additionalMaterialsLorry = lorry(15) # create a lorry whose max_load capacity is 10kg
additionalMaterialsLorry.pickup_deliviery(additionalMaterials) # load the lorry to the max level
print(additionalMaterialsLorry) # display the lorrys load composition and cargo

################# End of Testing #################
