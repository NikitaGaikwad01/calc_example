"""Multiplication Class"""
from calc.calculation import Calculation

class Multiplication(Calculation):
    """Defining the Multiplication Logic"""

    def getresult(self):
        """Performing Operation"""
        return self.value_a * self.value_b
