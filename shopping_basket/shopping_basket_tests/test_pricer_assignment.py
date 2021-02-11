import pytest

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

    def test_first_basket(self, first_basket, catalogue, offers):
        pricer = BasketPricer(first_basket, catalogue, offers)
        assert pricer._sub_total == 5.16
        assert pricer._discount == 1.98
        assert pricer._total == 3.18
