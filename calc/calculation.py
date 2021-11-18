""" Calculation Abstract Class """


class Calculation:
    """ Defining Class Constructor in here """

    # pylint: disable=too-few-public-methods

    def __init__(self, value_a, value_b):
        # self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """ Returning the values back """
        return cls(value_a, value_b)
