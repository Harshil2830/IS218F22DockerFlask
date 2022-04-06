from calculator.operations import Addition, Subtraction, Multiplication


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(1, 2) == -1


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(1, 1) == 1
