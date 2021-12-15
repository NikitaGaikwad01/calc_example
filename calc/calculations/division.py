"""Division Class for the project"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Defining the calculator class for dividing two numbers"""

    def getoutput(self):
        """ Using self to reference the data contained in the object instance """
        division_of_values = self.values[0]
        for value in self.values[1:]:
            division_of_values = division_of_values / value
        return round(division_of_values, 3)