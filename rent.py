# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import datetime, timedelta
from settings import FAMILY_DISCOUNT, FAMILY_MIN_SIZE, FAMILY_MAX_SIZE, PRICES


class Rent(object):
    rents = []

    def __init__(self):
        super(Rent, self).__init__()

    def _calculate_price(self, bikes, hours, family=False):
        """
            1 week = 168 hours
            1 day = 24 hours
        """
        weeks = hours / 168
        days = (hours % 168) / 24
        hours = (hours % 168) % 24
        price_for_bike = (weeks * PRICES["week"]) + (days * PRICES["day"]) + (hours * PRICES["hour"])
        price = price_for_bike * bikes

        if family and (FAMILY_MIN_SIZE <= bikes <= FAMILY_MAX_SIZE):
            price = price - price * FAMILY_DISCOUNT

        return Decimal(price)

    def rent_bikes(self, bikes, hours, family=False, **kwars):
        return_time = datetime.now() + timedelta(hours=hours)
        rent = {
            'bikes': bikes,
            'hours': hours,
            'price': 0,
            'family_surname': None,
            'return_time': return_time.strftime('%d/%m/%Y a las %H:%M')
        }

        if family:
            rent["family_surname"] = kwars.get("surname", "Anonymous")

        rent["price"] = self._calculate_price(bikes, hours, family=family)
        self.rents.append(rent)
        return rent

    def show_rents(self):
        return self.rents

    def show_prices(self):
        return PRICES
