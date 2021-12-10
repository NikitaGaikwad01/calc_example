"""Multiplication Class for the project"""

from projectcalc.calculation_project import Calculation

class Multiplicationcalc(Calculation):
    """Defining the calculator class for multiplying two numbers"""

    def getoutput(self):
        """ Using self to reference the data contained in the object instance """
        multiplication_of_values = 1.0
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return round(multiplication_of_values, 3)
