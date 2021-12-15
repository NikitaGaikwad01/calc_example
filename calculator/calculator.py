""" import all the methods from calc_methods"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.calculations.history_project import History

class Calculator:
    """ Creating a Calculator Module for initial processing stage """

    @staticmethod
    def add_operation(tuple_values: tuple):
        """Performing addition operation"""
        History.add_calculation_history(Addition.create(tuple_values).getoutput())
        #History.add_calculation_history(tuple_values)
        return True

    @staticmethod
    def sub_operation(tuple_values: tuple):
        """Performing subtraction operation"""
        History.add_calculation_history(Subtraction.create(tuple_values).getoutput())
        return True

    @staticmethod
    def multiply_operation(tuple_values: tuple):
        """Performing multiplication operation"""
        History.add_calculation_history(Multiplication.create(tuple_values).getoutput())
        return True

    @staticmethod
    def divide_operation(tuple_values: tuple):
        """Performing division operation"""
        History.add_calculation_history(Division.create(tuple_values).getoutput())
        return True

    @staticmethod
    def get_last_value():
        """result of the calculation"""
        return History.get_last_calculation()
