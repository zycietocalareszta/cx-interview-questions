def verify_atomic_weight_for_substance(formula: str, expected: float):
    pass


def test_for_chemical_trivial_case():
    verify_atomic_weight_for_substance("", 0.0)


def test_for_chemical_O2():
    verify_atomic_weight_for_substance("O2", 2 * 15.999)

# Add more tests here.
