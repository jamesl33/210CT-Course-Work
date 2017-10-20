#!/usr/bin/python3

from lorry import lorry
from material import material

################# Pseudo Code #################
################# Pseudo Code #################

################# Labsheet Main ################# Comment out code inside of 'Labsheet Main' when running unit test

known_correct_values = {"Gold": 4, "Copper": 6}

gold = material('Gold', 4, 100)
copper = material('Copper', 7, 65)
plastic = material('Plastic', 15, 50)

materials = [gold, plastic, copper]
lorry1 = lorry(10)
lorry1.pickup_deliviery(materials)
print(lorry1)

################# Labsheet Main #################

################# Unit Test ################# Uncomment code inside of 'Unit Test' when unit testing

# import unittest
#
# class UnitTest(unittest.TestCase):
#     def test_labsheet(self):
#         known_correct_values = {"Gold": 4, "Copper": 6}
#
#         gold = material('Gold', 4, 100)
#         copper = material('Copper', 7, 65)
#         plastic = material('Plastic', 15, 50)
#
#         materials = [gold, plastic, copper]
#         lorry1 = lorry(10)
#         lorry1.pickup_deliviery(materials)
#
#         self.assertEqual(lorry1.get_cargo(), known_correct_values)
#         self.assertEqual(lorry1.get_loadComposition(), 790)
#
#     def test_extra(self):
#         known_correct_values = {"Ruby": 2, "Copper": 7, "Diamond": 1, "Plastic": 1, "Gold": 4}
#
#         gold = material('Gold', 4, 100)
#         copper = material('Copper', 7, 65)
#         plastic = material('Plastic', 15, 50)
#         diamond = material('Diamond', 1, 1000)
#         ruby = material('Ruby', 2, 500)
#
#         materials = [gold, plastic, copper, diamond, ruby]
#
#         lorry1 = lorry(15)
#         lorry1.pickup_deliviery(materials)
#
#         self.assertEqual(lorry1.get_cargo(), known_correct_values)
#         self.assertEqual(lorry1.get_loadComposition(), 2905)
#
# if __name__ == '__main__':
#     unittest.main()

################# Unit Test #################

