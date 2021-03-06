import pytest
from decimal import Decimal


from basket_pricer.discount_calculators import (
    x_for_y_calculator,
    x_get_y_calculator,
    x_percent_calculator,
    x_get_cheapest_calculator,
)


class TestXForYCalculator:
    """ Test "Buy X products for a price of Y punds" discount calculator """

    def test_two_for_one_1(self):
        assert x_for_y_calculator(2, 1, 1, 1.00) == Decimal("0.00")

    def test_two_for_one_2(self):
        assert x_for_y_calculator(2, 1, 2, 1.00) == Decimal("1.00")

    def test_two_for_one_5(self):
        assert x_for_y_calculator(2, 1, 5, 1.00) == Decimal("2.00")

    def test_three_for_one_4(self):
        assert x_for_y_calculator(3, 1, 4, 1.22) == Decimal("2.44")

    def test_three_for_two_4(self):
        assert x_for_y_calculator(3, 2, 4, 1) == Decimal("1.00")

    def test_two_for_three_2(self):
        with pytest.raises(ValueError):
            x_for_y_calculator(2, 3, 2, 1.00)


class TestXGetYCalculator:
    """ Test "Buy X products get Y products for free" discount calculator """

    def test_two_get_one_1(self):
        assert x_get_y_calculator(2, 1, 1, 1.00) == Decimal("0.00")

    def test_two_get_one_2(self):
        assert x_get_y_calculator(2, 1, 2, 1.00) == Decimal("1.00")

    def test_two_get_one_5(self):
        assert x_get_y_calculator(2, 1, 5, 1.00) == Decimal("2.00")

    def test_three_get_one_4(self):
        assert x_get_y_calculator(3, 1, 4, 1.22) == Decimal("1.22")

    def test_three_get_two_4(self):
        assert x_get_y_calculator(3, 2, 4, 1) == Decimal("2.00")

    def test_two_get_three_2(self):
        with pytest.raises(ValueError):
            x_get_y_calculator(2, 3, 2, 1.00)


class TestXPercentCalculator:
    """ Test "X %" discount calculator """

    def test_25_percent_1(self):
        assert x_percent_calculator(25, 1, 1.00) == Decimal("0.25")

    def test_25_percent_2(self):
        assert x_percent_calculator(25, 2, 1.00) == Decimal("0.50")

    def test_25_percent_5(self):
        assert x_percent_calculator(25, 5, 1.00) == Decimal("1.25")

    def test_100_percent_5(self):
        assert x_percent_calculator(100, 5, 1.00) == Decimal("5.00")

    def test_33_percent_5(self):
        assert x_percent_calculator(100, 5, 1.26) == Decimal("6.30")

    def test_101_percent_5(self):
        with pytest.raises(ValueError):
            x_percent_calculator(101, 5, 1.00)


class TestXGetCheapestCalculator:
    """ Test "Buy N of {X} get cheapest free" discount calculator """

    @pytest.fixture
    def prices(self):
        return 1.29, 1.33, 1.29, 0.99, 1.33, 1.33

    def test_two(self, prices):
        assert x_get_cheapest_calculator(2, (1.29, 1.33)) == Decimal("1.29")
        assert x_get_cheapest_calculator(2, prices) == Decimal("3.61")

    def test_more(self, prices):
        assert x_get_cheapest_calculator(3, prices) == Decimal("2.32")
        assert x_get_cheapest_calculator(4, prices) == Decimal("1.29")
