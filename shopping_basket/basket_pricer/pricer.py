class BasketPricer:
    def __init__(self, basket: dict, catalogue: dict, offers: dict = None):
        """
        Class designed to calculate discounts for products which were put into the shopping basket.

        :param basket: mapping of products and their amount
        :param catalogue: mapping of product names and their prices
        :param offers: mapping of product names and the list of their discounts
        """
        self.basket = basket
        self.catalogue = catalogue
        self.offers = offers

    @property
    def sub_total(self):
        """
        Calculate sub-total and return it as a float.
        """
        sub_total = 0.00
        return sub_total

    @property
    def discount(self):
        """
        Calculate discount and return it as a float.
        """
        discount = 0.00
        return discount

    @property
    def total(self):
        """
        Calculate total and return it as a float.
        """
        return (
            self.sub_total - self.discount if self.sub_total >= self.discount else 0.00
        )
