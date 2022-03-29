""" This is the Calculator Class"""
from calculator.calculation import Addition, Subtraction, Multiplication


class Calculator:
    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calc = Addition.create(tuple_list)
        return calc.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calc = Subtraction.create(tuple_list)
        return calc.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the subtract method"""
        calc = Multiplication.create(tuple_list)
        return calc.get_result()
