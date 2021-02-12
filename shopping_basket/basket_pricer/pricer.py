import re
import logging
from collections import Counter
from decimal import Decimal

from basket_pricer.discount_calculators import (
    x_for_y_calculator,
    x_get_y_calculator,
    x_percent_calculator,
)

logging.getLogger(__name__).addHandler(logging.NullHandler())


class BasketPricer:
    """Class designed to calculate discounts for products which were put into the shopping basket.

    :param basket: mapping of products and their quantity
    :param catalogue: mapping of product names and their prices
    :param offers: mapping of product names and the list of their discounts
    """

    DCN_TYP_REGEXPS = {
        "X_FOR_Y": re.compile(r"^([0-9]+)for([0-9]+)$"),
        "X_GET_Y": re.compile(r"^([0-9]+)get([0-9]+)$"),
        "X_PERCENT": re.compile(r"^([0-9]+)%$"),
    }

    def __init__(self, basket: dict, catalogue: dict, offers: dict = None):
        self._basket = basket
        self.catalogue = catalogue
        self.offers = offers

        self.sub_total = self.calculate_sub_total()
        self.discount = self.calculate_discount()
        self.total = self.calculate_total()

    def __str__(self):
        return f"""sub-total: £{self.sub_total}
discount: £{self.discount}
total: £{self.total}
"""

    def __call__(self):
        print(self)

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, value):
        self._basket = Counter(value)
        # Recalculate everything on basket replacement
        self.sub_total = self.calculate_sub_total()
        self.discount = self.calculate_discount()
        self.total = self.calculate_total()

    def calculate_sub_total(self):
        """Calculates sub-total and returns it.

        :return: sub-total
        :rtype: Decimal
        """

        sub_total = Decimal("0.00")
        for product, quantity in self._basket.items():
            sub_total += quantity * Decimal(str(self.catalogue[product]))

        return sub_total

    def calculate_discount(self):
        """Calculates discount and returns it as a Decimal.

        :return: discount
        :rtype: Decimal
        """

        discount = Decimal("0.00")
        if not self.offers:
            return discount
        discounted_products = set(self._basket.keys()) & set(self.offers.keys())
        for discounted_product in discounted_products:
            quantity_of_discounted_products = self._basket[discounted_product]
            discounted_product_price = self.catalogue[discounted_product]
            product_offers = self.offers[discounted_product]
            if isinstance(product_offers, str):
                product_offers = (product_offers,)
            for offer in product_offers:
                try:
                    discount += self._calculate_single_discount(
                        offer, quantity_of_discounted_products, discounted_product_price
                    )
                except ValueError:
                    logging.warning(f"Invalid offer: {discounted_product}: {offer}.")

        return discount

    def calculate_total(self):
        """Calculates total basing on sub_total and discount and returns it.

        :return: total
        :rtype: Decimal
        """

        return (
            self.sub_total - self.discount
            if self.sub_total >= self.discount
            else Decimal("0.00")
        )

    def _calculate_single_discount(
        self, discount_name, products_quantity, product_price
    ):
        """Calculates a discount for a single offer

        :param discount_name: name of a discount (one of the supported in DCN_TYP_REGEXPS mapping)
        :param products_quantity: quantity of products
        :param product_price: price of a single product
        :return: calculated discount
        :rtype: Decimal
        :raises ValueError: if a discount_name is not supported (not in DCN_TYP_REGEXPS)
        """

        calculated_discount = Decimal("0.00")
        for discount_type, regex in self.DCN_TYP_REGEXPS.items():
            discount_name_match = re.match(regex, discount_name)
            if discount_name_match:
                x = int(discount_name_match.group(1))
                try:
                    y = int(discount_name_match.group(2))
                except IndexError:
                    calculated_discount = x_percent_calculator(
                        x, products_quantity, product_price
                    )
                else:
                    if discount_type == "X_FOR_Y":
                        calculated_discount = x_for_y_calculator(
                            x, y, products_quantity, product_price
                        )
                    elif discount_type == "X_GET_Y":
                        calculated_discount = x_get_y_calculator(
                            x, y, products_quantity, product_price
                        )
                    else:
                        raise ValueError(f"Unsupported discount type: {discount_type}")

        return calculated_discount

    def __validate_basket(self):
        """Validates if basket is str -> integer mapping

        TODO: implement
        """
        pass

    def __validate_catalogue(self):
        """Validates if catalogue is str -> int/float mapping

        TODO: implement
        """
        pass

    def __validate_offers(self):
        """Validates if offers is str -> str/collection mapping

        TODO: implement
        """
        pass
