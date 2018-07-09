# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal
from datetime import datetime, timedelta

from settings import PRICES

from rent import Rent


"""
    Price to rent 3 bikes for 24 hours with a family = $42
    Price to rent 3 bikes for 24 hours without a family = $60
    Price to rent 3 bikes for 400 hours with a family = $504
"""


class TestRent(unittest.TestCase):

    def setUp(self):
        self.obj = Rent()

    def tearDown(self):
        pass

    def test_show_rents(self):
        self.obj.rent_bikes(1, 1, family=False)
        self.assertTrue(len(self.obj.show_rents()) != 0)

    def test_show_prices(self):
        rent_prices = self.obj.show_prices()
        self.assertEqual(rent_prices.get("hour", 0), PRICES.get("hour", 0))
        self.assertEqual(rent_prices.get("day", 0), PRICES.get("day", 0))
        self.assertEqual(rent_prices.get("week", 0), PRICES.get("week", 0))

    def test_rent(self):
        rent = self.obj.rent_bikes(1, 1, family=False)
        self.assertTrue(bool(rent))
        self.assertEqual(rent.get("bikes", None), 1)
        self.assertEqual(rent.get("price", None), PRICES.get("hour", 0))
        self.assertTrue(len(self.obj.show_rents()) != 0)

    def test_family_rent(self):
        rent = self.obj.rent_bikes(3, 24, family=True, surname="del Corro")
        self.assertEqual(rent.get("bikes", None), 3)
        self.assertEqual(rent.get("price", None), Decimal(42))
        self.assertEqual(rent.get("family_surname", None), "del Corro")

    def test_bad_family_rent(self):
        rent = self.obj.rent_bikes(2, 24, family=True, surname="del Corro")
        self.assertEqual(rent.get("bikes", None), 2)
        self.assertEqual(rent.get("price", None), Decimal(40))
        self.assertEqual(rent.get("family_surname", None), "del Corro")

    def test_long_time_family(self):
        rent = self.obj.rent_bikes(3, 400, family=True, surname="del Corro")
        self.assertEqual(rent.get("price", None), Decimal(504))


if __name__ == '__main__':
    unittest.main()
