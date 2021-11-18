"""Testing the Calculator Program"""
import pprint
import pytest
from calculator.calculator import Calculator

# Defining the Fixture
@pytest.fixture
def clear_history():
    """Calling the clear history Method"""
    Calculator.clear_history()

# pylint: disable=unused-argument, redefined-outer-name
def test_calculator_addition(clear_history):
    """Testing the Add Method for our calculator class"""
    assert Calculator.addition_nums(5, 5) == 10
    assert Calculator.addition_nums(20, 30) == 50
    assert Calculator.addition_nums(3, 2) == 5
    assert Calculator.addition_nums(4, 2) == 6
    assert Calculator.addition_nums(50, 5) == 55
    assert Calculator.get_calculation_count() == 5
    assert Calculator.get_first_calculation_history() == 10
    pprint.pprint(Calculator.history)

# pylint: disable=unused-argument, redefined-outer-name
def test_calculator_subtraction(clear_history):
    """Testing the subtraction Method for our calculator class"""
    assert Calculator.subtraction_nums(4,3) == 1
    assert Calculator.subtraction_nums(50,20) == 30
    assert Calculator.get_calculation_count() == 2
    pprint.pprint(Calculator.history)

# pylint: disable=unused-argument, redefined-outer-name
def test_calculator_multiplication(clear_history):
    """Testing the multiplication method for calculator class"""
    assert Calculator.multiplication_nums(3,2) == 6
    assert Calculator.multiplication_nums(10,20) == 200
    assert Calculator.multiplication_nums(4,4) == 16
    assert Calculator.get_calculation_count() == 3
    pprint.pprint(Calculator.history)

# pylint: disable=unused-argument, redefined-outer-name
def test_calculator_division(clear_history):
    """Testing the division method for calculator class"""
    assert Calculator.division_nums(10, 5) == 2
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)
