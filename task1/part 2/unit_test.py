#!/usr/bin/python3
"""unit_test.py: Unit testing for the Lorry class
"""

import unittest
from material import Material
from lorry import Lorry


class UnitTest(unittest.TestCase):
    """UnitTest"""
    def test_labsheet(self):
        """test_labsheet: Test labsheet values
        """
        known_correct_values = {"Gold": 4, "Copper": 6}

        gold = Material('Gold', 4, 100)
        copper = Material('Copper', 7, 65)
        plastic = Material('Plastic', 15, 50)

        materials = [gold, plastic, copper]
        lorry1 = Lorry(10)
        lorry1.pickup_delivery(materials)

        self.assertEqual(lorry1.cargo, known_correct_values)
        self.assertEqual(lorry1.load_composition, 790)

    def test_extra(self):
        """test_extra: Test extra values to make sure the code should work with any material
        objects
        """
        known_correct_values = {"Ruby": 2, "Copper": 7, "Diamond": 1, "Plastic": 1, "Gold": 4}

        gold = Material('Gold', 4, 100)
        copper = Material('Copper', 7, 65)
        plastic = Material('Plastic', 15, 50)
        diamond = Material('Diamond', 1, 1000)
        ruby = Material('Ruby', 2, 500)

        materials = [gold, plastic, copper, diamond, ruby]

        lorry1 = Lorry(15)
        lorry1.pickup_delivery(materials)

        self.assertEqual(lorry1.cargo, known_correct_values)
        self.assertEqual(lorry1.load_composition, 2905)


if __name__ == '__main__':
    unittest.main()
