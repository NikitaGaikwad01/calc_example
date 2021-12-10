"""Main Calculator Operation Class"""
import logging
import sys

from projectcalc.additioncalc_project import Additioncalc
from projectcalc.subtractioncalc_project import Subtractioncalc
from projectcalc.multiplicationcalc_project import Multiplicationcalc
from projectcalc.divisioncalc_project import Divisioncalc
from projectcalc.history_project import History
from file_handler.read_csv import CSVFileRead

sys.tracebacklimit = 0
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

fileproject_handler = logging.FileHandler('log/project.log')
fileproject_handler.setLevel(logging.DEBUG)
fileproject_handler.setFormatter(formatter)

streamproject_handler = logging.StreamHandler()
streamproject_handler.setFormatter(formatter)

logger.addHandler(fileproject_handler)
logger.addHandler(streamproject_handler)

class Calculator:
    """Calling the calculator methods for performing operation"""

    def __init__(self, path):
        self.data = CSVFileRead.read_userdata(path)
        self.path = path

    def get_userdata(self):
        """Taking the user data"""
        csv_userdata = self.data
        var_a = csv_userdata['a'].values
        var_b = csv_userdata['b'].values
        add_result = [round(i,3) for i in csv_userdata['add_result'].values]
        sub_result = [round(i,3) for i in csv_userdata['sub_result'].values]
        multiply_result = [round(i,3) for i in csv_userdata['multiply_result'].values]
        divide_result = [round(i,3) for i in csv_userdata['div_result'].values]
        return var_a, var_b, add_result, sub_result, multiply_result, divide_result

    @staticmethod
    def add_operation(*args):
        """Performing addition operation"""
        add = Additioncalc(args).getoutput()
        History.add_calculation_history(add)
        return History.get_last_calculation()

    @staticmethod
    def sub_operation(*args):
        """Performing subtraction operation"""
        sub = Subtractioncalc(args).getoutput()
        History.add_calculation_history(sub)
        return History.get_last_calculation()

    @staticmethod
    def multiply_operation(*args):
        """Performing multiply operation"""
        mul = Multiplicationcalc(args).getoutput()
        History.add_calculation_history(mul)
        return History.get_last_calculation()

    @staticmethod
    def divide_operation(*args):
        """Performing divide operation"""
        try:
            div = Divisioncalc(args).getoutput()
            History.add_calculation_history(div)
        except ZeroDivisionError as err:
            logger.exception(err)
            return 0.0
        else:
            logger.debug('Division : %f / %f = %f', args[0], args[1], div)
            return History.get_last_calculation()
