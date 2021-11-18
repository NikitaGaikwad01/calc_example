"""Addition Calculation Class"""
from calc.calculation import Calculation


class Addition(Calculation):
    """Defining Method for adding two numbers"""

    def getresult(self):
        """Adding the values for performing operation"""
        return self.value_a + self.value_b
