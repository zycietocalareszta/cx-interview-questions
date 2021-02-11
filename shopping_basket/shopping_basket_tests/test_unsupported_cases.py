import pytest

from basket_pricer.pricer import BasketPricer


xfail = pytest.mark.xfail


@xfail(reason="Basket validation not implemented.")
def test_garbage_basket():
    BasketPricer({1: 1.3}, {"abc": 1.22})


@xfail(reason="Catalogue validation not implemented.")
def test_garbage_catalogue():
    BasketPricer({"test": 1}, {"test": "dasda"})


@xfail(reason="Offers validation not implemented.")
def test_garbage_offers():
    BasketPricer({"test": 1}, {"test": 1.12}, {"test": (123,)})
