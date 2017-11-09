#!/usr/bin/python3

from lorry import lorry
from material import material

known_correct_values = {"Gold": 4, "Copper": 6}

gold = material('Gold', 4, 100)
copper = material('Copper', 7, 65)
plastic = material('Plastic', 15, 50)

materials = [gold, plastic, copper]
lorry1 = lorry(10)
lorry1.pickup_deliviery(materials)
print(lorry1)
