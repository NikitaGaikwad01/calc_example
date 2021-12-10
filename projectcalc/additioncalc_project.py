"""Addition Class for the project"""

from projectcalc.calculation_project import Calculation

class Additioncalc(Calculation):
    """Defining the calculator class for adding two numbers"""

    def getoutput(self):
        """Performing the addition operation"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = sum_of_values + value
        return round(sum_of_values, 3)
