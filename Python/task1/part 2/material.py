#!/usr/bin/python3

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
        """decriment"""
        self.quantity -= 1

    def __gt__(self, other):
        assert isinstance(other, (int, Material))
        return self.price_per_kilo > other

    def __str__(self):
        info = ''
        info = info + 'Name: {0}\nPPK: {1}\nQuantity: {2}\n'.format(self.name, self.price_per_kilo,\
                                                                    self.quantity)
        return info
