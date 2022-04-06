"""Testing the Calculator"""
from calculator import Calculator
from calculator.calculation import Addition, Subtraction, Multiplication



def test_calculator_is_instance():
    """ Testing the Calculator Instance"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculation_multiplication_instance():
    """Testing the Calculator Multiplication instance"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtraction instance"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)


def test_calculation_addition_instance():
    """Testing the Calculator Addition instance"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_add_get_result_method():
    """Testing the Calculator addition"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtraction"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert calculation.get_result() == -3


def test_calculation_multiply_get_result_method():
    """Testing the Calculator multiplication"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator Addition"""
    calculator = Calculator()
    assert calculator.add((1, 2)) == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract((1, 2)) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Multiplication"""
    calculator = Calculator()
    assert calculator.multiply((2, 2)) == 4

