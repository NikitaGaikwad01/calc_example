# pylint: disable=line-too-long
"""This is the division calculation that is being inherits the value A and value B from the calculation class"""
# pylint: disable=line-too-long
#this is called a namespace it is like files and folders the classes are files and the folders organize the classes
# pylint: disable=line-too-long
#It looks like a folder and file path but it is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Division(Calculation):
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        #you need to use self to reference the data contained in the instance of the object.
        #This is encapsulation
        """ divide two numbers and store the result"""
        try:
            return self.value_a / self.value_b
        except ZeroDivisionError:
            return 0
