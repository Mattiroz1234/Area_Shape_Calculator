from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(name="Rectangle")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    
