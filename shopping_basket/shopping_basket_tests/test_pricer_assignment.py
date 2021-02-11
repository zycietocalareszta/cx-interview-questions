import pytest
from decimal import Decimal

from basket_pricer.pricer import BasketPricer


class TestAssignment:
    @pytest.fixture
    def first_basket(self):
        basket = {
            "Baked Beans": 4,
            "Biscuits": 1,
        }

        return basket

    @pytest.fixture
    def second_basket(self):
        basket = {
            "Baked Beans": 2,
            "Biscuits": 1,
            "Sardines": 2,
        }

        return basket

    @pytest.fixture
    def catalogue(self):
        catalogue = {
            "Baked Beans": 0.99,
            "Biscuits": 1.20,
            "Sardines": 1.89,
            "Shampoo (Small)": 2.00,
            "Shampoo (Medium)": 2.50,
            "Shampoo (Large)": 3.50,
        }

        return catalogue

    @pytest.fixture
    def offers(self):
        offers = {
            "Baked Beans": "2get1",
            "Sardines": "25%",
        }

        return offers

    def test_pricers(self, first_basket, second_basket, catalogue, offers):
        second_pricer = BasketPricer(first_basket, catalogue, offers)
        assert second_pricer._sub_total == Decimal("5.16")
        assert second_pricer._discount == Decimal("1.98")
        assert second_pricer._total == Decimal("3.18")

        second_pricer = BasketPricer(second_basket, catalogue, offers)
        assert second_pricer._sub_total == Decimal("6.96")
        assert second_pricer._discount == Decimal("1.94")
        assert second_pricer._total == Decimal("5.02")
