"""Subraction Class for the project"""

from projectcalc.calculation_project import Calculation

class Subtractioncalc(Calculation):
    """Defining the calculator class for subtracting two numbers"""

    def getoutput(self):
        """ Using self to reference the data contained in the object instance """
        subtraction_of_values = self.values[0]
        for value in self.values[1:]:
            subtraction_of_values = subtraction_of_values - value
        return round(subtraction_of_values, 3)
