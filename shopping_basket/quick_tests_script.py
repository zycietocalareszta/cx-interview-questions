if __name__ == "__main__":
    import re

    from basket_pricer import BasketPricer

    basket = {
        "apple": 7,
        "banana": 12,
        "doge": 2,
    }
    second_basket = {
        "apple": 3,
        "banana": 7,
    }
    catalogue = {
        "apple": 0.37,
        "banana": 1.27,
        "doge": 10000,
    }
    offers = {
        "apple": "3get1",
        "banana": "2for1",
        "doge": "33%",
    }
    invalid_offers = {
        "apple": "2get3",
    }

    # Initilize pricer
    test_pricer = BasketPricer(basket, catalogue, offers)
    # Execute pricer (prints the amounts)
    test_pricer()
    # Access amounts separately
    print(f"{test_pricer.sub_total} | {test_pricer.discount} | {test_pricer.total}\n")

    # Replace basket
    test_pricer.basket = second_basket
    test_pricer()
    # Provide invalid discount
    test_pricer.DCN_TYP_REGEXPS = {
        "X_GET_Y": re.compile(r"^(.*)$"),
    }
    # Raises exception
    test_pricer.calculate_discount()

    # Raises exception due to "Buy 2 get 3 free" offer
    test_pricer = BasketPricer(second_basket, catalogue, invalid_offers)
    test_pricer()
