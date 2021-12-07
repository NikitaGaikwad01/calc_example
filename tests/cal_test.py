"""Testing the Calculator"""
import unittest
from tests import csv_reader
from csv_reader import FileReader
import pytest
import csv_input_file

from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static():
    """testing that our calculator has a static method for addition"""

    """Arrange"""
    data = FileReader.read_from_file("addition.csv")
    value_a = data._get_value(0, 1, takeable=True)
    value_b = data._get_value(0, 2, takeable=True)
    addition_result =data._get_value(0, 0, takeable=True)

    """Act"""
    result = Calculator.add_numbers(value_a,value_b)

    """Assert"""
    assert result == addition_result

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0,2.0) == -3.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calculator"""
	#pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(10.0,2.0)== 5.0

class MyTestCase(unittest.TestCase):
    """A test case is the individual unit of testing.unittest provides a base class"""
    def test_calculator_divide_by_zero(self):
        """Testing the divide method of the calculator when dividing by zero"""
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide_numbers(4.0,0)
if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    FileReader.main()
