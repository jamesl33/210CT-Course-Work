#!/usr/bin/python3

import unittest
from material import material
from lorry import lorry

class UnitTest(unittest.TestCase):
    def test_labsheet(self):
        known_correct_values = {"Gold": 4, "Copper": 6}

        gold = material('Gold', 4, 100)
        copper = material('Copper', 7, 65)
        plastic = material('Plastic', 15, 50)

        materials = [gold, plastic, copper]
        lorry1 = lorry(10)
        lorry1.pickup_delivery(materials)

        self.assertEqual(lorry1.cargo, known_correct_values)
        self.assertEqual(lorry1.loadComposition, 790)

    def test_extra(self):
        known_correct_values = {"Ruby": 2, "Copper": 7, "Diamond": 1, "Plastic": 1, "Gold": 4}

        gold = material('Gold', 4, 100)
        copper = material('Copper', 7, 65)
        plastic = material('Plastic', 15, 50)
        diamond = material('Diamond', 1, 1000)
        ruby = material('Ruby', 2, 500)

        materials = [gold, plastic, copper, diamond, ruby]

        lorry1 = lorry(15)
        lorry1.pickup_delivery(materials)

        self.assertEqual(lorry1.cargo, known_correct_values)
        self.assertEqual(lorry1.loadComposition, 2905)

if __name__ == '__main__':
    unittest.main()
