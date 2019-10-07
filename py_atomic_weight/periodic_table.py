def InvalidAtomicSymbol(KeyError):
    """
    Raised when an invalid atomic symbol is looked up.
    """


def get_atomic_weight_for_element(element_symbol: str) -> float:
    """
    This function needs to be implemented.

    Given an element's atomic symbol such as "O", "He" or "Ti" return the
    element's corresponding atomic weight as a floating point number.

    If an atomic symbol which does not exist is requested, then
    raise a InvalidAtomicSymbol exception.

    All the data you need to implement this function is in periodic_table.json.

    This function can look up data in that file, or alternativly you can
    extract the relevant data and build a structure here. Whichever
    approach you take, please include any code you used to do this.
    """
    if element_symbol == "O":
        return 15.999
    else:
        raise NotImplemented("You need to implement this function.")
