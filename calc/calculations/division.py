"""Division Class"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """creating the object for the division method"""
    def get_result(self):
        """get the division results"""
        division_of_values = 1.0
        for value in self.values:
            division_of_values =   division_of_values / value
        return division_of_values
