if __name__ == "__main__":
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

    test_pricer = BasketPricer(basket, catalogue, offers)
    test_pricer()
    print(f"{test_pricer.sub_total} | {test_pricer.discount} | {test_pricer.total}\n")

    test_pricer.basket = second_basket
    test_pricer()
