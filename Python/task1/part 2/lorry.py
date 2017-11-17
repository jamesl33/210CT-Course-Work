#!/usr/bin/python3

class lorry:
    def __init__(self, maxLoad):
        """__init__

        :param maxLoad: Maximum load capacity of the lorry (r
        """
        assert(isinstance(maxLoad, int))
        self.maxLoad = maxLoad
        self.loadComposition = 0
        self.cargo = {} # {material name: amount}

    def current_cargo_weight(self):
        weight = 0
        for material in self.cargo:
            weight += self.cargo[material]
        return weight

    def most_expensive_material(self, materials):
        """most_expensive_material

        :param materials: List of availble materials
        :return material: The most expensive material in the list
        """
        assert(isinstance(materials, list))
        cost = 0
        for i in range(len(materials)):
            if (materials[i] > cost) and (materials[i].quantity > 0):
                cost = materials[i].pricePerKilo
                most_expensive = i
        return most_expensive

    def pickup_delivery(self, materials):
        """pickup_delivery: fills the lorrys cargo with the most profitable load

        :param materials: List of availble materials
        """
        assert(isinstance(materials, list))
        while self.current_cargo_weight() < self.maxLoad:
            cargo = self.cargo
            loadComposition = self.loadComposition
            most_expensive_index = self.most_expensive_material(materials)

            if materials[most_expensive_index].name in cargo:
                self.cargo[(materials[most_expensive_index].name)] += 1
                self.loadComposition += materials[most_expensive_index].pricePerKilo
            else:
                self.cargo[(materials[most_expensive_index].name)] = 1
                self.loadComposition += materials[most_expensive_index].pricePerKilo

            materials[most_expensive_index].decriment()

    def __str__(self):
        info = 'Load composition value = {0}\n'.format(self.loadComposition)
        for key in self.cargo:
            info = info + '{0}kg of {1} and '.format(self.cargo[key], key)
        info = info[:-4]
        return info
