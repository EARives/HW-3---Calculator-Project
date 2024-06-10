from typing import List, Type
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1]

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

