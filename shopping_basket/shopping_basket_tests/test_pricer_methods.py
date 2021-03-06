import pytest
import re
from decimal import Decimal

from basket_pricer.pricer import BasketPricer


class TestPricerMethods:
    """ Contains tests for BasketPricer class methods """

    @pytest.fixture
    def basket(self):
        basket = {
            "apple": 10,
            "banana": 2,
            "doge": 1,
        }

        return basket

    @pytest.fixture
    def catalogue(self):
        catalogue = {
            "apple": 0.3,
            "banana": 1.1,
            "doge": 10000,
        }

        return catalogue

    @pytest.fixture
    def offers(self):
        offers = {
            "apple": "3get1",
            "banana": ["2for1"],
            "doge": "33%",
            "peanuts": ["33%"],
        }

        return offers

    @pytest.fixture
    def multiple_offers(self):
        offers = {"doge": ["33%", "2for1"], "apple": "99%"}

        return offers

    @pytest.fixture
    def empty_pricer(self):
        return BasketPricer({}, {})

    @pytest.fixture
    def pricer_with_basket_and_catalogue(self, basket, catalogue):
        return BasketPricer(basket, catalogue)

    @pytest.fixture
    def pricer_with_basket_catalogue_and_offers(self, basket, catalogue, offers):
        return BasketPricer(basket, catalogue, offers)

    @pytest.fixture
    def pricer_with_multiple_offers(self, basket, catalogue, multiple_offers):
        return BasketPricer(basket, catalogue, multiple_offers)

    def test_sub_total(
        self,
        empty_pricer,
        pricer_with_basket_and_catalogue,
        pricer_with_basket_catalogue_and_offers,
        pricer_with_multiple_offers,
    ):
        assert empty_pricer.calculate_sub_total() == Decimal("0.00")
        assert pricer_with_basket_and_catalogue.calculate_sub_total() == Decimal(
            "10005.20"
        )
        assert pricer_with_basket_catalogue_and_offers.calculate_sub_total() == Decimal(
            "10005.20"
        )
        assert pricer_with_multiple_offers.calculate_sub_total() == Decimal("10005.20")

    def test_discount(
        self,
        empty_pricer,
        pricer_with_basket_and_catalogue,
        pricer_with_basket_catalogue_and_offers,
        pricer_with_multiple_offers,
    ):
        assert empty_pricer.calculate_discount() == Decimal("0.00")
        assert pricer_with_basket_and_catalogue.calculate_discount() == Decimal("0.00")
        assert pricer_with_basket_catalogue_and_offers.calculate_discount() == Decimal(
            "3302"
        )
        assert pricer_with_multiple_offers.calculate_discount() == Decimal("3302.97")

    def test_total(
        self,
        empty_pricer,
        pricer_with_basket_and_catalogue,
        pricer_with_basket_catalogue_and_offers,
        pricer_with_multiple_offers,
    ):
        assert empty_pricer.calculate_total() == Decimal("0.00")
        assert pricer_with_basket_and_catalogue.calculate_total() == Decimal("10005.2")
        assert pricer_with_basket_catalogue_and_offers.calculate_total() == Decimal(
            "6703.2"
        )
        assert pricer_with_multiple_offers.calculate_total() == Decimal("6702.23")

    def test_calculate_discount(self, empty_pricer):
        assert empty_pricer._calculate_single_discount("2for1", 2, 2.36) == Decimal(
            "2.36"
        )
        assert empty_pricer._calculate_single_discount("3for1", 7, 0.12) == Decimal(
            "0.48"
        )
        assert empty_pricer._calculate_single_discount("2get1", 2, 2.36) == Decimal(
            "2.36"
        )
        assert empty_pricer._calculate_single_discount("3get1", 7, 0.12) == Decimal(
            "0.24"
        )
        assert empty_pricer._calculate_single_discount("50%", 2, 2.36) == Decimal(
            "2.36"
        )

        with pytest.raises(ValueError):
            empty_pricer._calculate_single_discount("2get3", 2, 2.36)
        with pytest.raises(ValueError):
            empty_pricer._calculate_single_discount("120%", 2, 2.36)
        with pytest.raises(ValueError):
            empty_pricer._calculate_single_discount("2for3", 2, 2.36)

    def test_discount_exception(self, pricer_with_basket_catalogue_and_offers):
        from re import compile

        pricer_with_basket_catalogue_and_offers.DCN_TYP_REGEXPS = {
            "X_GET_Y": compile(r"^(.*)$"),
        }
        with pytest.raises(ValueError):
            pricer_with_basket_catalogue_and_offers._calculate_single_discount(
                "3get1", 3, 1.00
            )

        pricer_with_basket_catalogue_and_offers.DCN_TYP_REGEXPS = {
            "X_WOW_Y": re.compile(r"^([0-9]+)wow([0-9]+)$"),
        }
        with pytest.raises(ValueError):
            pricer_with_basket_catalogue_and_offers._calculate_single_discount(
                "3wow1", 3, 1.00
            )


def test_regexps():
    x_for_y_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_FOR_Y"], "2for1")
    assert x_for_y_match is not None
    assert len(x_for_y_match.groups()) == 2
    assert x_for_y_match.group(1) == "2"
    assert x_for_y_match.group(2) == "1"

    x_for_y_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_FOR_Y"], "2get1")
    assert x_for_y_match is None

    x_get_y_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_GET_Y"], "2get1")
    assert x_get_y_match is not None
    assert len(x_get_y_match.groups()) == 2
    assert x_get_y_match.group(1) == "2"
    assert x_get_y_match.group(2) == "1"

    x_get_y_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_GET_Y"], "2for1")
    assert x_get_y_match is None

    x_percent_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_PERCENT"], "25%")
    assert x_percent_match is not None
    assert len(x_percent_match.groups()) == 1
    assert x_percent_match.group(1) == "25"

    x_percent_match = re.match(BasketPricer.DCN_TYP_REGEXPS["X_PERCENT"], "not%")
    assert x_percent_match is None
