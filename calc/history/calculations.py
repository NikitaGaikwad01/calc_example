"""Calculation history Class"""
class Calculations:
    """Calculation history Class"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear history Class"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """count history Class"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """last history Class"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """first history Class"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
