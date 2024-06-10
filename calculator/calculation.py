from decimal import Decimal

class Calculation:
    """Class to perform basic calculations"""

    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        """Perform the calculation"""
        return self.operation(self.a, self.b)


