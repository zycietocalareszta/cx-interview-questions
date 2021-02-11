import pytest

from basket_pricer.discount_calculators import (
    x_for_y_calculator,
    x_get_y_calculator,
    x_percent_calculator,
)


class TestXForYCalculator:
    def test_two_for_one_1(self):
        assert x_for_y_calculator(2, 1, 1, 1.00) == 0.00

    def test_two_for_one_2(self):
        assert x_for_y_calculator(2, 1, 2, 1.00) == 1.00

    def test_two_for_one_5(self):
        assert x_for_y_calculator(2, 1, 5, 1.00) == 2.00

    def test_three_for_one_4(self):
        assert x_for_y_calculator(3, 1, 4, 1.00) == 2.00

    def test_three_for_two_4(self):
        assert x_for_y_calculator(3, 2, 4, 1.00) == 1.00

    def test_two_for_three_2(self):
        with pytest.raises(ValueError):
            x_for_y_calculator(2, 3, 2, 1.00)


class TestXGetYCalculator:
    def test_two_get_one_1(self):
        assert x_get_y_calculator(2, 1, 1, 1.00) == 0.00

    def test_two_get_one_2(self):
        assert x_get_y_calculator(2, 1, 2, 1.00) == 1.00

    def test_two_get_one_5(self):
        assert x_get_y_calculator(2, 1, 5, 1.00) == 2.00

    def test_three_get_one_4(self):
        assert x_get_y_calculator(3, 1, 4, 1.00) == 1.00

    def test_three_get_two_4(self):
        assert x_get_y_calculator(3, 2, 4, 1.00) == 2.00

    def test_two_get_three_2(self):
        with pytest.raises(ValueError):
            x_get_y_calculator(2, 3, 2, 1.00)


class TestXPercentCalculator:
    def test_25_percent_1(self):
        assert x_percent_calculator(25, 1, 1.00) == 0.25

    def test_25_percent_2(self):
        assert x_percent_calculator(25, 2, 1.00) == 0.50

    def test_25_percent_5(self):
        assert x_percent_calculator(25, 5, 1.00) == 1.25

    def test_100_percent_5(self):
        assert x_percent_calculator(100, 5, 1.00) == 5.00

    def test_101_percent_5(self):
        with pytest.raises(ValueError):
            x_percent_calculator(101, 5, 1.00)
