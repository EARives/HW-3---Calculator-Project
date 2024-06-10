class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

