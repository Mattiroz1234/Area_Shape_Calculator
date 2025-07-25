from calculator import Shape
from math import sqrt

class Hexagon(Shape):
    def __init__(self, side):
        super().__init__(name="hexagon")
        if side <= 0:
            raise ValueError("side must be positive number")
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) / 2) * self.side ** 2

    def get_perimeter(self):
        return self.side * 6