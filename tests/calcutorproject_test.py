"""Class for testing the calculation operation for project 2"""
import pytest
from projectcalculator.maincalculator import Calculator
from projectcalc.history_project import History
# pylint: disable=unused-argument,redefined-outer-name,line-too-long

var_a, var_b, add_result, sub_result, multiply_result, div_result = Calculator('file_handler/user_input/data.csv').get_userdata()
length = len(add_result)

@pytest.fixture
def clear_history():
    """Calling the clear history Method"""
    History.clear_history()

def test_project_calculator_addition(clear_history):
    """Testing the addition operation"""

    for i in range(length):
        assert Calculator.add_operation(var_a[i], var_b[i] )== add_result[i]
    assert History.get_count_of_operation() == 5
    assert History.get_first_calculation() == add_result[0]
    assert History.get_last_calculation() == add_result[-1]


def test_project_calculator_subtraction(clear_history):
    """Testing the subtraction operation"""
    for i in range(length):
        assert Calculator.sub_operation(var_a[i], var_b[i] )== sub_result[i]

def test_project_calculator_multiplication(clear_history):
    """Testing the multiplication operation"""
    for i in range(length):
        assert Calculator.multiply_operation(var_a[i], var_b[i] )== multiply_result[i]

def test_project_calculator_divide(clear_history):
    """Testing the division operation"""
    for i in range(length):
        assert Calculator.divide_operation(var_a[i], var_b[i] )== div_result[i]
