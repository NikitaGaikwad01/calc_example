""" import all the methods from calc_methods"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division


class Calculator:
    """ Creating a Calculator Module for initial processing stage """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Creating History method for clearing the calc history"""
        Calculator.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        Calculator.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Gets last calculation from history array """
        return Calculator.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Gets number of calculations from history array """
        return len(Calculator.history)

    @staticmethod
    def addition_nums(value_a, value_b):
        """ Creating a method calling the Addition logic  """
        addition = Addition.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def subtraction_nums(value_a, value_b):
        """ Creating a method calling the subtraction logic """
        subtraction = Subtraction.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def multiplication_nums(value_a, value_b):
        """Creating a method calling the multiplication logic """
        multiplication = Multiplication.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def division_nums(value_a, value_b):
        """ Creating a method calling the division logic """
        division = Division.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation_added()
