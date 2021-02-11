import pytest
import re

from basket_pricer.pricer import BasketPricer


class TestPricerMethods:
    def test_regexps(self):
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
