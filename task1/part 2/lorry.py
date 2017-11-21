#!/usr/bin/python3
"""lorry.py: Contains the class for the lorry object which is used
to calculate the most expensive load
"""


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
        self.cargo = {}

    def pickup_delivery(self, materials):
        """pickup_delivery: fills the lorrys cargo with the most profitable load

        :param materials: List of availble materials
        """
        assert isinstance(materials, list)
        while self._current_weight() < self.max_load:
            material = self.most_expensive_material(materials)
            if material.name not in self.cargo:
                self.cargo[material.name] = 0
            self.cargo[material.name] += 1
            self.load_composition += material.price_per_kilo
            material.decriment()

    def _current_weight(self):
        return sum(self.cargo.values())

    def __str__(self):
        info = 'Load composition value = {0}\n'.format(self.load_composition)
        for key in self.cargo:
            info = info + '{0}kg of {1} and '.format(self.cargo[key], key)
        info = info[:-4]
        return info

    @classmethod
    def most_expensive_material(cls, materials):
        """most_expensive_material

        :param materials: List of availble materials
        :return material: The most expensive material in the list
        """
        assert isinstance(materials, list)
        cost = 0
        for material in materials:
            if material > cost and material.quantity > 0:
                cost = material.price_per_kilo
                most_expensive = material
        return most_expensive
