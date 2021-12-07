"""Testing Multiplication Functionality"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiply():
    """Testing the functionality for the multiply"""
    mynumbers = (1.0, 2.0)
    multiply = Multiplication(mynumbers)
    assert multiply.get_result() == 2.0
