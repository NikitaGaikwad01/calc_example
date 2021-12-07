"""Testing Divison"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (2.0,1.0)
    division= Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 2.0
    #Arrange
    mynumbers = (4.0,0.0)
    division= Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.0
