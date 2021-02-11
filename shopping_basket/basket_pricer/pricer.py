import re
import logging
from collections import Counter

from basket_pricer.discount_calculators import (
    x_for_y_calculator,
    x_get_y_calculator,
    x_percent_calculator,
)


class BasketPricer:
    DCN_TYP_REGEXPS = {
        "X_FOR_Y": re.compile(r"^([0-9]+)for([0-9]+)$"),
        "X_GET_Y": re.compile(r"^([0-9]+)get([0-9]+)$"),
        "X_PERCENT": re.compile(r"^([0-9]+)%$"),
    }

    def __init__(self, basket: dict, catalogue: dict, offers: dict = None):
        """
        Class designed to calculate discounts for products which were put into the shopping basket.

        :param basket: mapping of products and their amount
        :param catalogue: mapping of product names and their prices
        :param offers: mapping of product names and the list of their discounts
        """
        self._basket = basket
        self.catalogue = catalogue
        self.offers = offers

        self._sub_total = self.sub_total()
        self._discount = self.discount()
        self._total = self.total()

    def __str__(self):
        return f"""sub-total: £{self._sub_total}
discount: £{self._discount}
total: £{self._total}
"""

    def __call__(self):
        print(self)

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, value):
        self._basket = Counter(value)
        # Recalculate on basket replacement
        self._sub_total = self.sub_total()
        self._discount = self.discount()
        self._total = self.total()

    def sub_total(self):
        """
        Calculates sub-total and returns it as a float.
        """
        sub_total = 0.00
        for item, amount in self._basket.items():
            sub_total += amount * self.catalogue[item]

        return sub_total

    def discount(self):
        """
        Calculates discount and returns it as a float.
        """
        discount = 0.00
        if not self.offers:
            return discount
        discounted_products = set(self._basket.keys()) & set(self.offers.keys())
        for discounted_product in discounted_products:
            amount_of_discounted_products = self._basket[discounted_product]
            discounted_product_price = self.catalogue[discounted_product]
            product_offers = self.offers[discounted_product]
            if isinstance(product_offers, str):
                product_offers = (product_offers,)
            for offer in product_offers:
                try:
                    discount += self.__calculate_discount(
                        offer, amount_of_discounted_products, discounted_product_price
                    )
                except ValueError as ex:
                    logging.warning(
                        f"Invalid offer: {discounted_product}: {offer} | {ex}"
                    )
                    continue

        return discount

    def total(self):
        """
        Calculates total and returns it as a float.
        """
        return (
            self._sub_total - self._discount
            if self._sub_total >= self._discount
            else 0.00
        )

    def __calculate_discount(self, discount_name, products_amount, product_price):
        """
        Calculates a discount for a single offer

        :param discount_name: name of a discount (one of the ones supported in DCN_TYP_REGEXPS mapping)
        :param products_amount: amount of products
        :param product_price: price of a single product
        """
        calculated_discount = 0.00
        for discount_type, regex in self.DCN_TYP_REGEXPS.items():
            discount_name_match = re.match(regex, discount_name)
            if discount_name_match:
                x = discount_name_match.group(1)
                try:
                    y = discount_name_match.group(2)
                except IndexError:
                    calculated_discount = x_percent_calculator(
                        x, products_amount, product_price
                    )
                else:
                    if discount_type == "X_FOR_Y":
                        calculated_discount = x_for_y_calculator(
                            x, y, products_amount, product_price
                        )
                    else:
                        calculated_discount = x_get_y_calculator(
                            x, y, products_amount, product_price
                        )

        return calculated_discount

    def __validate_basket(self):
        # TODO: implement
        pass

    def __validate_catalogue(self):
        # TODO: implement
        pass

    def __validate_offers(self):
        # TODO: implement
        pass
