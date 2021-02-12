from decimal import Decimal, ROUND_UP


def x_for_y_calculator(x: int, y: int, products_quantity, product_price):
    """Calculates discount for "Buy X products for a price of Y products" type of discounts.
    This discount can bundle, meaning "2 for 1" applies to 4 products as "4 for 2".

    :param x: how many products a customer has to buy for the discount to apply
    :param y: for how many products a customer has to pay
    :param products_quantity: number of products in the basket
    :param product_price: price for a single product
    :return: calculated discount
    :rtype: Decimal
    :raises ValueError: if Y is greater than X
    """

    if products_quantity < x:
        return 0
    if y > x or y <= 0:
        raise ValueError(
            f"Discount makes customer buy each {x} products for a price of {y}."
        )
    number_of_discountable_bundles = products_quantity // x

    return number_of_discountable_bundles * (x - y) * Decimal(str(product_price))


def x_get_y_calculator(x: int, y: int, products_quantity, product_price):
    """Calculates discount for "Buy X products get Y products free" type of discounts.
    This discount can bundle, meaning "2 get 1 free" applies to 4 products as "4 get 2 free".

    :param x: how many products a customer has to buy for the discount to apply
    :param y: how many products a customer gets for free
    :param products_quantity: number of products in a basket
    :param product_price: price of a single product
    :return: calculated discount
    :rtype: Decimal
    :raises ValueError: if Y is greater than X
    """

    x = int(x)
    y = int(y)
    if products_quantity < x:
        return 0
    if y > x or y <= 0:
        raise ValueError(
            f"Discount makes customer get {y} products for each {x} in the basket."
        )
    number_of_discountable_bundles = products_quantity // x

    return number_of_discountable_bundles * y * Decimal(str(product_price))


def x_percent_calculator(x: int, products_quantity, product_price):
    """Calculates discount for "X % discount" type of discounts.

    :param x: discount percentage
    :param products_quantity: number of products in a basket
    :param product_price: price of a single product
    :return: calculated discount
    :rtype: Decimal
    :raises ValueError: if X is more than 100 or less than 0
    """

    x = int(x)
    if x > 100 or x < 0:
        raise ValueError(
            f"Discount percentage cannot be negative nor more than 100: {x}."
        )
    else:
        # Be good to customers, give them some extra pennies
        calculated_discount = (
            products_quantity * Decimal(str(product_price)) * Decimal(str(x / 100))
        )
        return calculated_discount.quantize(Decimal(".01"), rounding=ROUND_UP)


def x_get_cheapest_calculator(n: int, products_prices: tuple):
    """Calculates discount for "Buy N products from a set of {X} and get cheapest free" discount type.

    TODO: Implement handling in basket_pricer.pricer.BasketPricer

    :param n: number of products in the basket
    :param products_prices: tuple of product prices from the set of {X}
    :return: calculated discount
    :rtype: Decimal
    """

    sorted_prices = sorted(products_prices, reverse=True)
    calculated_discount = Decimal("0.00")
    i = 1
    for price in sorted_prices:
        if i % n == 0:
            calculated_discount += Decimal(str(price))
        i += 1

    return calculated_discount
