"""Designing history method"""

class History:
    """Designing the calculator history methods"""
    temp_history = []

    @staticmethod
    def clear_history():
        """Clear the history for calculator"""
        History.temp_history.clear()

    @staticmethod
    def add_calculation_history(calculation):
        """Calculation to history"""
        History.temp_history.append(calculation)

    @staticmethod
    def get_first_calculation():
        """Getting first calculation for the operation"""
        return History.temp_history[0]

    @staticmethod
    def get_last_calculation():
        """Getting last calculation for the operation"""
        return History.temp_history[-1]

    @staticmethod
    def get_count_of_operation():
        """Getting the count for the no, of operation performed"""
        return len(History.temp_history)
