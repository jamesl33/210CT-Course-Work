#!/usr/bin/python3

class Lorry:
    """Lorry: Lorry class representing a lorry which is used to calculate the
    most expensive load
    """
    def __init__(self, maxLoad):
        """__init__

        :param maxLoad: Maximum load capacity of the lorry (r
        """
        assert isinstance(maxLoad, int)
        self.max_load = maxLoad
        self.load_composition = 0
        self.cargo = {} # {material name: amount}

    def current_cargo_weight(self):
        """current_cargo_weight: Returns the current cargo weight
        """
        weight = 0
        for material in self.cargo:
            weight += self.cargo[material]
        return weight

    def pickup_delivery(self, materials):
        """pickup_delivery: fills the lorrys cargo with the most profitable load

        :param materials: List of availble materials
        """
        assert isinstance(materials, list)
        while self.current_cargo_weight() < self.max_load:
            cargo = self.cargo
            most_expensive_index = self.most_expensive_material(materials)

            if materials[most_expensive_index].name in cargo:
                self.cargo[(materials[most_expensive_index].name)] += 1
                self.load_composition += materials[most_expensive_index].price_per_kilo
            else:
                self.cargo[(materials[most_expensive_index].name)] = 1
                self.load_composition += materials[most_expensive_index].price_per_kilo

            materials[most_expensive_index].decriment()

    def most_expensive_material(self, materials):
        """most_expensive_material

        :param materials: List of availble materials
        :return material: The most expensive material in the list
        """
        assert isinstance(materials, list)
        cost = 0
        for i in range(len(materials)):
            if (materials[i] > cost) and (materials[i].quantity > 0):
                cost = materials[i].price_per_kilo
                most_expensive = i
        return most_expensive

    def __str__(self):
        info = 'Load composition value = {0}\n'.format(self.load_composition)
        for key in self.cargo:
            info = info + '{0}kg of {1} and '.format(self.cargo[key], key)
        info = info[:-4]
        return info
