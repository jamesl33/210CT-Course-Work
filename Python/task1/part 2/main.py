#!/usr/bin/python3

from lorry import Lorry
from material import Material

def main():
    """main: Driver code to show working implimentation of labsheet question
    """
    gold = Material('Gold', 4, 100)
    copper = Material('Copper', 7, 65)
    plastic = Material('Plastic', 15, 50)

    materials = [gold, plastic, copper]
    lorry1 = Lorry(10)
    lorry1.pickup_delivery(materials)
    print(lorry1)

main()
