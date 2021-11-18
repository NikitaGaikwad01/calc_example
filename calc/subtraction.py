"""Subtraction Class"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """Defining method for performing subtraction"""

    def getresult(self):
        """Performing subtraction logic"""
        return self.value_a - self.value_b
