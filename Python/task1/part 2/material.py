#!/usr/bin/python3

class material:
    def __init__(self, name, quantity, price_per_kilo):
        assert(isinstance(name, str))
        assert(isinstance(quantity, int))
        assert(isinstance(price_per_kilo, int))

        self.name = name
        self.pricePerKilo = price_per_kilo
        self.quantity = quantity

    def decriment(self):
        self.quantity -= 1

    def __gt__(self, other):
        assert(isinstance(other, (int, material)))
        return self.pricePerKilo > other

    def __str__(self):
        info = ''
        info = info + 'Name: {0}\nPPK: {1}\nQuantity: {2}\n'.format(self.name, self.price, self.quantity)
        return info
