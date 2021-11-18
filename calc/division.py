"""Division Class"""
from calc.calculation import Calculation


class Division(Calculation):
    """Defining Method for performing Division Operation"""

    def getresult(self):
        """Performing Division Operation"""
        return self.value_a / self.value_b
