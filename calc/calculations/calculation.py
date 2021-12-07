from abc import ABC,abstractmethod
class Calculation(ABC):
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self,values: tuple):
        """ constructor method"""
        self._values = Calculation.convert_args_to_list_float(values)
    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
    @abstractmethod
    def get_result(self):
        """abstract method get_result"""
        pass
