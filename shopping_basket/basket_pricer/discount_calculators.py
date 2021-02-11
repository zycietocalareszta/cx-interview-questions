from decimal import Decimal, ROUND_UP


def x_for_y_calculator(x, y, products_quantity, product_price):
    """
    Returns discount for "Buy X for a price of Y" type of discounts.
    This discount can bundle, meaning "2 for 1" applies to 4 products as "4 for 2".

    :param x: how many products a customer has to buy for the discount to apply
    :param y: for how many products a customer has to pay
    :param products_quantity: number of products in the basket
    :param product_price: price for a single product
    """
    x = int(x)
    y = int(y)
    if products_quantity < x:
        return 0
    if y > x or y <= 0:
        raise ValueError(
            f"Discount makes customer buy each {x} products for a price of {y}."
        )
    number_of_discountable_bundles = products_quantity // x

    return number_of_discountable_bundles * (x - y) * Decimal(str(product_price))


def x_get_y_calculator(x, y, products_quantity, product_price):
    """
    Returns discount for "Buy X get Y free" type of discounts.
    This discount can bundle, meaning "2 get 1 free" applies to 4 products as "4 get 2 free".

    :param x: how many products a customer has to buy for the discount to apply
    :param y: how many products a customer gets for free
    :param products_quantity: number of products in a basket
    :param product_price: price of a single product
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


def x_percent_calculator(x, products_quantity, product_price):
    """
    Returns discount for "X % discount" type of discounts.

    :param x: discount percentage
    :param products_quantity: number of products in a basket
    :param product_price: price of a single product
    """
    x = int(x)
    if x > 100 or x < 0:
        raise ValueError(
            f"Discount percentage cannot be negative nor more than 100: {x}."
        )
    else:
        # Be good to customers, give them some extra pennies
        return (
            products_quantity * Decimal(str(product_price)) * Decimal(str(x / 100))
        ).quantize(Decimal(".01"), rounding=ROUND_UP)
