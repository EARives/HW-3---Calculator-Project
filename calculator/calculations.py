from typing import Type
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculations:
    """Class to manage a history of calculations"""
    history = []

    @staticmethod
    def add_calculation(calculation: Type[Calculation]):
        """Add a calculation to the history"""
        Calculations.history.append(calculation)

    @staticmethod
    def clear_history():
        """Clear the calculation history"""
        Calculations.history.clear()

    @staticmethod
    def count_history():
        """Return the number of calculations in history"""
        return len(Calculations.history)

