#!/usr/bin/python3

class material:
    """
    class attributes:
        __name: string representing the name of the material
        __pricePerKilo: integer representing the price of the material per kilogram
        __quantity: integer for the total amount of the material which is available
    """
    def __init__(self, name, quantity, price_per_kilo):
        if type(quantity) != int:
            raise TypeError('quantity: must be of type int')

        if type(name) != str:
            raise TypeError ('name: must be of type string')

        if type(price_per_kilo) != int:
            raise TypeError ('price_per_kilo: must be of type integer')

        self.__name = name
        self.__pricePerKilo = price_per_kilo
        self.__quantity = quantity

    def get_price(self):
        return self.__pricePerKilo

    def get_quantity(self):
        return self.__quantity

    def get_name(self):
        return self.__name

    def decriment(self):
        self.__quantity -= 1

    def __str__(self):
        """
        output:
            displays 'name', 'price per kilogram' and 'quantity' followed by a new line
        """
        info = ''
        info = info + 'Name: {0}\nPPK: {1}\nQuantity: {2}\n'.format(self.get_name(), self.get_price(), self.get_quantity())
        return info

