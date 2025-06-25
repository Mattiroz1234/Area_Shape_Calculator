from calculator import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name="Square")
        if radius <= 0:
            raise ValueError("radius must be positive number.")
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * pi

    def get_perimeter(self):
        return self.radius * 2 * pi