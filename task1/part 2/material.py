#!/usr/bin/python3
"""material.py: Class representing a material and is used in conjunction with
'lorry' to figure out the best load composition
"""


class Material:
    """material: Material class representing a possible material which can be
    loaded into a lorry """
    def __init__(self, name, quantity, price_per_kilo):
        assert isinstance(name, str)
        assert isinstance(quantity, int)
        assert isinstance(price_per_kilo, int)

        self.name = name
        self.price_per_kilo = price_per_kilo
        self.quantity = quantity

    def decriment(self):
        self.quantity -= 1

    def __gt__(self, other):
        if isinstance(other, int):
            return self.price_per_kilo > other
        elif isinstance(other, Material):
            return self.price_per_kilo > other.price_per_kilo
        return False

    def __str__(self):
        return 'Name: {0}\nPPK: {1}\nQuantity: {2}\n'.format(self.name, self.price_per_kilo,
                                                             self.quantity)
