from calculator import Shape

class Triangle(Shape):
    def __init__(self, bace, height):
        super().__init__(name="Rectangle")
        if bace <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.bace = bace
        self.height = height

    def get_area(self):
        return (self.bace * self.height) * 0.5

    def get_perimeter(self):
        return "not available"